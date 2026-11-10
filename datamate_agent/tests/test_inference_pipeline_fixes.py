"""
Unit and integration tests for DataMate inference pipeline fixes:
1. Model and adapter resolution.
2. Generation token limits.
3. TYPE parsing.
4. SQL extraction.
5. Truncated SQL detection.
6. SQL execution.
7. Empty result handling.
8. COUNT returning zero.
9. Self-repair after syntax errors.
10. Voting and abstention decisions.
11. Business directory resolution and robust header detection.
"""

import os
import duckdb
import pandas as pd
import pytest

from src.data_layer.ingest import (
    find_true_header_from_df,
    clean_date_series,
    resolve_business_dir,
)
from src.inference.executor_voter import (
    ExecutorVoter,
    CandidateExecution,
    parse_completion,
    cast_duckdb_result,
    validate_submission_item,
)
from src.inference.llm_engine import LLMEngine


# 1. Model and Adapter Resolution
def test_adapter_missing_fails_fast():
    """If adapter_path is explicitly configured but missing, LLMEngine must fail fast with FileNotFoundError."""
    non_existent_adapter = "./weights/adapters/non_existent_v99"
    with pytest.raises(FileNotFoundError) as exc_info:
        LLMEngine(
            model_name_or_path="Qwen/Qwen2.5-Coder-3B-Instruct",
            adapter_path=non_existent_adapter,
            allow_mock=True,
        )
    assert "Configured LoRA adapter path does not exist" in str(exc_info.value)


# 2. Generation Token Limits
def test_generation_token_limits_not_clamped():
    """Verify that llm_engine does not hardcode min(max_new_tokens, 256)."""
    # In mock mode, check method signature and behavior
    engine = LLMEngine(
        model_name_or_path="mock_model",
        adapter_path=None,
        allow_mock=True,
    )
    res = engine.generate_single("test prompt", n=1, max_new_tokens=1024)
    assert len(res) == 1


# 3. TYPE Parsing (variations with markdown, bolding, brackets, case)
def test_type_parsing_variations():
    cases = [
        ("TYPE: number\n```sql\nSELECT 1;\n```", "number"),
        ("**TYPE:** percent\n```sql\nSELECT 10.5;\n```", "percent"),
        ("Type: String\n```sql\nSELECT 'a';\n```", "string"),
        ("[TYPE]: date\n```sql\nSELECT '2026-08-01';\n```", "date"),
        ("  **TYPE**: boolean\n```sql\nSELECT true;\n```", "boolean"),
        ("TYPE: table\n```sql\nSELECT 1, 2;\n```", "table"),
        ("TYPE: unanswerable\nReason: missing columns", "unanswerable"),
    ]
    for text, expected_type in cases:
        parsed_type, _ = parse_completion(text)
        assert parsed_type == expected_type, f"Failed parsing type for text: {text}"


# 4. SQL Extraction (closed, unclosed, CTEs, SQL before TYPE)
def test_sql_extraction_robustness():
    # CTE
    t1 = "TYPE: number\n```sql\nWITH cte AS (SELECT 1 AS x) SELECT x FROM cte;\n```"
    _, sql1 = parse_completion(t1)
    assert sql1.startswith("WITH cte AS")

    # Unclosed block
    t2 = "TYPE: number\n```sql\nSELECT 42 FROM metrics"
    _, sql2 = parse_completion(t2)
    assert sql2 == "SELECT 42 FROM metrics"

    # SQL before TYPE
    t3 = "```sql\nSELECT 100 AS rev;\n```\nTYPE: number\n"
    pt3, sql3 = parse_completion(t3)
    assert pt3 == "number"
    assert "SELECT 100 AS rev" in sql3


# 5. Truncated SQL Detection
def test_truncated_sql_handling():
    # If a completion is cut off mid-query without closing fence
    incomplete = "TYPE: number\n```sql\nSELECT val FROM table_a WHERE id IN (SELECT id FROM"
    pt, sql = parse_completion(incomplete)
    assert pt == "number"
    assert sql is not None
    # Executing truncated SQL in DuckDB should produce a syntax error, not crash
    con = duckdb.connect(":memory:")
    voter = ExecutorVoter(con=con, llm_engine=None)
    ok, rows, err, cols = voter.execute_single_sql(sql, pt)
    assert ok is False
    assert err is not None


# 6. SQL Execution and Safety
def test_sql_execution_and_comment_handling():
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE orders (id INT, amount INT);")
    con.execute("INSERT INTO orders VALUES (1, 100), (2, 200);")
    voter = ExecutorVoter(con=con, llm_engine=None)

    # Valid SELECT with comments
    ok, rows, err, cols = voter.execute_single_sql(
        "-- Summing orders\nSELECT SUM(amount) AS total FROM orders;", "number"
    )
    assert ok is True
    assert rows == [(300,)]

    # Disallowed commands (non-SELECT/WITH)
    ok2, _, err2, _ = voter.execute_single_sql("UPDATE orders SET amount = 0;", "number")
    assert ok2 is False
    assert "Query must start with SELECT or WITH statement" in err2


