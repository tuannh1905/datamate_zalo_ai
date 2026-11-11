"""
Content-Driven Database Profiler for DataMate Challenge.
Replaces canonical view drafting and debt macros with robust, content-based schema profiling:
1. install_macros: Installs accent-insensitive vn() macro and type helpers in DuckDB.
2. union_homogeneous: Automatically merges monthly/periodic table shards into single unified tables.
3. normalize_types: Safe in-database casting of DATE, BIGINT, and DOUBLE columns.
4. build_profile: Extracts row counts, type distributions, min/max ranges, enums with frequencies, and verified joins.
5. render_schema: Produces compact, question-relevant schema representation within token budgets.
6. diagnose_empty_result: Diagnoses empty or NULL execution results to guide self-repair turns.
7. prepare: End-to-end preparation pipeline for business context.
"""

import logging
import re
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

import duckdb

logger = logging.getLogger(__name__)


def _q(identifier: str) -> str:
    """Safely quotes an SQL identifier with double quotes."""
    escaped = str(identifier).replace('"', '""')
    return f'"{escaped}"'


def remove_accents(s: str) -> str:
    """Removes Vietnamese diacritics and converts đ/Đ to d/D."""
    if not s or not isinstance(s, str):
        return ""
    s = s.replace("đ", "d").replace("Đ", "D")
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).strip()


def install_macros(con: duckdb.DuckDBPyConnection) -> None:
    """
    Registers accent-insensitive and cleaning SQL macros in DuckDB.
    - vn(s): Accent-insensitive, lowercase conversion for Vietnamese strings.
    - clean_num(s): Parses formatted Vietnamese numeric strings into DOUBLE.
    - to_date(s): Multi-format safe date parser into DATE.
    Uses TEMPORARY MACRO so it succeeds even on read_only=True cached connections.
    """
    for macro_prefix in ["CREATE OR REPLACE TEMPORARY MACRO", "CREATE OR REPLACE MACRO"]:
        try:
            con.execute(
                f"""
                {macro_prefix} vn(s) AS 
                LOWER(REPLACE(REPLACE(strip_accents(CAST(s AS VARCHAR)), 'đ', 'd'), 'Đ', 'd'));
                """
            )
            con.execute(
                f"""
                {macro_prefix} clean_num(s) AS 
                CASE 
                    WHEN LOWER(TRIM(CAST(s AS VARCHAR))) LIKE '%k' THEN 
                        TRY_CAST(REPLACE(REPLACE(REPLACE(SUBSTRING(TRIM(CAST(s AS VARCHAR)), 1, LENGTH(TRIM(CAST(s AS VARCHAR))) - 1), '.', ''), ',', '.'), ' ', '') AS DOUBLE) * 1000.0
                    ELSE 
                        TRY_CAST(REPLACE(REPLACE(REPLACE(REGEXP_EXTRACT(CAST(s AS VARCHAR), '^[-+]?[0-9]+(?:[.,][0-9]+)*'), '.', ''), ',', '.'), ' ', '') AS DOUBLE)
                END;
                """
            )
            con.execute(
                f"""
                {macro_prefix} to_date(s) AS 
                COALESCE(
                    TRY_CAST(s AS DATE),
                    TRY_STRPTIME(CAST(s AS VARCHAR), '%d/%m/%Y'),
                    TRY_STRPTIME(CAST(s AS VARCHAR), '%d-%m-%Y'),
                    TRY_STRPTIME(CAST(s AS VARCHAR), '%Y/%m/%d')
                );
                """
            )
            break
        except Exception as e:
            logger.debug(f"install_macros try failed with {macro_prefix}: {e}")


@dataclass
class ColumnProfile:
    name: str
    dtype: str
    non_null_count: int = 0
    null_count: int = 0
    distinct_count: int = 0
    vmin: Optional[Any] = None
    vmax: Optional[Any] = None
    sample_values: List[str] = field(default_factory=list)
    enum_counts: List[Tuple[str, int]] = field(default_factory=list)
    original_name: Optional[str] = None


@dataclass
class TableProfile:
    name: str
    row_count: int
    columns: Dict[str, ColumnProfile] = field(default_factory=dict)
    is_shard_union: bool = False
    source_tables: List[str] = field(default_factory=list)


