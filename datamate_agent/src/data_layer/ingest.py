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
            
            # Fetch sample rows
            try:
                samples = self.con.execute(f"SELECT * FROM {tbl} LIMIT 2").fetchall()
                sample_str = f"Sample rows ({len(samples)}): {samples}"
            except Exception:
                sample_str = ""

            lines.append(f"Table `{tbl}`:\n" + "\n".join(col_desc) + f"\n{sample_str}\n")
        return "\n".join(lines)


def normalize_identifier(name: str) -> str:
    """
    Normalizes column or table names into clean snake_case ASCII strings.
    E.g. 'Mã đơn hàng' -> 'ma_don_hang', 'Giá bán (VND)' -> 'gia_ban_vnd'.
    """
    if not name or not isinstance(name, str):
        return "col"
    nfkd = unicodedata.normalize("NFKD", str(name).strip())
    ascii_text = nfkd.encode("ascii", "ignore").decode("utf-8")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text.lower()).strip("_")
    if cleaned and cleaned[0].isdigit():
        cleaned = "col_" + cleaned
    return cleaned or "col"


def clean_number_series(s: pd.Series) -> pd.Series:
    """
    Vectorized parser for Vietnamese formatted currency and quantity strings.
    """
    if pd.api.types.is_numeric_dtype(s):
        return s
    
    # Strip whitespace and currency suffixes
    str_s = s.astype(str).str.strip()
    str_s = str_s.str.replace(r"(?i)\s*(?:đ|vnd|dong|%)\s*$", "", regex=True).str.strip()
    
    # If formatted as 1.000.000 (dots as thousands) or 1,000,000 (commas as thousands)
    # Check if commas are used
    has_comma = str_s.str.contains(",", regex=False)
    has_dot = str_s.str.contains(".", regex=False)
    
    # Simple heuristic: remove commas first
    cand = str_s.str.replace(",", "", regex=False)
    num = pd.to_numeric(cand, errors="coerce")
    
    # For rows where numeric failed, but contains dots (e.g. 560.000)
    failed_mask = num.isna() & has_dot & ~str_s.isin(["nan", "None", "", "null"])
    if failed_mask.any():
        cand2 = str_s[failed_mask].str.replace(".", "", regex=False)
        num.loc[failed_mask] = pd.to_numeric(cand2, errors="coerce")
        
    return num


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
    1. Forward-fill empty grouped rows for order metadata (Rulebook Section 8).
    2. Normalize column headers into unique snake_case ASCII identifiers.
    3. Vectorized normalization of numbers and dates.
    """
    df = df.copy()

    # Rulebook Section 8: Forward-fill empty grouped rows
    first_col = df.columns[0]
    if len(df.columns) > 2 and df[first_col].isna().sum() > 0:
        if df[first_col].first_valid_index() is not None:
            group_cols = []
            for col in df.columns[:5]:
                col_lower = str(col).lower()
                if any(k in col_lower for k in ["mã", "don", "ngày", "ngay", "khách", "khach", "trạng", "trang"]):
                    group_cols.append(col)
            if group_cols:
                df[group_cols] = df[group_cols].ffill()

    # Clean headers & build mapping
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

    # Vectorized cleaning for dates and numbers
    for col in df.columns:
        col_lower = col.lower()
        if any(d in col_lower for d in ["ngay", "date", "thoi_gian"]):
            df[col] = clean_date_series(df[col])
        elif any(n in col_lower for n in ["gia", "tien", "thanh_toan", "so_luong", "soluong", "no", "tong", "chiet_khau", "giam"]):
            df[col] = clean_number_series(df[col])

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
                        df = pd.read_csv(fpath, encoding=enc, low_memory=False)
                        break
                    except Exception:
                        continue
                if df is not None:
                    clean_df, col_map = preprocess_dataframe(df)
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
                print(f"Error loading CSV {fname}: {e}")

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
                        sdf = pd.read_excel(excel_file, sheet_name=sname)
                        if not sdf.empty:
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