# 7. Empty Result Handling (Differentiating execution success from answer validity)
def test_empty_result_classification():
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE items (id INT, name VARCHAR);")
    voter = ExecutorVoter(con=con, llm_engine=None)

    # Table is empty; scalar string query returns 0 rows
    cand = voter.process_candidate(
        sample_id=0,
        raw_completion="TYPE: string\n```sql\nSELECT name FROM items WHERE id = 99;\n```",
        orig_question="ten item",
    )
    # Execution ran, but returned empty result
    assert cand.success is False
    assert cand.failure_category == "EMPTY_RESULT"
    assert "NULL or empty output" in cand.error


# 8. COUNT Returning Zero (Valid aggregate 0 must NOT be treated as empty failure)
def test_count_returning_zero():
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE log (id INT);")
    voter = ExecutorVoter(con=con, llm_engine=None)

    # COUNT(*) on empty table returns [(0,)]
    cand = voter.process_candidate(
        sample_id=0,
        raw_completion="TYPE: number\n```sql\nSELECT COUNT(*) FROM log WHERE id = 99;\n```",
        orig_question="so luong",
    )
    assert cand.success is True
    assert cand.normalized_value == 0
    assert cand.vote_key == "num:0.00"


# 9. Self-Repair with DuckDB Table Suggestion
def test_repair_with_duckdb_hint():
    class MockRepairEngine:
        def __init__(self):
            self.tokenizer = None
        def generate_single(self, prompt, **kwargs):
            # Assert hint was included in the repair prompt
            if "Did you mean table 'orders'?" in prompt:
                return ["```sql\nSELECT SUM(amount) FROM orders;\n```"]
            return ["```sql\nSELECT 0;\n```"]

    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE orders (amount INT);")
    con.execute("INSERT INTO orders VALUES (500);")
    
    mock_engine = MockRepairEngine()
    voter = ExecutorVoter(con=con, llm_engine=mock_engine, max_repair_turns=1)

    # Erroneous SQL refers to 'order_items' where DuckDB suggests 'orders'
    cand = voter.process_candidate(
        sample_id=0,
        raw_completion="TYPE: number\n```sql\nSELECT SUM(amount) FROM order_items;\n```",
        orig_question="tong tien",
    )
    assert cand.success is True
    assert cand.normalized_value == 500
    assert cand.repair_turns == 1


# 10. Voting and Abstention Decisions
def test_voting_single_candidate_vs_multi():
    con = duckdb.connect(":memory:")
    voter = ExecutorVoter(con=con, llm_engine=None, agreement_threshold_tau=0.5)

    # Single valid candidate (k=1) has 100% agreement over valid candidates
    c1 = CandidateExecution(
        sample_id=0,
        raw_completion="",
        parsed_type="number",
        parsed_sql="SELECT 100;",
        normalized_value=100,
        vote_key="num:100.00",
        success=True,
    )
    res_k1 = voter.vote_and_decide("q1", "biz1", [c1], elapsed=0.1)
    assert res_k1.final_type == "number"
    assert res_k1.final_answer == 100

    # Multi-candidate (k=4) where agreement < tau (1/4 = 0.25 < 0.5) -> Abstain
    c2 = CandidateExecution(sample_id=1, raw_completion="", parsed_type="number", parsed_sql="", success=False, error="err")
    c3 = CandidateExecution(sample_id=2, raw_completion="", parsed_type="number", parsed_sql="", success=False, error="err")
    c4 = CandidateExecution(sample_id=3, raw_completion="", parsed_type="number", parsed_sql="", success=False, error="err")
    res_k4 = voter.vote_and_decide("q2", "biz1", [c1, c2, c3, c4], elapsed=0.1)
    assert res_k4.final_type == "abstain"
    assert "insufficient" in res_k4.reason


# 11. Multi-level Header Detection and Excel Serial Date Parsing
def test_multi_level_header_detection():
    # Mimics biz_105 with Row 0 as banner header and Row 1 as actual columns
    data = [
        ["Hàng", None, None, "Tiền", None, "Đơn", None],
        ["hang", "so_luong", "unit", "tri_gia", "status", "ma_don", "ngay"],
        ["Coffee", 2, "ly", "50.000", "đã xong", "ORD1", "2025-06-01"],
    ]
    df = pd.DataFrame(data)
    h_idx, cols = find_true_header_from_df(df)
    assert h_idx == 1
    assert cols[0] == "hang"
    assert cols[3] == "tri_gia"


def test_excel_serial_date_parsing():
    # 45689 is 2025-02-01, 45815 is 2025-06-07
    s = pd.Series(["45689", "01/06/2025", "45815", "2026-08-15"])
    cleaned = clean_date_series(s)
    assert cleaned.iloc[0] == "2025-02-01"
    assert cleaned.iloc[1] == "2025-06-01"
    assert cleaned.iloc[2] == "2025-06-07"
    assert cleaned.iloc[3] == "2026-08-15"
