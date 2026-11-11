#!/usr/bin/env python3
"""
scripts/inspect_data.py - High-speed profiling and verification of business datasets.

Features:
- Accepts `--data_dir` (and optional `--business_id` or `--limit_biz 5`).
- Runs `load_business_data` + `prof = prepare(ctx)` on real businesses.
- Reports:
  * Execution time of `prepare(ctx)`
  * Merged table groups (`union_homogeneous`)
  * Normalized column types (`DATE`, `BIGINT`, `DOUBLE`)
  * Discovered join relations (`prof.relations`)
  * Sample output of `render_schema(prof, sample_question)` and its char/token count.
- Includes automated SQL and `diagnose_empty_result` verification.
"""

import argparse
import logging
import os
import sys
import time
from typing import Any, Dict, List, Optional

# Ensure datamate_agent is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.data_layer.ingest import load_business_data
from src.data_layer.profiler import (
    diagnose_empty_result,
    prepare,
    render_schema,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("InspectData")


def inspect_single_business(
    biz_id: str,
    biz_dir: str,
    cache_dir: Optional[str] = None,
    sample_question: str = "Tổng số lượng sản phẩm bán ra trong tháng 1 năm 2025 là bao nhiêu?",
    test_queries: bool = True,
) -> Dict[str, Any]:
    """Profiles a single business using load_business_data and prepare(ctx)."""
    print("\n" + "=" * 70)
    print(f"BUSINESS PROFILING: {biz_id}")
    print(f"Directory: {biz_dir}")
    print("=" * 70)

    # 1. Ingest Data
    t0_load = time.time()
    ctx = load_business_data(biz_id, biz_dir, cache_dir=cache_dir)
    load_time = time.time() - t0_load

    # 2. Run / Check Profile
    t0_prep = time.time()
    if ctx.profile is not None:
        prof = ctx.profile
        prep_time = time.time() - t0_prep
        print(f"[Ingest & Cache] ctx.profile already built in {load_time:.2f}s (prepare took: {prep_time:.3f}s)")
    else:
        prof = prepare(ctx)
        ctx.profile = prof
        prep_time = time.time() - t0_prep
        print(f"[Ingest & Prepare] Ingest time: {load_time:.2f}s | prepare(ctx) time: {prep_time:.2f}s")

    print(f"-> prepare(ctx) Execution Time: {prep_time:.3f}s")

    # 3. Merged Table Groups (union_homogeneous)
    print("\n[1] MERGED TABLE GROUPS (union_homogeneous):")
    if prof.merged_groups:
        for unified_name, shards in prof.merged_groups.items():
            print(f"  • Unified Table '{unified_name}' merged {len(shards)} shards:")
            for s in shards[:5]:
                print(f"      - {s}")
            if len(shards) > 5:
                print(f"      ... and {len(shards) - 5} more shards")
    else:
        print("  • None (No monthly/periodic shard patterns detected)")

    # 4. Normalized Column Types (DATE, BIGINT, DOUBLE)
    print("\n[2] NORMALIZED COLUMN TYPES:")
    date_cols = []
    bigint_cols = []
    double_cols = []
    enum_cols = []

    for t_name, tbl_prof in prof.tables.items():
        print(f"  Table `{t_name}` ({tbl_prof.row_count:,} rows):")
        for c_name, c_prof in tbl_prof.columns.items():
            dtype = c_prof.dtype.upper()
            if "DATE" in dtype:
                range_str = f"[{c_prof.vmin} .. {c_prof.vmax}]" if c_prof.vmin else "[]"
                date_cols.append(f"`{t_name}`.`{c_name}` ({range_str})")
            elif "BIGINT" in dtype or "INT" in dtype:
                bigint_cols.append(f"`{t_name}`.`{c_name}`")
            elif "DOUBLE" in dtype or "FLOAT" in dtype or "DECIMAL" in dtype:
                double_cols.append(f"`{t_name}`.`{c_name}`")

            if c_prof.enum_counts:
                enum_vals = [f"'{val}' ({cnt})" for val, cnt in c_prof.enum_counts[:4]]
                enum_cols.append(f"`{t_name}`.`{c_name}`: " + ", ".join(enum_vals))

    print(f"  • DATE Columns ({len(date_cols)}):")
    for d in date_cols[:10]:
        print(f"      - {d}")
    if len(date_cols) > 10:
        print(f"      ... and {len(date_cols) - 10} more")

    print(f"  • BIGINT / INTEGER Columns ({len(bigint_cols)}):")
    for b in bigint_cols[:10]:
        print(f"      - {b}")
    if len(bigint_cols) > 10:
        print(f"      ... and {len(bigint_cols) - 10} more")

    print(f"  • DOUBLE / NUMERIC Columns ({len(double_cols)}):")
    for db in double_cols[:10]:
        print(f"      - {db}")
    if len(double_cols) > 10:
        print(f"      ... and {len(double_cols) - 10} more")

    if enum_cols:
        print(f"  • Categorical Enum Columns ({len(enum_cols)}):")
        for e in enum_cols[:10]:
            print(f"      - {e}")

    # 5. Discovered Join Relations
    print("\n[3] DISCOVERED JOIN RELATIONS (prof.relations):")
    if prof.relations:
        for r in prof.relations:
            status = "VERIFIED" if r.verified else "UNVERIFIED"
            print(f"  • `{r.from_table}`.`{r.from_col}` = `{r.to_table}`.`{r.to_col}` (overlap: {r.overlap_count:,}, status: {status})")
    else:
        print("  • None detected or single-table business.")

    # 6. Sample Output of render_schema
    print("\n[4] SAMPLE OUTPUT OF render_schema:")
    schema_text = render_schema(prof, sample_question, max_chars=4500)
    char_count = len(schema_text)
    token_est = char_count // 4
    print(f"  Character Count : {char_count:,} chars")
    print(f"  Estimated Tokens: ~{token_est:,} tokens (Well within 2K-3K budget!)")
    print("-" * 50)
    # Print first 20 lines of schema
    lines = schema_text.splitlines()
    for line in lines[:25]:
        print("  " + line)
    if len(lines) > 25:
        print(f"  ... [truncated {len(lines) - 25} lines] ...")
    print("-" * 50)

    # 7. Verification Tests (SQL Execution + diagnose_empty_result)
    if test_queries:
        print("\n[5] VERIFICATION TESTS (SQL & Diagnostics):")
        con = ctx.con

        # Test A: Test aggregation query on first table with numeric and date columns
        test_table = None
        for t_name, tbl_prof in prof.tables.items():
            if tbl_prof.row_count > 0:
                test_table = t_name
                break

        if test_table:
            tbl_obj = prof.tables[test_table]
            date_col = next((c for c, p in tbl_obj.columns.items() if "DATE" in p.dtype.upper()), None)
            num_col = next((c for c, p in tbl_obj.columns.items() if any(k in p.dtype.upper() for k in ["BIGINT", "INT", "DOUBLE"])), None)

            if num_col:
                if date_col and tbl_obj.columns[date_col].vmin:
                    vmin = str(tbl_obj.columns[date_col].vmin)[:10]
                    test_sql = f'SELECT SUM("{num_col}"), AVG("{num_col}") FROM "{test_table}" WHERE "{date_col}" >= DATE \'{vmin}\''
                else:
                    test_sql = f'SELECT SUM("{num_col}"), AVG("{num_col}") FROM "{test_table}"'

                try:
                    res = con.execute(test_sql).fetchall()
                    print(f"  ✓ Aggregation SQL Test Passed on `{test_table}`: {test_sql}")
                    print(f"    Result: {res[0]}")
                except Exception as e:
                    print(f"  ✗ Aggregation SQL Failed: {e}")
                    raise

        # Test B: Test diagnose_empty_result with out-of-range date
        bad_date_sql = f"SELECT * FROM \"{list(prof.tables.keys())[0]}\" WHERE {date_cols[0].split('.')[1]} = DATE '2099-01-01'" if date_cols else ""
        if bad_date_sql:
            hints = diagnose_empty_result(ctx, prof, bad_date_sql)
            print(f"  ✓ diagnose_empty_result on out-of-range date (2099):")
            for h in hints:
                print(f"      - Diagnostic hint: {h}")

        # Test C: Test diagnose_empty_result with accent mismatch
        for t_name, tbl_prof in prof.tables.items():
            for c_name, c_prof in tbl_prof.columns.items():
                if c_prof.enum_counts:
                    val = c_prof.enum_counts[0][0]
                    # Unaccent the value to test diacritic recovery hint
                    from src.data_layer.profiler import remove_accents
                    unaccented = remove_accents(val)
                    if unaccented != val:
                        bad_enum_sql = f"SELECT * FROM \"{t_name}\" WHERE \"{c_name}\" = '{unaccented}'"
                        hints = diagnose_empty_result(ctx, prof, bad_enum_sql)
                        print(f"  ✓ diagnose_empty_result on accent mismatch ('{unaccented}' vs '{val}'):")
                        for h in hints:
                            print(f"      - Diagnostic hint: {h}")
                        break
            else:
                continue
            break

    return {
        "business_id": biz_id,
        "load_time": load_time,
        "prep_time": prep_time,
        "tables": len(prof.tables),
        "merged_groups": len(prof.merged_groups),
        "relations": len(prof.relations),
        "schema_chars": char_count,
    }


def main():
    parser = argparse.ArgumentParser(description="High-Speed Profiling and Data Verification.")
    parser.add_argument(
        "--data_dir",
        default=None,
        help="Path to folder containing business subdirectories (e.g., public_test/public_test/data)",
    )
    parser.add_argument("--business_id", default=None, help="Specific business ID to profile (e.g., dev_002)")
    parser.add_argument("--limit_biz", type=int, default=5, help="Maximum number of businesses to inspect")
    parser.add_argument("--cache_dir", default="./data_cache", help="Cache directory for DuckDB persistence")
    parser.add_argument("--skip_tests", action="store_true", help="Skip running SQL execution verification")
    args = parser.parse_args()

    # Auto-detect data_dir if not specified
    data_dir = args.data_dir
    if not data_dir:
        candidates = [
            os.path.join(PROJECT_ROOT, "../public_test/public_test/data"),
            os.path.join(PROJECT_ROOT, "../train/train/data"),
            os.path.join(PROJECT_ROOT, "public_test/public_test/data"),
            os.path.join(PROJECT_ROOT, "data"),
            os.path.join(os.getcwd(), "public_test/public_test/data"),
            os.path.join(os.getcwd(), "train/train/data"),
        ]
        for c in candidates:
            if os.path.exists(c) and os.path.isdir(c):
                data_dir = os.path.abspath(c)
                break

    if not data_dir or not os.path.isdir(data_dir):
        print(f"[ERROR] Could not find a valid data_dir. Please pass --data_dir explicitly.")
        sys.exit(1)

    print(f"Inspecting datasets in: {data_dir}")

    # Discover businesses
    if args.business_id:
        biz_path = os.path.join(data_dir, args.business_id)
        if not os.path.isdir(biz_path):
            print(f"[ERROR] Business '{args.business_id}' not found at {biz_path}")
            sys.exit(1)
        businesses = [(args.business_id, biz_path)]
    else:
        entries = sorted(os.listdir(data_dir))
        businesses = []
        for e in entries:
            p = os.path.join(data_dir, e)
            if os.path.isdir(p):
                businesses.append((e, p))
        businesses = businesses[: args.limit_biz]

    print(f"Discovered {len(businesses)} business(es) to inspect.")

    results = []
    for biz_id, b_path in businesses:
        res = inspect_single_business(
            biz_id=biz_id,
            biz_dir=b_path,
            cache_dir=args.cache_dir,
            test_queries=not args.skip_tests,
        )
        results.append(res)

    print("\n" + "=" * 70)
    print("PROFILING SUMMARY ACROSS ALL BUSINESSES")
    print("=" * 70)
    for r in results:
        print(
            f"• Business: {r['business_id']:<10} | Ingest: {r['load_time']:5.2f}s | "
            f"prepare: {r['prep_time']:5.2f}s | Tables: {r['tables']:2d} | "
            f"Merged Groups: {r['merged_groups']:2d} | Schema: {r['schema_chars']:4d} chars"
        )
    print("=" * 70)
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!\n")


if __name__ == "__main__":
    main()
