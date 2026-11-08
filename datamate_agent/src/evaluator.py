"""
Official Evaluator for DataMate Challenge (Zalo AI Challenge).
Implements exact normalization logic, answer matching per type, and Penalized Accuracy (PA).
"""

import math
import re
import unicodedata
from typing import Any, Dict, List, Optional, Tuple, Union


def normalize_string(text: Any) -> str:
    """
    Normalizes a string according to competition rules:
    1. Unicode NFC
    2. Lowercase
    3. Replace any character that is NOT a letter, digit, or whitespace with a single space
    4. Strip leading/trailing whitespace and collapse multiple spaces into one.
    Preserves Vietnamese diacritics.
    """
    if text is None:
        return ""
    text_str = str(text)
    # 1. Unicode NFC
    nfc_text = unicodedata.normalize("NFC", text_str)
    # 2. Lowercase
    lowered = nfc_text.lower()
    # 3. Replace any character that is NOT a letter, digit, or whitespace with a space
    cleaned = "".join(
        ch if (ch.isalnum() or ch.isspace()) else " " for ch in lowered
    )
    # 4. Strip and collapse multiple spaces
    normalized = re.sub(r"\s+", " ", cleaned).strip()
    return normalized


def _to_float(val: Any) -> Optional[float]:
    try:
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, str):
            clean_str = val.replace(",", "").replace("%", "").strip()
            return float(clean_str)
    except (ValueError, TypeError):
        return None
    return None


def match_number(pred: Any, gold: Any) -> bool:
    """
    number: Exact match. Integers (VND amounts, counts, quantities) or rounded to 2 decimals.
    """
    p_num = _to_float(pred)
    g_num = _to_float(gold)
    if p_num is None or g_num is None:
        return False
    # If gold is effectively an integer
    if math.isclose(g_num, round(g_num), abs_tol=1e-5):
        return math.isclose(p_num, g_num, abs_tol=1e-4) or round(p_num) == round(g_num)
    # Otherwise rounded to 2 decimals
    return round(p_num, 2) == round(g_num, 2)


def match_percent(pred: Any, gold: Any) -> bool:
    """
    percent: Exact match after rounding to 2 decimal places; sign must match.
    """
    p_num = _to_float(pred)
    g_num = _to_float(gold)
    if p_num is None or g_num is None:
        return False
    # Check sign if non-zero
    if abs(p_num) > 1e-6 and abs(g_num) > 1e-6:
        if (p_num < 0) != (g_num < 0):
            return False
    return round(p_num, 2) == round(g_num, 2)


def match_string(pred: Any, gold: Any, aliases: Optional[List[Any]] = None) -> bool:
    """
    string: Normalized exact equality against reference or any item in alias.
    """
    pred_norm = normalize_string(pred)
    gold_norm = normalize_string(gold)
    if pred_norm == gold_norm:
        return True
    if aliases:
        for alias in aliases:
            if isinstance(alias, list):
                for sub_a in alias:
                    if pred_norm == normalize_string(sub_a):
                        return True
            else:
                if pred_norm == normalize_string(alias):
                    return True
    return False


def match_date(pred: Any, gold: Any) -> bool:
    """
    date: Exact match ISO yyyy-mm-dd (or yyyy-mm for month questions).
    """
    p_str = normalize_string(pred).replace(" ", "-")
    g_str = normalize_string(gold).replace(" ", "-")
    return p_str == g_str


def match_boolean(pred: Any, gold: Any) -> bool:
    """
    boolean: Exact match (true / false).
    """
    def _to_bool(val: Any) -> Optional[bool]:
        if isinstance(val, bool):
            return val
        s = normalize_string(val)
        if s in ["true", "dung", "co", "1"]:
            return True
        if s in ["false", "sai", "khong", "0"]:
            return False
        return None

    p_b = _to_bool(pred)
    g_b = _to_bool(gold)
    if p_b is None or g_b is None:
        return False
    return p_b == g_b


def match_element(pred: Any, gold: Any, alias_item: Optional[Any] = None) -> bool:
    """
    Matches a single scalar element in a list or table row.
    """
    if isinstance(gold, (int, float)) or (isinstance(gold, str) and gold.replace("-", "").isdigit()):
        if match_number(pred, gold):
            return True
    aliases = []
    if alias_item is not None:
        if isinstance(alias_item, list):
            aliases = alias_item
        else:
            aliases = [alias_item]
    return match_string(pred, gold, aliases)


def match_list(pred: Any, gold: Any, aliases: Optional[List[Any]] = None) -> bool:
    """
    list: Ordered match position-by-position using string or number rules.
    """
    if not isinstance(pred, list) or not isinstance(gold, list):
        return False
    if len(pred) != len(gold):
        return False

    for idx, (p_item, g_item) in enumerate(zip(pred, gold)):
        pos_alias = None
        if aliases and idx < len(aliases):
            pos_alias = aliases[idx]
        if not match_element(p_item, g_item, pos_alias):
            return False
    return True


