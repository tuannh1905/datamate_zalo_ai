import os
import pandas as pd
import pytest
from src.context.date_resolver import DateResolver, remove_accents


def test_remove_accents():
    assert remove_accents("tháng 7 năm 2026") == "thang 7 nam 2026"
    assert remove_accents("7 ngày gần nhất") == "7 ngay gan nhat"
    assert remove_accents("quý 2 năm nay") == "quy 2 nam nay"
    assert remove_accents("Đơn hàng đã huỷ") == "don hang da huy"


def test_unaccented_month_and_year():
    resolver = DateResolver()
    res = resolver.resolve("doanh thu thang 7 nam 2026 la bao nhieu", "2026-08-27")
    assert res.start_date == "2026-07-01"
    assert res.end_date == "2026-07-31"
    assert len(res.windows) >= 1
    assert res.windows[0].start_date == "2026-07-01"


def test_n_days_recent_unaccented():
    resolver = DateResolver()
    res = resolver.resolve("tong so don trong 7 ngay gan nhat", "2026-08-27")
    assert res.start_date == "2026-08-21"
    assert res.end_date == "2026-08-27"


def test_quarters():
    resolver = DateResolver()
    # quy 2 nam nay
    res_q2 = resolver.resolve("doanh thu quy 2 nam nay", "2026-08-27")
    assert res_q2.start_date == "2026-04-01"
    assert res_q2.end_date == "2026-06-30"

    # quy 3 nam 2025
    res_q3 = resolver.resolve("ban duoc bao nhieu trong quy 3 nam 2025", "2026-08-27")
    assert res_q3.start_date == "2025-07-01"
    assert res_q3.end_date == "2025-09-30"


def test_comparison_pairs():
    resolver = DateResolver()
    # hom nay so voi hom qua
    res_comp = resolver.resolve("doanh thu hom nay tang hay giam bao nhieu % so voi hom qua", "2026-08-27")
    assert res_comp.start_date == "2026-08-27"
    assert res_comp.end_date == "2026-08-27"
    assert res_comp.comp_start_date == "2026-08-26"
    assert res_comp.comp_end_date == "2026-08-26"
    assert len(res_comp.windows) == 2


def test_hom_kia_and_cuoi_tuan():
    resolver = DateResolver()
    res_hk = resolver.resolve("doanh thu hom kia", "2026-08-27")
    assert res_hk.start_date == "2026-08-25"
    assert res_hk.end_date == "2026-08-25"

    res_ct = resolver.resolve("doanh thu cuoi tuan vua roi", "2026-08-27")
    assert res_ct.start_date is not None
    assert res_ct.end_date is not None


def test_invalid_month_13_does_not_crash():
    resolver = DateResolver()
    # Month 13 should not crash with IllegalMonthError
    res = resolver.resolve("doanh thu thang 13 nam 2026", "2026-08-27")
    assert res is not None
    assert res.as_of_date == "2026-08-27"


def test_tet_resolution_with_calendar():
    # Mock lunar calendar DataFrame
    cal_data = {
        "date": ["2026-02-10", "2026-02-26"],
        "weekday": [2, 4],
        "lunar_day": [23, 10],
        "lunar_month": [12, 1],
        "lunar_year": [2025, 2026],
        "lunar_leap": [False, False],
        "holiday": [None, None],
    }
    cal_df = pd.DataFrame(cal_data)
    resolver = DateResolver(cal_df)
    res = resolver.resolve("doanh thu dip Tet nam 2026", "2026-08-27")
    assert res.start_date == "2026-02-10"
    assert res.end_date == "2026-02-26"
    assert res.comp_start_date is not None
