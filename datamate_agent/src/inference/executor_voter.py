"""
Execution and Majority Voting Engine for DataMate Challenge.
Executes generated SQL queries in DuckDB with strict 5.0s timeout,
handles automated self-repair turns on errors,
triggers +4 thinking samples on low agreement,
and majority votes using canonical voting keys (outputting 'abstain' if share < tau=0.5).
"""

import concurrent.futures
import json
import logging
import math
import re
import threading
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

import duckdb

from ..evaluator import canonicalize_for_voting, normalize_string
from .llm_engine import LLMEngine

logger = logging.getLogger(__name__)


def validate_submission_item(item: Dict[str, Any]) -> bool:
    """
    Validates that a submission item adheres strictly to the competition schema.
    Returns True if valid, False otherwise.
    """
    if not isinstance(item, dict) or "id" not in item or "type" not in item:
        return False
    t = item["type"]
    if t == "abstain":
        return True
    if t == "unanswerable":
        return True
    if "answer" not in item or item["answer"] is None:
        return False

    ans = item["answer"]
    if t == "number":
        return isinstance(ans, (int, float)) and not math.isnan(ans)
    elif t == "percent":
        return isinstance(ans, (int, float)) and not math.isnan(ans)
    elif t == "string":
        return isinstance(ans, str) and len(ans.strip()) > 0
    elif t == "date":
        return isinstance(ans, str) and len(ans.strip()) >= 7
    elif t == "boolean":
        return isinstance(ans, bool)
    elif t == "list":
        return isinstance(ans, list) and len(ans) > 0
    elif t == "table":
        return (
            isinstance(ans, dict)
            and "columns" in ans
            and "rows" in ans
            and isinstance(ans["columns"], list)
            and isinstance(ans["rows"], list)
            and len(ans["rows"]) > 0
        )
    return False


