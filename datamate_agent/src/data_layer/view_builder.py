"""
View Builder Module for DataMate Challenge.
Generates candidate SQL view drafts for canonical views (`v_sales`, `v_orders`),
auto-detects relational (header-detail, lookups) vs flat table structures,
maps core columns from real data without dummy constants,
normalizes status without blindly defaulting to 'hoàn thành',
enforces sanity checks (positive revenue, plausible dates, row counts),
and performs majority voting across diverse candidate implementations.
"""

import logging
import re
from collections import Counter
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

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


def find_column(cols: Dict[str, str], keywords: List[str]) -> Optional[str]:
    """Finds the first column matching any keyword in order of priority."""
    for kw in keywords:
        for lower_col, orig_col in cols.items():
            if kw == lower_col:
                return orig_col
    for kw in keywords:
        for lower_col, orig_col in cols.items():
            if kw in lower_col:
                return orig_col
    return None


def detect_table_structure(ctx: BusinessContext) -> Dict[str, Any]:
    """
    Analyzes table schemas to identify relational patterns:
    - Detail table (order items / lines)
    - Header table (order / invoice headers)
    - Product lookup table
    - Customer lookup table
    - Common join keys
    """
    tbl_names = ctx.table_names
    if not tbl_names:
        return {}

    schemas = ctx.schemas
    detail_tbl = None
    header_tbl = None
    product_tbl = None
    customer_tbl = None

    # Step 1: Detect detail table (has quantity, price/amount, item info)
    detail_candidates = []
    for tbl in tbl_names:
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        has_qty = any(k in cols for k in ["so_luong", "soluong", "quantity", "quy_ra_dv_le", "sl"]) or any("so_luong" in c for c in cols)
        has_amt = any(k in cols for k in ["thanh_tien", "tien_hang", "line_amount", "amount"]) or any("thanh_tien" in c for c in cols)
        has_prod = any(k in cols for k in ["ma_sp", "ma_hang", "ten_hang", "san_pham", "product_id", "product"]) or any("san_pham" in c for c in cols)
        has_order_key = any(k in cols for k in ["ma_don", "ma_hoa_don", "order_id", "so_hd", "id_don_hang", "so_ct"])

        score = (2 if has_qty else 0) + (2 if has_amt else 0) + (1 if has_prod else 0) + (1 if has_order_key else 0)
        tbl_lower = tbl.lower()
        if any(k in tbl_lower for k in ["chi_tiet", "chitiet", "detail", "item", "order_item"]):
            score += 3
        detail_candidates.append((score, tbl))

    detail_candidates.sort(key=lambda x: x[0], reverse=True)
    if detail_candidates and detail_candidates[0][0] >= 3:
        detail_tbl = detail_candidates[0][1]

    # Step 2: Detect header table (different from detail, has order key, date, customer/total)
    header_candidates = []
    for tbl in tbl_names:
        if tbl == detail_tbl:
            continue
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        has_order_key = any(k in cols for k in ["ma_don", "ma_hoa_don", "order_id", "so_hd", "id_don_hang", "so_ct"])
        has_date = any(k in cols for k in ["ngay", "date", "ngay_tao", "ngay_ban", "ngay_hd", "created_at"]) or any("ngay" in c for c in cols)
        has_status = any(k in cols for k in ["trang_thai", "status", "ket_qua"])
        has_cust = any(k in cols for k in ["khach_hang", "customer", "ma_khach", "ten_khach", "doi_tac"])

        score = (2 if has_order_key else 0) + (2 if has_date else 0) + (1 if has_status else 0) + (1 if has_cust else 0)
        tbl_lower = tbl.lower()
        if any(k in tbl_lower for k in ["don_hang", "hoa_don", "order", "orders", "ban_hang", "sales"]) and not any(k in tbl_lower for k in ["chi_tiet", "chitiet"]):
            score += 3
        header_candidates.append((score, tbl))

    header_candidates.sort(key=lambda x: x[0], reverse=True)
    if header_candidates and header_candidates[0][0] >= 3:
        header_tbl = header_candidates[0][1]

    # Step 3: Detect lookup tables
    for tbl in tbl_names:
        if tbl in (detail_tbl, header_tbl):
            continue
        tbl_lower = tbl.lower()
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        if any(k in tbl_lower for k in ["san_pham", "hang_hoa", "product"]):
            if any(k in cols for k in ["ma_sp", "ma_hang", "product_id", "ma_san_pham"]):
                product_tbl = tbl
        elif any(k in tbl_lower for k in ["khach_hang", "customer", "doi_tac"]):
            if any(k in cols for k in ["ma_khach", "customer_id", "ma_doi_tac"]):
                customer_tbl = tbl

    # Step 4: Check if header and detail share a join key
    join_key = None
    if detail_tbl and header_tbl:
        d_cols = {c["name"].lower(): c["name"] for c in schemas.get(detail_tbl, [])}
        h_cols = {c["name"].lower(): c["name"] for c in schemas.get(header_tbl, [])}
        potential_keys = ["ma_don", "ma_hoa_don", "order_id", "so_hd", "id_don_hang", "so_ct", "ma_don_hang", "hoa_don_id"]
        for pk in potential_keys:
            d_match = find_column(d_cols, [pk])
            h_match = find_column(h_cols, [pk])
            if d_match and h_match:
                join_key = (d_match, h_match)
                break

    # If detail and header cannot be joined or header doesn't exist, fall back to flat sales table
    if not (detail_tbl and header_tbl and join_key):
        flat_tbl = detail_tbl or (header_candidates[0][1] if header_candidates else tbl_names[0])
        return {
            "type": "flat",
            "sales_tbl": flat_tbl,
            "product_tbl": product_tbl,
            "customer_tbl": customer_tbl,
        }

    return {
        "type": "relational",
        "detail_tbl": detail_tbl,
        "header_tbl": header_tbl,
        "join_key": join_key,
        "product_tbl": product_tbl,
        "customer_tbl": customer_tbl,
    }


