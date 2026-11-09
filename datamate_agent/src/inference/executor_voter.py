"""
Execution and Majority Voting Engine for DataMate Challenge.
Executes generated SQL queries in DuckDB with timeout,
handles automated self-repair turns on errors,
triggers +4 thinking samples on low agreement,
and majority votes using normalized keys (outputting 'abstain' if share < tau=0.5).
"""

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

from ..evaluator import normalize_string
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
    - Matches the LAST occurrence of TYPE: at start of a line.
    - If no TYPE is found, returns (None, sql) to fail the sample.
    - Supports closed and unclosed ```sql blocks, CTEs (WITH), and SELECT.
    """
    if not text or not isinstance(text, str):
        return None, None

    # 1. Extract TYPE: find all occurrences of ^TYPE:\s*([a-zA-Z_]+) at start of lines
    type_matches = list(re.finditer(r"(?im)^TYPE:\s*([a-zA-Z_]+)", text))
    pred_type: Optional[str] = None
    type_pos = -1
    if type_matches:
        last_match = type_matches[-1]
        raw_type = last_match.group(1).lower().strip()
        if raw_type in ["number", "percent", "string", "date", "boolean", "list", "table", "unanswerable", "abstain"]:
            pred_type = raw_type
            type_pos = last_match.end()

    # 2. Extract SQL block: only search after the last TYPE line (if found), or whole text
    search_region = text[type_pos:] if type_pos >= 0 else text
    sql: Optional[str] = None

    # Check for closed ```sql ... ```
    closed_blocks = list(re.finditer(r"```(?:sql)?\s*([\s\S]*?)\s*```", search_region, re.IGNORECASE))
    if closed_blocks:
        for blk in closed_blocks:
            cand = blk.group(1).strip()
            if re.search(r"(?i)^\s*(?:WITH|SELECT)\b", cand):
                sql = cand
                break
        if not sql:
            sql = closed_blocks[0].group(1).strip()

    # If no closed block found, check for unclosed ```sql ... to end of text
    if not sql:
        unclosed_match = re.search(r"```(?:sql)?\s*([\s\S]+)$", search_region, re.IGNORECASE)
        if unclosed_match:
            cand = unclosed_match.group(1).strip()
            cand = re.sub(r"```.*$", "", cand).strip()
            sql = cand

    # If still no markdown block found, fallback to first WITH or SELECT query
    if not sql:
        with_match = re.search(r"(?is)\b(WITH\b[\s\S]+)", search_region)
        select_match = re.search(r"(?is)\b(SELECT\b[\s\S]+)", search_region)
        if with_match and select_match:
            sql = with_match.group(1).strip() if with_match.start() < select_match.start() else select_match.group(1).strip()
        elif with_match:
            sql = with_match.group(1).strip()
        elif select_match:
            sql = select_match.group(1).strip()

    if sql:
        sql = sql.strip().rstrip(";")

    return pred_type, sql


def cast_duckdb_result(result_rows: List[Tuple], pred_type: str, col_names: List[str], sql: str = "") -> Any:
    """
    Converts raw DuckDB cursor fetch result into canonical competition types.
    Returns None if result is empty or NULL (unless valid 0 from COUNT).
    """
    if not result_rows:
        # Check if query has COUNT aggregation where 0 rows might be 0
        if pred_type == "number" and re.search(r"(?i)\bCOUNT\b", sql):
            return 0
        return None

    if pred_type == "unanswerable":
        return None

    # Scalar types (1 row, 1 col)
    if pred_type in ["number", "percent", "string", "date", "boolean"]:
        val = result_rows[0][0]
        if val is None:
            return None

        if pred_type == "number":
            try:
                f = float(val)
                if math.isnan(f):
                    return None
                return int(round(f)) if math.isclose(f, round(f), abs_tol=1e-5) else round(f, 2)
            except Exception:
                return None

        elif pred_type == "percent":
            try:
                f = float(val)
                if math.isnan(f):
                    return None
                return round(f, 2)
            except Exception:
                return None

        elif pred_type == "string":
            s = str(val).strip()
            return s if s and s.lower() != "none" else None

        elif pred_type == "date":
            s = str(val).strip()
            if len(s) >= 10 and s[4] == "-" and s[7] == "-":
                return s[:10]
            elif len(s) >= 7 and s[4] == "-":
                return s[:7]
            return s if s else None

        elif pred_type == "boolean":
            if isinstance(val, bool):
                return val
            s = str(val).lower().strip()
            return s in ["true", "1", "t", "dung", "co"]

    # List type
    elif pred_type == "list":
        res_list = []
        for r in result_rows:
            item = r[0] if len(r) > 0 else None
            if item is None:
                continue
            if isinstance(item, (int, float)):
                if not math.isnan(item):
                    res_list.append(int(item) if math.isclose(item, round(item), abs_tol=1e-5) else round(item, 2))
            else:
                s = str(item).strip()
                if s:
                    res_list.append(s)
        return res_list if res_list else None

    # Table type
    elif pred_type == "table":
        rows = []
        for r in result_rows:
            row_items = []
            for cell in r:
                if isinstance(cell, (int, float)):
                    row_items.append(int(cell) if math.isclose(cell, round(cell), abs_tol=1e-5) else round(cell, 2))
                else:
                    row_items.append(str(cell).strip() if cell is not None else "")
            rows.append(row_items)
        return {"columns": col_names, "rows": rows} if rows else None

    return result_rows[0][0]


