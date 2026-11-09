"""
Date Resolver for DataMate Challenge.
Resolves Vietnamese natural language time expressions ("tuần rồi", "tháng này", "Tết", "hôm nay", "thang 7 nam 2026", "quy 2 nam nay")
against `as_of_date` and `calendar.csv` into exact ISO date windows according to Rulebook Section 2.
Features:
- Robust diacritics removal before regex matching (handles both accented and unaccented Vietnamese).
- Support for Quarters (quý 1..4, quý này, quý trước), Years (năm nay, năm ngoái, năm YYYY), Days (hôm kia, cuối tuần, N ngày/tuần qua).
- Dual-window parsing for comparison questions ("hôm nay so với hôm qua", "tuần này so với tuần trước", "cùng kỳ").
- Fail-safe try/except blocks to prevent runtime crashes on invalid inputs (e.g. tháng 13).
- Structured List[TimeWindow] and formatted explanations.
"""

import calendar
import datetime
import logging
import os
import re
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

import pandas as pd

logger = logging.getLogger(__name__)


def remove_accents(text: str) -> str:
    """Normalizes text by removing Vietnamese accents and lowercasing."""
    if not text:
        return ""
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).lower()


@dataclass
class TimeWindow:
    label: str
    start_date: Optional[str]
    end_date: Optional[str]
    description: str


@dataclass
class DateResolution:
    as_of_date: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    comp_start_date: Optional[str] = None
    comp_end_date: Optional[str] = None
    time_scope: str = "custom"
    shift_name: Optional[str] = None
    windows: List[TimeWindow] = field(default_factory=list)
    explanation: str = ""


