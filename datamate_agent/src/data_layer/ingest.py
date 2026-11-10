"""
Data Ingestion Module for DataMate Challenge.
Loads raw CSV, XLSX, and SQLite files for a business into DuckDB.
Handles Vietnamese formatting (currencies, dates, encodings, delimiters, merged headers),
snake_case ASCII column normalization, original->clean column mapping,
and DuckDB view persistence/caching.
"""

import json
import logging
import os
import re
import sqlite3
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

import duckdb
import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class BusinessContext:
    business_id: str
    business_dir: str
    con: duckdb.DuckDBPyConnection
    table_names: List[str]
    schemas: Dict[str, List[Dict[str, Any]]]
    readme_text: str = ""
    column_mappings: Dict[str, Dict[str, str]] = field(default_factory=dict)
    is_cached: bool = False
    cached_db_path: Optional[str] = None
    canonical_views: Dict[str, Any] = field(default_factory=dict)
    debt_macros_registered: bool = False

    def get_schema_summary(self) -> str:
        lines = []
        for tbl in self.table_names:
            cols = self.schemas.get(tbl, [])
            col_desc = []
            for c in cols:
                orig = c.get("original", c["name"])
                dtype = c.get("type", "TEXT")
                if orig != c["name"]:
                    col_desc.append(f"  - {c['name']} ({dtype}, original: '{orig}')")
                else:
                    col_desc.append(f"  - {c['name']} ({dtype})")

            # Fetch compact sample rows (truncated to prevent VRAM explosion on large tables)
            try:
                raw_samples = self.con.execute(f"SELECT * FROM {tbl} LIMIT 1").fetchall()
                compact_samples = []
                for row in raw_samples:
                    compact_row = tuple(
                        (str(v)[:20] + "...") if isinstance(v, str) and len(str(v)) > 20 else v
                        for v in row
                    )
                    compact_samples.append(compact_row)
                sample_str = f"Sample row: {compact_samples[0]}" if compact_samples else ""
                if len(sample_str) > 200:
                    sample_str = sample_str[:200] + "...)"
            except Exception:
                sample_str = ""

            lines.append(f"Table `{tbl}`:\n" + "\n".join(col_desc) + (f"\n{sample_str}\n" if sample_str else "\n"))

        # Auto-detect table relationships & join hints
        rel_hints = []
        tbl_cols = {t: [c["name"].lower() for c in self.schemas.get(t, [])] for t in self.table_names}
        tbl_orig_cols = {t: {c["name"].lower(): c["name"] for c in self.schemas.get(t, [])} for t in self.table_names}

        JOIN_ID_PATTERNS = [
            "ma_hoa_don", "ma_don", "ma_don_hang", "so_hd", "id_don_hang", "so_ct",
            "ma_nhap_hang", "ma_phieu_nhap", "ma_phieu", "so_phieu",
            "ma_hang", "ma_sp", "ma_khach", "ma_ncc"
        ]
        DATE_COL_NAMES = ["thoi_gian", "thoi_gian_tao", "ngay_ban", "ngay_tao", "ngay_hd", "ngay_nhap", "ngay_lap", "ngay", "date"]

        for i, t1 in enumerate(self.table_names):
            for j, t2 in enumerate(self.table_names):
                if i >= j:
                    continue
                c1_set = set(tbl_cols[t1])
                c2_set = set(tbl_cols[t2])
                common = c1_set.intersection(c2_set)

                matching_keys = [k for k in common if any(p in k for p in JOIN_ID_PATTERNS) or k.startswith("ma_") or k.endswith("_id")]
                if matching_keys:
                    best_key = matching_keys[0]
                    t1_date = [c for c in tbl_cols[t1] if any(d in c for d in DATE_COL_NAMES)]
                    t2_date = [c for c in tbl_cols[t2] if any(d in c for d in DATE_COL_NAMES)]

                    orig_k1 = tbl_orig_cols[t1].get(best_key, best_key)
                    orig_k2 = tbl_orig_cols[t2].get(best_key, best_key)

                    date_note = ""
                    if t1_date and not t2_date:
                        orig_d = tbl_orig_cols[t1].get(t1_date[0], t1_date[0])
                        date_note = f" (Note: Date '{orig_d}' is in `{t1}`)"
                    elif t2_date and not t1_date:
                        orig_d = tbl_orig_cols[t2].get(t2_date[0], t2_date[0])
                        date_note = f" (Note: Date '{orig_d}' is in `{t2}`)"

                    rel_hints.append(f"- Join `{t1}` and `{t2}` ON `{t1}.{orig_k1} = {t2}.{orig_k2}`{date_note}")

        if rel_hints:
            # Keep top 6 most relevant join hints to prevent prompt explosion on multi-table shops
            compact_rel_hints = rel_hints[:6]
            lines.append("Table Relationships & Join Hints:\n" + "\n".join(compact_rel_hints) + "\n")

        return "\n".join(lines)


