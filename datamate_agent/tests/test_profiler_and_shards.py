"""
Unit and integration tests for profiler.py and multi-file monthly shard unioning.
Verifies:
1. Safe Shard Unioning on monthly partitioned tables.
2. Type normalization (DATE, BIGINT, DOUBLE) preventing VARCHAR Binder Errors.
3. diagnose_empty_result on out-of-range dates, diacritic mismatches, and 1x1 NULL results.
"""

import os
import duckdb
import pytest

from src.data_layer.ingest import load_business_data
from src.data_layer.profiler import (
    diagnose_empty_result,
    install_macros,
    normalize_types,
    prepare,
    render_schema,
)


@pytest.fixture(scope="module")
def dev_002_ctx():
    """Loads dev_002 context from public_test if available, or creates a mock monthly shard database."""
    biz_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../public_test/public_test/data/dev_002"))
    if os.path.exists(biz_dir):
        ctx = load_business_data("dev_002", biz_dir, cache_dir="./data_cache")
        return ctx
    else:
        # Create in-memory mock monthly shards
        con = duckdb.connect(database=":memory:")
        install_macros(con)
        
        # Shard 1 (Jan 2025)
        con.execute("""
            CREATE TABLE raw_banhang_t1_2025 AS
            SELECT 
                'ORD001' AS ma_don_hang,
                '10/01/2025' AS ngay_dat_hang,
                'Đã hoàn thành' AS trang_thai_don_hang,
                '2 ly' AS so_luong_san_pham,
                '35k' AS gia_san_pham,
                '70.000 đ' AS tong_tien,
                'ly' AS don_vi_tinh;
        """)
        # Shard 2 (Feb 2025)
        con.execute("""
            CREATE TABLE raw_banhang_t2_2025 AS
            SELECT 
                'ORD002' AS ma_don_hang,
                '15/02/2025' AS ngay_dat_hang,
                'Đã hoàn thành' AS trang_thai_don_hang,
                '1 ly' AS so_luong_san_pham,
                '40000' AS gia_san_pham,
                '40000' AS tong_tien,
                'ly' AS don_vi_tinh;
        """)
        
        class MockCtx:
            business_id = "mock_shard_biz"
            business_dir = ""
            con = con
            table_names = ["raw_banhang_t1_2025", "raw_banhang_t2_2025"]
            schemas = {}
            readme_text = "Mock shard business"
            column_mappings = {}
            profile = None
            
        mock_ctx = MockCtx()
        mock_ctx.profile = prepare(mock_ctx)
        return mock_ctx


def test_monthly_shards_unified_and_typed(dev_002_ctx):
    """Verifies that monthly shard tables were unified into raw_banhang with proper types."""
    ctx = dev_002_ctx
    con = ctx.con

    assert "raw_banhang" in ctx.table_names, f"Expected unified 'raw_banhang' table, got: {ctx.table_names}"

    # Verify DuckDB does NOT fail with Binder Error on SUM/AVG
    res = con.execute("""
        SELECT 
            SUM(so_luong_san_pham) AS total_qty,
            AVG(gia_san_pham) AS avg_price,
            SUM(tong_tien) AS total_revenue
        FROM raw_banhang
        WHERE ngay_dat_hang BETWEEN DATE '2025-01-01' AND DATE '2025-01-31'
    """).fetchone()

    assert res is not None
    assert res[0] is not None and res[0] > 0, "Expected positive total quantity"
    assert res[1] is not None and res[1] > 0, "Expected positive average price"
    assert res[2] is not None and res[2] > 0, "Expected positive total revenue"


def test_diagnose_empty_result_out_of_range_date(dev_002_ctx):
    """Verifies that diagnose_empty_result catches out-of-range dates."""
    ctx = dev_002_ctx
    prof = ctx.profile

    bad_sql = "SELECT * FROM raw_banhang WHERE ngay_dat_hang = DATE '2029-01-01'"
    hints = diagnose_empty_result(ctx, prof, bad_sql)

    assert len(hints) > 0, "Expected diagnostic hints for out-of-range date"
    assert any("out of range" in h.lower() or "range" in h.lower() for h in hints), f"Hints: {hints}"


def test_diagnose_empty_result_accent_mismatch(dev_002_ctx):
    """Verifies that diagnose_empty_result suggests accent-insensitive match or exact enum."""
    ctx = dev_002_ctx
    prof = ctx.profile

    bad_sql = "SELECT * FROM raw_banhang WHERE trang_thai_don_hang = 'da hoan thanh'"
    hints = diagnose_empty_result(ctx, prof, bad_sql)

    assert len(hints) > 0, "Expected diagnostic hints for unaccented status"
    assert any("vn(" in h or "Đã hoàn thành" in h for h in hints), f"Hints: {hints}"


def test_diagnose_empty_result_null_scalar(dev_002_ctx):
    """Verifies that 1x1 NULL result from aggregate triggers empty diagnostics."""
    ctx = dev_002_ctx
    prof = ctx.profile

    null_scalar_sql = "SELECT SUM(tong_tien) FROM raw_banhang WHERE ngay_dat_hang = DATE '2030-01-01'"
    # Verify DuckDB produces 1x1 NULL
    val = ctx.con.execute(null_scalar_sql).fetchone()[0]
    assert val is None

    # Run diagnose_empty_result
    hints = diagnose_empty_result(ctx, prof, null_scalar_sql)
    assert len(hints) > 0, "Expected diagnostic hints for 1x1 NULL result"
    assert any("2030" in h or "range" in h.lower() for h in hints), f"Hints: {hints}"


def test_render_schema_compactness(dev_002_ctx):
    """Verifies that render_schema stays compact and under token budget."""
    ctx = dev_002_ctx
    prof = ctx.profile

    schema_text = render_schema(prof, "Tổng doanh thu bán hàng trong tháng 1 năm 2025 là bao nhiêu?")
    assert len(schema_text) < 3500, f"Schema representation too long: {len(schema_text)} chars"
    assert "raw_banhang" in schema_text
    assert "ngay_dat_hang (DATE)" in schema_text
    assert "so_luong_san_pham (BIGINT)" in schema_text