class DateResolver:
    def __init__(self, calendar_source: Optional[Union[str, pd.DataFrame]] = None):
        self.cal_df: Optional[pd.DataFrame] = None
        if calendar_source is not None:
            if isinstance(calendar_source, str) and os.path.exists(calendar_source):
                try:
                    self.cal_df = pd.read_csv(calendar_source)
                except Exception as e:
                    logger.debug(f"Could not load calendar from {calendar_source}: {e}")
            elif isinstance(calendar_source, pd.DataFrame):
                self.cal_df = calendar_source

    def resolve(self, question: str, as_of_date_str: str) -> DateResolution:
        """
        Parses relative time expressions in `question` and resolves them using `as_of_date_str`.
        Safely wraps all parsing logic in try/except.
        """
        try:
            return self._resolve_internal(question, as_of_date_str)
        except Exception as e:
            logger.warning(f"DateResolver encountered error on question '{question}': {e}. Returning safe fallback.")
            return DateResolution(
                as_of_date=as_of_date_str,
                time_scope="general",
                explanation=f"Mốc thời gian hôm nay: {as_of_date_str} (không xác định được khoảng thời gian cụ thể).",
            )

    def _resolve_internal(self, question: str, as_of_date_str: str) -> DateResolution:
        q_raw = question.strip()
        q_unaccent = remove_accents(q_raw)
        as_of_dt = datetime.datetime.strptime(as_of_date_str.strip(), "%Y-%m-%d").date()
        year = as_of_dt.year
        month = as_of_dt.month
        day = as_of_dt.day

        # 1. Shifts: "ca sáng", "ca chiều"
        shift = None
        if "ca sang" in q_unaccent:
            shift = "ca sáng (06:00:00 - 13:59:59)"
        elif "ca chieu" in q_unaccent:
            shift = "ca chiều (14:00:00 - 21:59:59)"

        # 2. Check Comparison Pairs ("so với hôm qua", "so với tuần trước", "hôm nay so với hôm qua", etc.)
        is_comparison = any(k in q_unaccent for k in ["so voi", "tang hay giam", "tang truong", "so sanh"])

        if is_comparison:
            # Pair A: hôm nay so với hôm qua
            if ("hom nay" in q_unaccent and "hom qua" in q_unaccent) or "so voi hom qua" in q_unaccent:
                s_main = as_of_date_str
                e_main = as_of_date_str
                yesterday = as_of_dt - datetime.timedelta(days=1)
                s_comp = yesterday.strftime("%Y-%m-%d")
                e_comp = s_comp
                w_main = TimeWindow("Hôm nay (kỳ chính)", s_main, e_main, f"Trong ngày hôm nay: {s_main}")
                w_comp = TimeWindow("Hôm qua (kỳ so sánh)", s_comp, e_comp, f"Trong ngày hôm qua: {s_comp}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=s_main,
                    end_date=e_main,
                    comp_start_date=s_comp,
                    comp_end_date=e_comp,
                    time_scope="today_vs_yesterday",
                    shift_name=shift,
                    windows=[w_main, w_comp],
                    explanation=(
                        f"Kỳ chính (Hôm nay): {s_main}. "
                        f"Kỳ so sánh (Hôm qua): {s_comp}."
                    ),
                )

            # Pair B: hôm qua so với hôm kia
            if ("hom qua" in q_unaccent and "hom kia" in q_unaccent) or "so voi hom kia" in q_unaccent:
                yesterday = as_of_dt - datetime.timedelta(days=1)
                day_before = as_of_dt - datetime.timedelta(days=2)
                s_main = yesterday.strftime("%Y-%m-%d")
                s_comp = day_before.strftime("%Y-%m-%d")
                w_main = TimeWindow("Hôm qua (kỳ chính)", s_main, s_main, f"Trong ngày hôm qua: {s_main}")
                w_comp = TimeWindow("Hôm kia (kỳ so sánh)", s_comp, s_comp, f"Trong ngày hôm kia: {s_comp}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=s_main,
                    end_date=s_main,
                    comp_start_date=s_comp,
                    comp_end_date=s_comp,
                    time_scope="yesterday_vs_day_before",
                    shift_name=shift,
                    windows=[w_main, w_comp],
                    explanation=(
                        f"Kỳ chính (Hôm qua): {s_main}. "
                        f"Kỳ so sánh (Hôm kia): {s_comp}."
                    ),
                )

            # Pair C: tuần này so với tuần trước / tuần rồi
            if ("tuan nay" in q_unaccent and any(k in q_unaccent for k in ["tuan truoc", "tuan roi"])) or any(k in q_unaccent for k in ["so voi tuan truoc", "so voi tuan roi"]):
                monday = as_of_dt - datetime.timedelta(days=as_of_dt.weekday())
                s_main = monday.strftime("%Y-%m-%d")
                e_main = as_of_date_str
                prev_monday = monday - datetime.timedelta(days=7)
                days_elapsed = (as_of_dt - monday).days
                prev_comp_end = prev_monday + datetime.timedelta(days=days_elapsed)
                s_comp = prev_monday.strftime("%Y-%m-%d")
                e_comp = prev_comp_end.strftime("%Y-%m-%d")
                w_main = TimeWindow("Tuần này (kỳ chính)", s_main, e_main, f"Từ thứ Hai {s_main} đến hôm nay {e_main}")
                w_comp = TimeWindow("Tuần trước (kỳ so sánh cùng số ngày)", s_comp, e_comp, f"Từ thứ Hai {s_comp} đến {e_comp}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=s_main,
                    end_date=e_main,
                    comp_start_date=s_comp,
                    comp_end_date=e_comp,
                    time_scope="this_week_vs_last_week",
                    shift_name=shift,
                    windows=[w_main, w_comp],
                    explanation=(
                        f"Kỳ chính (Tuần này): từ {s_main} đến {e_main}. "
                        f"Kỳ so sánh (Tuần trước, cùng số ngày): từ {s_comp} đến {e_comp}."
                    ),
                )

            # Pair D: tháng này so với tháng trước
            if ("thang nay" in q_unaccent and any(k in q_unaccent for k in ["thang truoc", "thang roi"])) or any(k in q_unaccent for k in ["so voi thang truoc", "so voi thang roi"]):
                first_of_month = as_of_dt.replace(day=1)
                s_main = first_of_month.strftime("%Y-%m-%d")
                e_main = as_of_date_str
                if month == 1:
                    p_year = year - 1
                    p_month = 12
                else:
                    p_year = year
                    p_month = month - 1
                _, p_last = calendar.monthrange(p_year, p_month)
                c_end_day = min(day, p_last)
                s_comp = datetime.date(p_year, p_month, 1).strftime("%Y-%m-%d")
                e_comp = datetime.date(p_year, p_month, c_end_day).strftime("%Y-%m-%d")
                w_main = TimeWindow("Tháng này (kỳ chính)", s_main, e_main, f"Từ đầu tháng {s_main} đến {e_main}")
                w_comp = TimeWindow("Tháng trước (kỳ so sánh cùng số ngày)", s_comp, e_comp, f"Từ {s_comp} đến {e_comp}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=s_main,
                    end_date=e_main,
                    comp_start_date=s_comp,
                    comp_end_date=e_comp,
                    time_scope="this_month_vs_last_month",
                    shift_name=shift,
                    windows=[w_main, w_comp],
                    explanation=(
                        f"Kỳ chính (Tháng này): từ {s_main} đến {e_main}. "
                        f"Kỳ so sánh (Tháng trước cùng số ngày): từ {s_comp} đến {e_comp}."
                    ),
                )

            # Pair E: năm nay so với năm ngoái / cùng kỳ
            if ("nam nay" in q_unaccent and any(k in q_unaccent for k in ["nam ngoai", "nam truoc", "cung ky"])) or any(k in q_unaccent for k in ["so voi nam ngoai", "so voi nam truoc", "so voi cung ky"]):
                s_main = f"{year}-01-01"
                e_main = as_of_date_str
                s_comp = f"{year-1}-01-01"
                e_comp = f"{year-1}-{month:02d}-{day:02d}"
                w_main = TimeWindow("Năm nay (kỳ chính)", s_main, e_main, f"Từ {s_main} đến {e_main}")
                w_comp = TimeWindow("Năm ngoái (kỳ so sánh cùng kỳ)", s_comp, e_comp, f"Từ {s_comp} đến {e_comp}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=s_main,
                    end_date=e_main,
                    comp_start_date=s_comp,
                    comp_end_date=e_comp,
                    time_scope="this_year_vs_last_year",
                    shift_name=shift,
                    windows=[w_main, w_comp],
                    explanation=(
                        f"Kỳ chính (Năm nay): từ {s_main} đến {e_main}. "
                        f"Kỳ so sánh (Cùng kỳ năm ngoái): từ {s_comp} đến {e_comp}."
                    ),
                )

        # 3. Check Tết / Mùa Tết
        tet_match = re.search(r"tet\s*(?:nam\s*)?(\d{4})?", q_unaccent)
        if ("tet" in q_unaccent or "mua tet" in q_unaccent or "dip tet" in q_unaccent) and self.cal_df is not None:
            tet_year = int(tet_match.group(1)) if (tet_match and tet_match.group(1)) else year
            try:
                # 23 tháng Chạp (lunar_month = 12, lunar_day = 23) of lunar year tet_year - 1
                row_start = self.cal_df[
                    (self.cal_df["lunar_year"] == tet_year - 1)
                    & (self.cal_df["lunar_month"] == 12)
                    & (self.cal_df["lunar_day"] == 23)
                ]
                # Mùng 10 tháng Giêng (lunar_month = 1, lunar_day = 10) of lunar year tet_year
                row_end = self.cal_df[
                    (self.cal_df["lunar_year"] == tet_year)
                    & (self.cal_df["lunar_month"] == 1)
                    & (self.cal_df["lunar_day"] == 10)
                ]
                if not row_start.empty and not row_end.empty:
                    s_date_str = str(row_start["date"].values[0])
                    e_date_str = str(row_end["date"].values[0])
                    s_dt = datetime.datetime.strptime(s_date_str, "%Y-%m-%d").date()
                    e_dt = datetime.datetime.strptime(e_date_str, "%Y-%m-%d").date()
                    days_count = (e_dt - s_dt).days + 1

                    c_end_dt = s_dt - datetime.timedelta(days=1)
                    c_start_dt = c_end_dt - datetime.timedelta(days=days_count - 1)
                    w_main = TimeWindow(f"Tết năm {tet_year}", s_date_str, e_date_str, f"23 Chạp ({s_date_str}) đến mùng 10 Giêng ({e_date_str})")
                    w_comp = TimeWindow("Kỳ trước Tết", c_start_dt.strftime("%Y-%m-%d"), c_end_dt.strftime("%Y-%m-%d"), f"Trước Tết: {c_start_dt} đến {c_end_dt}")

                    return DateResolution(
                        as_of_date=as_of_date_str,
                        start_date=s_date_str,
                        end_date=e_date_str,
                        comp_start_date=c_start_dt.strftime("%Y-%m-%d"),
                        comp_end_date=c_end_dt.strftime("%Y-%m-%d"),
                        time_scope="tet",
                        shift_name=shift,
                        windows=[w_main, w_comp],
                        explanation=(
                            f"Tết năm {tet_year}: Từ {s_date_str} (23 tháng Chạp) đến hết {e_date_str} (mùng 10 tháng Giêng). "
                            f"Kỳ so sánh trước Tết: {c_start_dt.strftime('%Y-%m-%d')} đến {c_end_dt.strftime('%Y-%m-%d')}."
                        ),
                    )
            except Exception:
                pass

        # 4. Check "N ngày / tuần / tháng gần nhất / qua"
        n_days_match = re.search(r"(\d+)\s*ngay\s*(?:gan\s*nhat|qua|tro\s*lai\s*day)", q_unaccent)
        if n_days_match:
            n = int(n_days_match.group(1))
            start_n = as_of_dt - datetime.timedelta(days=n - 1)
            s_str = start_n.strftime("%Y-%m-%d")
            w = TimeWindow(f"{n} ngày gần nhất", s_str, as_of_date_str, f"{n} ngày kể cả hôm nay")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_str,
                end_date=as_of_date_str,
                time_scope="n_days_recent",
                shift_name=shift,
                windows=[w],
                explanation=f"{n} ngày gần nhất (kể cả hôm nay): {s_str} đến {as_of_date_str}.",
            )

        n_weeks_match = re.search(r"(\d+)\s*tuan\s*(?:gan\s*nhat|qua|tro\s*lai\s*day)", q_unaccent)
        if n_weeks_match:
            n = int(n_weeks_match.group(1))
            start_n = as_of_dt - datetime.timedelta(days=(7 * n) - 1)
            s_str = start_n.strftime("%Y-%m-%d")
            w = TimeWindow(f"{n} tuần gần nhất", s_str, as_of_date_str, f"{n} tuần kể cả hôm nay")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_str,
                end_date=as_of_date_str,
                time_scope="n_weeks_recent",
                shift_name=shift,
                windows=[w],
                explanation=f"{n} tuần gần nhất: {s_str} đến {as_of_date_str}.",
            )

        # 5. Check Quarters: "quý 1", "quý 2", "quý 3", "quý 4", "quý này", "quý trước"
        quarter_match = re.search(r"quy\s*([1-4])(?:\s*(?:nam|/)\s*(\d{4}))?", q_unaccent)
        if quarter_match:
            q_num = int(quarter_match.group(1))
            q_year_str = quarter_match.group(2)
            if q_year_str:
                q_year = int(q_year_str)
            else:
                curr_q = (month - 1) // 3 + 1
                q_year = year if q_num <= curr_q else (year - 1)

            q_start_month = (q_num - 1) * 3 + 1
            q_end_month = q_num * 3
            _, q_last_day = calendar.monthrange(q_year, q_end_month)
            s_q = f"{q_year}-{q_start_month:02d}-01"
            e_q = f"{q_year}-{q_end_month:02d}-{q_last_day:02d}"
            w = TimeWindow(f"Quý {q_num}/{q_year}", s_q, e_q, f"Toàn bộ Quý {q_num} năm {q_year}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_q,
                end_date=e_q,
                time_scope="quarter",
                shift_name=shift,
                windows=[w],
                explanation=f"Quý {q_num}/{q_year}: từ {s_q} đến hết {e_q}.",
            )

        if "quy nay" in q_unaccent:
            curr_q = (month - 1) // 3 + 1
            q_start_month = (curr_q - 1) * 3 + 1
            s_q = f"{year}-{q_start_month:02d}-01"
            e_q = as_of_date_str
            w = TimeWindow(f"Quý này (Quý {curr_q}/{year})", s_q, e_q, f"Từ đầu Quý {curr_q} đến hôm nay")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_q,
                end_date=e_q,
                time_scope="this_quarter",
                shift_name=shift,
                windows=[w],
                explanation=f"Quý này (Quý {curr_q}/{year}): từ {s_q} đến hết hôm nay {e_q}.",
            )

        if "quy truoc" in q_unaccent or "quy roi" in q_unaccent:
            curr_q = (month - 1) // 3 + 1
            if curr_q == 1:
                p_q = 4
                p_q_year = year - 1
            else:
                p_q = curr_q - 1
                p_q_year = year
            q_start_month = (p_q - 1) * 3 + 1
            q_end_month = p_q * 3
            _, q_last_day = calendar.monthrange(p_q_year, q_end_month)
            s_q = f"{p_q_year}-{q_start_month:02d}-01"
            e_q = f"{p_q_year}-{q_end_month:02d}-{q_last_day:02d}"
            w = TimeWindow(f"Quý trước (Quý {p_q}/{p_q_year})", s_q, e_q, f"Toàn bộ Quý {p_q} năm {p_q_year}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_q,
                end_date=e_q,
                time_scope="last_quarter",
                shift_name=shift,
                windows=[w],
                explanation=f"Quý trước (Quý {p_q}/{p_q_year}): từ {s_q} đến hết {e_q}.",
            )

        # 6. Check Specific Month: "tháng M năm YYYY" or "tháng M/YYYY" or "tháng M"
        specific_month_match = re.search(r"thang\s*(\d{1,2})(?:\s*(?:nam|/)\s*(\d{4}))?", q_unaccent)
        if specific_month_match:
            m_num = int(specific_month_match.group(1))
            # Validate month range (1..12). If outside, ignore to prevent crashes!
            if 1 <= m_num <= 12:
                y_str = specific_month_match.group(2)
                if y_str:
                    m_year = int(y_str)
                else:
                    m_year = year if m_num <= month else (year - 1)
                _, m_last = calendar.monthrange(m_year, m_num)
                m_start = datetime.date(m_year, m_num, 1).strftime("%Y-%m-%d")
                m_end = datetime.date(m_year, m_num, m_last).strftime("%Y-%m-%d")
                w = TimeWindow(f"Tháng {m_num}/{m_year}", m_start, m_end, f"Toàn bộ tháng {m_num}/{m_year}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=m_start,
                    end_date=m_end,
                    time_scope="specific_month",
                    shift_name=shift,
                    windows=[w],
                    explanation=f"Tháng {m_num}/{m_year}: từ {m_start} đến hết {m_end}.",
                )

        # 7. Check "hôm nay", "hôm qua", "hôm kia", "cuối tuần"
        if "hom kia" in q_unaccent:
            day_before = as_of_dt - datetime.timedelta(days=2)
            db_str = day_before.strftime("%Y-%m-%d")
            w = TimeWindow("Hôm kia", db_str, db_str, f"Ngày hôm kia: {db_str}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=db_str,
                end_date=db_str,
                time_scope="day_before_yesterday",
                shift_name=shift,
                windows=[w],
                explanation=f"Ngày hôm kia: {db_str}.",
            )

        if "hom qua" in q_unaccent:
            yesterday = as_of_dt - datetime.timedelta(days=1)
            y_str = yesterday.strftime("%Y-%m-%d")
            w = TimeWindow("Hôm qua", y_str, y_str, f"Ngày hôm qua: {y_str}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=y_str,
                end_date=y_str,
                time_scope="yesterday",
                shift_name=shift,
                windows=[w],
                explanation=f"Ngày hôm qua: {y_str}.",
            )

        if "cuoi tuan" in q_unaccent:
            # Saturday & Sunday of the current or previous week
            sat = as_of_dt + datetime.timedelta(days=(5 - as_of_dt.weekday()))
            sun = sat + datetime.timedelta(days=1)
            if sat > as_of_dt:
                sat -= datetime.timedelta(days=7)
                sun -= datetime.timedelta(days=7)
            s_wk = sat.strftime("%Y-%m-%d")
            e_wk = sun.strftime("%Y-%m-%d")
            w = TimeWindow("Cuối tuần", s_wk, e_wk, f"Thứ Bảy ({s_wk}) và Chủ Nhật ({e_wk})")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_wk,
                end_date=e_wk,
                time_scope="weekend",
                shift_name=shift,
                windows=[w],
                explanation=f"Cuối tuần: từ {s_wk} đến hết {e_wk}.",
            )

        if "hom nay" in q_unaccent:
            if any(k in q_unaccent for k in ["tinh den hom nay", "den hom nay", "het hom nay", "con no", "ton kho"]):
                w = TimeWindow("Tính đến hôm nay", None, as_of_date_str, f"Từ đầu dữ liệu đến {as_of_date_str}")
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=None,
                    end_date=as_of_date_str,
                    time_scope="up_to_today",
                    shift_name=shift,
                    windows=[w],
                    explanation=f"Tính đến hết hôm nay: tất cả phát sinh từ đầu dữ liệu đến hết ngày {as_of_date_str}.",
                )
            w = TimeWindow("Hôm nay", as_of_date_str, as_of_date_str, f"Trong ngày hôm nay: {as_of_date_str}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=as_of_date_str,
                end_date=as_of_date_str,
                time_scope="today",
                shift_name=shift,
                windows=[w],
                explanation=f"Trong ngày hôm nay: {as_of_date_str}.",
            )

        # 8. Check Weeks: "tuần này", "tuần trước"
        if "tuan nay" in q_unaccent:
            monday = as_of_dt - datetime.timedelta(days=as_of_dt.weekday())
            s_w = monday.strftime("%Y-%m-%d")
            w = TimeWindow("Tuần này", s_w, as_of_date_str, f"Thứ Hai ({s_w}) đến hôm nay ({as_of_date_str})")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_w,
                end_date=as_of_date_str,
                time_scope="this_week",
                shift_name=shift,
                windows=[w],
                explanation=f"Tuần này: từ thứ Hai {s_w} đến hết hôm nay {as_of_date_str}.",
            )

        if any(k in q_unaccent for k in ["tuan truoc", "tuan roi"]):
            prev_monday = as_of_dt - datetime.timedelta(days=as_of_dt.weekday() + 7)
            prev_sunday = prev_monday + datetime.timedelta(days=6)
            s_pw = prev_monday.strftime("%Y-%m-%d")
            e_pw = prev_sunday.strftime("%Y-%m-%d")
            w = TimeWindow("Tuần trước", s_pw, e_pw, f"Thứ Hai ({s_pw}) đến Chủ nhật ({e_pw})")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_pw,
                end_date=e_pw,
                time_scope="last_week",
                shift_name=shift,
                windows=[w],
                explanation=f"Tuần trước/rồi (cả tuần): từ thứ Hai {s_pw} đến Chủ nhật {e_pw}.",
            )

        # 9. Check Months: "tháng này", "tháng trước"
        if "thang nay" in q_unaccent:
            first_of_month = as_of_dt.replace(day=1)
            s_tm = first_of_month.strftime("%Y-%m-%d")
            if month == 1:
                p_year = year - 1
                p_month = 12
            else:
                p_year = year
                p_month = month - 1
            _, p_last = calendar.monthrange(p_year, p_month)
            c_end_day = min(day, p_last)
            s_comp = datetime.date(p_year, p_month, 1).strftime("%Y-%m-%d")
            e_comp = datetime.date(p_year, p_month, c_end_day).strftime("%Y-%m-%d")
            w = TimeWindow("Tháng này", s_tm, as_of_date_str, f"Từ đầu tháng {s_tm} đến {as_of_date_str}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_tm,
                end_date=as_of_date_str,
                comp_start_date=s_comp,
                comp_end_date=e_comp,
                time_scope="this_month",
                shift_name=shift,
                windows=[w],
                explanation=(
                    f"Tháng này: từ {s_tm} đến hết hôm nay {as_of_date_str}. "
                    f"So với tháng trước (cùng số ngày): từ {s_comp} đến {e_comp}."
                ),
            )

        if any(k in q_unaccent for k in ["thang truoc", "thang roi"]):
            if month == 1:
                p_year = year - 1
                p_month = 12
            else:
                p_year = year
                p_month = month - 1
            _, p_last = calendar.monthrange(p_year, p_month)
            s_lm = datetime.date(p_year, p_month, 1).strftime("%Y-%m-%d")
            e_lm = datetime.date(p_year, p_month, p_last).strftime("%Y-%m-%d")
            w = TimeWindow("Tháng trước", s_lm, e_lm, f"Toàn bộ tháng trước: {s_lm} đến {e_lm}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_lm,
                end_date=e_lm,
                time_scope="last_month",
                shift_name=shift,
                windows=[w],
                explanation=f"Tháng trước/rồi (toàn bộ): {s_lm} đến {e_lm}.",
            )

        # 10. Check Years: "năm nay", "năm ngoái", "từ đầu năm", "năm YYYY"
        if any(k in q_unaccent for k in ["tu dau nam", "dau nam toi nay", "nam nay"]):
            s_yr = f"{year}-01-01"
            w = TimeWindow("Năm nay", s_yr, as_of_date_str, f"Từ đầu năm {s_yr} đến hôm nay {as_of_date_str}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_yr,
                end_date=as_of_date_str,
                time_scope="this_year",
                shift_name=shift,
                windows=[w],
                explanation=f"Từ đầu năm nay đến hôm nay: từ {s_yr} đến {as_of_date_str}.",
            )

        if any(k in q_unaccent for k in ["nam ngoai", "nam truoc"]):
            s_lyr = f"{year-1}-01-01"
            e_lyr = f"{year-1}-12-31"
            w = TimeWindow("Năm ngoái", s_lyr, e_lyr, f"Toàn bộ năm ngoái: {s_lyr} đến {e_lyr}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_lyr,
                end_date=e_lyr,
                time_scope="last_year",
                shift_name=shift,
                windows=[w],
                explanation=f"Năm ngoái (toàn bộ): {s_lyr} đến {e_lyr}.",
            )

        specific_year_match = re.search(r"nam\s*(\d{4})", q_unaccent)
        if specific_year_match:
            spec_year = int(specific_year_match.group(1))
            s_sy = f"{spec_year}-01-01"
            e_sy = f"{spec_year}-12-31"
            w = TimeWindow(f"Năm {spec_year}", s_sy, e_sy, f"Toàn bộ năm {spec_year}")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=s_sy,
                end_date=e_sy,
                time_scope="specific_year",
                shift_name=shift,
                windows=[w],
                explanation=f"Năm {spec_year}: từ {s_sy} đến hết {e_sy}.",
            )

        # 11. Default fallback
        w_def = TimeWindow("Hôm nay", as_of_date_str, as_of_date_str, f"Mốc thời gian hôm nay: {as_of_date_str}")
        return DateResolution(
            as_of_date=as_of_date_str,
            time_scope="general",
            shift_name=shift,
            windows=[w_def],
            explanation=f"Mốc thời gian hôm nay: {as_of_date_str}.",
        )