def match_table(pred: Any, gold: Any) -> bool:
    """
    table: {"columns": [...], "rows": [[...], ...]}.
    Columns matched by normalized name (or by position if names don't match).
    Rows matched as a set using string/number rules.
    """
    if not isinstance(pred, dict) or not isinstance(gold, dict):
        return False
    pred_rows = pred.get("rows", [])
    gold_rows = gold.get("rows", [])
    if not isinstance(pred_rows, list) or not isinstance(gold_rows, list):
        return False
    if len(pred_rows) != len(gold_rows):
        return False

    # Match rows as a multiset
    unmatched_gold = list(gold_rows)
    for p_row in pred_rows:
        if not isinstance(p_row, list):
            return False
        found_match = False
        for i, g_row in enumerate(unmatched_gold):
            if isinstance(g_row, list) and len(p_row) == len(g_row):
                if all(match_element(p_val, g_val) for p_val, g_val in zip(p_row, g_row)):
                    found_match = True
                    unmatched_gold.pop(i)
                    break
        if not found_match:
            return False

    return len(unmatched_gold) == 0


def is_match(
    pred_type: str,
    pred_answer: Any,
    gold_type: str,
    gold_answer: Any,
    gold_aliases: Optional[List[Any]] = None,
) -> bool:
    """
    Determines if a prediction matches gold reference.
    """
    # 1. Unanswerable check
    gold_is_unanswerable = (
        gold_type == "unanswerable" or gold_answer is None or gold_answer == "unanswerable"
    )
    if gold_is_unanswerable:
        return pred_type == "unanswerable"

    if pred_type == "unanswerable":
        return gold_is_unanswerable

    if pred_type != gold_type:
        # Cross-type forgiveness for number vs percent if both match number/percent
        if {pred_type, gold_type} == {"number", "percent"}:
            return match_percent(pred_answer, gold_answer)
        return False

    # 2. Type-specific matching
    if pred_type == "number":
        return match_number(pred_answer, gold_answer)
    elif pred_type == "percent":
        return match_percent(pred_answer, gold_answer)
    elif pred_type == "string":
        return match_string(pred_answer, gold_answer, gold_aliases)
    elif pred_type == "date":
        return match_date(pred_answer, gold_answer)
    elif pred_type == "boolean":
        return match_boolean(pred_answer, gold_answer)
    elif pred_type == "list":
        return match_list(pred_answer, gold_answer, gold_aliases)
    elif pred_type == "table":
        return match_table(pred_answer, gold_answer)

    return False


def score_single_prediction(
    pred: Dict[str, Any],
    gold: Dict[str, Any],
) -> Tuple[int, str]:
    """
    Computes score for a single prediction item:
    +1: Correct
     0: Abstain
    -1: Wrong
    Returns (score, status_str).
    """
    pred_type = pred.get("type", "").strip().lower()
    pred_answer = pred.get("answer")

    # Abstain scores 0 regardless of gold
    if pred_type == "abstain":
        return 0, "abstain"

    gold_type = gold.get("type", "").strip().lower()
    gold_answer = gold.get("answer")
    gold_aliases = gold.get("alias", [])

    if is_match(pred_type, pred_answer, gold_type, gold_answer, gold_aliases):
        return 1, "correct"
    else:
        return -1, "wrong"


def evaluate_predictions(
    predictions: List[Dict[str, Any]],
    gold_dict: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Evaluates list of predictions against reference dictionary keyed by question id.
    Computes Penalized Accuracy (PA): (1/N) * sum(s_i).
    """
    total = len(gold_dict)
    if total == 0:
        return {
            "penalized_accuracy": 0.0,
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "abstain": 0,
            "unanswered": 0,
            "accuracy": 0.0,
        }

    pred_map = {p["id"]: p for p in predictions if "id" in p}
    total_score = 0
    correct_count = 0
    wrong_count = 0
    abstain_count = 0
    details = []

    for qid, gold in gold_dict.items():
        if qid not in pred_map:
            # Missing prediction defaults to abstain (score 0)
            score = 0
            status = "abstain_missing"
            abstain_count += 1
        else:
            pred = pred_map[qid]
            score, status = score_single_prediction(pred, gold)
            if score == 1:
                correct_count += 1
            elif score == 0:
                abstain_count += 1
            else:
                wrong_count += 1

        total_score += score
        details.append({
            "id": qid,
            "score": score,
            "status": status,
        })

    pa = total_score / total
    answered = correct_count + wrong_count
    acc = (correct_count / answered) if answered > 0 else 0.0

    return {
        "penalized_accuracy": round(pa, 4),
        "total": total,
        "correct": correct_count,
        "wrong": wrong_count,
        "abstain": abstain_count,
        "accuracy": round(acc, 4),
        "details": details,
    }
