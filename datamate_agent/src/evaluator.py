"""
Evaluator for DataMate Challenge (Community Reproduction / Proxy Evaluator).
Implements exact normalization logic, answer matching per type, canonical voting key derivation,
and Penalized Accuracy (PA).
"""

import datetime
from decimal import Decimal
import math
import re
import unicodedata
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import numpy as np
except ImportError:
    np = None

try:
    import pandas as pd
except ImportError:
    pd = None


def normalize_string(text: Any) -> str:
    """
    Normalizes a string according to competition rules:
    1. Unicode NFC
    2. Lowercase
    3. Replace any character that is NOT a letter, digit, or whitespace (and replace '_') with a single space
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
    # 3. Replace any char that is not alnum or space (and replace _) with space
    cleaned = "".join(
        ch if (ch.isalnum() or ch.isspace()) and ch != "_" else " " for ch in lowered
    )
    # 4. Strip and collapse multiple spaces
    normalized = re.sub(r"\s+", " ", cleaned).strip()
    return normalized


def _to_float(val: Any) -> Optional[float]:
    try:
        if val is None:
            return None
        if isinstance(val, (int, float)):
            if math.isnan(val):
                return None
            return float(val)
        if isinstance(val, Decimal):
            f = float(val)
            return None if math.isnan(f) else f
        if np is not None and isinstance(val, (np.number, np.bool_)):
            f = float(val)
            return None if math.isnan(f) else f
        if isinstance(val, str):
            clean_str = val.replace("%", "").strip()
            if not clean_str:
                return None
            # Handle Vietnamese / European decimal comma
            if "," in clean_str and "." not in clean_str:
                parts = clean_str.split(",")
                if len(parts) == 2 and len(parts[1]) in (1, 2) and parts[0].lstrip("-").isdigit():
                    clean_str = clean_str.replace(",", ".")
                elif len(parts) == 2 and len(parts[1]) == 3 and parts[0].lstrip("-").isdigit():
                    clean_str = clean_str.replace(",", "")
                else:
                    clean_str = clean_str.replace(",", ".")
            elif "," in clean_str and "." in clean_str:
                if clean_str.rfind(".") < clean_str.rfind(","):
                    clean_str = clean_str.replace(".", "").replace(",", ".")
                else:
                    clean_str = clean_str.replace(",", "")
            f = float(clean_str)
            return None if math.isnan(f) else f
    except (ValueError, TypeError):
        return None
    return None


def canonicalize_for_voting(ans_type: Optional[str], raw_df_or_val: Any) -> Tuple[Any, Optional[str]]:
    """
    Canonicalizes raw execution outputs or references for voting and scoring.
    Used by BOTH ExecutorVoter and Evaluator to ensure equivalent answers produce identical keys:
    - number / percent: Decimal/numpy/scalar -> float -> round(2). If is_integer() -> int.
    - string: Unicode NFC -> .lower() -> strip non-alphanumeric (keep Vietnamese letters & digits, replace _ with space) -> collapse whitespace.
    - date: ISO YYYY-MM-DD (or YYYY-MM).
    - boolean: Cast truthy/falsy -> bool.
    - list: Convert 1-col DF or iterable to list, normalizing elements.
    - table: Convert DF/dict to {"columns": [...], "rows": [[...], ...]} and generate order-independent canonical row-set key.
    - unanswerable: (None, "unanswerable")
    - abstain: (None, "abstain")

    Returns:
        (clean_display_value, canonical_voting_key)
        If extraction fails or value is invalid/NULL, returns (None, None).
    """
    if not ans_type:
        return None, None
    ans_type = ans_type.strip().lower()

    if ans_type == "unanswerable":
        return None, "unanswerable:__null__"
    if ans_type == "abstain":
        return None, "abstain"

    if raw_df_or_val is None:
        return None, None

    # Helper: unpack single-element containers (DataFrames, Series, cursor rows like [(val,)])
    val = raw_df_or_val

    # Handle pandas DataFrame / Series
    if pd is not None:
        if isinstance(val, pd.DataFrame):
            if ans_type in ["number", "percent", "string", "date", "boolean"]:
                if val.empty or val.shape[0] == 0 or val.shape[1] == 0:
                    return None, None
                val = val.iloc[0, 0]
            elif ans_type == "list":
                if val.empty:
                    return None, None
                # If 1-column or 1-row
                if val.shape[1] == 1:
                    val = val.iloc[:, 0].tolist()
                elif val.shape[0] == 1:
                    val = val.iloc[0, :].tolist()
                else:
                    val = val.iloc[:, 0].tolist()
            elif ans_type == "table":
                if val.empty:
                    return None, None
                cols = [str(c) for c in val.columns]
                rows = val.values.tolist()
                val = {"columns": cols, "rows": rows}
        elif isinstance(val, pd.Series):
            if ans_type in ["number", "percent", "string", "date", "boolean"]:
                if val.empty:
                    return None, None
                val = val.iloc[0]
            elif ans_type == "list":
                val = val.tolist()

    # Handle DuckDB cursor rows (e.g. [(val,)] or [('a',), ('b',)])
    if isinstance(val, (list, tuple)):
        if ans_type in ["number", "percent", "string", "date", "boolean"]:
            if len(val) == 0:
                return None, None
            first = val[0]
            if isinstance(first, (list, tuple)):
                if len(first) == 0:
                    return None, None
                val = first[0]
            else:
                val = first
        elif ans_type == "list":
            # list of single-item tuples: [('A',), ('B',)] -> ['A', 'B']
            unpacked = []
            for item in val:
                if isinstance(item, (list, tuple)):
                    unpacked.append(item[0] if len(item) > 0 else None)
                else:
                    unpacked.append(item)
            val = unpacked

    if val is None:
        return None, None

    # Check for pandas/numpy NaN
    if not isinstance(val, (list, tuple, dict)) and pd is not None:
        try:
            if pd.isna(val):
                return None, None
        except Exception:
            pass

    # 1. NUMBER / PERCENT
    if ans_type == "number":
        f = _to_float(val)
        if f is None or math.isnan(f):
            return None, None
        rounded = round(f, 2)
        clean_val = int(rounded) if rounded.is_integer() else rounded
        key = f"num:{rounded:.2f}"
        return clean_val, key

    elif ans_type == "percent":
        f = _to_float(val)
        if f is None or math.isnan(f):
            return None, None
        rounded = round(f, 2)
        clean_val = int(rounded) if rounded.is_integer() else rounded
        key = f"pct:{rounded:.2f}"
        return clean_val, key

    # 2. STRING
    elif ans_type == "string":
        s = str(val).strip()
        if not s or s.lower() in ("none", "null", "nan"):
            return None, None
        norm = normalize_string(s)
        if not norm:
            return None, None
        clean_val = s
        key = f"str:{norm}"
        return clean_val, key

    # 3. DATE
    elif ans_type == "date":
        if isinstance(val, (datetime.date, datetime.datetime)):
            clean_val = val.strftime("%Y-%m-%d")
        else:
            s = str(val).strip()
            # Normalize dashes / slashes
            s = s.replace("/", "-").replace(".", "-")
            # Extract YYYY-MM-DD or YYYY-MM
            m_ymd = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})", s)
            m_ym = re.match(r"^(\d{4})-(\d{1,2})$", s)
            m_dmy = re.match(r"^(\d{1,2})-(\d{1,2})-(\d{4})", s)
            if m_ymd:
                y, m, d = int(m_ymd.group(1)), int(m_ymd.group(2)), int(m_ymd.group(3))
                clean_val = f"{y:04d}-{m:02d}-{d:02d}"
            elif m_dmy:
                d, m, y = int(m_dmy.group(1)), int(m_dmy.group(2)), int(m_dmy.group(3))
                clean_val = f"{y:04d}-{m:02d}-{d:02d}"
            elif m_ym:
                y, m = int(m_ym.group(1)), int(m_ym.group(2))
                clean_val = f"{y:04d}-{m:02d}"
            else:
                clean_val = s
        if not clean_val:
            return None, None
        key = f"date:{clean_val}"
        return clean_val, key

    # 4. BOOLEAN
    elif ans_type == "boolean":
        if isinstance(val, bool):
            clean_val = val
        else:
            s_bool = normalize_string(val)
            if s_bool in ("true", "1", "dung", "co"):
                clean_val = True
            elif s_bool in ("false", "0", "sai", "khong"):
                clean_val = False
            else:
                return None, None
        key = f"bool:{clean_val}"
        return clean_val, key

    # 5. LIST
    elif ans_type == "list":
        if not isinstance(val, (list, tuple)):
            return None, None
        clean_list = []
        elem_keys = []
        for item in val:
            if item is None:
                continue
            if pd is not None and not isinstance(item, (list, tuple, dict)):
                try:
                    if pd.isna(item):
                        continue
                except Exception:
                    pass
            # Try float/number first
            f_item = _to_float(item)
            if f_item is not None and not isinstance(item, bool):
                r_item = round(f_item, 2)
                item_val = int(r_item) if r_item.is_integer() else r_item
                clean_list.append(item_val)
                elem_keys.append(f"num:{item_val}")
            else:
                s_item = str(item).strip()
                if not s_item or s_item.lower() in ("none", "null", "nan"):
                    continue
                clean_list.append(s_item)
                elem_keys.append(f"str:{normalize_string(s_item)}")
        if not clean_list:
            return None, None
        key = f"list:{'|'.join(elem_keys)}"
        return clean_list, key

    # 6. TABLE
    elif ans_type == "table":
        if not isinstance(val, dict):
            return None, None
        cols = val.get("columns", [])
        rows = val.get("rows", [])
        if not isinstance(rows, list) or len(rows) == 0:
            return None, None

        clean_rows = []
        canonical_row_strings = []

        for row in rows:
            if not isinstance(row, (list, tuple)):
                continue
            clean_row = []
            row_keys = []
            for cell in row:
                if cell is None:
                    clean_row.append(None)
                    row_keys.append("null")
                    continue
                if pd is not None and not isinstance(cell, (list, tuple, dict)):
                    try:
                        if pd.isna(cell):
                            clean_row.append(None)
                            row_keys.append("null")
                            continue
                    except Exception:
                        pass
                f_cell = _to_float(cell)
                if f_cell is not None and not isinstance(cell, bool):
                    r_cell = round(f_cell, 2)
                    c_val = int(r_cell) if r_cell.is_integer() else r_cell
                    clean_row.append(c_val)
                    row_keys.append(f"num:{c_val}")
                else:
                    c_str = str(cell).strip()
                    clean_row.append(c_str)
                    row_keys.append(f"str:{normalize_string(c_str)}")
            clean_rows.append(clean_row)
            canonical_row_strings.append("|".join(row_keys))

        if not clean_rows:
            return None, None

        # Sort row strings to make table voting key order-independent
        sorted_row_keys = sorted(canonical_row_strings)
        clean_table = {
            "columns": [str(c).strip() for c in cols] if isinstance(cols, list) else [],
            "rows": clean_rows,
        }
        key = f"table:{'#'.join(sorted_row_keys)}"
        return clean_table, key

    return None, None


def match_number(pred: Any, gold: Any) -> bool:
    """
    number: Exact match. Integers (VND amounts, counts, quantities) or rounded to 2 decimals.
    """
    p_clean, p_key = canonicalize_for_voting("number", pred)
    g_clean, g_key = canonicalize_for_voting("number", gold)
    if p_key is None or g_key is None:
        return False
    return p_key == g_key


def match_percent(pred: Any, gold: Any) -> bool:
    """
    percent: Exact match after rounding to 2 decimal places; sign must match.
    """
    p_clean, p_key = canonicalize_for_voting("percent", pred)
    g_clean, g_key = canonicalize_for_voting("percent", gold)
    if p_clean is None or g_clean is None:
        return False
    # Check sign if non-zero
    if abs(p_clean) > 1e-6 and abs(g_clean) > 1e-6:
        if (p_clean < 0) != (g_clean < 0):
            return False
    return p_key == g_key


def match_string(pred: Any, gold: Any, aliases: Optional[List[Any]] = None) -> bool:
    """
    string: Normalized exact equality against reference or any item in alias.
    """
    p_clean, p_key = canonicalize_for_voting("string", pred)
    g_clean, g_key = canonicalize_for_voting("string", gold)
    if p_key is None or g_key is None:
        return False
    if p_key == g_key:
        return True
    if aliases:
        for alias in aliases:
            if isinstance(alias, list):
                for sub_a in alias:
                    _, sub_key = canonicalize_for_voting("string", sub_a)
                    if p_key == sub_key:
                        return True
            else:
                _, a_key = canonicalize_for_voting("string", alias)
                if p_key == a_key:
                    return True
    return False


def match_date(pred: Any, gold: Any) -> bool:
    """
    date: Exact match ISO yyyy-mm-dd (or yyyy-mm for month questions).
    """
    p_clean, p_key = canonicalize_for_voting("date", pred)
    g_clean, g_key = canonicalize_for_voting("date", gold)
    if p_key is None or g_key is None:
        return False
    return p_key == g_key


def match_boolean(pred: Any, gold: Any) -> bool:
    """
    boolean: Exact match (true / false).
    """
    p_clean, p_key = canonicalize_for_voting("boolean", pred)
    g_clean, g_key = canonicalize_for_voting("boolean", gold)
    if p_key is None or g_key is None:
        return False
    return p_key == g_key


def match_element(pred: Any, gold: Any, alias_item: Optional[Any] = None) -> bool:
    """
    Matches a single scalar element in a list or table row.
    """
    # Check number match first if both look numeric
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
    p_clean, _ = canonicalize_for_voting("list", pred)
    g_clean, _ = canonicalize_for_voting("list", gold)
    if not isinstance(p_clean, list) or not isinstance(g_clean, list):
        return False
    if len(p_clean) != len(g_clean):
        return False

    for idx, (p_item, g_item) in enumerate(zip(p_clean, g_clean)):
        pos_alias = None
        if aliases and idx < len(aliases):
            pos_alias = aliases[idx]
        if not match_element(p_item, g_item, pos_alias):
            return False
    return True


def match_table(pred: Any, gold: Any) -> bool:
    """
    table: {"columns": [...], "rows": [[...], ...]}.
    Rows matched as a multiset using canonical string/number rules.
    """
    p_clean, p_key = canonicalize_for_voting("table", pred)
    g_clean, g_key = canonicalize_for_voting("table", gold)
    if p_key is None or g_key is None:
        return False
    if p_key == g_key:
        return True

    pred_rows = p_clean.get("rows", [])
    gold_rows = g_clean.get("rows", [])
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
    pred_t = (pred_type or "").strip().lower()
    gold_t = (gold_type or "").strip().lower()

    # 1. Unanswerable check
    gold_is_unanswerable = (
        gold_t == "unanswerable" or gold_answer is None or gold_answer == "unanswerable"
    )
    if gold_is_unanswerable:
        return pred_t == "unanswerable"

    if pred_t == "unanswerable":
        return gold_is_unanswerable

    if pred_t != gold_t:
        # Cross-type forgiveness for number vs percent
        if {pred_t, gold_t} == {"number", "percent"}:
            return match_percent(pred_answer, gold_answer)
        return False

    # 2. Type-specific matching
    if pred_t == "number":
        return match_number(pred_answer, gold_answer)
    elif pred_t == "percent":
        return match_percent(pred_answer, gold_answer)
    elif pred_t == "string":
        return match_string(pred_answer, gold_answer, gold_aliases)
    elif pred_t == "date":
        return match_date(pred_answer, gold_answer)
    elif pred_t == "boolean":
        return match_boolean(pred_answer, gold_answer)
    elif pred_t == "list":
        return match_list(pred_answer, gold_answer, gold_aliases)
    elif pred_t == "table":
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