def parse_completion(text: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extracts TYPE and SQL query from LLM completion.
    - Case-insensitively extracts TYPE: (number|percent|string|date|boolean|list|table|unanswerable|abstain).
    - If no TYPE is found, returns (None, sql) to fail the sample.
    - If TYPE is unanswerable, returns ('unanswerable', None).
    - Extracts SQL from ```sql ... ```, ``` ... ```, or fallback to the last WITH/SELECT statement.
    """
    if not text or not isinstance(text, str):
        return None, None

    # 1. Case-insensitive extraction of TYPE
    type_matches = list(re.finditer(
        r"(?im)^\s*(?:\*\*)?(?:\[)?TYPE(?:\])?(?::(?:\*\*)?|(?:\*\*)?:)?\s*([a-zA-Z_]+)",
        text
    ))
    if not type_matches:
        # Also try inline TYPE:
        type_matches = list(re.finditer(r"(?i)\bTYPE:\s*([a-zA-Z_]+)", text))

    pred_type: Optional[str] = None
    type_pos = -1
    valid_types = ["number", "percent", "string", "date", "boolean", "list", "table", "unanswerable", "abstain"]

    if type_matches:
        for m in reversed(type_matches):
            raw_t = m.group(1).lower().strip()
            if raw_t in valid_types:
                pred_type = raw_t
                type_pos = m.end()
                break

    if not pred_type:
        return None, None

    if pred_type == "unanswerable":
        return "unanswerable", None

    # 2. Extract SQL query
    search_region = text[type_pos:] if type_pos >= 0 else text

    def _extract_sql_from_region(region: str) -> Optional[str]:
        # Closed code blocks: ```sql ... ``` or ``` ... ```
        closed_blocks = list(re.finditer(r"```(?:sql)?\s*([\s\S]*?)\s*```", region, re.IGNORECASE))
        if closed_blocks:
            for blk in reversed(closed_blocks):
                cand = blk.group(1).strip()
                if re.search(r"(?i)^\s*(?:WITH|SELECT)\b", cand):
                    return cand
            return closed_blocks[-1].group(1).strip()

        # Unclosed code block: ```sql ... to end of region
        unclosed_match = re.search(r"```(?:sql)?\s*([\s\S]+)$", region, re.IGNORECASE)
        if unclosed_match:
            cand = unclosed_match.group(1).strip()
            cand = re.sub(r"```.*$", "", cand).strip()
            return cand

        # Fallback to finding the last WITH or SELECT statement up to ; or end of string
        statements = list(re.finditer(r"(?is)\b(WITH\b[\s\S]+?|SELECT\b[\s\S]+?)(?:;|\Z)", region))
        if statements:
            return statements[-1].group(1).strip()

        return None

    sql = _extract_sql_from_region(search_region)
    if not sql and type_pos >= 0:
        sql = _extract_sql_from_region(text)

    if sql:
        sql = sql.strip().rstrip(";")

    return pred_type, sql


def cast_duckdb_result(result_rows: List[Tuple], pred_type: str, col_names: List[str], sql: str = "") -> Any:
    """
    Coerces raw DuckDB cursor rows to canonical Python types via canonicalize_for_voting.
    Returns None if result is empty or NULL (unless valid 0 from COUNT).
    """
    if not result_rows:
        if pred_type == "number" and re.search(r"(?i)\bCOUNT\b", sql):
            return 0
        return None

    clean_val, _ = canonicalize_for_voting(pred_type, result_rows)
    return clean_val


def make_vote_key(pred_type: str, value: Any) -> Optional[str]:
    """
    Computes canonical voting key via canonicalize_for_voting.
    """
    _, key = canonicalize_for_voting(pred_type, value)
    return key


@dataclass
class CandidateExecution:
    sample_id: int
    raw_completion: str
    parsed_type: str
    parsed_sql: Optional[str]
    raw_result: Any = None
    normalized_value: Any = None
    vote_key: Optional[str] = None
    success: bool = False
    error: Optional[str] = None
    failure_category: Optional[str] = None
    repair_turns: int = 0
    is_thinking: bool = False


@dataclass
class QuestionInferenceResult:
    question_id: str
    business_id: str
    final_type: str
    final_answer: Any
    confidence: float
    total_samples: int
    agreement_count: int
    elapsed_time: float
    candidates: List[CandidateExecution] = field(default_factory=list)
    vote_distribution: Dict[str, int] = field(default_factory=dict)
    reason: Optional[str] = None

    def to_submission_dict(self) -> Dict[str, Any]:
        """
        Converts to official competition submission JSON object with schema validation.
        """
        if self.final_type == "abstain":
            return {"id": self.question_id, "type": "abstain"}
        elif self.final_type == "unanswerable":
            res = {"id": self.question_id, "type": "unanswerable"}
            if self.reason:
                res["reason"] = self.reason
            return res
        else:
            item = {
                "id": self.question_id,
                "type": self.final_type,
                "answer": self.final_answer,
            }
            if not validate_submission_item(item):
                return {"id": self.question_id, "type": "abstain"}
            return item

    def to_log_dict(self) -> Dict[str, Any]:
        """
        Formats per-question log object for /result/logs/<id>.json.
        """
        return {
            "id": self.question_id,
            "business_id": self.business_id,
            "elapsed_time": round(self.elapsed_time, 4),
            "final_type": self.final_type,
            "final_answer": self.final_answer,
            "confidence": round(self.confidence, 4),
            "agreement_count": self.agreement_count,
            "total_samples": self.total_samples,
            "vote_distribution": self.vote_distribution,
            "abstain_reason": self.reason,
            "generated_sql_samples": [
                {
                    "sample_id": c.sample_id,
                    "type": c.parsed_type,
                    "sql": c.parsed_sql,
                    "success": c.success,
                    "vote_key": c.vote_key,
                    "error": c.error,
                    "failure_category": c.failure_category,
                    "repair_turns": c.repair_turns,
                    "is_thinking": c.is_thinking,
                }
                for c in self.candidates
            ],
            "execution_outputs": [c.normalized_value for c in self.candidates if c.success],
        }


class ExecutorVoter:
    def __init__(
        self,
        con: duckdb.DuckDBPyConnection,
        llm_engine: Optional[LLMEngine] = None,
        agreement_threshold_tau: float = 0.5,
        sql_timeout_seconds: float = 5.0,  # Strict 5.0-second timeout
        max_repair_turns: int = 2,
        schema_summary: Optional[str] = None,
    ):
        self.con = con
        self.llm_engine = llm_engine
        self.tau = agreement_threshold_tau
        self.timeout = sql_timeout_seconds
        self.max_repairs = max_repair_turns
        self.schema_summary = schema_summary

    def _execute_query_internal(self, sql: str) -> Tuple[bool, Any, Optional[str], List[str]]:
        """
        Internal execution helper with regex self-healing.
        """
        curr_sql = sql
        rel = None
        err_last = None

        for attempt in range(3):
            try:
                rel = self.con.execute(curr_sql)
                err_last = None
                break
            except Exception as ex:
                err_last = str(ex)

                # Self-healing 1: DuckDB table suggestion
                m_tbl = re.search(r'Table with name ([a-zA-Z0-9_]+) does not exist!\s*Did you mean "([^"]+)"\?', err_last)
                if m_tbl:
                    w_tbl, r_tbl = m_tbl.group(1), m_tbl.group(2)
                    curr_sql = re.sub(r'\b' + re.escape(w_tbl) + r'\b', r_tbl, curr_sql, flags=re.IGNORECASE)
                    continue

                # Self-healing 2: DuckDB column suggestion
                m_col = re.search(r'(?:Column with name|Referenced column) "([a-zA-Z0-9_]+)" not found.*Did you mean "([^"]+)"\?', err_last)
                if m_col:
                    w_col, r_col = m_col.group(1), m_col.group(2)
                    curr_sql = re.sub(r'\b' + re.escape(w_col) + r'\b', r_col, curr_sql, flags=re.IGNORECASE)
                    continue

                # Self-healing 3: LOWER() on non-VARCHAR type
                if "no function matches the given name and argument types 'lower(" in err_last.lower():
                    new_sql = re.sub(r'(?i)\blower\s*\(\s*([^()]+?)\s*\)', r'LOWER(CAST(\1 AS VARCHAR))', curr_sql)
                    if new_sql != curr_sql:
                        curr_sql = new_sql
                        continue

                break

        if err_last is not None:
            return False, None, err_last, []

        col_names = [desc[0] for desc in rel.description] if rel.description else []
        rows = rel.fetchall()

        # Self-healing 4: If status equality '=' returned empty result or [(0,)], try ILIKE
        if (not rows or rows == [(0,)] or rows == [(None,)]) and re.search(r"(?i)\b(?:trang_thai|status|tinh_trang)\s*=\s*'([^']*)'", curr_sql):
            alt_sql = re.sub(r"(?i)\b(trang_thai|status|tinh_trang)\s*=\s*'([^']*)'", r"\1 ILIKE '%\2%'", curr_sql)
            if alt_sql != curr_sql:
                try:
                    alt_rel = self.con.execute(alt_sql)
                    alt_rows = alt_rel.fetchall()
                    if alt_rows and alt_rows != [(0,)] and alt_rows != [(None,)]:
                        return True, alt_rows, None, col_names
                except Exception:
                    pass

        return True, rows, None, col_names

    def execute_single_sql(self, sql: str, pred_type: Optional[str]) -> Tuple[bool, Any, Optional[str], List[str]]:
        """
        Executes a SQL query in DuckDB with safety and strict 5.0-second timeout.
        Rejects queries containing destructive keywords (DROP, DELETE, UPDATE, INSERT, ALTER, COPY).
        Returns (success, result_rows, error_message, column_names).
        """
        if not sql or not sql.strip():
            return False, None, "Empty SQL query", []

        # Strip comments and code fences
        cleaned_sql = re.sub(r"```(?:sql)?", "", sql, flags=re.IGNORECASE)
        cleaned_sql = re.sub(r"```", "", cleaned_sql)
        cleaned_sql = re.sub(r"--[^\n]*", "", cleaned_sql)
        cleaned_sql = re.sub(r"/\*[\s\S]*?\*/", "", cleaned_sql).strip()
        cleaned_sql = cleaned_sql.rstrip(";")

        # Must start with SELECT or WITH
        if not re.match(r"(?i)^\s*(?:SELECT|WITH)\b", cleaned_sql):
            return False, None, "Query must start with SELECT or WITH statement", []

        # Rejection of destructive keywords
        DESTRUCTIVE_PATTERN = re.compile(r"(?i)\b(DROP|DELETE|UPDATE|INSERT|ALTER|COPY)\b")
        if DESTRUCTIVE_PATTERN.search(cleaned_sql):
            return False, None, "Destructive SQL operation rejected", []

        # ThreadPoolExecutor execution with timeout and conn.interrupt()
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(self._execute_query_internal, cleaned_sql)
                try:
                    return future.result(timeout=self.timeout)
                except concurrent.futures.TimeoutError:
                    try:
                        self.con.interrupt()
                    except Exception:
                        pass
                    return False, None, f"SQL query timed out after {self.timeout}s (interrupted)", []
        except Exception as e:
            return False, None, str(e), []

    def repair_sql_turn(self, bad_sql: str, error_msg: str, orig_question: str) -> Optional[str]:
        """
        Requests the LLM to fix a failed SQL statement given DuckDB error message
        and database table column names.
        """
        if not self.llm_engine:
            return None

        from ..context.prompt_builder import build_chat_prompt
        compact_schema = self.schema_summary or ""

        hint = ""
        m_sugg = re.search(r'Did you mean "([^"]+)"\?', error_msg)
        if m_sugg:
            hint = f"\nHint from DuckDB: Did you mean table/column '{m_sugg.group(1)}'?"

        m_col = re.search(r'Referenced column "([^"]+)" not found in FROM clause!', error_msg)
        if m_col and self.con:
            missing_col = m_col.group(1)
            matching_tables = []
            try:
                all_tbls = [t[0] for t in self.con.execute("SHOW TABLES").fetchall()]
                for t in all_tbls:
                    if t.startswith("raw_") and not t.endswith("_df"):
                        c_names = [c[0].lower() for c in self.con.execute(f'DESCRIBE "{t}"').fetchall()]
                        if missing_col.lower() in c_names:
                            matching_tables.append(t)
            except Exception:
                pass
            if matching_tables:
                hint += f"\nHint: Column '{missing_col}' is present in table(s): {matching_tables}. You must query or JOIN with one of these tables."

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert DuckDB SQL repair assistant.\n"
                    "Fix the erroneous SQL query so that it executes without errors and answers the question.\n"
                    "Output ONLY the corrected SQL query within a ```sql ... ``` code block."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"The following DuckDB SQL query produced an error:\n"
                    f"```sql\n{bad_sql}\n```\n\n"
                    f"DuckDB Error:\n{error_msg}{hint}\n\n"
                    f"Question:\n{orig_question}\n\n"
                    + (f"Database Tables & Columns:\n{compact_schema}\n\n" if compact_schema else "")
                    + "Please fix the SQL query to resolve the error and answer the question. Output ONLY ```sql ... ```."
                ),
            },
        ]
        repair_prompt = build_chat_prompt(
            tokenizer=self.llm_engine.tokenizer,
            messages=messages,
            prefill="```sql\n",
        )
        try:
            completions = self.llm_engine.generate_single(
                repair_prompt,
                n=1,
                temperature=0.0,
                max_new_tokens=512,
            )
            if completions:
                raw_out = completions[0].strip()
                if not raw_out.startswith("```"):
                    raw_out = f"```sql\n{raw_out}\n```"
                _, rep_sql = parse_completion(raw_out)
                if not rep_sql:
                    m = re.search(r"(?is)\b(WITH|SELECT)\b[\s\S]+", raw_out)
                    if m:
                        rep_sql = m.group(0).split("```")[0].strip()
                if rep_sql:
                    rep_sql = rep_sql.strip().rstrip(";")
                return rep_sql
        except Exception as e:
            logger.debug(f"Repair turn failed: {e}")
        return None

    def process_candidate(
        self,
        sample_id: int,
        raw_completion: str,
        orig_question: str,
        is_thinking: bool = False,
    ) -> CandidateExecution:
        """
        Parses, executes, and self-repairs a candidate sample.
        Canonicalizes output into competition types.
        """
        pred_type, sql = parse_completion(raw_completion)

        if not pred_type:
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type="failed",
                parsed_sql=sql,
                success=False,
                error="Missing or invalid TYPE in completion",
                failure_category="OUTPUT_PARSE_ERROR",
                is_thinking=is_thinking,
            )

        if pred_type == "unanswerable":
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type="unanswerable",
                parsed_sql=None,
                raw_result=None,
                normalized_value=None,
                vote_key="unanswerable",
                success=True,
                failure_category="SUCCESS",
                is_thinking=is_thinking,
            )

        if not sql:
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=None,
                success=False,
                error="No SQL query found",
                failure_category="SQL_EXTRACTION_ERROR",
                is_thinking=is_thinking,
            )

        current_sql = sql
        success = False
        last_error = None
        failure_cat = None
        rows = None
        col_names = []
        repair_count = 0

        for turn in range(self.max_repairs + 1):
            ok, res_rows, err, cols = self.execute_single_sql(current_sql, pred_type)
            if ok:
                norm_val, v_key = canonicalize_for_voting(pred_type, res_rows)
                if norm_val is not None and v_key is not None:
                    success = True
                    rows = res_rows
                    col_names = cols
                    failure_cat = "SUCCESS"
                    break
                else:
                    last_error = f"Query executed successfully but returned NULL or empty output for TYPE '{pred_type}'"
                    failure_cat = "EMPTY_RESULT"
                    if turn < self.max_repairs:
                        rep = self.repair_sql_turn(current_sql, last_error, orig_question)
                        if rep:
                            current_sql = rep
                            repair_count += 1
                            continue
                    break
            else:
                last_error = err
                failure_cat = "SQL_EXECUTION_ERROR"
                if turn < self.max_repairs:
                    rep = self.repair_sql_turn(current_sql, err, orig_question)
                    if rep:
                        current_sql = rep
                        repair_count += 1
                        continue
                break

        if success and rows is not None:
            norm_val, v_key = canonicalize_for_voting(pred_type, rows)
            if norm_val is None or v_key is None:
                return CandidateExecution(
                    sample_id=sample_id,
                    raw_completion=raw_completion,
                    parsed_type=pred_type,
                    parsed_sql=current_sql,
                    raw_result=rows,
                    normalized_value=None,
                    vote_key=None,
                    success=False,
                    error=f"Query returned NULL or empty result for type '{pred_type}'",
                    failure_category="EMPTY_RESULT",
                    repair_turns=repair_count,
                    is_thinking=is_thinking,
                )

            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=current_sql,
                raw_result=rows,
                normalized_value=norm_val,
                vote_key=v_key,
                success=True,
                failure_category="SUCCESS",
                repair_turns=repair_count,
                is_thinking=is_thinking,
            )
        else:
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=current_sql,
                success=False,
                error=last_error,
                failure_category=failure_cat or "SQL_EXECUTION_ERROR",
                repair_turns=repair_count,
                is_thinking=is_thinking,
            )

    def vote_and_decide(
        self,
        question_id: str,
        business_id: str,
        candidates: List[CandidateExecution],
        elapsed: float,
        denominator: Optional[int] = None,
    ) -> QuestionInferenceResult:
        """
        Groups valid executions by (ans_type, canonical_voting_key).
        Computes top_share = top_group_count / total_samples (where denominator is 8, or 12).
        If top_share >= 0.5, outputs the representative formatted answer of the winning group.
        Otherwise, outputs abstain.
        """
        valid_candidates = [c for c in candidates if c.success and c.vote_key is not None]
        total_samples = denominator or len(candidates)

        if not valid_candidates or total_samples == 0:
            first_err = candidates[0].error if candidates else "No candidates"
            cat = candidates[0].failure_category if candidates else "FINAL_ABSTENTION"
            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type="abstain",
                final_answer=None,
                confidence=0.0,
                total_samples=total_samples,
                agreement_count=0,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution={},
                reason=f"All candidate SQL queries failed ({cat}): {first_err}",
            )

        # Group by (type, vote_key)
        group_counts: Dict[Tuple[str, str], int] = Counter(
            (c.parsed_type, c.vote_key) for c in valid_candidates
        )
        (top_type, top_key), top_count = group_counts.most_common(1)[0]
        top_share = top_count / total_samples

        vote_distribution = {f"{t}:{k}": cnt for (t, k), cnt in group_counts.items()}

        if top_share >= self.tau:
            winning_cand = next(
                c for c in valid_candidates if c.parsed_type == top_type and c.vote_key == top_key
            )
            final_t = winning_cand.parsed_type
            final_a = winning_cand.normalized_value

            # Validate against official competition schema
            test_sub = {"id": question_id, "type": final_t, "answer": final_a}
            if not validate_submission_item(test_sub):
                logger.warning(f"Winning candidate for {question_id} failed schema validation: {test_sub}. Abstaining.")
                final_t = "abstain"
                final_a = None

            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type=final_t,
                final_answer=final_a,
                confidence=top_share,
                total_samples=total_samples,
                agreement_count=top_count,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution=vote_distribution,
            )
        else:
            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type="abstain",
                final_answer=None,
                confidence=top_share,
                total_samples=total_samples,
                agreement_count=top_count,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution=vote_distribution,
                reason=f"Voting agreement insufficient ({top_count}/{total_samples} = {top_share:.2f}) < tau={self.tau}",
            )
