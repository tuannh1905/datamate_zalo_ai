"""
Data Ingestion Module for DataMate Challenge.
Loads raw CSV, XLSX, and SQLite files for a business into DuckDB.
Normalizes headers, dates, amounts, and handles forward-fill for Vietnamese small-business records.
"""

import os
import re
import sqlite3
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import duckdb
import pandas as pd


@dataclass
class BusinessContext:
    business_id: str
    business_dir: str
    con: duckdb.DuckDBPyConnection
    table_names: List[str]
    schemas: Dict[str, List[Dict[str, Any]]]
    readme_text: str = ""
    column_mappings: Dict[str, Dict[str, str]] = field(default_factory=dict)

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
                raw_samples = self.con.execute(f"SELECT * FROM {tbl} LIMIT 2").fetchall()
                compact_samples = []
                for row in raw_samples:
                    compact_row = tuple(
                        (str(v)[:30] + "...") if isinstance(v, str) and len(str(v)) > 30 else v
                        for v in row
                    )
                    compact_samples.append(compact_row)
                sample_str = f"Sample rows ({len(compact_samples)}): {compact_samples}"
                if len(sample_str) > 300:
                    sample_str = sample_str[:300] + "...]"
            except Exception:
                sample_str = ""

            lines.append(f"Table `{tbl}`:\n" + "\n".join(col_desc) + f"\n{sample_str}\n")
        return "\n".join(lines)


def fix_mojibake_filename(name: str) -> str:
    """Attempts to fix cp437 mojibake encoding produced by zip / gdown."""
    try:
        return name.encode("cp437").decode("utf-8")
    except Exception:
        return name