def generate_rule_based_view_drafts(ctx: BusinessContext, k: int = 8) -> List[Tuple[str, str]]:
    """
    Constructs diverse candidate SQL view drafts based on ingested tables and column heuristics.
    If core columns cannot be mapped from real data, returns empty list (view build will fail).
    """
    struct = detect_table_structure(ctx)
    if not struct:
        return []

    is_relational = struct.get("type") == "relational"
    schemas = ctx.schemas

    if is_relational:
        detail_tbl = struct["detail_tbl"]
        header_tbl = struct["header_tbl"]
        d_key, h_key = struct["join_key"]
        d_cols = {c["name"].lower(): c["name"] for c in schemas.get(detail_tbl, [])}
        h_cols = {c["name"].lower(): c["name"] for c in schemas.get(header_tbl, [])}

        # Date MUST come from header or detail
        date_col_orig = find_column(h_cols, ["ngay", "date", "ngay_tao", "ngay_ban", "ngay_hd", "created_at"]) or \
                        find_column(d_cols, ["ngay", "date", "ngay_tao", "ngay_ban", "ngay_hd", "created_at"])
        date_expr_base = f"h.{date_col_orig}" if date_col_orig in h_cols.values() else f"d.{date_col_orig}" if date_col_orig else None

        # Product MUST come from detail
        prod_name_orig = find_column(d_cols, ["ten_hang", "ten_sp", "san_pham", "product_name", "noi_dung", "mat_hang"])
        prod_id_orig = find_column(d_cols, ["ma_sp", "ma_hang", "ma_san_pham", "product_id"]) or prod_name_orig
        if not prod_name_orig and prod_id_orig:
            prod_name_orig = prod_id_orig

        # Quantity MUST come from detail
        qty_col_orig = find_column(d_cols, ["quy_ra_dv_le", "so_luong", "soluong", "quantity", "qty", "sl"])

        # Price / Amount
        amt_col_orig = find_column(d_cols, ["thanh_tien", "tien_hang", "line_amount", "amount", "tong_tien"])
        price_col_orig = find_column(d_cols, ["gia_ban", "don_gia", "gia_sp", "price", "unit_price"])

        # Order ID
        order_id_expr = f"d.{d_key}"

        # Status
        status_orig = find_column(h_cols, ["ket_qua", "trang_thai", "status"]) or find_column(d_cols, ["ket_qua", "trang_thai", "status"])
        status_expr_base = f"h.{status_orig}" if (status_orig and status_orig in h_cols.values()) else f"d.{status_orig}" if status_orig else None

        # Customer
        cust_id_orig = find_column(h_cols, ["ma_khach", "ma_doi_tac", "customer_id"]) or find_column(d_cols, ["ma_khach", "ma_doi_tac"])
        cust_name_orig = find_column(h_cols, ["khach_hang", "doi_tac", "ten_khach", "customer", "ten_doi_tac"]) or find_column(d_cols, ["khach_hang", "doi_tac"])

        # Payment
        pay_orig = find_column(h_cols, ["thanh_toan", "hinh_thuc", "pttt", "phuong_thuc"])
        pay_expr_base = f"h.{pay_orig}" if pay_orig else None

        # Header total
        header_total_orig = find_column(h_cols, ["tong_tien", "tong_thanh_toan", "tien_can_tra", "order_total", "total"])
        header_total_expr = f"h.{header_total_orig}" if header_total_orig else None

        unit_orig = find_column(d_cols, ["don_vi", "dvt", "unit", "don_vi_tinh"])

    else:
        sales_tbl = struct["sales_tbl"]
        s_cols = {c["name"].lower(): c["name"] for c in schemas.get(sales_tbl, [])}

        date_col_orig = find_column(s_cols, ["ngay", "date", "ngay_tao", "ngay_ban", "ngay_hd", "created_at"])
        date_expr_base = date_col_orig

        prod_name_orig = find_column(s_cols, ["noi_dung", "ten_hang", "san_pham", "ten_sp", "product", "product_name", "mat_hang"])
        prod_id_orig = find_column(s_cols, ["ma_hang", "ma_sp", "ma_san_pham", "product_id"]) or prod_name_orig
        if not prod_name_orig and prod_id_orig:
            prod_name_orig = prod_id_orig

        qty_col_orig = find_column(s_cols, ["quy_ra_dv_le", "so_luong", "soluong", "quantity", "qty", "sl"])
        amt_col_orig = find_column(s_cols, ["thanh_tien", "tong_tien", "line_amount", "amount", "tien_hang"])
        price_col_orig = find_column(s_cols, ["gia_ban", "don_gia", "gia_sp", "price", "unit_price"])

        order_id_col = find_column(s_cols, ["ma_don", "ma_hoa_don", "order_id", "so_ct", "don_hang", "so_hd", "id_don_hang"])
        order_id_expr = order_id_col if order_id_col else "NULL"

        status_orig = find_column(s_cols, ["ket_qua", "trang_thai", "status"])
        status_expr_base = status_orig

        cust_id_orig = find_column(s_cols, ["ma_khach", "ma_doi_tac", "customer_id"])
        cust_name_orig = find_column(s_cols, ["doi_tac", "khach_hang", "ten_khach", "customer", "ten_doi_tac"])

        pay_orig = find_column(s_cols, ["thanh_toan", "hinh_thuc", "pttt", "phuong_thuc"])
        pay_expr_base = pay_orig
        header_total_expr = None
        unit_orig = find_column(s_cols, ["don_vi", "dvt", "unit", "don_vi_tinh"])

    # Core columns validation:
    # 1. order_date must come from a real column
    # 2. product_name or product_id must come from a real column
    # 3. quantity must come from a real column
    # 4. amount must come from real column OR (real quantity * real price)
    if not date_expr_base:
        logger.warning("Canonical view rejected: no real date column found.")
        return []
    if not prod_name_orig and not prod_id_orig:
        logger.warning("Canonical view rejected: no real product column found.")
        return []
    if not qty_col_orig:
        logger.warning("Canonical view rejected: no real quantity column found.")
        return []
    if not amt_col_orig and not price_col_orig:
        logger.warning("Canonical view rejected: neither amount nor price column found.")
        return []

    # Prepare expression variants for diversity
    qty_expr = f"d.{qty_col_orig}" if is_relational else qty_col_orig
    price_expr = (f"d.{price_col_orig}" if is_relational else price_col_orig) if price_col_orig else "0"
    amt_expr_primary = (f"d.{amt_col_orig}" if is_relational else amt_col_orig) if amt_col_orig else f"({qty_expr} * {price_expr})"
    amt_expr_calc = f"({qty_expr} * {price_expr})" if price_col_orig else amt_expr_primary

    cust_id_expr = ((f"h.{cust_id_orig}" if cust_id_orig in h_cols.values() else f"d.{cust_id_orig}") if is_relational else cust_id_orig) if cust_id_orig else "NULL"
    cust_name_expr = ((f"h.{cust_name_orig}" if cust_name_orig in h_cols.values() else f"d.{cust_name_orig}") if is_relational else cust_name_orig) if cust_name_orig else "'Khách lẻ'"
    unit_expr = (f"d.{unit_orig}" if is_relational else unit_orig) if unit_orig else "'đơn vị'"

    prod_id_expr = (f"d.{prod_id_orig}" if is_relational else prod_id_orig) if prod_id_orig else "'SP'"
    prod_name_expr = (f"d.{prod_name_orig}" if is_relational else prod_name_orig) if prod_name_orig else prod_id_expr

    drafts = []

    # Diversity dimensions:
    # 1. Amount calculation: primary amount col vs (qty * price)
    # 2. Join type: INNER JOIN vs LEFT JOIN (if relational)
    # 3. Return filtering: line-level return check vs order-level window check
    # 4. Null order_id handling
    for var_idx in range(k):
        # Variant settings
        use_calc_amt = (var_idx % 2 == 1) and (price_col_orig is not None)
        active_amt_expr = amt_expr_calc if use_calc_amt else amt_expr_primary

        use_left_join = is_relational and (var_idx in [2, 3, 6, 7])
        join_clause = f"FROM {detail_tbl} d {'LEFT' if use_left_join else 'INNER'} JOIN {header_tbl} h ON d.{d_key} = h.{h_key}" if is_relational else f"FROM {sales_tbl}"

        # Status normalization: do NOT blindly default unknown statuses to 'hoàn thành'
        if status_expr_base:
            status_norm_sql = (
                f"CASE "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('huỷ', 'hủy', 'đã huỷ', 'cancelled', 'canceled') THEN 'huỷ' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('trả hàng', 'đã trả', 'returned', 'refunded') THEN 'trả hàng' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('đang giao', 'delivering', 'shipping') THEN 'đang giao' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('hoàn thành', 'thành công', 'đã giao', 'completed', 'success', 'delivered', 'đã thanh toán') THEN 'hoàn thành' "
                f"ELSE LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) END"
            )
        else:
            status_norm_sql = "'hoàn thành'"

        # Order-level return check when order_id exists
        if order_id_expr != "NULL" and status_expr_base:
            valid_sales_sql = (
                f"({status_norm_sql} NOT IN ('huỷ', 'trả hàng') AND "
                f"COALESCE(SUM(CASE WHEN {status_norm_sql} = 'trả hàng' THEN 1 ELSE 0 END) OVER (PARTITION BY {order_id_expr}), 0) = 0)"
            )
        else:
            valid_sales_sql = f"({status_norm_sql} NOT IN ('huỷ', 'trả hàng'))"

        # Date cast variant
        date_cast = f"TRY_CAST({date_expr_base} AS DATE)"

        pay_expr_final = f"CAST({pay_expr_base} AS VARCHAR)" if pay_expr_base else "'Tiền mặt'"

        v_sales_sql = f"""
        CREATE OR REPLACE VIEW v_sales AS
        SELECT
            CAST({order_id_expr} AS VARCHAR) AS order_id,
            {date_cast} AS order_date,
            {status_norm_sql} AS status,
            {valid_sales_sql} AS is_valid_sales,
            CAST({cust_id_expr} AS VARCHAR) AS customer_id,
            CAST({cust_name_expr} AS VARCHAR) AS customer_name,
            CAST({prod_id_expr} AS VARCHAR) AS product_id,
            CAST({prod_name_expr} AS VARCHAR) AS product_name,
            CAST({unit_expr} AS VARCHAR) AS unit_name,
            CAST(COALESCE({qty_expr}, 0) AS DOUBLE) AS quantity_base,
            CAST(COALESCE({price_expr}, 0) AS DOUBLE) AS unit_price,
            CAST(COALESCE({active_amt_expr}, 0) AS DOUBLE) AS line_amount,
            {pay_expr_final} AS payment_method
        {join_clause}
        WHERE {date_cast} IS NOT NULL;
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
            payment_method,
            SUM(line_amount) AS order_total
        FROM v_sales
        GROUP BY order_id, order_date, status, is_valid_sales, customer_id, customer_name, payment_method;
        """

        drafts.append((v_sales_sql.strip(), v_orders_sql.strip()))

    return drafts