def make_vote_key(pred_type: str, value: Any) -> Optional[str]:
    """
    Converts a normalized prediction into a deterministic typed voting key.
    Returns None if value is None and pred_type is not unanswerable.
    """
    if pred_type == "unanswerable":
        return "unanswerable:__null__"
    if value is None:
        return None

    if pred_type == "number":
        try:
            return f"num:{float(value):.2f}"
        except Exception:
            return f"num:{value}"
    elif pred_type == "percent":
        try:
            return f"pct:{float(value):.2f}"
        except Exception:
            return f"pct:{value}"
    elif pred_type == "string":
        return f"str:{normalize_string(value)}"
    elif pred_type == "date":
        return f"date:{str(value).strip().lower()}"
    elif pred_type == "boolean":
        return f"bool:{bool(value)}"
    elif pred_type == "list":
        if isinstance(value, list) and value:
            items_str = "|".join(normalize_string(v) if isinstance(v, str) else str(v) for v in value)
            return f"list:{items_str}"
        return None
    elif pred_type == "table":
        if isinstance(value, dict) and value.get("rows"):
            rows = value.get("rows", [])
            rows_str = sorted(["|".join(normalize_string(c) if isinstance(c, str) else str(c) for c in r) for r in rows])
            return f"table:{'#'.join(rows_str)}"
        return None
    return f"{pred_type}:{value}"


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
    repair_turns: int = 0


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
        Formats per-question log object for `/result/logs/<id>.json`.
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
            "generated_sql_samples": [
                {
                    "sample_id": c.sample_id,
                    "type": c.parsed_type,
                    "sql": c.parsed_sql,
                    "success": c.success,
                    "vote_key": c.vote_key,
                    "error": c.error,
                }
                for c in self.candidates
            ],
            "execution_outputs": [c.normalized_value for c in self.candidates if c.success],
        }


