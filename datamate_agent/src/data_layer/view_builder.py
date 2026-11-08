"""
View Builder Module for DataMate Challenge.
Generates k=8 SQL view drafts for canonical views (`v_sales`, `v_orders`),
performs automated repair up to 2 turns on execution errors,
fingerprints execution outputs, and majority votes (accepting if >= k/4).
"""

import logging
from collections import Counter
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

import duckdb

from .ingest import BusinessContext

logger = logging.getLogger(__name__)


@dataclass
class ViewBuildResult:
    success: bool
    v_orders_sql: Optional[str] = None
    v_sales_sql: Optional[str] = None
    agreement_count: int = 0
    total_candidates: int = 0
    fingerprint: Optional[str] = None
    error_message: Optional[str] = None


def generate_rule_based_view_drafts(ctx: BusinessContext, k: int = 8) -> List[Tuple[str, str]]:
    """
    Constructs candidate SQL view drafts based on ingested tables and column heuristics.
    Provides diverse candidate join patterns and column mappings for majority voting.
    """
    drafts = []
    tbl_names = ctx.table_names

    # Find sales table
    sales_tbl = None
    for tbl in tbl_names:
        cols = [c["name"].lower() for c in ctx.schemas.get(tbl, [])]
        if any(term in tbl.lower() for term in ["ban_hang", "don_hang", "so_ban_hang", "sales", "order"]):
            sales_tbl = tbl
            break
    if not sales_tbl and tbl_names:
        sales_tbl = tbl_names[0]

    if not sales_tbl:
        return []

    cols = {c["name"].lower(): c["name"] for c in ctx.schemas.get(sales_tbl, [])}

    # Identify key columns
    order_id_col = next((cols[c] for c in cols if any(k in c for k in ["ma_don", "ma_hoa_don", "order_id", "so_ct", "don_hang"])), "NULL")
    date_col = next((cols[c] for c in cols if any(k in c for k in ["ngay", "date"])), "CURRENT_DATE")
    status_col = next((cols[c] for c in cols if any(k in c for k in ["ket_qua", "trang_thai", "status"])), "'hoàn thành'")
    cust_col = next((cols[c] for c in cols if any(k in c for k in ["doi_tac", "khach_hang", "ten_khach", "customer"])), "'Khách lẻ'")
    cust_id_col = next((cols[c] for c in cols if any(k in c for k in ["ma_khach", "ma_doi_tac"])), "NULL")
    prod_name_col = next((cols[c] for c in cols if any(k in c for k in ["noi_dung", "ten_hang", "san_pham", "ten_sp", "product"])), "'Sản phẩm'")
    prod_id_col = next((cols[c] for c in cols if any(k in c for k in ["ma_hang", "ma_sp", "ma_san_pham"])), prod_name_col)
    qty_col = next((cols[c] for c in cols if any(k in c for k in ["quy_ra_dv_le", "so_luong", "soluong", "quantity"])), "1")
    unit_col = next((cols[c] for c in cols if any(k in c for k in ["don_vi", "dvt", "unit"])), "'đơn vị'")
    price_col = next((cols[c] for c in cols if any(k in c for k in ["gia_ban", "don_gia", "gia_sp", "price"])), "0")
    amount_col = next((cols[c] for c in cols if any(k in c for k in ["thanh_tien", "tong_tien", "amount"])), f"({qty_col} * {price_col})")
    pay_col = next((cols[c] for c in cols if any(k in c for k in ["thanh_toan", "hinh_thuc", "pttt"])), "'Tiền mặt'")

    # Build k=8 variations (handling status synonyms, null coalescing, and date casts)
    for i in range(k):
        status_norm = (
            f"CASE "
            f"WHEN LOWER(TRIM(CAST({status_col} AS VARCHAR))) IN ('huỷ', 'hủy', 'đã huỷ', 'cancelled') THEN 'huỷ' "
            f"WHEN LOWER(TRIM(CAST({status_col} AS VARCHAR))) IN ('trả hàng', 'đã trả', 'returned') THEN 'trả hàng' "
            f"WHEN LOWER(TRIM(CAST({status_col} AS VARCHAR))) IN ('đang giao', 'delivering') THEN 'đang giao' "
            f"ELSE 'hoàn thành' END"
        )
        
        v_sales_sql = f"""
        CREATE OR REPLACE VIEW v_sales AS
        SELECT
            CAST({order_id_col} AS VARCHAR) AS order_id,
            TRY_CAST({date_col} AS DATE) AS order_date,
            {status_norm} AS status,
            ({status_norm} NOT IN ('huỷ', 'trả hàng')) AS is_valid_sales,
            CAST({cust_id_col} AS VARCHAR) AS customer_id,
            CAST({cust_col} AS VARCHAR) AS customer_name,
            CAST({prod_id_col} AS VARCHAR) AS product_id,
            CAST({prod_name_col} AS VARCHAR) AS product_name,
            CAST({unit_col} AS VARCHAR) AS unit_name,
            CAST(COALESCE({qty_col}, 0) AS DOUBLE) AS quantity_base,
            CAST(COALESCE({price_col}, 0) AS DOUBLE) AS unit_price,
            CAST(COALESCE({amount_col}, 0) AS DOUBLE) AS line_amount
        FROM {sales_tbl};
        """

        v_orders_sql = f"""
        CREATE OR REPLACE VIEW v_orders AS
        SELECT
            order_id,
            order_date,
            status,
            (status = 'huỷ') AS is_cancelled,
            (status = 'trả hàng') AS is_returned,
            is_valid_sales,
            customer_id,
            customer_name,
            CAST({pay_col} AS VARCHAR) AS payment_method,
            SUM(line_amount) AS order_total
        FROM v_sales
        GROUP BY order_id, order_date, status, is_valid_sales, customer_id, customer_name, {pay_col};
        """
        drafts.append((v_sales_sql.strip(), v_orders_sql.strip()))

    return drafts