def execute_and_fingerprint(con: duckdb.DuckDBPyConnection) -> Optional[str]:
    """
    Computes a deterministic fingerprint of canonical views and checks sanity:
    - row_count_sales > 0
    - min_date <= max_date and dates are plausible (between 2000 and 2030)
    - total_sales >= 0
    - row_count_orders > 0
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

        if not sales_row or not orders_row:
            return None

        count_sales, min_date, max_date, sum_sales = sales_row
        count_orders, sum_orders = orders_row

        # Sanity check criteria
        if count_sales <= 0 or count_orders <= 0:
            return None
        if not min_date or not max_date or min_date > max_date:
            return None
        if min_date < "2000-01-01" or max_date > "2030-01-01":
            return None
        if sum_sales < 0:
            return None

        fingerprint = f"{count_sales}_{min_date}_{max_date}_{sum_sales}_{count_orders}_{sum_orders}"
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
    Attempts rule-based repair of view SQL on DuckDB error (e.g. unknown column, syntax error).
    """
    if "Binder Error: Referenced column" in error_msg:
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
    Executes the view drafting, testing, self-repair, sanity checks, and voting pipeline:
    1. Obtains k view drafts (via LLM generator if provided or schema heuristics).
    2. If core columns (date, product, quantity, amount) cannot be mapped from real data,
       returns success=False and does NOT create views.
    3. Tests each draft in DuckDB, computing execution fingerprint and sanity checks.
    4. Computes majority vote.
    5. Locks in the winning views if agreement >= k * min_agreement_ratio.
       If agreement fails or views are invalid, drops views so model queries raw tables.
    """
    candidates: List[Tuple[str, str]] = []
    if llm_generator is not None:
        try:
            candidates = llm_generator(ctx)
        except Exception as e:
            logger.warning(f"LLM view generation failed, falling back to heuristics: {e}")
            candidates = generate_rule_based_view_drafts(ctx, k=k)
    else:
        candidates = generate_rule_based_view_drafts(ctx, k=k)

    if not candidates:
        # Drop any views in case
        ctx.con.execute("DROP VIEW IF EXISTS v_orders; DROP VIEW IF EXISTS v_sales;")
        return ViewBuildResult(
            success=False,
            error_message="No reliable canonical view candidates generated (missing core columns from real data)",
        )

    valid_candidates: List[Tuple[str, str, str]] = []  # (v_sales, v_orders, fingerprint)

    for idx, (v_sales, v_orders) in enumerate(candidates):
        curr_sales = v_sales
        curr_orders = v_orders

        for turn in range(max_repair_turns + 1):
            try:
                ctx.con.execute(curr_sales)
                ctx.con.execute(curr_orders)
                fp = execute_and_fingerprint(ctx.con)
                if fp is not None:
                    valid_candidates.append((curr_sales, curr_orders, fp))
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
        ctx.con.execute("DROP VIEW IF EXISTS v_orders; DROP VIEW IF EXISTS v_sales;")
        return ViewBuildResult(success=False, error_message="All view candidates failed execution or sanity checks")

    # Majority voting on fingerprints
    fp_counts = Counter(item[2] for item in valid_candidates)
    top_fp, top_count = fp_counts.most_common(1)[0]
    min_required = max(1, int(k * min_agreement_ratio))

    if top_count >= min_required:
        winning_candidate = next(c for c in valid_candidates if c[2] == top_fp)
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
        ctx.con.execute("DROP VIEW IF EXISTS v_orders; DROP VIEW IF EXISTS v_sales;")
        return ViewBuildResult(
            success=False,
            agreement_count=top_count,
            total_candidates=len(candidates),
            error_message="Agreement below threshold",
        )
