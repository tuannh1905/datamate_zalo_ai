import duckdb
from src.inference.executor_voter import (
    ExecutorVoter,
    cast_duckdb_result,
    validate_submission_item,
    make_vote_key,
    QuestionInferenceResult,
    CandidateExecution,
)


def test_validate_submission_item():
    assert validate_submission_item({"id": "q1", "type": "number", "answer": 42}) is True
    assert validate_submission_item({"id": "q2", "type": "percent", "answer": -12.45}) is True
    assert validate_submission_item({"id": "q3", "type": "string", "answer": "Coca"}) is True
    assert validate_submission_item({"id": "q4", "type": "date", "answer": "2026-08-15"}) is True
    assert validate_submission_item({"id": "q5", "type": "boolean", "answer": True}) is True
    assert validate_submission_item({"id": "q6", "type": "list", "answer": ["A", "B"]}) is True
    assert validate_submission_item({"id": "q7", "type": "table", "answer": {"columns": ["c"], "rows": [["v"]]}}) is True
    assert validate_submission_item({"id": "q8", "type": "unanswerable"}) is True
    assert validate_submission_item({"id": "q9", "type": "abstain"}) is True

    # Invalid cases
    assert validate_submission_item({"id": "q10", "type": "number", "answer": None}) is False
    assert validate_submission_item({"id": "q11", "type": "string", "answer": ""}) is False
    assert validate_submission_item({"id": "q12", "type": "list", "answer": []}) is False
    assert validate_submission_item({"id": "q13", "type": "number", "answer": float("nan")}) is False


def test_no_null_candidate_voting():
    # When query returns NULL, it should not participate in voting or produce answer: null
    con = duckdb.connect(database=":memory:")
    con.execute("CREATE TABLE t (val INT);")
    # Table is empty, SUM returns NULL
    voter = ExecutorVoter(con=con, llm_engine=None)
    
    cand = voter.process_candidate(
        sample_id=0,
        raw_completion="Notes:\n- sum\nTYPE: number\n```sql\nSELECT SUM(val) FROM t;\n```",
        orig_question="tong",
    )
    assert cand.success is False
    assert cand.normalized_value is None
    assert cand.vote_key is None


def test_sql_safety_and_comments():
    con = duckdb.connect(database=":memory:")
    con.execute("CREATE TABLE orders (id INT, last_update TIMESTAMP);")
    con.execute("INSERT INTO orders VALUES (1, '2026-01-01 00:00:00');")
    voter = ExecutorVoter(con=con, llm_engine=None)

    # Query with column name 'last_update' and comments should NOT be blocked
    sql_with_update_col = """
    -- Calculate from orders table
    SELECT id, last_update FROM orders;
    """
    ok, rows, err, cols = voter.execute_single_sql(sql_with_update_col, "table")
    assert ok is True
    assert len(rows) == 1

    # Malicious DROP statement must be blocked
    malicious = "DROP TABLE orders;"
    ok_m, _, err_m, _ = voter.execute_single_sql(malicious, "table")
    assert ok_m is False
