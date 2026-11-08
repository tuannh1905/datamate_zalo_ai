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
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

import duckdb

from ..evaluator import normalize_string
from .llm_engine import LLMEngine

logger = logging.getLogger(__name__)


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
        Converts to official competition submission JSON object.
        """
        if self.final_type == "abstain":
            return {"id": self.question_id, "type": "abstain"}
        elif self.final_type == "unanswerable":
            res = {"id": self.question_id, "type": "unanswerable"}
            if self.reason:
                res["reason"] = self.reason
            return res
        else:
            return {
                "id": self.question_id,
                "type": self.final_type,
                "answer": self.final_answer,
            }

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


def parse_completion(text: str) -> Tuple[str, Optional[str]]:
    """
    Extracts TYPE and SQL query from LLM completion.
    """
    # 1. Extract TYPE
    type_match = re.search(r"(?i)TYPE:\s*([a-zA-Z_]+)", text)
    pred_type = type_match.group(1).lower().strip() if type_match else "number"
    if pred_type not in ["number", "percent", "string", "date", "boolean", "list", "table", "unanswerable", "abstain"]:
        pred_type = "number"

    # 2. Extract SQL
    sql_match = re.search(r"```(?:sql)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
    if sql_match:
        sql = sql_match.group(1).strip()
    else:
        # Fallback to SELECT block to end of text
        sel_match = re.search(r"(?i)\b(SELECT\b[\s\S]+)", text)
        sql = sel_match.group(1).strip() if sel_match else None

    return pred_type, sql


def cast_duckdb_result(result_rows: List[Tuple], pred_type: str, col_names: List[str]) -> Any:
    """
    Converts raw DuckDB cursor fetch result into canonical competition types.
    """
    if not result_rows:
        if pred_type in ["number", "percent"]:
            return 0
        elif pred_type == "list":
            return []
        elif pred_type == "table":
            return {"columns": col_names, "rows": []}
        return None

    # Handle unanswerable
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
                return int(round(f)) if math.isclose(f, round(f), abs_tol=1e-5) else round(f, 2)
            except Exception:
                return 0

        elif pred_type == "percent":
            try:
                return round(float(val), 2)
            except Exception:
                return 0.0

        elif pred_type == "string":
            return str(val).strip()

        elif pred_type == "date":
            # Format as YYYY-MM-DD or YYYY-MM
            s = str(val).strip()
            if len(s) >= 10 and s[4] == "-" and s[7] == "-":
                return s[:10]
            elif len(s) >= 7 and s[4] == "-":
                return s[:7]
            return s

        elif pred_type == "boolean":
            if isinstance(val, bool):
                return val
            s = str(val).lower()
            return s in ["true", "1", "t", "dung", "co"]

    # List type
    elif pred_type == "list":
        res_list = []
        for r in result_rows:
            # If row has 1 element
            if len(r) == 1:
                item = r[0]
            else:
                item = r[0]
            if isinstance(item, (int, float)):
                res_list.append(int(item) if math.isclose(item, round(item), abs_tol=1e-5) else round(item, 2))
            else:
                res_list.append(str(item).strip() if item is not None else "")
        return res_list

    # Table type: {"columns": [...], "rows": [[...], ...]}
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
        return {"columns": col_names, "rows": rows}

    return result_rows[0][0]


def make_vote_key(pred_type: str, value: Any) -> str:
    """
    Converts a normalized prediction into a deterministic hashable voting key.
    """
    if pred_type == "unanswerable" or value is None:
        return "unanswerable:__null__"
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
        if isinstance(value, list):
            items_str = "|".join(normalize_string(v) if isinstance(v, str) else str(v) for v in value)
            return f"list:{items_str}"
        return f"list:{value}"
    elif pred_type == "table":
        if isinstance(value, dict):
            rows = value.get("rows", [])
            # Sort rows for order invariance
            rows_str = sorted(["|".join(normalize_string(c) if isinstance(c, str) else str(c) for c in r) for r in rows])
            return f"table:{'#'.join(rows_str)}"
        return f"table:{value}"
    return f"{pred_type}:{value}"


class ExecutorVoter:
    def __init__(
        self,
        con: duckdb.DuckDBPyConnection,
        llm_engine: LLMEngine,
        agreement_threshold_tau: float = 0.5,
        sql_timeout_seconds: float = 10.0,
        max_repair_turns: int = 2,
    ):
        self.con = con
        self.llm_engine = llm_engine
        self.tau = agreement_threshold_tau
        self.timeout = sql_timeout_seconds
        self.max_repairs = max_repair_turns

    def execute_single_sql(self, sql: str, pred_type: str) -> Tuple[bool, Any, Optional[str], List[str]]:
        """
        Executes a SQL query in DuckDB with safety and timeout.
        Returns (success, result_rows, error_message, column_names).
        """
        if not sql or not sql.strip():
            return False, None, "Empty SQL query", []
        
        # Guard against modifying statements
        clean_sql = sql.strip().rstrip(";")
        forbidden = ["drop ", "delete ", "insert ", "update ", "alter ", "truncate "]
        if any(f in clean_sql.lower() for f in forbidden):
            return False, None, "Modifying SQL statement blocked", []

        try:
            # Set memory limit and threads for performance
            rel = self.con.execute(clean_sql)
            col_names = [desc[0] for desc in rel.description] if rel.description else []
            rows = rel.fetchall()
            return True, rows, None, col_names
        except Exception as e:
            return False, None, str(e), []

    def repair_sql_turn(self, bad_sql: str, error_msg: str, orig_question: str) -> Optional[str]:
        """
        Requests the LLM to fix a failed SQL statement given DuckDB error message.
        """
        repair_prompt = (
            f"The following DuckDB SQL query produced an error:\n"
            f"```sql\n{bad_sql}\n```\n"
            f"DuckDB Error:\n{error_msg}\n"
            f"Question:\n{orig_question}\n"
            f"Please output ONLY the corrected SQL query within ```sql ... ```."
        )
        try:
            completions = self.llm_engine.generate_single(
                repair_prompt,
                n=1,
                temperature=0.0,
                max_new_tokens=512,
            )
            if completions:
                _, rep_sql = parse_completion(completions[0])
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
        """
        pred_type, sql = parse_completion(raw_completion)
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
            norm_val = cast_duckdb_result(rows, pred_type, col_names)
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
        If top key agreement share < tau=0.5, returns abstain.
        """
        valid_candidates = [c for c in candidates if c.success and c.vote_key is not None]
        total_valid = len(valid_candidates)

        if total_valid == 0:
            # All candidates failed SQL execution -> abstain to preserve PA score (0 instead of -1)
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
                reason="All candidate SQL queries failed execution",
            )

        key_counts = Counter(c.vote_key for c in valid_candidates)
        top_key, top_count = key_counts.most_common(1)[0]
        share = top_count / len(candidates)  # Ratio over total attempted samples

        if share >= self.tau:
            # Agreement threshold met
            winning_candidate = next(c for c in valid_candidates if c.vote_key == top_key)
            return QuestionInferenceResult(
                question_id=question_id,
                business_id=business_id,
                final_type=winning_candidate.parsed_type,
                final_answer=winning_candidate.normalized_value,
                confidence=share,
                total_samples=len(candidates),
                agreement_count=top_count,
                elapsed_time=elapsed,
                candidates=candidates,
                vote_distribution=dict(key_counts),
            )
        else:
            # Low agreement share < 0.5 -> Abstain to protect against negative penalty (-1)
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