@dataclass
class Relation:
    from_table: str
    from_col: str
    to_table: str
    to_col: str
    overlap_count: int = 0
    verified: bool = True


@dataclass
class ProfileResult:
    business_id: str
    tables: Dict[str, TableProfile] = field(default_factory=dict)
    relations: List[Relation] = field(default_factory=list)
    merged_groups: Dict[str, List[str]] = field(default_factory=dict)


def normalize_types(con: duckdb.DuckDBPyConnection, table: str) -> None:
    """
    Safely casts columns in-place in DuckDB:
    - TIMESTAMP / TIMESTAMP_NS -> DATE if time is 00:00:00 or column is a date column.
    - VARCHAR columns matching DATE patterns -> DATE.
    - VARCHAR columns matching numeric / amount keywords -> BIGINT or DOUBLE.
    Always uses quoted identifiers _q(table) and _q(col).
    """
    try:
        col_infos = con.execute(f"PRAGMA table_info({_q(table)})").fetchall()
    except Exception as e:
        logger.debug(f"Could not inspect table {table} for normalization: {e}")
        return

    if not col_infos:
        return

    DATE_KEYWORDS = {
        "ngay", "date", "thoi_gian", "ngay_tao", "ngay_dat", "ngay_lap",
        "ngay_ban", "ngay_ct", "ngay_hd", "ngay_nhap", "ngay_tra"
    }
    AMOUNT_KEYWORDS = {
        "gia", "tien", "so_luong", "thanh_tien", "don_gia", "chiet_khau",
        "giam_gia", "tong_tien", "no", "ton_kho", "phi", "von", "loi_nhuan",
        "doanh_thu", "sl", "ck", "km"
    }
    IDENTIFIER_KEYWORDS = {
        "id", "ma", "code", "barcode", "sdt", "phone", "dien_thoai",
        "ghi_chu", "note", "mo_ta", "ten", "name", "dia_chi", "email",
        "so_xe", "bien_so", "don_vi", "dvt"
    }

    try:
        row_count = con.execute(f"SELECT COUNT(*) FROM {_q(table)}").fetchone()[0]
    except Exception:
        row_count = 0

    if row_count == 0:
        return

    select_exprs = []
    has_changes = False

    for col_info in col_infos:
        c_name = col_info[1]
        c_type = str(col_info[2]).upper()
        col_norm = c_name.lower()
        col_tokens = set(col_norm.split("_"))

        # 1. Timestamp handling: treat/convert consistently as DATE
        if c_type.startswith("TIMESTAMP"):
            # Check if non-zero time components exist
            try:
                non_zero_time = con.execute(
                    f"SELECT COUNT(*) FROM {_q(table)} WHERE {_q(c_name)} IS NOT NULL AND CAST({_q(c_name)} AS TIME) != TIME '00:00:00'"
                ).fetchone()[0]
            except Exception:
                non_zero_time = 0

            is_date_col = bool(col_tokens & DATE_KEYWORDS) or any(k in col_norm for k in DATE_KEYWORDS)
            if non_zero_time == 0 or is_date_col:
                select_exprs.append(f"TRY_CAST({_q(c_name)} AS DATE) AS {_q(c_name)}")
                has_changes = True
                continue

        # 2. VARCHAR / TEXT column normalization
        if c_type in ("VARCHAR", "TEXT", "STRING"):
            # 2a. Check if it is a DATE column
            is_date_named = bool(col_tokens & DATE_KEYWORDS) or any(k in col_norm for k in DATE_KEYWORDS)
            try:
                date_check = con.execute(
                    f"""
                    SELECT 
                        COUNT({_q(c_name)}) AS total_non_null,
                        COUNT(to_date({_q(c_name)})) AS parsed_dates
                    FROM {_q(table)}
                    WHERE {_q(c_name)} IS NOT NULL AND TRIM(CAST({_q(c_name)} AS VARCHAR)) != ''
                    """
                ).fetchone()
                total_nn = date_check[0] if date_check else 0
                parsed_dt = date_check[1] if date_check else 0
            except Exception:
                total_nn, parsed_dt = 0, 0

            if total_nn > 0 and (parsed_dt / total_nn >= 0.80 or (is_date_named and parsed_dt / total_nn >= 0.50)):
                select_exprs.append(f"to_date({_q(c_name)}) AS {_q(c_name)}")
                has_changes = True
                continue

            # 2b. Check if it is a NUMERIC / AMOUNT column (and not an identifier)
            is_ident = bool(col_tokens & IDENTIFIER_KEYWORDS) or any(c_name.lower().startswith(p) for p in ["ma_", "id_"])
            is_amount_named = (
                any(w in col_norm for w in ["so_luong", "thanh_tien", "don_gia", "tong_tien", "chiet_khau", "giam_gia"])
                or bool(col_tokens & AMOUNT_KEYWORDS)
            )

            if not is_ident:
                try:
                    num_check = con.execute(
                        f"""
                        SELECT 
                            COUNT({_q(c_name)}) AS total_non_null,
                            COUNT(TRY_CAST({_q(c_name)} AS BIGINT)) AS valid_ints,
                            COUNT(TRY_CAST({_q(c_name)} AS DOUBLE)) AS valid_doubles,
                            COUNT(clean_num({_q(c_name)})) AS valid_cleaned
                        FROM {_q(table)}
                        WHERE {_q(c_name)} IS NOT NULL AND TRIM(CAST({_q(c_name)} AS VARCHAR)) != ''
                        """
                    ).fetchone()
                    tot = num_check[0] if num_check else 0
                    v_int = num_check[1] if num_check else 0
                    v_dbl = num_check[2] if num_check else 0
                    v_cln = num_check[3] if num_check else 0
                except Exception:
                    tot, v_int, v_dbl, v_cln = 0, 0, 0, 0

                if tot > 0:
                    if v_int / tot >= 0.85:
                        select_exprs.append(f"TRY_CAST({_q(c_name)} AS BIGINT) AS {_q(c_name)}")
                        has_changes = True
                        continue
                    elif v_dbl / tot >= 0.85:
                        select_exprs.append(f"TRY_CAST({_q(c_name)} AS DOUBLE) AS {_q(c_name)}")
                        has_changes = True
                        continue
                    elif (v_cln / tot >= 0.85) or (is_amount_named and v_cln / tot >= 0.60):
                        # Test if all cleaned values are integers
                        try:
                            int_cln_check = con.execute(
                                f"""
                                SELECT COUNT(*) FROM {_q(table)}
                                WHERE clean_num({_q(c_name)}) IS NOT NULL
                                  AND clean_num({_q(c_name)}) % 1 != 0
                                """
                            ).fetchone()[0]
                        except Exception:
                            int_cln_check = 1

                        if int_cln_check == 0:
                            select_exprs.append(f"TRY_CAST(clean_num({_q(c_name)}) AS BIGINT) AS {_q(c_name)}")
                        else:
                            select_exprs.append(f"clean_num({_q(c_name)}) AS {_q(c_name)}")
                        has_changes = True
                        continue

        # Keep original column
        select_exprs.append(_q(c_name))

    if has_changes:
        try:
            query = f"CREATE OR REPLACE TABLE {_q(table)} AS SELECT {', '.join(select_exprs)} FROM {_q(table)}"
            con.execute(query)
            logger.debug(f"Normalized types in table '{table}'.")
        except Exception as e:
            logger.warning(f"Failed to normalize types in table '{table}': {e}")


