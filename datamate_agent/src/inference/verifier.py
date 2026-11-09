"""
src/inference/verifier.py - Plausibility & Confidence Verifier for DataMate Challenge.

Evaluates whether an executed SQL candidate result is plausible, type-compliant,
and high-confidence. Allows Tier 1 to exit immediately without wasting GPU compute on
redundant samples.
"""

import math
import re
from typing import Any, Dict, List, Optional, Tuple

from .executor_voter import CandidateExecution


def verify_candidate_execution(
    cand: CandidateExecution,
    orig_question: str,
    as_of_date: Optional[str] = None,
) -> Tuple[bool, float, Optional[str]]:
    """
    Evaluates candidate execution result.
    Returns:
        (is_high_confidence: bool, confidence_score: float, reason: Optional[str])
    """
    # 1. Execution Failure or Syntax Error
    if not cand.success or cand.error:
        err_msg = cand.error or "SQL execution failed"
        return False, 0.0, f"Execution error: {err_msg}"

    # 2. TYPE missing or unanswerable
    pred_type = cand.parsed_type
    if not pred_type or pred_type == "failed":
        return False, 0.0, "Missing or invalid TYPE definition"

    if pred_type == "unanswerable":
        # Unanswerable is a valid answer if reason is coherent
        return True, 0.95, "Legitimate unanswerable prediction"

    # 3. NULL / Empty Result Check
    val = cand.normalized_value
    if val is None:
        return False, 0.1, f"Query executed but returned NULL or empty output for TYPE '{pred_type}'"

    q_lower = orig_question.lower()
    score = 1.0

    # 4. Type-specific boundary and sanity checks
    if pred_type == "number":
        if not isinstance(val, (int, float)) or math.isnan(val):
            return False, 0.2, f"Expected numeric result, got '{type(val).__name__}'"
        
        # Check negative numbers: usually invalid for revenue, debt, inventory, count
        # UNLESS question explicitly asks for growth, change, difference, or profit/loss
        allow_negative = any(kw in q_lower for kw in [
            "tăng", "giảm", "chênh lệch", "hơn", "kém", "lỗ", "âm", "hiệu", "thay đổi"
        ])
        if val < 0 and not allow_negative:
            # Negative amount without explicit change question is suspicious
            return False, 0.4, f"Negative value ({val}) for absolute metric without difference context"

    elif pred_type == "percent":
        if not isinstance(val, (int, float)) or math.isnan(val):
            return False, 0.2, f"Expected numeric percentage, got '{type(val).__name__}'"
        
        # Percentage share (tỉ trọng, tỉ lệ huỷ, tỉ lệ đơn) is strictly in [0, 100]
        is_share_ratio = any(kw in q_lower for kw in ["tỉ trọng", "ti trong", "tỉ lệ huỷ", "ti le huy", "tỷ lệ"])
        if is_share_ratio and (val < 0.0 or val > 100.0):
            return False, 0.3, f"Percentage ratio {val}% out of expected bounds [0, 100]"

    elif pred_type == "date":
        if not isinstance(val, str) or len(val.strip()) < 7:
            return False, 0.2, f"Invalid date output format: '{val}'"
        # Must match ISO YYYY-MM-DD or YYYY-MM
        if not re.match(r"^\d{4}-\d{2}(-\d{2})?$", val.strip()):
            return False, 0.3, f"Date string does not match ISO format: '{val}'"

    elif pred_type == "string":
        if not isinstance(val, str) or not val.strip() or val.strip().lower() in ["none", "null", "nan"]:
            return False, 0.2, f"Invalid or empty string result: '{val}'"

    elif pred_type == "boolean":
        if not isinstance(val, bool):
            return False, 0.2, f"Expected boolean, got '{type(val).__name__}'"

    elif pred_type == "list":
        if not isinstance(val, list) or len(val) == 0:
            return False, 0.2, "List result is empty"
        if any(item is None or str(item).strip().lower() in ["none", "null", "nan"] for item in val):
            return False, 0.4, "List contains NULL or empty elements"

    elif pred_type == "table":
        if not isinstance(val, dict) or not val.get("rows"):
            return False, 0.2, "Table result is missing or contains 0 rows"

    # All checks passed: high confidence
    is_high = score >= 0.9
    return is_high, score, None
