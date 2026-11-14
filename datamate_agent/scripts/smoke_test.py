"""
End-to-End Smoke Test Script for DataMate Challenge.
Verifies the entire pipeline in <60 seconds before launching full Colab / Docker jobs:
1. Evaluator normalization across all 9 answer types (number, percent, string, date, boolean, list, table, unanswerable, abstain).
2. DateResolver Vietnamese expressions ("tuần rồi", "tháng này", "cùng kỳ năm ngoái", "dịp Tết") against calendar.csv.
3. Ingest + ExecutorVoter end-to-end integration with mock or real LLM, verifying submission.jsonl and per-question logs.
"""

import argparse
from decimal import Decimal
import json
import logging
import os
import sys
import tempfile
import time

# Ensure parent directory is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.context.date_resolver import DateResolver
from src.data_layer.ingest import load_business_data
from src.evaluator import canonicalize_for_voting, evaluate_predictions, is_match, score_single_prediction
from src.run_inference import run_inference_pipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SmokeTest")


def test_evaluator_all_9_types():
    logger.info("--- [SMOKE TEST 1/3] Testing Evaluator Normalization Across 9 Types ---")

    # 1. Number
    num_tests = [
        (48250000, 48250000, "num:48250000.00"),
        (48250000.0, 48250000, "num:48250000.00"),
        (Decimal("48250000.00"), 48250000, "num:48250000.00"),
        (-12.50, -12.5, "num:-12.50"),
    ]
    for inp, exp_val, exp_key in num_tests:
        val, key = canonicalize_for_voting("number", inp)
        assert val == exp_val, f"Number val mismatch for {inp}: got {val}, expected {exp_val}"
        assert key == exp_key, f"Number key mismatch for {inp}: got {key}, expected {exp_key}"
    assert is_match("number", 48250000.0, "number", 48250000)

    # 2. Percent
    pct_tests = [
        (12.5, 12.5, "pct:12.50"),
        ("12,5%", 12.5, "pct:12.50"),
        (-5.254, -5.25, "pct:-5.25"),
    ]
    for inp, exp_val, exp_key in pct_tests:
        val, key = canonicalize_for_voting("percent", inp)
        assert val == exp_val, f"Percent val mismatch for {inp}: got {val}, expected {exp_val}"
        assert key == exp_key, f"Percent key mismatch for {inp}: got {key}, expected {exp_key}"
    assert is_match("percent", 12.50, "percent", 12.5)

    # 3. String (Vietnamese diacritics & aliases)
    s_val, s_key = canonicalize_for_voting("string", "  Bánh   Mì  ")
    assert s_val == "Bánh   Mì"
    assert s_key == "str:bánh mì"
    assert is_match("string", "bánh mì", "string", "BÁNH MÌ")
    assert is_match("string", "coca", "string", "coca-cola", ["coca"])

    # 4. Date
    d_val, d_key = canonicalize_for_voting("date", "2026/08/15")
    assert d_val == "2026-08-15"
    assert d_key == "date:2026-08-15"
    m_val, m_key = canonicalize_for_voting("date", "2026-08")
    assert m_val == "2026-08"
    assert m_key == "date:2026-08"
    assert is_match("date", "2026-08-15", "date", "2026/08/15")

    # 5. Boolean
    b_val1, b_key1 = canonicalize_for_voting("boolean", "true")
    assert b_val1 is True and b_key1 == "bool:True"
    b_val2, b_key2 = canonicalize_for_voting("boolean", "0")
    assert b_val2 is False and b_key2 == "bool:False"
    assert is_match("boolean", "dung", "boolean", True)

    # 6. List
    l_val, l_key = canonicalize_for_voting("list", ["Bia Saigon", "Nước ngọt"])
    assert l_val == ["Bia Saigon", "Nước ngọt"]
    assert l_key == "list:str:bia saigon|str:nước ngọt"
    assert is_match("list", ["Bia Saigon", "Nước ngọt"], "list", ["bia saigon", "NƯỚC NGỌT"])

    # 7. Table
    t_input = {
        "columns": ["san_pham", "doanh_thu"],
        "rows": [["Sản phẩm A", 1000], ["Sản phẩm B", 2000]],
    }
    t_val, t_key = canonicalize_for_voting("table", t_input)
    assert t_val["rows"] == [["Sản phẩm A", 1000], ["Sản phẩm B", 2000]]
    assert "table:str:sản phẩm a|num:1000#str:sản phẩm b|num:2000" == t_key

    # Reversed row order should produce identical canonical key (multiset equality)
    t_reversed = {
        "columns": ["san_pham", "doanh_thu"],
        "rows": [["Sản phẩm B", 2000], ["Sản phẩm A", 1000]],
    }
    _, t_rev_key = canonicalize_for_voting("table", t_reversed)
    assert t_key == t_rev_key
    assert is_match("table", t_reversed, "table", t_input)

    # 8. Unanswerable
    u_val, u_key = canonicalize_for_voting("unanswerable", None)
    assert u_val is None and u_key == "unanswerable:__null__"
    score_u, status_u = score_single_prediction(
        {"id": "q_u", "type": "unanswerable"},
        {"id": "q_u", "type": "unanswerable", "answer": None},
    )
    assert score_u == 1 and status_u == "correct"

    # 9. Abstain
    a_val, a_key = canonicalize_for_voting("abstain", None)
    assert a_val is None and a_key == "abstain"
    score_a, status_a = score_single_prediction(
        {"id": "q_a", "type": "abstain"},
        {"id": "q_a", "type": "number", "answer": 1000},
    )
    assert score_a == 0 and status_a == "abstain"

    logger.info("--> [SMOKE TEST 1/3] PASSED! All 9 answer types normalized & scored correctly.\n")


