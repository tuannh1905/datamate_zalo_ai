"""
tests/test_p1_workflow_optimizations.py - Tests for Rule Router, Confidence Verifier, and Tiered Inference.
"""

import duckdb
import pytest

from src.context.rule_router import parse_markdown_sections, route_rulebook
from src.inference.executor_voter import CandidateExecution, ExecutorVoter
from src.inference.verifier import verify_candidate_execution


SAMPLE_RULEBOOK = """
# DataMate Rulebook

Mọi đáp án tính theo luật dưới đây. Hôm nay là trường as_of_date.

## 1. Đơn hàng và doanh thu
Đơn tính vào doanh thu là đơn không huỷ và không trả hàng.
Bán được bao nhiêu tiền là doanh thu.

## 2. Thời gian
Ngày X, hôm nay, hôm qua. Tuần bắt đầu thứ Hai.

## 3. Xếp hạng
Mặt hàng bán chạy theo số lượng quy về đơn vị cơ bản.

## 4. Công nợ
Đơn được tính vào nợ là đơn không huỷ.
Nợ một đơn tại ngày X là phần chưa trả của tổng đơn.

## 5. Kho, nhập hàng, giá vốn
Tồn kho hết hôm nay. Giá vốn bình quân gia quyền.

## 6. Theo ngành
### Cà phê
Size M, Size L.

## 7. Không trả lời được
Câu không trả lời được khi dữ liệu không đủ. Nộp type unanswerable.
""".strip()


def test_rule_router_revenue():
    q = "Doanh thu tháng này của quán là bao nhiêu tiền?"
    routed = route_rulebook(SAMPLE_RULEBOOK, q)
    assert "## 1. Đơn hàng và doanh thu" in routed
    assert "## 2. Thời gian" in routed
    assert "## 7. Không trả lời được" in routed
    assert "## 4. Công nợ" not in routed
    assert "## 5. Kho, nhập hàng, giá vốn" not in routed


def test_rule_router_debt():
    q = "Tính tổng công nợ khách hàng còn nợ đến hết ngày hôm nay?"
    routed = route_rulebook(SAMPLE_RULEBOOK, q)
    assert "## 4. Công nợ" in routed
    assert "## 2. Thời gian" in routed
    assert "## 7. Không trả lời được" in routed
    assert "## 1. Đơn hàng và doanh thu" not in routed
    assert "## 5. Kho, nhập hàng, giá vốn" not in routed


def test_rule_router_inventory():
    q = "Giá trị hàng tồn kho còn lại là bao nhiêu?"
    routed = route_rulebook(SAMPLE_RULEBOOK, q)
    assert "## 5. Kho, nhập hàng, giá vốn" in routed
    assert "## 7. Không trả lời được" in routed
    assert "## 4. Công nợ" not in routed


def test_rule_router_fallback():
    # Empty question should safely return full rulebook
    routed = route_rulebook(SAMPLE_RULEBOOK, "")
    assert routed == SAMPLE_RULEBOOK


def test_verifier_number_valid():
    cand = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="number",
        parsed_sql="SELECT 1500000",
        normalized_value=1500000,
        success=True,
    )
    is_high, score, err = verify_candidate_execution(cand, "Doanh thu là bao nhiêu?")
    assert is_high is True
    assert score >= 0.9
    assert err is None


def test_verifier_negative_number_without_diff():
    cand = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="number",
        parsed_sql="SELECT -500",
        normalized_value=-500,
        success=True,
    )
    is_high, score, err = verify_candidate_execution(cand, "Doanh thu bán được bao nhiêu?")
    assert is_high is False  # Negative sales amount without change question is rejected
    assert "Negative value" in err


def test_verifier_negative_number_with_growth():
    cand = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="number",
        parsed_sql="SELECT -500",
        normalized_value=-500,
        success=True,
    )
    # Question explicitly mentions 'giảm' / 'chênh lệch'
    is_high, score, err = verify_candidate_execution(cand, "Doanh thu tuần này tăng hay giảm bao nhiêu so với tuần trước?")
    assert is_high is True


def test_verifier_null_rejected():
    cand = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="number",
        parsed_sql="SELECT NULL",
        normalized_value=None,
        success=False,
        error="Query returned NULL",
    )
    is_high, score, err = verify_candidate_execution(cand, "Tính tổng tiền")
    assert is_high is False
    assert score == 0.0


def test_verifier_unanswerable():
    cand = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="unanswerable",
        parsed_sql="SELECT NULL",
        normalized_value=None,
        success=True,
    )
    is_high, score, _ = verify_candidate_execution(cand, "Hỏi về lợi nhuận không có cột")
    assert is_high is True