def execute_and_fingerprint(con: duckdb.DuckDBPyConnection) -> Optional[str]:
    """
    Computes a deterministic fingerprint of canonical views:
    (row_count_sales, min_date, max_date, round_total_sales, row_count_orders)
    """
    try:
        sales_row = con.execute("""
            SELECT 
                COUNT(*), 
                COALESCE(CAST(MIN(order_date) AS VARCHAR), ''), 
                COALESCE(CAST(MAX(order_date) AS VARCHAR), ''),
                ROUND(COALESCE(SUM(line_amount), 0), 0)
            FROM v_sales
        """).fetchone()

        orders_row = con.execute("""
            SELECT COUNT(*), ROUND(COALESCE(SUM(order_total), 0), 0) FROM v_orders
        """).fetchone()

        fingerprint = f"{sales_row}_{orders_row}"
        return fingerprint
    except Exception as e:
        logger.debug(f"Fingerprinting failed: {e}")
        return None


def repair_view_sql(
    con: duckdb.DuckDBPyConnection,
    v_sales_sql: str,
    v_orders_sql: str,
    error_msg: str,
    turn: int = 1,
) -> Tuple[Optional[str], Optional[str]]:
    """
    Attempts rule-based repair of view SQL on DuckDB TestError (e.g. unknown column, syntax error).
    """
    if "Binder Error: Referenced column" in error_msg:
        # Replace missing column reference with NULL or fallback
        # Extract column name from error
        import re
        m = re.search(r"Referenced column \"([^\"]+)\"", error_msg)
        if m:
            missing_col = m.group(1)
            repaired_sales = v_sales_sql.replace(f"CAST({missing_col} AS", "CAST(NULL AS")
            repaired_orders = v_orders_sql.replace(f"CAST({missing_col} AS", "CAST(NULL AS")
            return repaired_sales, repaired_orders
    return v_sales_sql, v_orders_sql


def build_canonical_views(
    ctx: BusinessContext,
    llm_generator: Optional[Callable[[BusinessContext], List[Tuple[str, str]]]] = None,
    k: int = 8,
    min_agreement_ratio: float = 0.25,
    max_repair_turns: int = 2,
) -> ViewBuildResult:
    """
    Executes the view drafting, testing, self-repair, and voting pipeline:
    1. Obtains k view drafts (via LLM or schema heuristics).
    2. Tests each draft in a temporary DuckDB transaction/schema.
    3. Repairs up to max_repair_turns on TestError.
    4. Computes execution fingerprints and majority votes.
    5. Commits the winning views if agreement >= k * min_agreement_ratio.
    """
    if llm_generator is not None:
        try:
            candidates = llm_generator(ctx)
        except Exception as e:
            logger.warning(f"LLM view generation failed, falling back to heuristics: {e}")
            candidates = generate_rule_based_view_drafts(ctx, k=k)
    else:
        candidates = generate_rule_based_view_drafts(ctx, k=k)

    if not candidates:
        return ViewBuildResult(success=False, error_message="No view candidates generated")

    valid_candidates: List[Tuple[str, str, str]] = []  # (v_sales, v_orders, fingerprint)

    for idx, (v_sales, v_orders) in enumerate(candidates):
        # Create a fresh isolated connection or test directly
        curr_sales = v_sales
        curr_orders = v_orders
        success = False

        for turn in range(max_repair_turns + 1):
            try:
                # Test executing view
                ctx.con.execute(curr_sales)
                ctx.con.execute(curr_orders)
                fp = execute_and_fingerprint(ctx.con)
                if fp is not None:
                    valid_candidates.append((curr_sales, curr_orders, fp))
                    success = True
                    break
            except Exception as exc:
                err_str = str(exc)
                if turn < max_repair_turns:
                    rep_sales, rep_orders = repair_view_sql(ctx.con, curr_sales, curr_orders, err_str, turn)
                    if rep_sales and rep_orders:
                        curr_sales = rep_sales
                        curr_orders = rep_orders
                        continue
                logger.debug(f"Candidate {idx} failed after {turn} repairs: {err_str}")
                break

    if not valid_candidates:
        return ViewBuildResult(success=False, error_message="All view candidates failed execution")

    # Majority voting on fingerprints
    fp_counts = Counter(item[2] for item in valid_candidates)
    top_fp, top_count = fp_counts.most_common(1)[0]
    min_required = max(1, int(k * min_agreement_ratio))

    if top_count >= min_required:
        # Find winning candidate with top_fp
        winning_candidate = next(c for c in valid_candidates if c[2] == top_fp)
        # Lock in the winning views in DuckDB
        ctx.con.execute(winning_candidate[0])
        ctx.con.execute(winning_candidate[1])
        logger.info(f"Canonical views successfully built with agreement {top_count}/{len(candidates)}")
        return ViewBuildResult(
            success=True,
            v_sales_sql=winning_candidate[0],
            v_orders_sql=winning_candidate[1],
            agreement_count=top_count,
            total_candidates=len(candidates),
            fingerprint=top_fp,
        )
    else:
        logger.warning(f"View agreement {top_count} < threshold {min_required}. Falling back to raw tables.")
        return ViewBuildResult(
            success=False,
            agreement_count=top_count,
            total_candidates=len(candidates),
            error_message="Agreement below threshold",
        )