class ExecutorVoter:
    def __init__(
        self,
        con: duckdb.DuckDBPyConnection,
        llm_engine: LLMEngine,
        agreement_threshold_tau: float = 0.5,
        sql_timeout_seconds: float = 10.0,
        max_repair_turns: int = 2,
        schema_summary: Optional[str] = None,
    ):
        self.con = con
        self.llm_engine = llm_engine
        self.tau = agreement_threshold_tau
        self.timeout = sql_timeout_seconds
        self.max_repairs = max_repair_turns
        self.schema_summary = schema_summary

    def execute_single_sql(self, sql: str, pred_type: Optional[str]) -> Tuple[bool, Any, Optional[str], List[str]]:
        """
        Executes a SQL query in DuckDB with safety and timeout.
        Returns (success, result_rows, error_message, column_names).
        """
        if not sql or not sql.strip():
            return False, None, "Empty SQL query", []

        # Strip comments
        cleaned_sql = re.sub(r"--[^\n]*", "", sql)
        cleaned_sql = re.sub(r"/\*[\s\S]*?\*/", "", cleaned_sql).strip()
        cleaned_sql = cleaned_sql.rstrip(";")

        # P0-9: Query must start with SELECT or WITH (no blind substring keyword blocking)
        if not re.match(r"(?i)^\s*(?:SELECT|WITH)\b", cleaned_sql):
            return False, None, "Query must start with SELECT or WITH statement", []

        timer = None
        timed_out = [False]

        def on_timeout():
            timed_out[0] = True
            try:
                self.con.interrupt()
            except Exception:
                pass

        try:
            if self.timeout and self.timeout > 0:
                timer = threading.Timer(self.timeout, on_timeout)
                timer.daemon = True
                timer.start()

            rel = self.con.execute(cleaned_sql)
            col_names = [desc[0] for desc in rel.description] if rel.description else []
            rows = rel.fetchall()
            return True, rows, None, col_names
        except Exception as e:
            if timed_out[0]:
                return False, None, f"SQL query timed out after {self.timeout}s (interrupted)", []
            return False, None, str(e), []
        finally:
            if timer is not None:
                timer.cancel()

    def repair_sql_turn(self, bad_sql: str, error_msg: str, orig_question: str) -> Optional[str]:
        """
        P1-15: Requests the LLM to fix a failed SQL statement given DuckDB error message,
        compact database schema context, and formatted via build_chat_prompt.
        """
        from ..context.prompt_builder import build_chat_prompt
        compact_schema = self.schema_summary or ""
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
                    f"DuckDB Error:\n{error_msg}\n\n"
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
                raw_out = completions[0]
                if not raw_out.strip().startswith("```"):
                    raw_out = "```sql\n" + raw_out
                _, rep_sql = parse_completion(raw_out)
                return rep_sql
        except Exception as e:
            logger.debug(f"Repair turn failed: {e}")
        return None

    def process_candidate(
        self,
        sample_id: int,
        raw_completion: str,
        orig_question: str,
    ) -> CandidateExecution:
        """
        Parses, executes, and repairs a single LLM completion candidate.
        P0-4 / P0-6: Fails sample if TYPE is missing, or if result is NULL/empty for scalar types.
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
            )

        if pred_type == "unanswerable":
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=sql,
                raw_result=None,
                normalized_value=None,
                vote_key="unanswerable:__null__",
                success=True,
            )

        if not sql:
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=None,
                success=False,
                error="No SQL query found",
            )

        current_sql = sql
        success = False
        last_error = None
        rows = None
        col_names = []
        repair_count = 0

        for turn in range(self.max_repairs + 1):
            ok, res_rows, err, cols = self.execute_single_sql(current_sql, pred_type)
            if ok:
                success = True
                rows = res_rows
                col_names = cols
                break
            else:
                last_error = err
                if turn < self.max_repairs:
                    rep = self.repair_sql_turn(current_sql, err, orig_question)
                    if rep:
                        current_sql = rep
                        repair_count += 1
                        continue
                break

        if success and rows is not None:
            norm_val = cast_duckdb_result(rows, pred_type, col_names, sql=current_sql)
            if norm_val is None:
                # P0-6: Empty or NULL result is treated as FAILURE, not converted to 0
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
                    repair_turns=repair_count,
                )

            v_key = make_vote_key(pred_type, norm_val)
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=current_sql,
                raw_result=rows,
                normalized_value=norm_val,
                vote_key=v_key,
                success=True,
                repair_turns=repair_count,
            )
        else:
            return CandidateExecution(
                sample_id=sample_id,
                raw_completion=raw_completion,
                parsed_type=pred_type,
                parsed_sql=current_sql,
                success=False,
                error=last_error,
                repair_turns=repair_count,
            )

    def vote_and_decide(
        self,
        question_id: str,
        business_id: str,
        candidates: List[CandidateExecution],
        elapsed: float,
    ) -> QuestionInferenceResult:
        """
        Performs majority voting across candidate execution keys.
        If top key agreement share < tau=0.5 or winning candidate is invalid, returns abstain.
        """
        valid_candidates = [c for c in candidates if c.success and c.vote_key is not None]
        total_valid = len(valid_candidates)

        if total_valid == 0:
            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type="abstain",
                final_answer=None,
                confidence=0.0,
                total_samples=len(candidates),
                agreement_count=0,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution={},
                reason="All candidate SQL queries failed execution or returned NULL/empty",
            )

        key_counts = Counter(c.vote_key for c in valid_candidates)
        top_key, top_count = key_counts.most_common(1)[0]
        share = top_count / len(candidates)

        if share >= self.tau:
            winning_candidate = next(c for c in valid_candidates if c.vote_key == top_key)
            final_t = winning_candidate.parsed_type
            final_a = winning_candidate.normalized_value

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
                confidence=share,
                total_samples=len(candidates),
                agreement_count=top_count,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution=dict(key_counts),
            )
        else:
            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type="abstain",
                final_answer=None,
                confidence=share,
                total_samples=len(candidates),
                agreement_count=top_count,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution=dict(key_counts),
                reason=f"Top answer agreement ({top_count}/{len(candidates)} = {share:.2f}) < tau={self.tau}",
            )
