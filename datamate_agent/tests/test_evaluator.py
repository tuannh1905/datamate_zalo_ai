import pytest
from src.evaluator import (
    is_match,
    match_boolean,
    match_date,
    match_list,
    match_number,
    match_percent,
    match_string,
    match_table,
    normalize_string,
    score_single_prediction,
)


def test_string_alias_matching():
    # Primary gold is "coca-cola", alias includes "coca"
    assert match_string("coca", "coca-cola", aliases=["coca"]) is True
    assert match_string("pepsi", "coca-cola", aliases=["coca"]) is False

    # Diacritics and case normalization
    assert match_string("  BÁNH MÌ  ", "bánh mì") is True


def test_null_answer_fails():
    # Number with null answer must NOT match gold number
    assert match_number(None, 100) is False
    score, status = score_single_prediction(
        {"id": "q1", "type": "number", "answer": None},
        {"id": "q1", "type": "number", "answer": 100},
    )
    assert score == -1
    assert status == "wrong"


def test_negative_percentages():
    # Correct sign matching
    assert match_percent(-15.25, -15.25) is True
    assert match_percent(15.25, -15.25) is False
    assert match_percent(-15.25, 15.25) is False
    # Rounding to 2 decimals
    assert match_percent(-15.254, -15.25) is True


def test_table_multiset_matching():
    # Tables with different row orders should match (multiset equality)
    gold_table = {
        "columns": ["product", "revenue"],
        "rows": [["Sản phẩm A", 1000], ["Sản phẩm B", 2000]],
    }
    pred_table_reversed = {
        "columns": ["product", "revenue"],
        "rows": [["Sản phẩm B", 2000], ["Sản phẩm A", 1000]],
    }
    pred_table_wrong = {
        "columns": ["product", "revenue"],
        "rows": [["Sản phẩm B", 3000], ["Sản phẩm A", 1000]],
    }
    assert match_table(pred_table_reversed, gold_table) is True
    assert match_table(pred_table_wrong, gold_table) is False


def test_list_ordered_matching():
    # Lists must match position by position
    gold_list = ["Món 1", "Món 2", "Món 3"]
    pred_list_correct = ["Món 1", "Món 2", "Món 3"]
    pred_list_reversed = ["Món 3", "Món 2", "Món 1"]
    assert match_list(pred_list_correct, gold_list) is True
    assert match_list(pred_list_reversed, gold_list) is False


def test_abstain_scoring():
    pred = {"id": "q2", "type": "abstain"}
    gold = {"id": "q2", "type": "number", "answer": 500}
    score, status = score_single_prediction(pred, gold)
    assert score == 0
    assert status == "abstain"


def test_unanswerable_scoring():
    pred = {"id": "q3", "type": "unanswerable"}
    gold = {"id": "q3", "type": "unanswerable", "answer": None}
    score, status = score_single_prediction(pred, gold)
    assert score == 1
    assert status == "correct"
