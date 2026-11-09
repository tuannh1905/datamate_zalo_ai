import duckdb
import pytest
from src.data_layer.ingest import BusinessContext
from src.data_layer.view_builder import (
    build_canonical_views,
    detect_table_structure,
    generate_rule_based_view_drafts,
    generate_purchase_view_drafts,
)


def test_kiotviet_thoi_gian_view_build():
    """
    Tests that POS systems using 'thoi_gian' in header and relational details
    (like KiotViet biz_128, biz_120, biz_124) successfully build v_sales and v_orders.
    """
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE raw_danhsachhoadon AS
        SELECT 
            'HD0001' AS ma_hoa_don,
            '2026-06-15 14:30:00' AS thoi_gian,
            'Hoàn thành' AS trang_thai,
            'KH_01' AS ma_khach_hang,
            'Nguyễn Văn A' AS ten_khach_hang,
            150000 AS tong_tien,
            'Tiền mặt' AS phuong_thuc_thanh_toan;

        CREATE TABLE raw_danhsachhoadonchitiet AS
        SELECT 
            'HD0001' AS ma_hoa_don,
            'SP_01' AS ma_hang,
            'Cà phê đen' AS ten_hang,
            3 AS so_luong,
            50000 AS don_gia,
            150000 AS thanh_tien;
    """)

    schemas = {
        "raw_danhsachhoadon": [
            {"name": "ma_hoa_don", "type": "VARCHAR"},
            {"name": "thoi_gian", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ma_khach_hang", "type": "VARCHAR"},
            {"name": "ten_khach_hang", "type": "VARCHAR"},
            {"name": "tong_tien", "type": "BIGINT"},
            {"name": "phuong_thuc_thanh_toan", "type": "VARCHAR"},
        ],
        "raw_danhsachhoadonchitiet": [
            {"name": "ma_hoa_don", "type": "VARCHAR"},
            {"name": "ma_hang", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "don_gia", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ],
    }

    ctx = BusinessContext(
        business_id="biz_kiotviet_test",
        business_dir="/tmp/test",
        con=con,
        table_names=["raw_danhsachhoadon", "raw_danhsachhoadonchitiet"],
        schemas=schemas,
    )

    struct = detect_table_structure(ctx)
    assert struct["type"] == "relational"
    assert struct["detail_tbl"] == "raw_danhsachhoadonchitiet"
    assert struct["header_tbl"] == "raw_danhsachhoadon"
    assert struct["join_key"] == ("ma_hoa_don", "ma_hoa_don")

    res = build_canonical_views(ctx)
    assert res.success is True
    assert res.v_sales_sql is not None
    assert res.v_orders_sql is not None

    # Check v_sales row
    sales_rows = con.execute("""
        SELECT order_id, order_date, status, is_valid_sales, product_name, quantity_base, unit_price, line_amount 
        FROM v_sales
    """).fetchall()
    assert len(sales_rows) == 1
    assert sales_rows[0][0] == "HD0001"
    assert str(sales_rows[0][1]) == "2026-06-15"
    assert sales_rows[0][2] == "hoàn thành"
    assert sales_rows[0][3] is True
    assert sales_rows[0][4] == "Cà phê đen"
    assert sales_rows[0][5] == 3.0
    assert sales_rows[0][6] == 50000.0
    assert sales_rows[0][7] == 150000.0

    # Check v_orders row
    orders_rows = con.execute("SELECT order_id, order_total FROM v_orders").fetchall()
    assert len(orders_rows) == 1
    assert orders_rows[0][0] == "HD0001"
    assert orders_rows[0][1] == 150000.0


def test_purchase_canonical_view_build():
    """
    Tests that purchase records (danhsachnhaphang & danhsachchitietnhaphang)
    successfully build v_purchases view with correct supplier, date, and line amount.
    """
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE raw_danhsachnhaphang AS
        SELECT 
            'PN0001' AS ma_nhap_hang,
            '2026-06-10 09:15:00' AS thoi_gian,
            'Đã nhập hàng' AS trang_thai,
            'NCC_01' AS ma_ncc,
            'Vinamilk' AS nha_cung_cap,
            500000 AS tong_tien_hang;

        CREATE TABLE raw_danhsachchitietnhaphang AS
        SELECT 
            'PN0001' AS ma_nhap_hang,
            'NL_01' AS ma_hang,
            'Sữa tươi tiệt trùng' AS ten_hang,
            20 AS so_luong,
            25000 AS don_gia,
            500000 AS thanh_tien;
    """)

    schemas = {
        "raw_danhsachnhaphang": [
            {"name": "ma_nhap_hang", "type": "VARCHAR"},
            {"name": "thoi_gian", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ma_ncc", "type": "VARCHAR"},
            {"name": "nha_cung_cap", "type": "VARCHAR"},
            {"name": "tong_tien_hang", "type": "BIGINT"},
        ],
        "raw_danhsachchitietnhaphang": [
            {"name": "ma_nhap_hang", "type": "VARCHAR"},
            {"name": "ma_hang", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "don_gia", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ],
    }

    ctx = BusinessContext(
        business_id="biz_purchase_test",
        business_dir="/tmp/test",
        con=con,
        table_names=["raw_danhsachnhaphang", "raw_danhsachchitietnhaphang"],
        schemas=schemas,
    )

    struct = detect_table_structure(ctx)
    assert struct["purchase_type"] == "relational"
    assert struct["purchase_detail_tbl"] == "raw_danhsachchitietnhaphang"
    assert struct["purchase_header_tbl"] == "raw_danhsachnhaphang"
    assert struct["purchase_join_key"] == ("ma_nhap_hang", "ma_nhap_hang")

    res = build_canonical_views(ctx)
    assert res.success is True
    assert res.v_purchases_sql is not None

    p_rows = con.execute("""
        SELECT purchase_id, purchase_date, status, is_valid_purchase, supplier_name, product_name, quantity_base, line_amount 
        FROM v_purchases
    """).fetchall()
    assert len(p_rows) == 1
    assert p_rows[0][0] == "PN0001"
    assert str(p_rows[0][1]) == "2026-06-10"
    assert p_rows[0][2] == "hoàn thành"
    assert p_rows[0][3] is True
    assert p_rows[0][4] == "Vinamilk"
    assert p_rows[0][5] == "Sữa tươi tiệt trùng"
    assert p_rows[0][6] == 20.0
    assert p_rows[0][7] == 500000.0


def test_schema_summary_join_hints():
    """
    Tests that get_schema_summary() emits explicit table join relationships
    and flags which table holds the date column.
    """
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE raw_danhsachhoadon (ma_hoa_don VARCHAR, thoi_gian VARCHAR, tong_tien BIGINT);
        CREATE TABLE raw_danhsachhoadonchitiet (ma_hoa_don VARCHAR, ten_hang VARCHAR, thanh_tien BIGINT);
    """)

    schemas = {
        "raw_danhsachhoadon": [
            {"name": "ma_hoa_don", "type": "VARCHAR"},
            {"name": "thoi_gian", "type": "VARCHAR"},
            {"name": "tong_tien", "type": "BIGINT"},
        ],
        "raw_danhsachhoadonchitiet": [
            {"name": "ma_hoa_don", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ],
    }

    ctx = BusinessContext(
        business_id="biz_hints_test",
        business_dir="/tmp/test",
        con=con,
        table_names=["raw_danhsachhoadon", "raw_danhsachhoadonchitiet"],
        schemas=schemas,
    )

    summary = ctx.get_schema_summary()
    assert "Table Relationships & Join Hints:" in summary
    assert "Join `raw_danhsachhoadon` and `raw_danhsachhoadonchitiet` ON `raw_danhsachhoadon.ma_hoa_don = raw_danhsachhoadonchitiet.ma_hoa_don`" in summary
    assert "Date 'thoi_gian' is in `raw_danhsachhoadon`" in summary


def test_quantity_fallback_builds_view():
    """
    Tests that a table with amount/price but no explicit quantity column
    (e.g., service or ticket businesses) defaults quantity_base to 1.0 gracefully.
    """
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE raw_dichvu (
            ma_don VARCHAR,
            ngay_ban VARCHAR,
            trang_thai VARCHAR,
            ten_dv VARCHAR,
            thanh_tien BIGINT
        );
        INSERT INTO raw_dichvu VALUES ('DV01', '2026-07-01', 'hoàn thành', 'Cắt tóc nam', 70000);
    """)

    schemas = {
        "raw_dichvu": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ngay_ban", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ten_dv", "type": "VARCHAR"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ]
    }

    ctx = BusinessContext(
        business_id="biz_fallback_test",
        business_dir="/tmp/test",
        con=con,
        table_names=["raw_dichvu"],
        schemas=schemas,
    )

    res = build_canonical_views(ctx)
    assert res.success is True

    row = con.execute("SELECT order_id, product_name, quantity_base, line_amount FROM v_sales").fetchone()
    assert row[0] == "DV01"
    assert row[1] == "Cắt tóc nam"
    assert row[2] == 1.0
    assert row[3] == 70000.0
