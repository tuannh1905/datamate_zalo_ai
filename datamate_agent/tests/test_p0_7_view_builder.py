import duckdb
import pytest
import pandas as pd
from src.data_layer.ingest import BusinessContext
from src.data_layer.view_builder import (
    build_canonical_views,
    detect_table_structure,
    generate_rule_based_view_drafts,
)


def test_flat_table_view_build():
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE ban_hang AS
        SELECT 
            'DH01' AS ma_don,
            '2026-05-10' AS ngay_ban,
            'hoàn thành' AS trang_thai,
            'KH01' AS ma_khach,
            'Nguyễn Văn A' AS ten_khach,
            'SP01' AS ma_hang,
            'Bia Saigon' AS ten_hang,
            2 AS so_luong,
            15000 AS don_gia,
            30000 AS thanh_tien,
            'Tiền mặt' AS phuong_thuc
        UNION ALL
        SELECT 
            'DH02', '2026-05-11', 'huỷ', 'KH02', 'Trần B', 'SP02', 'Nước ngọt', 1, 10000, 10000, 'Chuyển khoản'
    """)

    schemas = {
        "ban_hang": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ngay_ban", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ma_khach", "type": "VARCHAR"},
            {"name": "ten_khach", "type": "VARCHAR"},
            {"name": "ma_hang", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "don_gia", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
            {"name": "phuong_thuc", "type": "VARCHAR"},
        ]
    }

    ctx = BusinessContext(
        business_id="biz_test_flat",
        business_dir="/tmp/test",
        con=con,
        table_names=["ban_hang"],
        schemas=schemas,
    )

    res = build_canonical_views(ctx)
    assert res.success is True
    assert res.agreement_count >= 2

    # Verify v_sales content
    sales = con.execute("SELECT order_id, status, is_valid_sales, line_amount FROM v_sales ORDER BY order_id").fetchall()
    assert len(sales) == 2
    assert sales[0][0] == "DH01"
    assert sales[0][1] == "hoàn thành"
    assert sales[0][2] is True
    assert sales[0][3] == 30000.0

    assert sales[1][0] == "DH02"
    assert sales[1][1] == "huỷ"
    assert sales[1][2] is False


def test_relational_header_detail_join():
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE don_hang AS
        SELECT 
            'DH10' AS ma_don,
            '2026-06-01' AS ngay_tao,
            'đã giao' AS trang_thai,
            'KH10' AS ma_khach,
            'Phạm C' AS ten_khach,
            50000 AS tong_tien,
            'Tiền mặt' AS hinh_thuc_thanh_toan;
            
        CREATE TABLE chi_tiet_don AS
        SELECT 
            'DH10' AS ma_don,
            'SP10' AS ma_sp,
            'Áo thun' AS ten_hang,
            2 AS so_luong,
            25000 AS don_gia,
            50000 AS thanh_tien;
    """)

    schemas = {
        "don_hang": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ngay_tao", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ma_khach", "type": "VARCHAR"},
            {"name": "ten_khach", "type": "VARCHAR"},
            {"name": "tong_tien", "type": "BIGINT"},
            {"name": "hinh_thuc_thanh_toan", "type": "VARCHAR"},
        ],
        "chi_tiet_don": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ma_sp", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "don_gia", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ]
    }

    ctx = BusinessContext(
        business_id="biz_test_relational",
        business_dir="/tmp/test",
        con=con,
        table_names=["don_hang", "chi_tiet_don"],
        schemas=schemas,
    )

    struct = detect_table_structure(ctx)
    assert struct["type"] == "relational"
    assert struct["detail_tbl"] == "chi_tiet_don"
    assert struct["header_tbl"] == "don_hang"

    res = build_canonical_views(ctx)
    assert res.success is True

    # Verify joined v_sales
    row = con.execute("SELECT order_id, order_date, product_name, quantity_base, line_amount, status FROM v_sales").fetchone()
    assert row[0] == "DH10"
    assert str(row[1]) == "2026-06-01"
    assert row[2] == "Áo thun"
    assert row[3] == 2.0
    assert row[4] == 50000.0
    assert row[5] == "hoàn thành"  # 'đã giao' maps to 'hoàn thành'