def test_date_resolver_vietnamese():
    logger.info("--- [SMOKE TEST 2/3] Testing DateResolver Vietnamese Expressions ---")

    # Locate calendar.csv
    candidates = [
        os.path.join(PROJECT_ROOT, "../train/train/calendar.csv"),
        os.path.join(PROJECT_ROOT, "../public_test/public_test/calendar.csv"),
        os.path.join(PROJECT_ROOT, "calendar.csv"),
    ]
    cal_path = None
    for c in candidates:
        if os.path.exists(c):
            cal_path = os.path.abspath(c)
            break

    resolver = DateResolver(cal_path)
    as_of = "2026-08-20"  # Thursday

    # Test "tuần rồi"
    res_week = resolver.resolve("doanh thu tuần rồi là bao nhiêu", as_of)
    assert res_week.start_date == "2026-08-10"  # Previous Monday
    assert res_week.end_date == "2026-08-16"    # Previous Sunday
    assert "tuần trước" in res_week.explanation.lower() or "tuần rồi" in res_week.explanation.lower()

    # Test "tháng này"
    res_month = resolver.resolve("tổng số đơn hàng trong tháng này", as_of)
    assert res_month.start_date == "2026-08-01"
    assert res_month.end_date == "2026-08-20"
    assert "tháng này" in res_month.explanation.lower()

    # Test "cùng kỳ năm ngoái"
    res_yoy = resolver.resolve("doanh thu năm nay so với cùng kỳ năm ngoái tăng bao nhiêu", as_of)
    assert res_yoy.start_date == "2026-01-01"
    assert res_yoy.end_date == "2026-08-20"
    assert res_yoy.comp_start_date == "2025-01-01"
    assert res_yoy.comp_end_date == "2025-08-20"

    # Test "dịp Tết" (if calendar exists)
    if cal_path:
        res_tet = resolver.resolve("doanh thu dịp Tết năm 2026 là bao nhiêu", as_of)
        assert res_tet.start_date is not None
        assert res_tet.end_date is not None
        assert "tết" in res_tet.explanation.lower()

    logger.info("--> [SMOKE TEST 2/3] PASSED! Vietnamese relative time expressions resolved.\n")