def union_homogeneous(ctx: Any) -> Dict[str, List[str]]:
    """
    Detects and merges monthly/periodic shard tables into single unified tables:
    - Tables sharing prefix patterns (e.g., BanHang_T1_2025 ... T5_2026, So_chi_tiet_ban_hang_1/2).
    - Uses UNION ALL BY NAME.
    - If raw types mismatch across shards, casts all columns to VARCHAR during the union,
      then normalizes types ONCE on the unified table.
    - Quoting is strictly applied to table and column names (_q(table)).
    Returns a dictionary mapping unified table names to the list of merged source tables.
    """
    con = ctx.con
    table_names = list(ctx.table_names)
    merged_groups: Dict[str, List[str]] = {}

    # Find candidate shard groups based on naming conventions
    SHARD_REGEX = re.compile(
        r"^(raw_)?(.*?)(?:_t\d{1,2}_\d{4}|_thang\d{1,2}_\d{4}|_\d{4}_\d{2}|_\d{2}_\d{4}|_\d+)$",
        re.IGNORECASE,
    )

    grouped_tables: Dict[str, List[str]] = {}
    for t in table_names:
        m = SHARD_REGEX.match(t)
        if m:
            prefix = m.group(1) or ""
            base = m.group(2).rstrip("_")
            group_key = f"{prefix}{base}"
            grouped_tables.setdefault(group_key, []).append(t)

    tables_to_remove: Set[str] = set()
    new_tables: List[str] = []

    for group_key, shards in grouped_tables.items():
        if len(shards) < 2:
            continue

        # Check column overlap to ensure homogeneity
        col_sets = []
        for s in shards:
            try:
                cols = [r[0].lower() for r in con.execute(f"DESCRIBE {_q(s)}").fetchall()]
                col_sets.append(set(cols))
            except Exception:
                pass

        if len(col_sets) != len(shards):
            continue

        base_set = col_sets[0]
        overlap_ratios = [len(base_set & cs) / max(len(base_set | cs), 1) for cs in col_sets]
        if not all(r >= 0.40 for r in overlap_ratios):
            continue

        unified_table = group_key
        logger.info(f"Unifying {len(shards)} homogeneous shards into '{unified_table}': {shards[:3]}...")

        # 1. Try standard UNION ALL BY NAME
        union_success = False
        try:
            subqueries = [f"SELECT * FROM {_q(s)}" for s in shards]
            union_sql = " UNION ALL BY NAME ".join(subqueries)
            con.execute(f"CREATE OR REPLACE TABLE {_q(unified_table)} AS {union_sql}")
            union_success = True
        except Exception as union_err:
            logger.warning(
                f"Direct UNION ALL BY NAME failed for '{unified_table}' ({union_err}). "
                f"Falling back to VARCHAR-cast union..."
            )

        # 2. Fallback: cast all columns to VARCHAR during union, then normalize ONCE
        if not union_success:
            try:
                varchar_subqueries = []
                for s in shards:
                    cols = [r[0] for r in con.execute(f"DESCRIBE {_q(s)}").fetchall()]
                    casts = ", ".join([f"CAST({_q(c)} AS VARCHAR) AS {_q(c)}" for c in cols])
                    varchar_subqueries.append(f"SELECT {casts} FROM {_q(s)}")
                varchar_union_sql = " UNION ALL BY NAME ".join(varchar_subqueries)
                con.execute(f"CREATE OR REPLACE TABLE {_q(unified_table)} AS {varchar_union_sql}")
                union_success = True
            except Exception as fb_err:
                logger.error(f"Failed to union shards into '{unified_table}': {fb_err}")
                continue

        # Normalize types ONCE on the unified table
        normalize_types(con, unified_table)

        # Also create clean alias view without raw_ prefix if needed
        clean_alias = unified_table[4:] if unified_table.startswith("raw_") else unified_table
        if clean_alias != unified_table:
            try:
                con.execute(f"CREATE OR REPLACE VIEW {_q(clean_alias)} AS SELECT * FROM {_q(unified_table)}")
            except Exception:
                pass

        merged_groups[unified_table] = shards
        tables_to_remove.update(shards)
        new_tables.append(unified_table)

    # Update ctx.table_names
    updated_tables = [t for t in ctx.table_names if t not in tables_to_remove]
    for nt in new_tables:
        if nt not in updated_tables:
            updated_tables.append(nt)
    ctx.table_names = updated_tables

    return merged_groups