def normalize_identifier(name: str) -> str:
    """
    Normalizes column or table names into clean snake_case ASCII strings.
    E.g. 'Mã đơn hàng' -> 'ma_don_hang', 'Giá bán (VND)' -> 'gia_ban_vnd'.
    Handles mojibake encoding recovery and Vietnamese 'đ'/'Đ' conversion.
    """
    if not name or not isinstance(name, str):
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
      - '25.000đ' -> 25000.0
      - '12,5' -> 12.5
      - '1.234,56' -> 1234.56
      - '1,234,567' -> 1234567.0
      - '1.234.567' -> 1234567.0
      - '12,5%' -> 12.5
      - '12.5' -> 12.5
    """
    if val is None or pd.isna(val):
        return None
    if isinstance(val, (int, float)):
        return float(val)

    s = str(val).strip()
    if not s or s.lower() in ("nan", "none", "null", "-", "—"):
        return None

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
        return float(s)
    except Exception:
        return None


def clean_number_series(s: pd.Series) -> pd.Series:
    """
    Vectorized parser for Vietnamese formatted currency and quantity strings.
    """
    if pd.api.types.is_numeric_dtype(s):
        return s
    return s.apply(parse_vietnamese_number_scalar)


def find_true_header_from_df(df: pd.DataFrame) -> Tuple[int, List[str]]:
    """
    Detects the true header row index: the first row with >= 3 non-empty cells.
    """
    for idx in range(min(15, len(df))):
        row = df.iloc[idx]
        non_empty = [c for c in row if pd.notna(c) and str(c).strip() != "" and str(c).lower() != "nan" and not str(c).startswith("Unnamed:")]
        if len(non_empty) >= 3:
            cols = [str(c).strip() if pd.notna(c) and str(c).strip() else f"col_{i}" for i, c in enumerate(row)]
            return idx, cols
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
    Handles formats like 'DD/MM/YYYY', 'YYYY-MM-DD', 'D thg M YYYY', 'D tháng M YYYY'.
    """
    if pd.api.types.is_datetime64_any_dtype(s):
        return s.dt.strftime("%Y-%m-%d")
    
    str_s = s.astype(str).str.strip()
    
    # Check Vietnamese text date: '1 thg 6 2025' or '15 tháng 12 2026'
    extr = str_s.str.extract(r"^(\d{1,2})\s*(?:thg|tháng|thg\.)\s*(\d{1,2})\s*(\d{4})")
    dt_vn = pd.to_datetime(extr[2] + "-" + extr[1] + "-" + extr[0], format="%Y-%m-%d", errors="coerce")
    
    dt_dmy = pd.to_datetime(str_s, format="%d/%m/%Y", errors="coerce")
    dt_ymd = pd.to_datetime(str_s, format="%Y-%m-%d", errors="coerce")
    dt_dt1 = pd.to_datetime(str_s, format="%Y-%m-%d %H:%M:%S", errors="coerce")
    dt_dt2 = pd.to_datetime(str_s, format="%d/%m/%Y %H:%M:%S", errors="coerce")
    
    merged_dt = dt_vn.fillna(dt_dmy).fillna(dt_ymd).fillna(dt_dt1).fillna(dt_dt2)
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
       - Match candidate columns by whole words (split by '_'), NOT substring.
       - Only cast if parsed rate >= 90%.
       - If casting loses > 20% of non-empty values, reverts to original column.
    """
    df = df.copy()

    # 1. Drop subtotal rows
    df = drop_subtotal_rows(df)

    # 2. Rulebook Section 8: Forward-fill empty grouped rows (only order metadata)
    ALLOWED_FFILL_WORDS = {"ma", "don", "so_phieu", "chung_tu", "ngay", "khach", "khach_hang", "trang_thai", "status", "tinh_trang"}
    first_col = df.columns[0]
    if len(df.columns) > 2 and df[first_col].isna().sum() > 0:
        if df[first_col].first_valid_index() is not None:
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
    DATE_KEYWORDS = {"ngay", "date", "thoi_gian", "ngay_lap", "ngay_ct", "ngay_dat", "ngay_ban"}
    AMOUNT_WORDS = {
        "gia", "don_gia", "gia_ban", "tien", "thanh_tien", "tong_tien",
        "so_luong", "soluong", "amount", "price", "quantity", "total",
        "no", "cong_no", "du_no", "chiet_khau", "giam_gia", "thanh_toan"
    }
    EXCLUDE_AMOUNT_WORDS = {"giao_hang", "noi_dung", "noi_giao", "don_vi", "ten"}

    for col in df.columns:
        words = set(col.lower().split("_"))
        if words & DATE_KEYWORDS:
            df[col] = clean_date_series(df[col])
        elif (words & AMOUNT_WORDS) and not any(ex in col.lower() for ex in EXCLUDE_AMOUNT_WORDS):
            orig_series = df[col]
            non_empty_mask = orig_series.notna() & (orig_series.astype(str).str.strip() != "") & (orig_series.astype(str).str.lower() != "nan")
            num_non_empty = int(non_empty_mask.sum())
            if num_non_empty > 0:
                cleaned = clean_number_series(orig_series)
                parsed_non_empty = int(cleaned[non_empty_mask].notna().sum())
                parse_rate = parsed_non_empty / num_non_empty
                loss_rate = (num_non_empty - parsed_non_empty) / num_non_empty

                if parse_rate >= 0.90 and loss_rate <= 0.20:
                    df[col] = cleaned
                else:
                    df[col] = orig_series

    return df, col_mapping


def load_business_data(business_id: str, business_dir: str) -> BusinessContext:
    """
    Ingests all files (.csv, .xlsx, .sqlite) in business_dir into an in-memory DuckDB database.
    """
    con = duckdb.connect(database=":memory:")
    table_names = []
    schemas: Dict[str, List[Dict[str, Any]]] = {}
    all_col_mappings: Dict[str, Dict[str, str]] = {}
    readme_text = ""

    if not os.path.exists(business_dir):
        return BusinessContext(
            business_id=business_id,
            business_dir=business_dir,
            con=con,
            table_names=[],
            schemas={},
            readme_text="",
        )

    # 1. Read README.md if present
    readme_path = os.path.join(business_dir, "README.md")
    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                readme_text = f.read()
        except Exception:
            try:
                with open(readme_path, "r", encoding="latin1") as f:
                    readme_text = f.read()
            except Exception:
                pass

    files = sorted(os.listdir(business_dir))

    # 2. Ingest CSV files
    for fname in files:
        if fname.lower().endswith(".csv") and fname.lower() != "calendar.csv":
            fpath = os.path.join(business_dir, fname)
            tbl_base = normalize_identifier(os.path.splitext(fname)[0])
            try:
                df = None
                for enc in ["utf-8", "utf-8-sig", "latin1", "cp1258"]:
                    try:
                        df = pd.read_csv(fpath, encoding=enc, header=None, low_memory=False)
                        break
                    except Exception:
                        continue
                if df is not None and not df.empty:
                    h_idx, cols = find_true_header_from_df(df)
                    data_df = df.iloc[h_idx + 1:].copy()
                    data_df.columns = cols
                    data_df = data_df.reset_index(drop=True)
                    clean_df, col_map = preprocess_dataframe(data_df)
                    tbl_name = f"raw_{tbl_base}"
                    con.register(f"{tbl_name}_df", clean_df)
                    con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                    table_names.append(tbl_name)
                    all_col_mappings[tbl_name] = col_map
                    schemas[tbl_name] = [
                        {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                        for col in clean_df.columns
                    ]
            except Exception as e:
                logger.error(f"Error loading CSV {fname}: {e}")

    # 3. Ingest Excel (.xlsx) files
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
                        if not raw_sdf.empty:
                            h_idx, cols = find_true_header_from_df(raw_sdf)
                            sdf = raw_sdf.iloc[h_idx + 1:].copy()
                            sdf.columns = cols
                            sdf = sdf.reset_index(drop=True)
                            sheet_dfs.append((sname, sdf))
                    except Exception:
                        pass

                if sheet_dfs:
                    first_cols = list(sheet_dfs[0][1].columns)
                    is_homogenous = len(sheet_dfs) > 1 and all(
                        list(s[1].columns) == first_cols for s in sheet_dfs
                    )

                    if is_homogenous:
                        combined = pd.concat([s[1] for s in sheet_dfs], ignore_index=True)
                        clean_df, col_map = preprocess_dataframe(combined)
                        tbl_name = f"raw_{tbl_base}"
                        con.register(f"{tbl_name}_df", clean_df)
                        con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                        table_names.append(tbl_name)
                        all_col_mappings[tbl_name] = col_map
                        schemas[tbl_name] = [
                            {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                            for col in clean_df.columns
                        ]
                    else:
                        for sname, sdf in sheet_dfs:
                            clean_df, col_map = preprocess_dataframe(sdf)
                            clean_sname = normalize_identifier(sname)
                            tbl_name = f"raw_{tbl_base}_{clean_sname}"
                            con.register(f"{tbl_name}_df", clean_df)
                            con.execute(f"CREATE TABLE {tbl_name} AS SELECT * FROM {tbl_name}_df")
                            table_names.append(tbl_name)
                            all_col_mappings[tbl_name] = col_map
                            schemas[tbl_name] = [
                                {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                                for col in clean_df.columns
                            ]
            except Exception as e:
                print(f"Error loading Excel {fname}: {e}")

    # 4. Ingest SQLite (.sqlite / .db) files
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
                        table_names.append(tbl_name)
                        all_col_mappings[tbl_name] = col_map
                        schemas[tbl_name] = [
                            {"name": col, "type": str(clean_df[col].dtype), "original": col_map.get(col, col)}
                            for col in clean_df.columns
                        ]
                    except Exception as te:
                        print(f"Error reading SQLite table {s_tbl}: {te}")
                sq_con.close()
            except Exception as e:
                print(f"Error loading SQLite {fname}: {e}")

    return BusinessContext(
        business_id=business_id,
        business_dir=business_dir,
        con=con,
        table_names=table_names,
        schemas=schemas,
        readme_text=readme_text,
        column_mappings=all_col_mappings,
    )