def fix_mojibake_filename(name: str) -> str:
    """Attempts to fix cp437 mojibake encoding produced by zip / gdown."""
    try:
        return name.encode("cp437").decode("utf-8")
    except Exception:
        return name


def normalize_identifier(name: Any) -> str:
    """
    Normalizes column or table names into clean snake_case ASCII strings.
    E.g. 'Mã đơn hàng' -> 'ma_don_hang', 'Giá bán (VND)' -> 'gia_ban_vnd'.
    Handles mojibake encoding recovery and Vietnamese 'đ'/'Đ' conversion.
    """
    if name is None or not isinstance(name, str):
        if name is not None:
            name = str(name)
        else:
            return "col"
    fixed_name = fix_mojibake_filename(str(name).strip())
    # Replace Vietnamese đ/Đ explicitly before NFKD
    fixed_name = fixed_name.replace("đ", "d").replace("Đ", "D")
    nfkd = unicodedata.normalize("NFKD", fixed_name)
    ascii_text = nfkd.encode("ascii", "ignore").decode("utf-8")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text.lower()).strip("_")
    if cleaned and cleaned[0].isdigit():
        cleaned = "col_" + cleaned
    return cleaned or "col"


def resolve_business_dir(data_dir: str, business_id: str) -> Optional[str]:
    """
    Resolves the actual directory for a business.
    Tries in order:
    1. <data_dir>/<business_id>
    2. <data_dir>/data/<business_id>
    3. One-level subdirectory scan: <data_dir>/*/<business_id> and <data_dir>/*/data/<business_id>
    Returns absolute path if found, or None if not found.
    """
    if not data_dir or not business_id:
        return None

    # Candidate paths to test directly
    candidates = [
        os.path.join(data_dir, business_id),
        os.path.join(data_dir, "data", business_id),
    ]
    for c in candidates:
        if os.path.exists(c) and os.path.isdir(c):
            return os.path.abspath(c)

    # Scan one level of subdirectories
    if os.path.exists(data_dir) and os.path.isdir(data_dir):
        try:
            for entry in os.listdir(data_dir):
                sub = os.path.join(data_dir, entry)
                if os.path.isdir(sub):
                    sub_cands = [
                        os.path.join(sub, business_id),
                        os.path.join(sub, "data", business_id),
                    ]
                    for sc in sub_cands:
                        if os.path.exists(sc) and os.path.isdir(sc):
                            return os.path.abspath(sc)
        except Exception:
            pass

    return None


def parse_vietnamese_number_scalar(val: Any) -> Optional[float]:
    """
    Parses a single scalar into a float according to Vietnamese number formatting.
    Handles:
      - '150.000 đ' -> 150000.0
      - '25.000đ' -> 25000.0
      - '12,5' -> 12.5
      - '1.234,56' -> 1234.56
      - '1,234,567' -> 1234567.0
      - '1.234.567' -> 1234567.0
      - '12,5%' -> 12.5
      - '12.5' -> 12.5
      - '(50.000)' -> -50000.0
      - '-12.500' -> -12500.0
    """
    if val is None or pd.isna(val):
        return None
    if isinstance(val, (int, float)):
        return float(val)

    s = str(val).strip()
    if not s or s.lower() in ("nan", "none", "null", "-", "—"):
        return None

    # Handle accounting parentheses for negatives e.g. (50.000)
    is_neg = False
    if s.startswith("(") and s.endswith(")"):
        is_neg = True
        s = s[1:-1].strip()
    elif s.startswith("-"):
        is_neg = True
        s = s[1:].strip()

    # Strip currency and percentage symbols and trailing/leading whitespace
    s = re.sub(r"(?i)\s*(?:đ|vnd|dong|%)\s*$", "", s).strip()
    s = re.sub(r"(?i)^(?:đ|vnd|dong)\s*", "", s).strip()
    s = s.replace(" ", "")

    if not s:
        return None

    has_dot = "." in s
    has_comma = "," in s

    # Both dot and comma present
    if has_dot and has_comma:
        last_dot = s.rfind(".")
        last_comma = s.rfind(",")
        if last_dot < last_comma:
            # e.g. "1.234,56" or "1.234.567,89" -> dot is thousands, comma is decimal
            s = s.replace(".", "").replace(",", ".")
        else:
            # e.g. "1,234.56" or "1,234,567.89" -> comma is thousands, dot is decimal
            s = s.replace(",", "")
    elif has_dot and not has_comma:
        if s.count(".") > 1:
            # Multiple dots: "1.234.567" -> thousands
            s = s.replace(".", "")
        else:
            # Single dot: e.g. "25.000" vs "12.5"
            parts = s.split(".")
            if len(parts) == 2 and len(parts[1]) == 3 and parts[0].isdigit():
                # Vietnamese currency with 3 trailing decimals is thousand separator
                s = s.replace(".", "")
    elif has_comma and not has_dot:
        if s.count(",") > 1:
            # Multiple commas: "1,234,567" -> thousands
            s = s.replace(",", "")
        else:
            # Single comma: "12,5" vs "1,234"
            parts = s.split(",")
            if len(parts) == 2 and len(parts[1]) == 3 and parts[0].isdigit():
                s = s.replace(",", "")
            elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                s = s.replace(",", ".")
            else:
                s = s.replace(",", "")

    try:
        f = float(s)
        return -f if is_neg else f
    except Exception:
        return None