def build_profile(ctx: Any) -> ProfileResult:
    """
    Builds rich content-driven profile for active tables in ctx:
    - Row counts, column types, min/max ranges (YYYY-MM-DD for dates).
    - Categorical enum values with frequencies (for distinct <= 15).
    - Discovered and verified join relations between tables.
    """
    con = ctx.con
    prof = ProfileResult(business_id=ctx.business_id)

    # 1. Profile Tables and Columns
    for tbl in ctx.table_names:
        # Skip temporary registered DataFrames
        if tbl.endswith("_df"):
            continue

        try:
            row_count = con.execute(f"SELECT COUNT(*) FROM {_q(tbl)}").fetchone()[0]
        except Exception:
            row_count = 0

        tbl_prof = TableProfile(name=tbl, row_count=row_count)
        col_mappings = ctx.column_mappings.get(tbl, {})

        try:
            col_infos = con.execute(f"PRAGMA table_info({_q(tbl)})").fetchall()
        except Exception:
            col_infos = []

        for c_info in col_infos:
            c_name = c_info[1]
            c_type = str(c_info[2]).upper()

            col_prof = ColumnProfile(
                name=c_name,
                dtype=c_type,
                original_name=col_mappings.get(c_name, c_name),
            )

            if row_count > 0:
                try:
                    stats = con.execute(
                        f"""
                        SELECT 
                            COUNT({_q(c_name)}) AS non_null,
                            COUNT(*) - COUNT({_q(c_name)}) AS null_cnt,
                            COUNT(DISTINCT {_q(c_name)}) AS distinct_cnt,
                            MIN({_q(c_name)}) AS vmin,
                            MAX({_q(c_name)}) AS vmax
                        FROM {_q(tbl)}
                        """
                    ).fetchone()
                    if stats:
                        col_prof.non_null_count = stats[0]
                        col_prof.null_count = stats[1]
                        col_prof.distinct_count = stats[2]
                        vmin = stats[3]
                        vmax = stats[4]

                        # Clean date formatting
                        if "DATE" in c_type or "TIMESTAMP" in c_type:
                            col_prof.vmin = str(vmin)[:10] if vmin is not None else None
                            col_prof.vmax = str(vmax)[:10] if vmax is not None else None
                        else:
                            col_prof.vmin = vmin
                            col_prof.vmax = vmax

                        # Collect enums or samples for categorical columns
                        if c_type in ("VARCHAR", "TEXT", "STRING") and col_prof.distinct_count > 0:
                            if col_prof.distinct_count <= 15:
                                enums = con.execute(
                                    f"""
                                    SELECT {_q(c_name)}, COUNT(*) 
                                    FROM {_q(tbl)} 
                                    WHERE {_q(c_name)} IS NOT NULL 
                                    GROUP BY 1 
                                    ORDER BY 2 DESC 
                                    LIMIT 10
                                    """
                                ).fetchall()
                                col_prof.enum_counts = [(str(r[0]), int(r[1])) for r in enums]
                            else:
                                samples = con.execute(
                                    f"SELECT DISTINCT {_q(c_name)} FROM {_q(tbl)} WHERE {_q(c_name)} IS NOT NULL LIMIT 3"
                                ).fetchall()
                                col_prof.sample_values = [str(r[0]) for r in samples]
                except Exception as e:
                    logger.debug(f"Error profiling column {tbl}.{c_name}: {e}")

            tbl_prof.columns[c_name] = col_prof

        prof.tables[tbl] = tbl_prof

    # 2. Discover Verified Join Relations
    JOIN_KEY_PATTERNS = ["ma_don", "ma_hd", "so_hd", "so_ct", "so_phieu", "ma_sp", "ma_hang", "ma_kh", "ma_ncc", "id_don"]
    active_tbls = [t for t in ctx.table_names if not t.endswith("_df") and prof.tables.get(t, TableProfile("", 0)).row_count > 0]

    for i in range(len(active_tbls)):
        for j in range(i + 1, len(active_tbls)):
            t1 = active_tbls[i]
            t2 = active_tbls[j]
            t1_cols = prof.tables[t1].columns
            t2_cols = prof.tables[t2].columns

            common_keys = set(t1_cols.keys()) & set(t2_cols.keys())
            for k in common_keys:
                is_key = (
                    any(p in k.lower() for p in JOIN_KEY_PATTERNS)
                    or k.lower().startswith("ma_")
                    or k.lower().endswith("_id")
                )
                if is_key:
                    try:
                        overlap_cnt = con.execute(
                            f"""
                            SELECT COUNT(*) 
                            FROM (SELECT DISTINCT {_q(k)} FROM {_q(t1)} WHERE {_q(k)} IS NOT NULL) a
                            JOIN (SELECT DISTINCT {_q(k)} FROM {_q(t2)} WHERE {_q(k)} IS NOT NULL) b
                              ON a.{_q(k)} = b.{_q(k)}
                            """
                        ).fetchone()[0]
                        if overlap_cnt > 0:
                            prof.relations.append(
                                Relation(
                                    from_table=t1,
                                    from_col=k,
                                    to_table=t2,
                                    to_col=k,
                                    overlap_count=overlap_cnt,
                                    verified=True,
                                )
                            )
                    except Exception:
                        pass

    return prof


