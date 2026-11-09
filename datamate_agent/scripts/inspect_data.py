#!/usr/bin/env python3
"""
scripts/inspect_data.py - High-speed profiling of business datasets for DataMate Challenge.

Analyzes:
- File & sheet names (with mojibake recovery)
- Number of rows (fast streaming/read_only mode)
- True header row detection (first row with >= 3 non-empty cells)
- Sample rows
- Detection of "Tổng cộng" / subtotal rows
- Column heuristics (date, amount/currency, status)
- README description (truncated to 500 chars)
- Structural pattern (flat single table, header-detail, monthly split files, multi-table SQLite)

Outputs markdown report to `reports/data_profile_<name>.md`.
"""

import argparse
import itertools
import os
import re
import sqlite3
import unicodedata
from typing import Any, Dict, List, Optional, Tuple

import openpyxl
import pandas as pd


def fix_mojibake_filename(name: str) -> str:
    """Attempts to fix cp437 mojibake encoding produced by zip / gdown."""
    try:
        fixed = name.encode("cp437").decode("utf-8")
        return fixed
    except Exception:
        return name


def normalize_identifier(name: str) -> str:
    if not name or not isinstance(name, str):
        return "col"
    name = fix_mojibake_filename(str(name))
    nfkd = unicodedata.normalize("NFKD", name.strip())
    ascii_text = nfkd.encode("ascii", "ignore").decode("utf-8")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text.lower()).strip("_")
    if cleaned and cleaned[0].isdigit():
        cleaned = "col_" + cleaned
    return cleaned or "col"


def find_true_header(rows: List[List[Any]]) -> Tuple[int, List[str]]:
    """
    Finds true header row index: the first row with >= 3 non-empty cells.
    Returns (header_idx, header_columns).
    """
    for idx, row in enumerate(rows):
        non_empty = [c for c in row if c is not None and str(c).strip() != "" and str(c).lower() != "nan" and str(c).lower() != "unnamed"]
        if len(non_empty) >= 3:
            cols = [str(c).strip() if c is not None else f"col_{i}" for i, c in enumerate(row)]
            return idx, cols
    if rows:
        return 0, [str(c).strip() if c is not None else f"col_{i}" for i, c in enumerate(rows[0])]
    return 0, []


def detect_subtotal_in_rows(sample_rows: List[List[Any]], header_idx: int) -> bool:
    keywords = ["tổng cộng", "tong cong", "tổng", "tong", "subtotal", "total"]
    for row in sample_rows[header_idx + 1:]:
        for cell in row:
            if cell is not None:
                c_str = str(cell).strip().lower()
                if any(c_str == k or c_str.startswith(f"{k}:") or c_str.startswith(f"{k} ") for k in keywords):
                    return True
    return False


def identify_column_types(cols: List[str]) -> Dict[str, List[str]]:
    dates, amounts, statuses, ids = [], [], [], []
    for c in cols:
        cl = str(c).lower()
        words = set(re.findall(r"[a-z0-9]+", cl))
        if any(k in cl for k in ["ngay", "date", "thoi_gian", "ngay_lap", "ngay_ct", "ngay_dat"]):
            dates.append(c)
        elif words & {"gia", "don_gia", "gia_ban", "tien", "thanh_tien", "tong_tien", "so_luong", "soluong", "no", "cong_no", "chiet_khau", "giam_gia", "amount", "price", "quantity"}:
            amounts.append(c)
        elif any(k in cl for k in ["thanh_tien", "don_gia", "so_luong", "tien_hang", "so_tien", "thanh_toan"]):
            # Guard against giao_hang, noi_dung
            if not ("giao_hang" in cl or "noi_dung" in cl or "noi_giao" in cl):
                amounts.append(c)
        elif any(k in cl for k in ["trang_thai", "status", "ket_qua", "tinh_trang"]):
            statuses.append(c)
        elif any(k in cl for k in ["ma_don", "order_id", "ma_hang", "ma_sp", "ma_khach", "so_ct"]):
            ids.append(c)
    return {"date": dates, "amount": amounts, "status": statuses, "id": ids}


def classify_business_structure(files: List[str], table_names: List[str]) -> str:
    sqlite_files = [f for f in files if f.endswith(".sqlite") or f.endswith(".db")]
    if sqlite_files:
        return f"SQLite Database ({len(table_names)} tables in {sqlite_files[0]})"
    
    has_header = any("hoadon" in t.lower() or "don_hang" in t.lower() or "donhang" in t.lower() for t in table_names)
    has_detail = any("chitiet" in t.lower() or "chi_tiet" in t.lower() for t in table_names)
    if has_header and has_detail:
        return "Header-Detail Relational (Orders + OrderDetails)"
    
    monthly_files = [f for f in files if re.search(r"[tT]\d{1,2}|202[456]", f)]
    if len(monthly_files) >= 2:
        return f"Multi-file Partitioned / Monthly Log ({len(monthly_files)} time-sliced files)"
    
    if len(table_names) == 1 or (len(table_names) > 1 and any("ban_hang" in t.lower() or "sales" in t.lower() for t in table_names)):
        return "Single Flat Sales Log / Multi-sheet Register"
    
    if len(table_names) > 1:
        return f"Multi-table Relational ({len(table_names)} tables)"
    
    return "Generic Tabular"