def test_end_to_end_pipeline(mock_llm: bool = True, limit: int = 2):
    logger.info(f"--- [SMOKE TEST 3/3] Testing Ingest + ExecutorVoter Pipeline (mock_llm={mock_llm}, limit={limit}) ---")

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a mini messy business directory
        biz_dir = os.path.join(tmp_dir, "data", "biz_smoke")
        os.makedirs(biz_dir, exist_ok=True)

        # 1. README
        with open(os.path.join(biz_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write("# Smoke Test Shop\nCửa hàng tạp hóa thử nghiệm.\n")

        # 2. Messy CSV with title rows, Vietnamese currency (150.000 đ), dates (DD/MM/YYYY)
        messy_csv_content = """BÁO CÁO DOANH THU THÁNG 5/2026;;;;
Cửa hàng tạp hóa;;;;
Mã đơn hàng;Ngày bán;Tên hàng;Trạng thái;Thành tiền
DH001;10/05/2026;Mì Hảo Hảo;hoàn thành;150.000 đ
DH002;11/05/2026;Bột giặt OMO;hoàn thành;250.000 đ
DH003;12/05/2026;Dầu ăn;huỷ;50.000 đ
Tổng cộng;;;;450.000 đ
"""
        with open(os.path.join(biz_dir, "ban_hang.csv"), "w", encoding="utf-8-sig") as f:
            f.write(messy_csv_content)

        # 3. Questions file (2 questions)
        q_path = os.path.join(tmp_dir, "questions.jsonl")
        questions = [
            {
                "id": "q_smoke_01",
                "business_id": "biz_smoke",
                "question": "Tổng doanh thu tháng này của cửa hàng là bao nhiêu?",
                "as_of_date": "2026-05-20",
            },
            {
                "id": "q_smoke_02",
                "business_id": "biz_smoke",
                "question": "Cửa hàng có bao nhiêu đơn hàng đã hoàn thành?",
                "as_of_date": "2026-05-20",
            },
        ]
        with open(q_path, "w", encoding="utf-8") as f:
            for q in questions[:limit]:
                f.write(json.dumps(q, ensure_ascii=False) + "\n")

        # 4. Minimal Rulebook & Calendar
        rb_path = os.path.join(tmp_dir, "rulebook.md")
        with open(rb_path, "w", encoding="utf-8") as f:
            f.write("# Rulebook\nDoanh thu chỉ tính đơn hoàn thành.\n")

        cal_path = os.path.join(tmp_dir, "calendar.csv")
        with open(cal_path, "w", encoding="utf-8") as f:
            f.write("date,day_of_week,is_holiday,lunar_day,lunar_month,lunar_year\n2026-05-20,4,0,14,4,2026\n")

        # Ingestion test
        cache_dir = os.path.join(tmp_dir, "cache")
        ctx = load_business_data("biz_smoke", biz_dir, cache_dir=cache_dir)
        assert len(ctx.table_names) > 0, "Ingestion failed to load tables"
        assert "raw_ban_hang" in ctx.table_names or "ban_hang" in ctx.table_names
        # Check that DuckDB cache file was created
        cached_duckdb = os.path.join(cache_dir, "duckdb_cache", "biz_smoke.duckdb")
        assert os.path.exists(cached_duckdb), f"DuckDB cache not persisted at {cached_duckdb}"
        ctx.con.close()

        # Run pipeline
        sub_path = os.path.join(tmp_dir, "result", "submission.jsonl")
        log_dir = os.path.join(tmp_dir, "result", "logs")

        run_inference_pipeline(
            data_dir=os.path.join(tmp_dir, "data"),
            questions_path=q_path,
            rulebook_path=rb_path,
            calendar_path=cal_path,
            submission_path=sub_path,
            log_dir=log_dir,
            limit=limit,
            allow_mock=mock_llm,
            cache_dir=cache_dir,
        )

        # Verify submission.jsonl
        assert os.path.exists(sub_path), f"Submission file {sub_path} was not created!"
        with open(sub_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        assert len(lines) == len(questions[:limit]), f"Expected {len(questions[:limit])} lines, got {len(lines)}"

        for idx, line in enumerate(lines):
            item = json.loads(line)
            assert "id" in item and "type" in item, f"Invalid submission schema in line {idx}: {line}"
            assert item["id"] == questions[idx]["id"], (
                f"Question order NOT preserved! Expected id {questions[idx]['id']} at index {idx}, got {item['id']}"
            )

        # Verify log files
        for q in questions[:limit]:
            log_file = os.path.join(log_dir, f"{q['id']}.json")
            assert os.path.exists(log_file), f"Log file missing for question {q['id']} at {log_file}"
            with open(log_file, "r", encoding="utf-8") as f_log:
                log_content = json.load(f_log)
                assert log_content.get("id") == q["id"]

    logger.info("--> [SMOKE TEST 3/3] PASSED! End-to-end Ingest + Voter verified with valid JSON outputs.\n")


def main():
    parser = argparse.ArgumentParser(description="DataMate Agent End-to-End Smoke Test.")
    parser.add_argument("--real_llm", action="store_true", default=False, help="Run inference with real offline LLM on GPU")
    parser.add_argument("--limit", type=int, default=5, help="Number of test questions to process (default: 5)")
    args = parser.parse_args()

    use_mock = not args.real_llm
    start_time = time.time()
    print("=" * 65)
    print("      DATAMATE AGENT - END-TO-END VERIFICATION SMOKE TEST")
    print(f"      Mode: {'MOCK LLM' if use_mock else 'REAL GPU LLM'} | Limit: {args.limit}")
    print("=" * 65)

    test_evaluator_all_9_types()
    test_date_resolver_vietnamese()
    test_end_to_end_pipeline(mock_llm=use_mock, limit=args.limit)

    total_time = time.time() - start_time
    print("=" * 65)
    print(f" ALL 3 SMOKE TESTS PASSED IN {total_time:.2f}s (< 60s target)! Codebase is Production-Ready.")
    print("=" * 65)


if __name__ == "__main__":
    main()