def render_schema(prof: ProfileResult, question: str = "", max_chars: int = 4500) -> str:
    """
    Renders compact schema summary for prompts:
    - Tables and row counts.
    - Column types, date ranges [vmin .. vmax], enums ∈ {val (count)}.
    - Verified join relationships: QUAN HE JOIN DA KIEM CHUNG.
    - Adaptive truncation prioritized by question keywords.
    """
    if not prof or not prof.tables:
        return "No tables available in schema."

    q_lower = remove_accents((question or "").lower())
    q_words = set(re.findall(r"\w+", q_lower))

    # Score tables by question relevance
    table_scores: List[Tuple[int, str]] = []
    for t_name, t_prof in prof.tables.items():
        score = 0
        t_clean = remove_accents(t_name.lower())
        if any(w in t_clean for w in q_words):
            score += 5
        for c_name in t_prof.columns.keys():
            c_clean = remove_accents(c_name.lower())
            if any(w in c_clean for w in q_words):
                score += 2
        # Prioritize non-empty tables and sales tables
        if any(w in t_clean for w in ["ban_hang", "banhang", "hoa_don", "don_hang", "chi_tiet"]):
            score += 3
        table_scores.append((score, t_name))

    # Sort high score first, then by table name
    table_scores.sort(key=lambda x: (x[0], -len(x[1])), reverse=True)
    sorted_tables = [t[1] for t in table_scores]

    lines = []
    current_len = 0

    for t_name in sorted_tables:
        t_prof = prof.tables[t_name]
        t_lines = [f"Table `{t_name}` ({t_prof.row_count} rows):"]

        for c_name, c_prof in t_prof.columns.items():
            dtype = c_prof.dtype
            orig = f", original: '{c_prof.original_name}'" if c_prof.original_name and c_prof.original_name != c_name else ""

            extra = ""
            if c_prof.enum_counts:
                enum_str = ", ".join([f"'{val}' ({cnt})" for val, cnt in c_prof.enum_counts[:6]])
                extra = f" ∈ {{{enum_str}}}"
            elif c_prof.vmin is not None and c_prof.vmax is not None:
                extra = f" [range: {c_prof.vmin} .. {c_prof.vmax}]"
            elif c_prof.sample_values:
                sample_str = ", ".join([f"'{s}'" for s in c_prof.sample_values[:2]])
                extra = f" (Sample: {sample_str})"

            t_lines.append(f"  - {c_name} ({dtype}{orig}){extra}")

        tbl_block = "\n".join(t_lines) + "\n"
        if current_len + len(tbl_block) > max_chars - 400 and len(lines) > 0:
            # Add compact table representation instead
            compact_block = f"Table `{t_name}`: " + ", ".join(list(t_prof.columns.keys())[:10]) + "\n"
            if current_len + len(compact_block) <= max_chars - 300:
                lines.append(compact_block)
                current_len += len(compact_block)
            break

        lines.append(tbl_block)
        current_len += len(tbl_block)

    # Add verified joins
    if prof.relations:
        join_lines = ["QUAN HE JOIN DA KIEM CHUNG:"]
        seen_joins = set()
        for r in prof.relations:
            j_key = tuple(sorted([f"{r.from_table}.{r.from_col}", f"{r.to_table}.{r.to_col}"]))
            if j_key not in seen_joins:
                seen_joins.add(j_key)
                join_lines.append(f"- `{r.from_table}`.`{r.from_col}` = `{r.to_table}`.`{r.to_col}`")
                if len(seen_joins) >= 6:
                    break
        join_block = "\n".join(join_lines) + "\n"
        if current_len + len(join_block) <= max_chars:
            lines.append(join_block)

    return "\n".join(lines).strip()