def count_lines_file(fpath: str) -> int:
    try:
        with open(fpath, "rb") as f:
            lines = 0
            buf_size = 1024 * 1024
            read_bytes = f.raw.read if hasattr(f, "raw") else f.read
            buf = read_bytes(buf_size)
            while buf:
                lines += buf.count(b"\n")
                buf = read_bytes(buf_size)
            return max(0, lines)
    except Exception:
        return 0


def profile_business(biz_dir: str, biz_id: str) -> Dict[str, Any]:
    readme_text = ""
    readme_path = os.path.join(biz_dir, "README.md")
    if os.path.exists(readme_path):
        for enc in ["utf-8", "utf-8-sig", "latin1", "cp1258"]:
            try:
                with open(readme_path, "r", encoding=enc) as f:
                    readme_text = f.read().strip()
                break
            except Exception:
                continue

    files = sorted(os.listdir(biz_dir))
    table_meta: Dict[str, Dict[str, Any]] = {}
    table_samples: Dict[str, List[Dict[str, Any]]] = {}

    for fname in files:
        if fname == "README.md" or fname == "calendar.csv":
            continue
        fixed_fname = fix_mojibake_filename(fname)
        fpath = os.path.join(biz_dir, fname)

        # 1. SQLite
        if fname.lower().endswith((".sqlite", ".db", ".sqlite3")):
            try:
                con = sqlite3.connect(fpath)
                cursor = con.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tbls = cursor.fetchall()
                for (t_name,) in tbls:
                    full_key = f"{fixed_fname} :: {t_name}"
                    cursor.execute(f"SELECT * FROM \"{t_name}\" LIMIT 3")
                    sample_rows = cursor.fetchall()
                    cursor.execute(f"PRAGMA table_info(\"{t_name}\")")
                    cols = [row[1] for row in cursor.fetchall()]
                    cursor.execute(f"SELECT COUNT(*) FROM \"{t_name}\"")
                    row_cnt = cursor.fetchone()[0]

                    table_meta[full_key] = {
                        "row_count": row_cnt,
                        "header_row_idx": 0,
                        "columns": cols,
                        "has_subtotals": False,
                    }
                    table_samples[full_key] = [dict(zip(cols, r)) for r in sample_rows]
                con.close()
            except Exception as e:
                table_meta[f"{fixed_fname} (Error)"] = {"error": str(e)}

        # 2. CSV
        elif fname.lower().endswith(".csv"):
            total_lines = count_lines_file(fpath)
            raw_rows = []
            for enc in ["utf-8", "utf-8-sig", "cp1258", "latin1"]:
                try:
                    df_head = pd.read_csv(fpath, header=None, nrows=15, encoding=enc)
                    raw_rows = df_head.values.tolist()
                    break
                except Exception:
                    continue
            if raw_rows:
                header_idx, cols = find_true_header(raw_rows)
                has_sub = detect_subtotal_in_rows(raw_rows, header_idx)
                full_key = fixed_fname
                row_cnt = max(0, total_lines - (header_idx + 1))
                table_meta[full_key] = {
                    "row_count": row_cnt,
                    "header_row_idx": header_idx,
                    "columns": cols,
                    "has_subtotals": has_sub,
                }
                samples = []
                for r in raw_rows[header_idx + 1: header_idx + 4]:
                    row_dict = {}
                    for i, c in enumerate(cols):
                        row_dict[c] = r[i] if i < len(r) else None
                    samples.append(row_dict)
                table_samples[full_key] = samples

        # 3. Excel (.xlsx, .xls) using openpyxl read_only mode
        elif fname.lower().endswith((".xlsx", ".xls")):
            try:
                wb = openpyxl.load_workbook(fpath, read_only=True, data_only=True)
                for sname in wb.sheetnames:
                    fixed_sname = fix_mojibake_filename(sname)
                    ws = wb[sname]
                    # Read first 15 rows
                    row_iter = ws.iter_rows(values_only=True)
                    first_rows = list(itertools.islice(row_iter, 15))
                    if not first_rows:
                        continue
                    
                    header_idx, cols = find_true_header(first_rows)
                    has_sub = detect_subtotal_in_rows(first_rows, header_idx)
                    row_cnt = max(0, (ws.max_row or len(first_rows)) - (header_idx + 1))
                    full_key = f"{fixed_fname} :: {fixed_sname}"

                    table_meta[full_key] = {
                        "row_count": row_cnt,
                        "header_row_idx": header_idx,
                        "columns": cols,
                        "has_subtotals": has_sub,
                    }
                    samples = []
                    for r in first_rows[header_idx + 1: header_idx + 4]:
                        row_dict = {}
                        for i, c in enumerate(cols):
                            row_dict[c] = r[i] if i < len(r) else None
                        samples.append(row_dict)
                    table_samples[full_key] = samples
                wb.close()
            except Exception as e:
                table_meta[f"{fixed_fname} (Error)"] = {"error": str(e)}

    structure = classify_business_structure(files, list(table_meta.keys()))
    return {
        "business_id": biz_id,
        "readme": readme_text,
        "files": files,
        "structure": structure,
        "table_meta": table_meta,
        "table_samples": table_samples,
    }