def test_missing_core_columns_fails_gracefully():
    # Table has no date column and no quantity
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE danh_muc AS
        SELECT 'SP01' AS ma_sp, 'Bút bi' AS ten_sp, 5000 AS gia;
    """)
    schemas = {
        "danh_muc": [
            {"name": "ma_sp", "type": "VARCHAR"},
            {"name": "ten_sp", "type": "VARCHAR"},
            {"name": "gia", "type": "BIGINT"},
        ]
    }
    ctx = BusinessContext(
        business_id="biz_no_core",
        business_dir="/tmp/test",
        con=con,
        table_names=["danh_muc"],
        schemas=schemas,
    )

    res = build_canonical_views(ctx)
    assert res.success is False
    assert "missing core columns" in res.error_message.lower()

    # Views must NOT exist
    with pytest.raises(Exception):
        con.execute("SELECT * FROM v_sales")


def test_status_norm_does_not_blindly_complete():
    # Test that unknown status like 'chờ duyệt' is not converted to 'hoàn thành'
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE ban_hang AS
        SELECT 
            'DH99' AS ma_don,
            '2026-07-01' AS ngay,
            'chờ duyệt' AS trang_thai,
            'Bánh mì' AS ten_hang,
            1 AS so_luong,
            15000 AS thanh_tien
    """)
    schemas = {
        "ban_hang": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ngay", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ]
    }
    ctx = BusinessContext(
        business_id="biz_status_check",
        business_dir="/tmp/test",
        con=con,
        table_names=["ban_hang"],
        schemas=schemas,
    )

    res = build_canonical_views(ctx)
    assert res.success is True
    row = con.execute("SELECT status FROM v_sales").fetchone()
    # It must be preserved as 'chờ duyệt', NOT 'hoàn thành'!
    assert row[0] == "chờ duyệt"


def test_order_level_return_invalidation():
    # An order has 2 items: 1 completed, 1 returned.
    # The order-level return check should mark both rows as is_valid_sales = False!
    con = duckdb.connect(":memory:")
    con.execute("""
        CREATE TABLE ban_hang AS
        SELECT 'DH_RET' AS ma_don, '2026-08-01' AS ngay, 'hoàn thành' AS trang_thai, 'Bánh' AS ten_hang, 1 AS so_luong, 20000 AS thanh_tien
        UNION ALL
        SELECT 'DH_RET' AS ma_don, '2026-08-01' AS ngay, 'trả hàng' AS trang_thai, 'Kẹo' AS ten_hang, 1 AS so_luong, 10000 AS thanh_tien
        UNION ALL
        SELECT 'DH_OK' AS ma_don, '2026-08-01' AS ngay, 'hoàn thành' AS trang_thai, 'Nước' AS ten_hang, 2 AS so_luong, 30000 AS thanh_tien
    """)
    schemas = {
        "ban_hang": [
            {"name": "ma_don", "type": "VARCHAR"},
            {"name": "ngay", "type": "VARCHAR"},
            {"name": "trang_thai", "type": "VARCHAR"},
            {"name": "ten_hang", "type": "VARCHAR"},
            {"name": "so_luong", "type": "BIGINT"},
            {"name": "thanh_tien", "type": "BIGINT"},
        ]
    }
    ctx = BusinessContext(
        business_id="biz_ret_check",
        business_dir="/tmp/test",
        con=con,
        table_names=["ban_hang"],
        schemas=schemas,
    )

    res = build_canonical_views(ctx)
    assert res.success is True

    # DH_RET should have is_valid_sales = False for BOTH rows because order had a return
    rows = con.execute("SELECT order_id, status, is_valid_sales FROM v_sales ORDER BY order_id, status").fetchall()
    ret_rows = [r for r in rows if r[0] == "DH_RET"]
    assert len(ret_rows) == 2
    assert ret_rows[0][2] is False
    assert ret_rows[1][2] is False

    # DH_OK should have is_valid_sales = True
    ok_rows = [r for r in rows if r[0] == "DH_OK"]
    assert len(ok_rows) == 1
    assert ok_rows[0][2] is True