def clean_number_series(s: pd.Series) -> pd.Series:
    """
    Vectorized parser for Vietnamese formatted currency and quantity strings.
    """
    if pd.api.types.is_numeric_dtype(s):
        return s
    return s.apply(parse_vietnamese_number_scalar)


def is_vietnamese_number_string(val: Any) -> bool:
    """
    Checks if a scalar string matches Vietnamese numeric/currency formatting.
    E.g. "1.250.000", "45,000đ", "12,5%", "150.000 đ", "25000", "12.5".
    """
    if val is None or pd.isna(val):
        return False
    if isinstance(val, (int, float)):
        return True
    s = str(val).strip()
    if not s or s.lower() in ("nan", "none", "null", "-", "—"):
        return False
    cleaned = re.sub(r"(?i)\s*(?:đ|vnd|dong|%)\s*$", "", s).strip()
    cleaned = re.sub(r"(?i)^(?:đ|vnd|dong)\s*", "", cleaned).strip()
    cleaned = cleaned.replace(" ", "")
    if not cleaned:
        return False
    # Starts with optional minus or enclosed in ()
    if cleaned.startswith("(") and cleaned.endswith(")"):
        cleaned = cleaned[1:-1]
    return bool(re.match(r"^-?\d+(?:[.,]\d+)*$", cleaned))