def generate_profile_report(dataset_name: str, biz_dirs: List[Tuple[str, str]], output_path: str):
    lines = []
    lines.append(f"# Data Profile Report: `{dataset_name}`")
    lines.append(f"Total Businesses: {len(biz_dirs)}\n")

    for i, (biz_id, b_path) in enumerate(sorted(biz_dirs), 1):
        print(f"[{i:2d}/{len(biz_dirs)}] Profiling {biz_id}...", flush=True)
        prof = profile_business(b_path, biz_id)
        lines.append(f"## Business `{biz_id}`")
        lines.append(f"- **Structure Archetype:** {prof['structure']}")
        readme_snippet = prof['readme'][:500].replace("\n", " ").strip()
        lines.append(f"- **README (truncated 500 chars):** {readme_snippet or '*(empty)*'}")
        lines.append(f"- **Files on disk ({len(prof['files'])}):** {', '.join(fix_mojibake_filename(f) for f in prof['files'])}")
        lines.append("")
        lines.append("### Tables / Sheets Detail:")
        
        for tbl_name, meta in prof["table_meta"].items():
            if "error" in meta:
                lines.append(f"- **`{tbl_name}`**: Error loading: {meta['error']}")
                continue
            cols = meta["columns"]
            row_cnt = meta["row_count"]
            header_idx = meta["header_row_idx"]
            has_sub = meta["has_subtotals"]
            type_heur = identify_column_types(cols)

            lines.append(f"#### Table `{tbl_name}`")
            lines.append(f"- **Rows:** {row_cnt:,} | **Header Row Index:** {header_idx} | **Subtotal Keywords Detected:** {'Yes' if has_sub else 'No'}")
            lines.append(f"- **Columns ({len(cols)}):** {', '.join(str(c) for c in cols[:15])}{'...' if len(cols) > 15 else ''}")
            lines.append(f"  - *Date cols:* {type_heur['date'] or 'None'}")
            lines.append(f"  - *Amount/Qty cols:* {type_heur['amount'] or 'None'}")
            lines.append(f"  - *Status cols:* {type_heur['status'] or 'None'}")
            lines.append(f"  - *ID/Code cols:* {type_heur['id'] or 'None'}")
            
            samples = prof["table_samples"].get(tbl_name, [])
            if samples:
                lines.append("- **Sample 3 rows:**")
                lines.append("```json")
                import json
                for s in samples:
                    clean_s = {k: (str(v)[:40] if v is not None else None) for k, v in list(s.items())[:8]}
                    lines.append(json.dumps(clean_s, ensure_ascii=False))
                lines.append("```")
            lines.append("")
        lines.append("---\n")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✓ Profile report successfully written to: {output_path}", flush=True)


def resolve_split_dirs(split_name: str) -> List[Tuple[str, str]]:
    possible_roots = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../{split_name}/{split_name}/data")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../{split_name}/data")),
        f"/content/dataset_gdrive/{split_name}/{split_name}/data",
        f"/content/dataset_gdrive/{split_name}/data",
        f"/data/{split_name}/data",
        f"/data/data",
        f"/data",
    ]
    target_data_dir = None
    for r in possible_roots:
        if os.path.exists(r) and os.path.isdir(r):
            entries = [os.path.join(r, e) for e in os.listdir(r) if os.path.isdir(os.path.join(r, e))]
            if entries:
                target_data_dir = r
                break

    if not target_data_dir:
        raise FileNotFoundError(f"Could not locate data directory for split '{split_name}'. Tried: {possible_roots}")

    biz_dirs = []
    for entry in sorted(os.listdir(target_data_dir)):
        full = os.path.join(target_data_dir, entry)
        if os.path.isdir(full):
            biz_dirs.append((entry, full))
    return biz_dirs


def main():
    parser = argparse.ArgumentParser(description="Inspect and profile business datasets.")
    parser.add_argument("--dataset", default="train", choices=["train", "public_test"], help="Dataset split to inspect")
    parser.add_argument("--output", default=None, help="Output markdown report path")
    args = parser.parse_args()

    biz_dirs = resolve_split_dirs(args.dataset)
    report_file = args.output or os.path.abspath(os.path.join(os.path.dirname(__file__), f"../reports/data_profile_{args.dataset}.md"))
    print(f"Inspecting {len(biz_dirs)} businesses in {args.dataset}...", flush=True)
    generate_profile_report(args.dataset, biz_dirs, report_file)


if __name__ == "__main__":
    main()
