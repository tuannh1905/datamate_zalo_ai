"""
Date Resolver for DataMate Challenge.
Resolves Vietnamese natural language time expressions ("tuần rồi", "tháng này", "Tết", "hôm nay")
against `as_of_date` and `calendar.csv` into exact ISO date windows according to Rulebook Section 2.
"""

import calendar
import datetime
import os
import re
from dataclasses import dataclass
from typing import Optional, Union

import pandas as pd


@dataclass
class DateResolution:
    as_of_date: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    comp_start_date: Optional[str] = None
    comp_end_date: Optional[str] = None
    time_scope: str = "custom"
    shift_name: Optional[str] = None
    explanation: str = ""


class DateResolver:
    def __init__(self, calendar_source: Optional[Union[str, pd.DataFrame]] = None):
        self.cal_df: Optional[pd.DataFrame] = None
        if calendar_source is not None:
            if isinstance(calendar_source, str) and os.path.exists(calendar_source):
                try:
                    self.cal_df = pd.read_csv(calendar_source)
                except Exception:
                    pass
            elif isinstance(calendar_source, pd.DataFrame):
                self.cal_df = calendar_source

    def resolve(self, question: str, as_of_date_str: str) -> DateResolution:
        """
        Parses relative time expressions in `question` and resolves them using `as_of_date_str`.
        """
        q_norm = question.lower()
        as_of_dt = datetime.datetime.strptime(as_of_date_str.strip(), "%Y-%m-%d").date()
        year = as_of_dt.year
        month = as_of_dt.month
        day = as_of_dt.day

        # 1. Check Shift ("ca sáng", "ca chiều")
        shift = None
        if "ca sáng" in q_norm or "ca sang" in q_norm:
            shift = "ca sáng (06:00:00 - 13:59:59)"
        elif "ca chiều" in q_norm or "ca chieu" in q_norm:
            shift = "ca chiều (14:00:00 - 21:59:59)"

        # 2. Check Tết / Mùa Tết / Dịp Tết
        tet_match = re.search(r"tết\s*(?:năm\s*)?(\d{4})?", q_norm)
        if ("tết" in q_norm or "mùa tết" in q_norm or "dịp tết" in q_norm) and self.cal_df is not None:
            tet_year = int(tet_match.group(1)) if (tet_match and tet_match.group(1)) else year
            try:
                # 23 tháng Chạp of lunar year tet_year - 1
                row_start = self.cal_df[
                    (self.cal_df["lunar_year"] == tet_year - 1)
                    & (self.cal_df["lunar_month"] == 12)
                    & (self.cal_df["lunar_day"] == 23)
                ]
                # Mùng 10 tháng Giêng of lunar year tet_year
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

                    # Comparison window: same number of days immediately preceding 23 Chạp
                    c_end_dt = s_dt - datetime.timedelta(days=1)
                    c_start_dt = c_end_dt - datetime.timedelta(days=days_count - 1)

                    return DateResolution(
                        as_of_date=as_of_date_str,
                        start_date=s_date_str,
                        end_date=e_date_str,
                        comp_start_date=c_start_dt.strftime("%Y-%m-%d"),
                        comp_end_date=c_end_dt.strftime("%Y-%m-%d"),
                        time_scope="tet",
                        shift_name=shift,
                        explanation=(
                            f"Tết năm {tet_year}: Từ {s_date_str} (23 tháng Chạp) đến hết {e_date_str} (mùng 10 tháng Giêng). "
                            f"Kỳ so sánh trước Tết: {c_start_dt.strftime('%Y-%m-%d')} đến {c_end_dt.strftime('%Y-%m-%d')}."
                        ),
                    )
            except Exception:
                pass

        # 3. Check "N ngày gần nhất"
        n_days_match = re.search(r"(\d+)\s*ngày\s*gần\s*nhất", q_norm)
        if n_days_match:
            n = int(n_days_match.group(1))
            start_n = as_of_dt - datetime.timedelta(days=n - 1)
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=start_n.strftime("%Y-%m-%d"),
                end_date=as_of_date_str,
                time_scope="n_days_recent",
                shift_name=shift,
                explanation=f"{n} ngày gần nhất (kể cả hôm nay): {start_n.strftime('%Y-%m-%d')} đến {as_of_date_str}.",
            )

        # 4. Check "hôm nay", "ngày hôm nay"
        if "hôm nay" in q_norm or "hom nay" in q_norm:
            # Check if it's "tính đến hôm nay" / "đến hết hôm nay" (cumulative)
            if any(k in q_norm for k in ["tính đến hôm nay", "đến hôm nay", "hết hôm nay", "còn nợ", "tồn kho"]):
                return DateResolution(
                    as_of_date=as_of_date_str,
                    start_date=None,
                    end_date=as_of_date_str,
                    time_scope="up_to_today",
                    shift_name=shift,
                    explanation=f"Tính đến hết hôm nay: tất cả phát sinh từ đầu dữ liệu đến hết ngày {as_of_date_str}.",
                )
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=as_of_date_str,
                end_date=as_of_date_str,
                time_scope="today",
                shift_name=shift,
                explanation=f"Trong ngày hôm nay: {as_of_date_str}.",
            )

        # 5. Check "hôm qua"
        if "hôm qua" in q_norm or "hom qua" in q_norm:
            yesterday = as_of_dt - datetime.timedelta(days=1)
            y_str = yesterday.strftime("%Y-%m-%d")
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=y_str,
                end_date=y_str,
                time_scope="yesterday",
                shift_name=shift,
                explanation=f"Ngày hôm qua: {y_str}.",
            )

        # 6. Check "tuần này"
        if "tuần này" in q_norm or "tuan nay" in q_norm:
            # Monday of current week
            monday = as_of_dt - datetime.timedelta(days=as_of_dt.weekday())
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=monday.strftime("%Y-%m-%d"),
                end_date=as_of_date_str,
                time_scope="this_week",
                shift_name=shift,
                explanation=f"Tuần này: từ thứ Hai {monday.strftime('%Y-%m-%d')} đến hết hôm nay {as_of_date_str}.",
            )

        # 7. Check "tuần trước", "tuần rồi"
        if any(k in q_norm for k in ["tuần trước", "tuan truoc", "tuần rồi", "tuan roi"]):
            prev_monday = as_of_dt - datetime.timedelta(days=as_of_dt.weekday() + 7)
            prev_sunday = prev_monday + datetime.timedelta(days=6)
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=prev_monday.strftime("%Y-%m-%d"),
                end_date=prev_sunday.strftime("%Y-%m-%d"),
                time_scope="last_week",
                shift_name=shift,
                explanation=f"Tuần trước/rồi (cả tuần): từ thứ Hai {prev_monday.strftime('%Y-%m-%d')} đến Chủ nhật {prev_sunday.strftime('%Y-%m-%d')}.",
            )

        # 8. Check "tháng này"
        if "tháng này" in q_norm or "thang nay" in q_norm:
            first_of_month = as_of_dt.replace(day=1)
            # Comparison: same number of days in previous month
            if month == 1:
                prev_month_year = year - 1
                prev_month_num = 12
            else:
                prev_month_year = year
                prev_month_num = month - 1

            _, last_day_prev = calendar.monthrange(prev_month_year, prev_month_num)
            comp_end_day = min(day, last_day_prev)
            comp_start = datetime.date(prev_month_year, prev_month_num, 1)
            comp_end = datetime.date(prev_month_year, prev_month_num, comp_end_day)

            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=first_of_month.strftime("%Y-%m-%d"),
                end_date=as_of_date_str,
                comp_start_date=comp_start.strftime("%Y-%m-%d"),
                comp_end_date=comp_end.strftime("%Y-%m-%d"),
                time_scope="this_month",
                shift_name=shift,
                explanation=(
                    f"Tháng này: từ {first_of_month.strftime('%Y-%m-%d')} đến hết hôm nay {as_of_date_str}. "
                    f"So với tháng trước (cùng số ngày): từ {comp_start.strftime('%Y-%m-%d')} đến {comp_end.strftime('%Y-%m-%d')}."
                ),
            )

        # 9. Check "tháng trước", "tháng rồi"
        if any(k in q_norm for k in ["tháng trước", "thang truoc", "tháng rồi", "thang roi"]):
            if month == 1:
                p_year = year - 1
                p_month = 12
            else:
                p_year = year
                p_month = month - 1
            _, p_last = calendar.monthrange(p_year, p_month)
            p_start = datetime.date(p_year, p_month, 1)
            p_end = datetime.date(p_year, p_month, p_last)
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=p_start.strftime("%Y-%m-%d"),
                end_date=p_end.strftime("%Y-%m-%d"),
                time_scope="last_month",
                shift_name=shift,
                explanation=f"Tháng trước/rồi (toàn bộ): {p_start.strftime('%Y-%m-%d')} đến {p_end.strftime('%Y-%m-%d')}.",
            )

        # 10. Check specific "tháng M/YYYY" or "tháng M"
        specific_month_match = re.search(r"tháng\s*(\d{1,2})(?:/(\d{4}))?", q_norm)
        if specific_month_match:
            m_num = int(specific_month_match.group(1))
            y_str = specific_month_match.group(2)
            if y_str:
                m_year = int(y_str)
            else:
                # Rulebook: "Tháng M không ghi năm: của năm nay nếu không sau hôm nay; sau hôm nay thì của năm trước"
                m_year = year if m_num <= month else (year - 1)
            _, m_last = calendar.monthrange(m_year, m_num)
            m_start = datetime.date(m_year, m_num, 1)
            m_end = datetime.date(m_year, m_num, m_last)
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=m_start.strftime("%Y-%m-%d"),
                end_date=m_end.strftime("%Y-%m-%d"),
                time_scope="specific_month",
                shift_name=shift,
                explanation=f"Tháng {m_num}/{m_year}: từ {m_start.strftime('%Y-%m-%d')} đến hết {m_end.strftime('%Y-%m-%d')}.",
            )

        # 11. Check "từ đầu năm", "từ đầu năm tới nay"
        if any(k in q_norm for k in ["từ đầu năm", "tu dau nam", "đầu năm tới nay", "dau nam toi nay"]):
            y_start = datetime.date(year, 1, 1)
            return DateResolution(
                as_of_date=as_of_date_str,
                start_date=y_start.strftime("%Y-%m-%d"),
                end_date=as_of_date_str,
                time_scope="year_to_date",
                shift_name=shift,
                explanation=f"Từ đầu năm đến hôm nay: từ {y_start.strftime('%Y-%m-%d')} đến {as_of_date_str}.",
            )

        # Default fallback
        return DateResolution(
            as_of_date=as_of_date_str,
            time_scope="general",
            shift_name=shift,
            explanation=f"Mốc thời gian hôm nay: {as_of_date_str}.",
        )