def diagnose_empty_result(ctx: Any, prof: ProfileResult, sql: str) -> List[str]:
    """
    Diagnoses empty query results (empty DataFrame or 1x1 NULL/None):
    - Detects date filters outside table [vmin .. vmax].
    - Detects literal mismatches against categorical enums.
    - Suggests accent-insensitive vn(col) matching.
    - Suggests verified join relationships.
    Returns a list of clear diagnostic hint strings.
    """
    hints = []
    if not sql or not prof:
        return hints

    sql_clean = sql.strip()

    # 1. Date range diagnostics
    date_matches = re.findall(r"['\"](\d{4}-\d{2}(?:-\d{2})?)['\"]", sql_clean)
    if date_matches:
        for dt_str in date_matches:
            for t_name, t_prof in prof.tables.items():
                if t_name.lower() in sql_clean.lower():
                    for c_name, c_prof in t_prof.columns.items():
                        if ("DATE" in c_prof.dtype or "TIMESTAMP" in c_prof.dtype) and c_prof.vmin and c_prof.vmax:
                            if dt_str < str(c_prof.vmin)[:7] or dt_str > str(c_prof.vmax):
                                hints.append(
                                    f"Date filter '{dt_str}' is OUTSIDE the available date range in table `{t_name}` "
                                    f"[{c_prof.vmin} .. {c_prof.vmax}]. If the requested date has no data, output TYPE: unanswerable."
                                )

    # 2. Categorical enum value diagnostics
    string_literals = re.findall(
        r"(?:[!=<>]=\s*|=\s*|\bIN\s*\(\s*|\bLIKE\s+|\bILIKE\s+)['\"]([^'\"]+)['\"]",
        sql_clean,
        re.IGNORECASE,
    )
    for lit in string_literals:
        if len(lit) < 2 or lit.startswith("%") or lit.isdigit():
            continue
        lit_norm = remove_accents(lit.lower())
        for t_name, t_prof in prof.tables.items():
            if t_name.lower() in sql_clean.lower():
                for c_name, c_prof in t_prof.columns.items():
                    if c_prof.enum_counts:
                        exact_vals = [e[0] for e in c_prof.enum_counts]
                        if lit not in exact_vals:
                            matched_enums = [
                                e[0] for e in c_prof.enum_counts
                                if lit_norm == remove_accents(e[0].lower()) or lit_norm in remove_accents(e[0].lower())
                            ]
                            if matched_enums:
                                hints.append(
                                    f"Literal '{lit}' does not match categorical column `{c_name}`. "
                                    f"Exact values in database: {matched_enums}. "
                                    f"Use exact string literal '{matched_enums[0]}' or use accent-insensitive macro: "
                                    f"vn({c_name}) = vn('{lit}')."
                                )

    # 3. Suggest vn() macro for text/name columns if matching without vn()
    if "LIKE" in sql_clean.upper() and "vn(" not in sql_clean:
        hints.append("For text matching on Vietnamese names or descriptions, use vn(col) LIKE '%' || vn('keyword') || '%'.")

    # 4. Join diagnostics
    joined_tables = [t for t in prof.tables.keys() if t.lower() in sql_clean.lower()]
    if len(joined_tables) >= 2:
        verified_joins = [
            f"`{r.from_table}`.`{r.from_col}` = `{r.to_table}`.`{r.to_col}`"
            for r in prof.relations
            if r.from_table in joined_tables and r.to_table in joined_tables
        ]
        if verified_joins:
            hints.append(f"Ensure JOIN conditions match verified table relations: {', '.join(verified_joins)}.")

    return hints


def prepare(ctx: Any) -> ProfileResult:
    """
    End-to-end content-driven preparation pipeline for business context:
    1. Installs vn() and helper macros on DuckDB connection.
    2. Merges monthly shard tables into single unified tables (union_homogeneous).
    3. Normalizes column types (normalize_types) in all tables.
    4. Profiles tables, columns, date ranges, and verified joins (build_profile).
    """
    install_macros(ctx.con)
    merged_groups = union_homogeneous(ctx)

    # Normalize types across all active tables
    for tbl in list(ctx.table_names):
        if not tbl.endswith("_df"):
            normalize_types(ctx.con, tbl)

    prof = build_profile(ctx)
    prof.merged_groups = merged_groups
    return prof
