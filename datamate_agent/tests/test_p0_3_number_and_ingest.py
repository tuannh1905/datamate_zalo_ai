import pandas as pd
import numpy as np
from src.data_layer.ingest import (
    clean_number_series,
    preprocess_dataframe,
    find_true_header_from_df,
    normalize_identifier,
)


def test_clean_number_series_vietnamese_formats():
    s = pd.Series([
        "25.000đ",
        "12,5",
        "1.234,56",
        "1,234,567",
        "1.234.567",
        "12,5%",
        "560,000",
        "4,000",
    ])
    cleaned = clean_number_series(s)
    expected = [
        25000.0,
        12.5,
        1234.56,
        1234567.0,
        1234567.0,
        12.5,
        560000.0,
        4000.0,
    ]
    for c, e in zip(cleaned, expected):
        assert c == e, f"Expected {e}, got {c}"


def test_preprocess_dataframe_preserves_text_columns():
    # Columns 'Giao hàng', 'Nội dung' should NOT be converted to numeric/NaN
    df = pd.DataFrame({
        "Mã đơn": ["ORD01", "ORD02", "ORD03"],
        "Giao hàng": ["Nhanh", "Tiết kiệm", "Hỏa tốc"],
        "Nội dung": ["Bột giặt OMO", "Dầu ăn Tường An", "Mì Hảo Hảo"],
        "Giá bán": ["25.000đ", "52.000đ", "4.500đ"],
    })
    cleaned_df, mapping = preprocess_dataframe(df)

    assert "giao_hang" in cleaned_df.columns
    assert "noi_dung" in cleaned_df.columns
    assert "gia_ban" in cleaned_df.columns

    # Verify text values are intact
    assert cleaned_df["giao_hang"].tolist() == ["Nhanh", "Tiết kiệm", "Hỏa tốc"]
    assert cleaned_df["noi_dung"].tolist() == ["Bột giặt OMO", "Dầu ăn Tường An", "Mì Hảo Hảo"]
    assert cleaned_df["gia_ban"].tolist() == [25000.0, 52000.0, 4500.0]


def test_drop_subtotal_rows():
    df = pd.DataFrame({
        "Mã đơn": ["ORD01", "ORD02", "Tổng cộng"],
        "Nội dung": ["Sản phẩm A", "Sản phẩm B", "Tổng kết doanh số"],
        "Thành tiền": ["100.000", "200.000", "300.000"],
    })
    cleaned_df, _ = preprocess_dataframe(df)
    # The subtotal row should be dropped
    assert len(cleaned_df) == 2
    assert "Tổng cộng" not in cleaned_df["ma_don"].values


def test_find_true_header_offset():
    # Title on row 0, subtitle on row 1, actual header on row 2
    raw_df = pd.DataFrame([
        ["BÁO CÁO BÁN HÀNG THÁNG 5", None, None, None],
        ["Cửa hàng tạp hóa Lan", None, None, None],
        ["Mã đơn hàng", "Ngày đặt hàng", "Tên sản phẩm", "Tổng tiền"],
        ["ORD001", "01/05/2025", "Sting dâu", "10,000"],
        ["ORD002", "01/05/2025", "Red Bull", "12,500"],
    ])
    h_idx, cols = find_true_header_from_df(raw_df)
    assert h_idx == 2
    assert cols == ["Mã đơn hàng", "Ngày đặt hàng", "Tên sản phẩm", "Tổng tiền"]


def test_mojibake_identifier():
    # Test mojibake string produced by cp437 zip extraction
    bad_name = "Danh s├ích h├áng h├│a"
    cleaned = normalize_identifier(bad_name)
    assert "danh_sach_hang_hoa" == cleaned