def find_true_header_from_df(df: pd.DataFrame) -> Tuple[int, List[str]]:
    """
    Detects the true header row index in Excel/CSV sheets.
    Automatically skips leading empty/title rows by finding the first row with >= 2 non-null string cells.
    Handles title banners and multi-level group headers.
    """
    if df.empty:
        return 0, []

    best_idx = 0
    best_score = -1
    best_cols = []

    for idx in range(min(15, len(df))):
        row = df.iloc[idx]
        non_empty_cells = [
            str(c).strip() for c in row
            if pd.notna(c) and str(c).strip() != "" and str(c).lower() != "nan" and not str(c).startswith("Unnamed:")
        ]
        count = len(non_empty_cells)
        if count < 2:
            continue

        # Check how many cells look like string identifiers/labels rather than dates/numeric data
        string_count = sum(
            1 for c in non_empty_cells
            if not re.match(r"^-?\d+([.,]\d+)*$", c) and not re.match(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", c)
        )

        is_likely_data = (count >= 3 and string_count < count * 0.5)
        if is_likely_data:
            if best_score > 0:
                break

        score = count * 2 + string_count * 3
        if score > best_score:
            best_score = score
            best_idx = idx
            best_cols = [str(c).strip() if pd.notna(c) and str(c).strip() else f"col_{i}" for i, c in enumerate(row)]

    if best_score > 0:
        return best_idx, best_cols
    return 0, [str(c) for c in df.columns]


def drop_subtotal_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes subtotal / 'Tổng cộng' rows from dataframe.
    """
    keywords = ["tổng cộng", "tong cong", "tổng", "tong", "subtotal", "total"]
    if df.empty:
        return df

    drop_indices = []
    for idx, row in df.iterrows():
        is_sub = False
        for cell in row:
            if pd.notna(cell):
                c_str = str(cell).strip().lower()
                if any(c_str == k or c_str.startswith(f"{k}:") or c_str.startswith(f"{k} ") for k in keywords):
                    is_sub = True
                    break
        if is_sub:
            drop_indices.append(idx)

    if drop_indices:
        return df.drop(index=drop_indices).reset_index(drop=True)
    return df


def clean_date_series(s: pd.Series) -> pd.Series:
    """
    Vectorized normalization of date series to ISO 'YYYY-MM-DD'.
    Handles formats like 'DD/MM/YYYY', 'DD-MM-YYYY', 'YYYY-MM-DD', 'D thg M YYYY', 'D tháng M YYYY',
    as well as Excel integer serial dates (e.g. 45689 -> 2025-02-01).
    """
    if pd.api.types.is_datetime64_any_dtype(s):
        return s.dt.strftime("%Y-%m-%d")

    # 1. Parse Excel numeric serial dates (typical range 35000 - 65000: 1995 to 2075)
    num_s = pd.to_numeric(s, errors="coerce")
    excel_mask = num_s.notna() & (num_s >= 35000) & (num_s <= 65000)
    dt_excel = pd.Series(pd.NaT, index=s.index)
    if excel_mask.any():
        dt_excel[excel_mask] = pd.to_datetime(num_s[excel_mask], unit="D", origin="1899-12-30", errors="coerce")

    str_s = s.astype(str).str.strip()

    # 2. Check Vietnamese text date: '1 thg 6 2025' or '15 tháng 12 2026'
    extr = str_s.str.extract(r"^(\d{1,2})\s*(?:thg|tháng|thg\.)\s*(\d{1,2})\s*(\d{4})")
    dt_vn = pd.to_datetime(extr[2] + "-" + extr[1] + "-" + extr[0], format="%Y-%m-%d", errors="coerce")

    dt_dmy = pd.to_datetime(str_s, format="%d/%m/%Y", errors="coerce")
    dt_dmy_dash = pd.to_datetime(str_s, format="%d-%m-%Y", errors="coerce")
    dt_ymd = pd.to_datetime(str_s, format="%Y-%m-%d", errors="coerce")
    dt_dt1 = pd.to_datetime(str_s, format="%Y-%m-%d %H:%M:%S", errors="coerce")
    dt_dt2 = pd.to_datetime(str_s, format="%d/%m/%Y %H:%M:%S", errors="coerce")
    dt_dt3 = pd.to_datetime(str_s, format="%d-%m-%Y %H:%M:%S", errors="coerce")

    merged_dt = (
        dt_excel.fillna(dt_vn)
        .fillna(dt_dmy)
        .fillna(dt_dmy_dash)
        .fillna(dt_ymd)
        .fillna(dt_dt1)
        .fillna(dt_dt2)
        .fillna(dt_dt3)
    )
    valid_mask = merged_dt.notna()
    res = str_s.copy()
    res.loc[valid_mask] = merged_dt.loc[valid_mask].dt.strftime("%Y-%m-%d")
    return res


def preprocess_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    """
    Preprocesses a raw DataFrame:
    1. Removes subtotal / summary rows.
    2. Forward-fill empty grouped rows for confirmed order metadata.
    3. Normalize column headers into unique snake_case ASCII identifiers.
    4. Type casting:
       - Match date columns by keyword or >70% date pattern matches -> clean_date_series.
       - Detect string columns where >70% of non-null values match Vietnamese number patterns
         (e.g., '1.250.000', '45,000đ', '12,5%') and parse them into clean DOUBLE / BIGINT.
       - Preserve text and identifier columns.
    """
    df = df.copy()

    # 1. Drop subtotal rows
    df = drop_subtotal_rows(df)

    # 2. Forward-fill empty grouped rows (only order metadata)
    ALLOWED_FFILL_WORDS = {"ma", "don", "so_phieu", "chung_tu", "ngay", "khach", "khach_hang", "trang_thai", "status", "tinh_trang"}
    if len(df.columns) > 2 and len(df) > 0:
        first_col = df.columns[0]
        if df[first_col].isna().sum() > 0 and df[first_col].first_valid_index() is not None:
            group_cols = []
            for col in df.columns[:6]:
                col_norm = normalize_identifier(str(col))
                words = set(col_norm.split("_"))
                if words & {"gia", "don_gia", "tien", "thanh_tien", "so_luong"}:
                    continue
                if words & ALLOWED_FFILL_WORDS:
                    group_cols.append(col)
            if group_cols:
                df[group_cols] = df[group_cols].ffill()

    # 3. Clean headers & build mapping
    col_mapping = {}
    new_cols = []
    seen = {}
    for col in df.columns:
        norm = normalize_identifier(str(col))
        if norm in seen:
            seen[norm] += 1
            norm = f"{norm}_{seen[norm]}"
        else:
            seen[norm] = 1
        new_cols.append(norm)
        col_mapping[norm] = str(col)
    df.columns = new_cols

    # 4. Safe type cleaning for dates and numbers
    DATE_KEYWORDS = {"ngay", "date", "thoi_gian", "ngay_lap", "ngay_ct", "ngay_dat", "ngay_ban", "ngay_tao"}
    IDENTIFIER_KEYWORDS = {"id", "ma", "code", "barcode", "sdt", "phone", "dien_thoai", "ghi_chu", "note", "mo_ta", "ten", "name"}

    for col in df.columns:
        words = set(col.lower().split("_"))

        # Check Date column
        if words & DATE_KEYWORDS:
            df[col] = clean_date_series(df[col])
            continue

        # If column is already numeric, keep numeric
        if pd.api.types.is_numeric_dtype(df[col]):
            continue

        orig_series = df[col]
        non_empty_mask = (
            orig_series.notna()
            & (orig_series.astype(str).str.strip() != "")
            & (orig_series.astype(str).str.lower() != "nan")
        )
        num_non_empty = int(non_empty_mask.sum())

        if num_non_empty == 0:
            # Completely empty column -> strictly VARCHAR in DuckDB
            df[col] = pd.Series([None] * len(df), dtype="string")
            continue

        # If not an identifier column, check if >70% match Vietnamese number patterns
        is_ident = bool(words & IDENTIFIER_KEYWORDS)
        if not is_ident:
            matching_count = sum(is_vietnamese_number_string(v) for v in orig_series[non_empty_mask])
            ratio = matching_count / num_non_empty

            if ratio >= 0.70:
                cleaned = clean_number_series(orig_series)
                parsed_non_empty = int(cleaned[non_empty_mask].notna().sum())
                parse_rate = parsed_non_empty / num_non_empty
                loss_rate = (num_non_empty - parsed_non_empty) / num_non_empty

                if parse_rate >= 0.70 and loss_rate <= 0.30:
                    # Check if all non-null parsed values are integer-like
                    valid_cleaned = cleaned[cleaned.notna()]
                    if len(valid_cleaned) > 0 and (valid_cleaned % 1 == 0).all():
                        df[col] = cleaned.astype("Int64")
                    else:
                        df[col] = cleaned.astype("float64")
                    continue

        # If column remains object and all values are null, cast to string
        if df[col].isna().all():
            df[col] = pd.Series([None] * len(df), dtype="string")

    return df, col_mapping


def get_duckdb_cache_dir(cache_dir: Optional[str] = None) -> str:
    """
    Resolves the directory for caching DuckDB files:
    <cache_dir>/duckdb_cache/
    """
    base = cache_dir or os.environ.get("LOCAL_CACHE_DIR") or os.environ.get("DATAMATE_CACHE_DIR") or "./data_cache"
    d = os.path.join(base, "duckdb_cache")
    os.makedirs(d, exist_ok=True)
    return d


def read_csv_robust(fpath: str) -> Optional[pd.DataFrame]:
    """
    Reads CSV trying encodings (utf-8-sig, utf-8, cp1258, latin1) and auto-detecting delimiters (',', ';', '\t').
    """
    encodings = ["utf-8-sig", "utf-8", "cp1258", "latin1"]
    delimiters = [",", ";", "\t"]

    best_df = None
    best_cols = 0

    for enc in encodings:
        for sep in delimiters:
            try:
                df = pd.read_csv(fpath, encoding=enc, sep=sep, header=None, low_memory=False)
                if df is not None and not df.empty:
                    # Drop completely empty rows and columns
                    df = df.dropna(how="all", axis=0).dropna(how="all", axis=1)
                    if not df.empty and df.shape[1] > best_cols:
                        best_df = df
                        best_cols = df.shape[1]
                        if best_cols > 1:
                            return best_df
            except Exception:
                continue

    return best_df


def load_business_data(
    business_id: str,
    business_dir: str,
    cache_dir: Optional[str] = None,
    force_refresh: bool = False,
    auto_build_views: bool = True,
) -> BusinessContext:
    """
    Ingests all files (.csv, .xlsx, .sqlite) in business_dir into a DuckDB database.
    Persists database and verified canonical views to:
        <local_cache_dir>/duckdb_cache/<business_id>.duckdb
        <local_cache_dir>/duckdb_cache/<business_id>_schema_meta.json
    If cached .duckdb exists and has valid views, loads it directly in read_only=True mode.
    """
    if not os.path.exists(business_dir):
        con = duckdb.connect(database=":memory:")
        return BusinessContext(
            business_id=business_id,
            business_dir=business_dir,
            con=con,
            table_names=[],
            schemas={},
            readme_text="",
        )

    # 1. Check DuckDB Disk Cache
    cache_root = get_duckdb_cache_dir(cache_dir)
    db_cache_path = os.path.join(cache_root, f"{business_id}.duckdb")
    meta_cache_path = os.path.join(cache_root, f"{business_id}_schema_meta.json")

    if not force_refresh and os.path.exists(db_cache_path) and os.path.exists(meta_cache_path):
        try:
            with open(meta_cache_path, "r", encoding="utf-8") as f_meta:
                meta = json.load(f_meta)

            # Check if source business_dir matches and files haven't been modified
            cached_dir = meta.get("business_dir", "")
            cached_views = meta.get("canonical_views", {})
            has_valid_views = bool(cached_views and cached_views.get("v_sales_sql"))

            con = duckdb.connect(database=db_cache_path, read_only=True)
            cached_tables = [r[0] for r in con.execute("SHOW TABLES").fetchall()]

            if (has_valid_views and "v_sales" in cached_tables and "v_orders" in cached_tables) or meta.get("ingested_successfully"):
                logger.info(f"Loaded cached DuckDB for business '{business_id}' (read_only=True): {db_cache_path}")
                return BusinessContext(
                    business_id=business_id,
                    business_dir=business_dir,
                    con=con,
                    table_names=meta.get("table_names", cached_tables),
                    schemas=meta.get("schemas", {}),
                    readme_text=meta.get("readme_text", ""),
                    column_mappings=meta.get("column_mappings", {}),
                    is_cached=True,
                    cached_db_path=db_cache_path,
                    canonical_views=cached_views,
                    debt_macros_registered=meta.get("debt_macros_registered", False),
                )
            else:
                con.close()
        except Exception as e:
            logger.warning(f"Error reading cache for '{business_id}' ({e}). Re-ingesting...")

    # 2. Ingest Fresh Database
    # Remove stale cache file if exists
    if os.path.exists(db_cache_path):
        try:
            os.remove(db_cache_path)
        except Exception:
            pass

    try:
        con = duckdb.connect(database=db_cache_path, read_only=False)
    except Exception as e:
        logger.warning(f"Could not open file-backed DuckDB '{db_cache_path}' ({e}), using :memory:")
        con = duckdb.connect(database=":memory:")
        db_cache_path = None

    table_names = []
    schemas: Dict[str, List[Dict[str, Any]]] = {}
    all_col_mappings: Dict[str, Dict[str, str]] = {}
    readme_text = ""

    # 2.1 Read README.md if present
    readme_path = os.path.join(business_dir, "README.md")
    if os.path.exists(readme_path):
        for enc in ["utf-8", "utf-8-sig", "latin1", "cp1258"]:
            try:
                with open(readme_path, "r", encoding=enc) as f:
                    readme_text = f.read()
                break
            except Exception:
                continue

    files = sorted(os.listdir(business_dir))

    # 2.2 Ingest CSV files
    for fname in files:
        if fname.lower().endswith(".csv") and fname.lower() != "calendar.csv":
            fpath = os.path.join(business_dir, fname)
            tbl_base = normalize_identifier(os.path.splitext(fname)[0])
            try:
                raw_df = read_csv_robust(fpath)
                if raw_df is not None and not raw_df.empty:
                    h_idx, cols = find_true_header_from_df(raw_df)
                    data_df = raw_df.iloc[h_idx + 1:].copy()
                    data_df.columns = cols
                    data_df = data_df.dropna(how="all", axis=0).dropna(how="all", axis=1).reset_index(drop=True)
                    clean_df, col_map = preprocess_dataframe(data_df)
                    tbl_name = f"raw_{tbl_base}"
                    con.register(f"{tbl_name}_df", clean_df)
                    con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                    con.unregister(f"{tbl_name}_df")
                    table_names.append(tbl_name)
                    all_col_mappings[tbl_name] = col_map
                    schemas[tbl_name] = [
                        {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                        for col in clean_df.columns
                    ]
                    # Also create alias view without raw_ prefix
                    if tbl_base != tbl_name:
                        try:
                            con.execute(f"CREATE VIEW {tbl_base} AS SELECT * FROM {tbl_name}")
                        except Exception:
                            pass
            except Exception as e:
                logger.error(f"Error loading CSV {fname}: {e}")

    # 2.3 Ingest Excel (.xlsx / .xls) files
    for fname in files:
        if fname.lower().endswith(".xlsx") or fname.lower().endswith(".xls"):
            fpath = os.path.join(business_dir, fname)
            tbl_base = normalize_identifier(os.path.splitext(fname)[0])
            try:
                excel_file = pd.ExcelFile(fpath, engine="openpyxl")
                sheet_names = excel_file.sheet_names

                sheet_dfs = []
                for sname in sheet_names:
                    try:
                        raw_sdf = pd.read_excel(excel_file, sheet_name=sname, header=None)
                        # Drop completely empty rows and columns
                        raw_sdf = raw_sdf.dropna(how="all", axis=0).dropna(how="all", axis=1)
                        if not raw_sdf.empty:
                            h_idx, cols = find_true_header_from_df(raw_sdf)
                            sdf = raw_sdf.iloc[h_idx + 1:].copy()
                            sdf.columns = cols
                            sdf = sdf.dropna(how="all", axis=0).dropna(how="all", axis=1).reset_index(drop=True)
                            if not sdf.empty:
                                sheet_dfs.append((sname, sdf))
                    except Exception:
                        pass

                if sheet_dfs:
                    first_cols = set(sheet_dfs[0][1].columns)
                    is_single_sheet = (len(sheet_dfs) == 1)

                    is_monthly_pattern = all(
                        bool(re.search(r"(?i)(?:thang|\bt\d{1,2}\b|\d{1,2}[._/]\d{4}|\b202\d\b|sheet\d+)", s[0]))
                        for s in sheet_dfs
                    )
                    overlap_ratios = [
                        len(first_cols & set(s[1].columns)) / max(len(first_cols), 1)
                        for s in sheet_dfs
                    ]
                    is_homogenous = len(sheet_dfs) > 1 and (
                        all(r >= 0.40 for r in overlap_ratios) or is_monthly_pattern
                    )

                    if is_single_sheet:
                        sname, sdf = sheet_dfs[0]
                        clean_df, col_map = preprocess_dataframe(sdf)
                        tbl_name = f"raw_{tbl_base}"
                        con.register(f"{tbl_name}_df", clean_df)
                        con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                        con.unregister(f"{tbl_name}_df")
                        table_names.append(tbl_name)
                        all_col_mappings[tbl_name] = col_map
                        schemas[tbl_name] = [
                            {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                            for col in clean_df.columns
                        ]
                        clean_sname = normalize_identifier(sname)
                        sheet_alias = f"raw_{tbl_base}_{clean_sname}"
                        if sheet_alias != tbl_name:
                            try:
                                con.execute(f"CREATE VIEW {sheet_alias} AS SELECT * FROM {tbl_name}")
                            except Exception:
                                pass
                        if tbl_base != tbl_name:
                            try:
                                con.execute(f"CREATE VIEW {tbl_base} AS SELECT * FROM {tbl_name}")
                            except Exception:
                                pass

                    elif is_homogenous:
                        combined = pd.concat([s[1] for s in sheet_dfs], ignore_index=True)
                        clean_df, col_map = preprocess_dataframe(combined)
                        tbl_name = f"raw_{tbl_base}"
                        con.register(f"{tbl_name}_df", clean_df)
                        con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                        con.unregister(f"{tbl_name}_df")
                        table_names.append(tbl_name)
                        all_col_mappings[tbl_name] = col_map
                        schemas[tbl_name] = [
                            {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                            for col in clean_df.columns
                        ]
                        for sname, _ in sheet_dfs:
                            clean_sname = normalize_identifier(sname)
                            sheet_alias = f"raw_{tbl_base}_{clean_sname}"
                            if sheet_alias != tbl_name:
                                try:
                                    con.execute(f"CREATE VIEW {sheet_alias} AS SELECT * FROM {tbl_name}")
                                except Exception:
                                    pass
                        if tbl_base != tbl_name:
                            try:
                                con.execute(f"CREATE VIEW {tbl_base} AS SELECT * FROM {tbl_name}")
                            except Exception:
                                pass

                    else:
                        for sname, sdf in sheet_dfs:
                            clean_df, col_map = preprocess_dataframe(sdf)
                            clean_sname = normalize_identifier(sname)
                            tbl_name = f"raw_{tbl_base}_{clean_sname}"
                            con.register(f"{tbl_name}_df", clean_df)
                            con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                            con.unregister(f"{tbl_name}_df")
                            table_names.append(tbl_name)
                            all_col_mappings[tbl_name] = col_map
                            schemas[tbl_name] = [
                                {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                                for col in clean_df.columns
                            ]
                        base_alias = f"raw_{tbl_base}"
                        if base_alias not in table_names and sheet_dfs:
                            first_clean_sname = normalize_identifier(sheet_dfs[0][0])
                            try:
                                con.execute(f"CREATE VIEW {base_alias} AS SELECT * FROM raw_{tbl_base}_{first_clean_sname}")
                            except Exception:
                                pass
            except Exception as e:
                logger.error(f"Error loading Excel {fname}: {e}")

    # 2.4 Ingest SQLite (.sqlite / .db) files
    for fname in files:
        if fname.lower().endswith(".sqlite") or fname.lower().endswith(".db"):
            fpath = os.path.join(business_dir, fname)
            tbl_prefix = normalize_identifier(os.path.splitext(fname)[0])
            try:
                sq_con = sqlite3.connect(fpath)
                cur = sq_con.cursor()
                sqlite_tables = cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
                ).fetchall()
                for (s_tbl,) in sqlite_tables:
                    try:
                        sdf = pd.read_sql_query(f"SELECT * FROM `{s_tbl}`", sq_con)
                        clean_df, col_map = preprocess_dataframe(sdf)
                        clean_tname = normalize_identifier(s_tbl)
                        tbl_name = f"raw_{tbl_prefix}_{clean_tname}" if tbl_prefix != clean_tname else f"raw_{clean_tname}"
                        con.register(f"{tbl_name}_df", clean_df)
                        con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                        con.unregister(f"{tbl_name}_df")
                        table_names.append(tbl_name)
                        all_col_mappings[tbl_name] = col_map
                        schemas[tbl_name] = [
                            {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                            for col in clean_df.columns
                        ]
                        if clean_tname != tbl_name:
                            try:
                                con.execute(f"CREATE VIEW {clean_tname} AS SELECT * FROM {tbl_name}")
                            except Exception:
                                pass
                    except Exception as te:
                        logger.error(f"Error reading SQLite table {s_tbl}: {te}")
                sq_con.close()
            except Exception as e:
                logger.error(f"Error loading SQLite {fname}: {e}")

    ctx = BusinessContext(
        business_id=business_id,
        business_dir=business_dir,
        con=con,
        table_names=table_names,
        schemas=schemas,
        readme_text=readme_text,
        column_mappings=all_col_mappings,
        is_cached=False,
        cached_db_path=db_cache_path,
    )

    # 3. Auto-build Canonical Views & Debt Macros into File-Backed DB and Cache Metadata
    if auto_build_views and db_cache_path is not None:
        try:
            from .view_builder import build_canonical_views
            from .debt_macros import register_debt_macros

            view_res = build_canonical_views(ctx, k=8)
            debt_status = register_debt_macros(ctx, plausibility_check=True)

            views_dict = {
                "success": view_res.success,
                "v_sales_sql": view_res.v_sales_sql,
                "v_orders_sql": view_res.v_orders_sql,
                "v_purchases_sql": view_res.v_purchases_sql,
            }
            ctx.canonical_views = views_dict
            ctx.debt_macros_registered = debt_status.registered

            # Save metadata json
            meta_data = {
                "business_id": business_id,
                "business_dir": business_dir,
                "ingested_successfully": True,
                "table_names": table_names,
                "schemas": schemas,
                "readme_text": readme_text,
                "column_mappings": all_col_mappings,
                "canonical_views": views_dict,
                "debt_macros_registered": debt_status.registered,
            }
            with open(meta_cache_path, "w", encoding="utf-8") as f_meta:
                json.dump(meta_data, f_meta, ensure_ascii=False, indent=2)

            # Reopen in read_only mode for safe multi-thread inference
            try:
                con.close()
                con_ro = duckdb.connect(database=db_cache_path, read_only=True)
                ctx.con = con_ro
                ctx.is_cached = True
            except Exception as ro_err:
                logger.warning(f"Could not reopen DuckDB in read_only mode ({ro_err}); keeping open connection.")

        except Exception as cache_err:
            logger.warning(f"Could not finalize DuckDB cache for '{business_id}': {cache_err}")

    return ctx
