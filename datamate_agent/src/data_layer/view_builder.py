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
    v_purchases_sql: Optional[str] = None
    agreement_count: int = 0
    total_candidates: int = 0
    fingerprint: Optional[str] = None
    error_message: Optional[str] = None


DATE_KEYWORDS = [
    "thoi_gian", "thoi_gian_tao", "thoi_gian_ban", "thoi_gian_lap", "thoi_gian_nhap",
    "ngay_ban", "ngay_tao", "ngay_hd", "ngay_lap", "ngay_nhap", "ngay_ct", "ngay_chung_tu",
    "ngay", "date", "thoi_diem", "created_at", "timestamp", "datetime", "time"
]

ORDER_ID_KEYWORDS = [
    "ma_hoa_don", "ma_don_hang", "ma_don", "order_id", "so_hd", "id_don_hang",
    "so_ct", "so_hoa_don", "ma_phieu", "so_don", "hoa_don_id"
]

PURCHASE_ID_KEYWORDS = [
    "ma_nhap_hang", "ma_don_nhap", "ma_phieu_nhap", "so_phieu_nhap", "ma_nhap",
    "so_phieu", "ma_phieu", "purchase_id"
]

QUANTITY_KEYWORDS = [
    "so_luong", "soluong", "quy_ra_dv_le", "so_luong_quy_doi",
    "quantity", "qty", "sl", "sl_ban", "sl_nhap", "so_luong_nhap", "so_luong_ban"
]

AMOUNT_KEYWORDS = [
    "thanh_tien", "tien_hang", "tong_tien_hang", "tong_tien", "tong_thanh_toan",
    "line_amount", "amount", "gia_tri", "can_tra_ncc", "tien_hang_tra"
]

PRICE_KEYWORDS = [
    "gia_ban", "don_gia", "gia_sp", "price", "unit_price",
    "gia_nhap", "don_gia_nhap"
]

PRODUCT_NAME_KEYWORDS = [
    "ten_hang", "ten_sp", "san_pham", "product_name", "noi_dung", "mat_hang", "ten_mat_hang",
    "ten_dv", "dich_vu", "ten_dich_vu", "hang_hoa", "mon", "ten_mon", "item"
]

PRODUCT_ID_KEYWORDS = [
    "ma_hang", "ma_sp", "ma_san_pham", "product_id", "ma_mat_hang", "barcode",
    "ma_dv", "ma_dich_vu", "ma_mon", "item_id"
]

CUSTOMER_KEYWORDS = [
    "khach_hang", "ten_khach", "ten_khach_hang", "customer", "doi_tac", "ten_doi_tac"
]

CUSTOMER_ID_KEYWORDS = [
    "ma_khach", "ma_khach_hang", "customer_id", "ma_doi_tac"
]

SUPPLIER_KEYWORDS = [
    "nha_cung_cap", "ten_ncc", "ten_nha_cung_cap", "supplier", "nha_cc"
]

SUPPLIER_ID_KEYWORDS = [
    "ma_ncc", "ma_nha_cung_cap", "supplier_id"
]

STATUS_KEYWORDS = [
    "trang_thai", "ket_qua", "status", "tinh_trang", "trang_thai_don"
]


def find_column(cols: Dict[str, str], keywords: List[str]) -> Optional[str]:
    """Finds the first column matching any keyword in order of priority."""
    # 1. Exact match
    for kw in keywords:
        for lower_col, orig_col in cols.items():
            if kw == lower_col:
                return orig_col
    # 2. Prefix or suffix match
    for kw in keywords:
        for lower_col, orig_col in cols.items():
            if lower_col.startswith(kw + "_") or lower_col.endswith("_" + kw):
                return orig_col
    # 3. Substring match
    for kw in keywords:
        for lower_col, orig_col in cols.items():
            if kw in lower_col:
                return orig_col
    return None


def is_purchase_table(tbl: str) -> bool:
    t_low = tbl.lower()
    return any(k in t_low for k in ["nhap_hang", "nhaphang", "phieu_nhap", "don_nhap", "nhap"]) and not any(k in t_low for k in ["ban_hang", "hoa_don"])


def detect_table_structure(ctx: BusinessContext) -> Dict[str, Any]:
    """
    Analyzes table schemas to identify relational patterns:
    - Sales detail table (order items / lines)
    - Sales header table (order / invoice headers)
    - Purchase detail table (goods receipt items)
    - Purchase header table (goods receipt headers)
    - Product / Customer / Supplier lookup tables
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
    supplier_tbl = None

    sales_tbl_candidates = [t for t in tbl_names if not is_purchase_table(t)]
    if not sales_tbl_candidates:
        sales_tbl_candidates = list(tbl_names)

    # Step 1: Detect sales detail table (has quantity, price/amount, item info)
    detail_candidates = []
    for tbl in sales_tbl_candidates:
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        has_qty = any(k in cols for k in QUANTITY_KEYWORDS) or any(any(k in c for k in ["so_luong", "soluong", "quy_ra_dv_le", "qty"]) for c in cols)
        has_amt = any(k in cols for k in AMOUNT_KEYWORDS) or any(any(k in c for k in ["thanh_tien", "tien_hang", "amount", "tong_tien"]) for c in cols)
        has_prod = any(k in cols for k in PRODUCT_ID_KEYWORDS + PRODUCT_NAME_KEYWORDS) or any(any(k in c for k in ["san_pham", "ten_hang", "ma_hang", "mat_hang"]) for c in cols)
        has_order_key = any(k in cols for k in ORDER_ID_KEYWORDS) or any(any(k in c for k in ["ma_don", "ma_hoa_don", "order_id", "so_hd"]) for c in cols)

        score = (2 if has_qty else 0) + (2 if has_amt else 0) + (1 if has_prod else 0) + (1 if has_order_key else 0)
        tbl_lower = tbl.lower()
        if any(k in tbl_lower for k in ["chi_tiet", "chitiet", "detail", "item", "order_item", "line"]):
            score += 3
        detail_candidates.append((score, tbl))

    detail_candidates.sort(key=lambda x: x[0], reverse=True)
    if detail_candidates and detail_candidates[0][0] >= 3:
        detail_tbl = detail_candidates[0][1]

    # Step 2: Detect sales header table (different from detail, has order key, date, customer/total)
    header_candidates = []
    for tbl in sales_tbl_candidates:
        if tbl == detail_tbl:
            continue
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        has_order_key = any(k in cols for k in ORDER_ID_KEYWORDS) or any(any(k in c for k in ["ma_don", "ma_hoa_don", "order_id", "so_hd"]) for c in cols)
        has_date = any(k in cols for k in DATE_KEYWORDS) or any(any(k in c for k in ["ngay", "thoi_gian", "date", "time"]) for c in cols)
        has_status = any(k in cols for k in STATUS_KEYWORDS)
        has_cust = any(k in cols for k in CUSTOMER_ID_KEYWORDS + CUSTOMER_KEYWORDS)

        score = (2 if has_order_key else 0) + (2 if has_date else 0) + (1 if has_status else 0) + (1 if has_cust else 0)
        tbl_lower = tbl.lower()
        if any(k in tbl_lower for k in ["don_hang", "hoa_don", "order", "orders", "ban_hang", "sales", "invoice"]) and not any(k in tbl_lower for k in ["chi_tiet", "chitiet"]):
            score += 3
        header_candidates.append((score, tbl))

    header_candidates.sort(key=lambda x: x[0], reverse=True)
    if header_candidates and header_candidates[0][0] >= 3:
        header_tbl = header_candidates[0][1]

    # Step 3: Check sales join key
    join_key = None
    if detail_tbl and header_tbl:
        d_cols = {c["name"].lower(): c["name"] for c in schemas.get(detail_tbl, [])}
        h_cols = {c["name"].lower(): c["name"] for c in schemas.get(header_tbl, [])}
        for pk in ORDER_ID_KEYWORDS + ["id", "code"]:
            d_match = find_column(d_cols, [pk])
            h_match = find_column(h_cols, [pk])
            if d_match and h_match:
                join_key = (d_match, h_match)
                break
        if not join_key:
            common_cols = [c for c in d_cols if c in h_cols and any(k in c for k in ["ma_", "_id", "id_", "so_"])]
            if common_cols:
                join_key = (d_cols[common_cols[0]], h_cols[common_cols[0]])

    # Step 4: Purchase tables detection
    purchase_tbl_candidates = [t for t in tbl_names if is_purchase_table(t)]
    p_detail_tbl = None
    p_header_tbl = None
    p_join_key = None
    p_tbl = None

    if purchase_tbl_candidates:
        # Step P1: Purchase detail
        p_detail_cands = []
        for tbl in purchase_tbl_candidates:
            cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
            has_qty = any(k in cols for k in QUANTITY_KEYWORDS)
            has_amt = any(k in cols for k in AMOUNT_KEYWORDS)
            has_prod = any(k in cols for k in PRODUCT_ID_KEYWORDS + PRODUCT_NAME_KEYWORDS)
            has_pkey = any(k in cols for k in PURCHASE_ID_KEYWORDS)
            score = (2 if has_qty else 0) + (2 if has_amt else 0) + (1 if has_prod else 0) + (1 if has_pkey else 0)
            tbl_lower = tbl.lower()
            if any(k in tbl_lower for k in ["chi_tiet", "chitiet", "detail"]):
                score += 3
            p_detail_cands.append((score, tbl))
        p_detail_cands.sort(key=lambda x: x[0], reverse=True)
        if p_detail_cands and p_detail_cands[0][0] >= 2:
            p_detail_tbl = p_detail_cands[0][1]

        # Step P2: Purchase header
        p_header_cands = []
        for tbl in purchase_tbl_candidates:
            if tbl == p_detail_tbl:
                continue
            cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
            has_pkey = any(k in cols for k in PURCHASE_ID_KEYWORDS)
            has_date = any(k in cols for k in DATE_KEYWORDS) or any(any(k in c for k in ["ngay", "thoi_gian", "date", "time"]) for c in cols)
            has_status = any(k in cols for k in STATUS_KEYWORDS)
            has_supp = any(k in cols for k in SUPPLIER_ID_KEYWORDS + SUPPLIER_KEYWORDS)
            score = (2 if has_pkey else 0) + (2 if has_date else 0) + (1 if has_status else 0) + (1 if has_supp else 0)
            tbl_lower = tbl.lower()
            if not any(k in tbl_lower for k in ["chi_tiet", "chitiet"]):
                score += 3
            p_header_cands.append((score, tbl))
        p_header_cands.sort(key=lambda x: x[0], reverse=True)
        if p_header_cands and p_header_cands[0][0] >= 2:
            p_header_tbl = p_header_cands[0][1]

        # Step P3: Purchase join key
        if p_detail_tbl and p_header_tbl:
            d_cols = {c["name"].lower(): c["name"] for c in schemas.get(p_detail_tbl, [])}
            h_cols = {c["name"].lower(): c["name"] for c in schemas.get(p_header_tbl, [])}
            for pk in PURCHASE_ID_KEYWORDS:
                d_match = find_column(d_cols, [pk])
                h_match = find_column(h_cols, [pk])
                if d_match and h_match:
                    p_join_key = (d_match, h_match)
                    break
            if not p_join_key:
                common_cols = [c for c in d_cols if c in h_cols and any(k in c for k in ["ma_", "_id", "id_", "so_"])]
                if common_cols:
                    p_join_key = (d_cols[common_cols[0]], h_cols[common_cols[0]])
        elif p_detail_tbl and not p_header_tbl:
            p_tbl = p_detail_tbl
        elif p_header_tbl and not p_detail_tbl:
            p_tbl = p_header_tbl
        elif purchase_tbl_candidates:
            p_tbl = purchase_tbl_candidates[0]

    # Step 5: Detect lookup tables
    for tbl in tbl_names:
        if tbl in (detail_tbl, header_tbl, p_detail_tbl, p_header_tbl):
            continue
        tbl_lower = tbl.lower()
        cols = {c["name"].lower(): c["name"] for c in schemas.get(tbl, [])}
        if any(k in tbl_lower for k in ["san_pham", "hang_hoa", "product"]):
            if any(k in cols for k in PRODUCT_ID_KEYWORDS):
                product_tbl = tbl
        elif any(k in tbl_lower for k in ["khach_hang", "customer", "doi_tac"]):
            if any(k in cols for k in CUSTOMER_ID_KEYWORDS):
                customer_tbl = tbl
        elif any(k in tbl_lower for k in ["nha_cung_cap", "ncc", "supplier"]):
            if any(k in cols for k in SUPPLIER_ID_KEYWORDS):
                supplier_tbl = tbl

    is_sales_relational = bool(detail_tbl and header_tbl and join_key)
    flat_sales_tbl = detail_tbl or (header_candidates[0][1] if header_candidates else (sales_tbl_candidates[0] if sales_tbl_candidates else tbl_names[0]))

    return {
        "type": "relational" if is_sales_relational else "flat",
        "detail_tbl": detail_tbl,
        "header_tbl": header_tbl,
        "join_key": join_key,
        "sales_tbl": flat_sales_tbl,
        "product_tbl": product_tbl,
        "customer_tbl": customer_tbl,
        "supplier_tbl": supplier_tbl,
        "purchase_type": "relational" if (p_detail_tbl and p_header_tbl and p_join_key) else ("flat" if p_tbl else None),
        "purchase_detail_tbl": p_detail_tbl,
        "purchase_header_tbl": p_header_tbl,
        "purchase_join_key": p_join_key,
        "purchase_tbl": p_tbl or p_detail_tbl,
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
        date_col_orig = find_column(h_cols, DATE_KEYWORDS) or find_column(d_cols, DATE_KEYWORDS)
        date_expr_base = f"h.{date_col_orig}" if (date_col_orig and date_col_orig in h_cols.values()) else (f"d.{date_col_orig}" if date_col_orig else None)

        # Product MUST come from detail
        prod_name_orig = find_column(d_cols, PRODUCT_NAME_KEYWORDS)
        prod_id_orig = find_column(d_cols, PRODUCT_ID_KEYWORDS) or prod_name_orig
        if not prod_name_orig and prod_id_orig:
            prod_name_orig = prod_id_orig

        # Quantity MUST come from detail
        qty_col_orig = find_column(d_cols, QUANTITY_KEYWORDS)

        # Price / Amount
        amt_col_orig = find_column(d_cols, AMOUNT_KEYWORDS)
        price_col_orig = find_column(d_cols, PRICE_KEYWORDS)

        # Order ID
        order_id_expr = f"d.{d_key}"

        # Status
        status_orig = find_column(h_cols, STATUS_KEYWORDS) or find_column(d_cols, STATUS_KEYWORDS)
        status_expr_base = f"h.{status_orig}" if (status_orig and status_orig in h_cols.values()) else (f"d.{status_orig}" if status_orig else None)

        # Customer
        cust_id_orig = find_column(h_cols, CUSTOMER_ID_KEYWORDS) or find_column(d_cols, CUSTOMER_ID_KEYWORDS)
        cust_name_orig = find_column(h_cols, CUSTOMER_KEYWORDS) or find_column(d_cols, CUSTOMER_KEYWORDS)

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

        date_col_orig = find_column(s_cols, DATE_KEYWORDS)
        date_expr_base = date_col_orig

        prod_name_orig = find_column(s_cols, PRODUCT_NAME_KEYWORDS)
        prod_id_orig = find_column(s_cols, PRODUCT_ID_KEYWORDS) or prod_name_orig
        if not prod_name_orig and prod_id_orig:
            prod_name_orig = prod_id_orig

        qty_col_orig = find_column(s_cols, QUANTITY_KEYWORDS)
        amt_col_orig = find_column(s_cols, AMOUNT_KEYWORDS)
        price_col_orig = find_column(s_cols, PRICE_KEYWORDS)

        order_id_col = find_column(s_cols, ORDER_ID_KEYWORDS)
        order_id_expr = order_id_col if order_id_col else "NULL"

        status_orig = find_column(s_cols, STATUS_KEYWORDS)
        status_expr_base = status_orig

        cust_id_orig = find_column(s_cols, CUSTOMER_ID_KEYWORDS)
        cust_name_orig = find_column(s_cols, CUSTOMER_KEYWORDS)

        pay_orig = find_column(s_cols, ["thanh_toan", "hinh_thuc", "pttt", "phuong_thuc"])
        pay_expr_base = pay_orig
        header_total_expr = None
        unit_orig = find_column(s_cols, ["don_vi", "dvt", "unit", "don_vi_tinh"])

    # Core columns validation:
    # 1. order_date must come from a real column
    # 2. product_name or product_id must come from a real column
    # 3. amount must come from real column OR (real quantity * real price)
    if not date_expr_base:
        logger.warning("Canonical view rejected: no real date column found.")
        return []
    if not prod_name_orig and not prod_id_orig:
        logger.warning("Canonical view rejected: no real product column found.")
        return []
    if not qty_col_orig and not amt_col_orig and not price_col_orig:
        logger.warning("Canonical view rejected: neither quantity, amount, nor price column found.")
        return []
    if not amt_col_orig and not price_col_orig:
        logger.warning("Canonical view rejected: neither amount nor price column found.")
        return []

    # Prepare expression variants for diversity
    qty_expr = (f"d.{qty_col_orig}" if is_relational else qty_col_orig) if qty_col_orig else "1.0"
    price_expr = (f"d.{price_col_orig}" if is_relational else price_col_orig) if price_col_orig else None
    amt_expr_primary = (f"d.{amt_col_orig}" if is_relational else amt_col_orig) if amt_col_orig else None

    if amt_expr_primary and not price_expr:
        price_expr = f"({amt_expr_primary} / NULLIF({qty_expr}, 0))"
    elif price_expr and not amt_expr_primary:
        amt_expr_primary = f"({qty_expr} * {price_expr})"

    price_expr_final = price_expr if price_expr else "0.0"
    amt_expr_primary_final = amt_expr_primary if amt_expr_primary else f"({qty_expr} * {price_expr_final})"
    amt_expr_calc = f"({qty_expr} * {price_expr_final})" if price_expr else amt_expr_primary_final

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
        active_amt_expr = amt_expr_calc if use_calc_amt else amt_expr_primary_final

        use_left_join = is_relational and (var_idx in [2, 3, 6, 7])
        join_clause = f"FROM {detail_tbl} d {'LEFT' if use_left_join else 'INNER'} JOIN {header_tbl} h ON d.{d_key} = h.{h_key}" if is_relational else f"FROM {sales_tbl}"

        # Status normalization: do NOT blindly default unknown statuses to 'hoàn thành'
        if status_expr_base:
            status_norm_sql = (
                f"CASE "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('huỷ', 'hủy', 'đã huỷ', 'đã hủy', 'cancelled', 'canceled', 'huy') THEN 'huỷ' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('trả hàng', 'đã trả', 'returned', 'refunded', 'tra hang') THEN 'trả hàng' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('đang giao', 'đang giao hàng', 'delivering', 'shipping', 'đang xử lý', 'chờ xử lý') THEN 'đang giao' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('hoàn thành', 'thành công', 'đã giao', 'completed', 'success', 'delivered', 'đã thanh toán', 'đã nhập', 'đã nhập hàng', 'da thanh toan', 'da hoan thanh', 'đã xong') THEN 'hoàn thành' "
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
            CAST(COALESCE({qty_expr}, 1.0) AS DOUBLE) AS quantity_base,
            CAST(COALESCE({price_expr_final}, 0) AS DOUBLE) AS unit_price,
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


def generate_purchase_view_drafts(ctx: BusinessContext, k: int = 8) -> List[str]:
    """
    Constructs candidate SQL view drafts for `v_purchases`.
    """
    struct = detect_table_structure(ctx)
    p_type = struct.get("purchase_type")
    if not p_type:
        return []

    schemas = ctx.schemas
    is_relational = (p_type == "relational")

    if is_relational:
        detail_tbl = struct["purchase_detail_tbl"]
        header_tbl = struct["purchase_header_tbl"]
        d_key, h_key = struct["purchase_join_key"]
        d_cols = {c["name"].lower(): c["name"] for c in schemas.get(detail_tbl, [])}
        h_cols = {c["name"].lower(): c["name"] for c in schemas.get(header_tbl, [])}

        date_col = find_column(h_cols, DATE_KEYWORDS) or find_column(d_cols, DATE_KEYWORDS)
        date_expr_base = f"h.{date_col}" if (date_col and date_col in h_cols.values()) else (f"d.{date_col}" if date_col else None)

        purchase_id_expr = f"d.{d_key}"

        prod_name = find_column(d_cols, PRODUCT_NAME_KEYWORDS)
        prod_id = find_column(d_cols, PRODUCT_ID_KEYWORDS) or prod_name
        if not prod_name and prod_id:
            prod_name = prod_id

        qty_col = find_column(d_cols, QUANTITY_KEYWORDS)
        amt_col = find_column(d_cols, AMOUNT_KEYWORDS)
        price_col = find_column(d_cols, PRICE_KEYWORDS)

        supp_id = find_column(h_cols, SUPPLIER_ID_KEYWORDS) or find_column(d_cols, SUPPLIER_ID_KEYWORDS)
        supp_name = find_column(h_cols, SUPPLIER_KEYWORDS) or find_column(d_cols, SUPPLIER_KEYWORDS)

        status_col = find_column(h_cols, STATUS_KEYWORDS) or find_column(d_cols, STATUS_KEYWORDS)
        status_expr_base = f"h.{status_col}" if (status_col and status_col in h_cols.values()) else (f"d.{status_col}" if status_col else None)
        unit_col = find_column(d_cols, ["don_vi", "dvt", "unit", "don_vi_tinh"])
    else:
        p_tbl = struct["purchase_tbl"]
        if not p_tbl:
            return []
        p_cols = {c["name"].lower(): c["name"] for c in schemas.get(p_tbl, [])}
        date_col = find_column(p_cols, DATE_KEYWORDS)
        date_expr_base = date_col
        purchase_id_col = find_column(p_cols, PURCHASE_ID_KEYWORDS)
        purchase_id_expr = purchase_id_col if purchase_id_col else "NULL"
        prod_name = find_column(p_cols, PRODUCT_NAME_KEYWORDS)
        prod_id = find_column(p_cols, PRODUCT_ID_KEYWORDS) or prod_name
        if not prod_name and prod_id:
            prod_name = prod_id
        qty_col = find_column(p_cols, QUANTITY_KEYWORDS)
        amt_col = find_column(p_cols, AMOUNT_KEYWORDS)
        price_col = find_column(p_cols, PRICE_KEYWORDS)
        supp_id = find_column(p_cols, SUPPLIER_ID_KEYWORDS)
        supp_name = find_column(p_cols, SUPPLIER_KEYWORDS)
        status_col = find_column(p_cols, STATUS_KEYWORDS)
        status_expr_base = status_col
        unit_col = find_column(p_cols, ["don_vi", "dvt", "unit", "don_vi_tinh"])

    if not date_expr_base:
        return []
    if not prod_name and not prod_id:
        return []
    if not amt_col and not price_col and not qty_col:
        return []

    qty_expr = (f"d.{qty_col}" if is_relational else qty_col) if qty_col else "1.0"
    amt_expr_primary = (f"d.{amt_col}" if is_relational else amt_col) if amt_col else None
    price_expr = (f"d.{price_col}" if is_relational else price_col) if price_col else None

    if amt_expr_primary and not price_expr:
        price_expr = f"({amt_expr_primary} / NULLIF({qty_expr}, 0))"
    elif price_expr and not amt_expr_primary:
        amt_expr_primary = f"({qty_expr} * {price_expr})"

    price_expr_final = price_expr if price_expr else "0.0"
    amt_expr_primary_final = amt_expr_primary if amt_expr_primary else f"({qty_expr} * {price_expr_final})"
    amt_expr_calc = f"({qty_expr} * {price_expr_final})" if price_expr else amt_expr_primary_final

    supp_id_expr = ((f"h.{supp_id}" if is_relational and supp_id in h_cols.values() else f"d.{supp_id}") if is_relational else supp_id) if supp_id else "NULL"
    supp_name_expr = ((f"h.{supp_name}" if is_relational and supp_name in h_cols.values() else f"d.{supp_name}") if is_relational else supp_name) if supp_name else "'Nhà cung cấp'"
    unit_expr = (f"d.{unit_col}" if is_relational else unit_col) if unit_col else "'đơn vị'"
    prod_id_expr = (f"d.{prod_id}" if is_relational else prod_id) if prod_id else "'SP'"
    prod_name_expr = (f"d.{prod_name}" if is_relational else prod_name) if prod_name else prod_id_expr

    drafts = []
    for var_idx in range(k):
        use_calc_amt = (var_idx % 2 == 1) and (price_col is not None)
        active_amt_expr = amt_expr_calc if use_calc_amt else amt_expr_primary_final
        use_left_join = is_relational and (var_idx in [2, 3, 6, 7])
        join_clause = f"FROM {detail_tbl} d {'LEFT' if use_left_join else 'INNER'} JOIN {header_tbl} h ON d.{d_key} = h.{h_key}" if is_relational else f"FROM {p_tbl}"

        if status_expr_base:
            status_norm_sql = (
                f"CASE "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('huỷ', 'hủy', 'đã huỷ', 'đã hủy', 'cancelled', 'canceled') THEN 'huỷ' "
                f"WHEN LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) IN ('hoàn thành', 'đã nhập', 'đã nhập hàng', 'thành công', 'completed', 'success') THEN 'hoàn thành' "
                f"ELSE LOWER(TRIM(CAST({status_expr_base} AS VARCHAR))) END"
            )
            valid_p_sql = f"({status_norm_sql} NOT IN ('huỷ'))"
        else:
            status_norm_sql = "'hoàn thành'"
            valid_p_sql = "TRUE"

        date_cast = f"TRY_CAST({date_expr_base} AS DATE)"

        v_purchases_sql = f"""
        CREATE OR REPLACE VIEW v_purchases AS
        SELECT
            CAST({purchase_id_expr} AS VARCHAR) AS purchase_id,
            {date_cast} AS purchase_date,
            {status_norm_sql} AS status,
            {valid_p_sql} AS is_valid_purchase,
            CAST({supp_id_expr} AS VARCHAR) AS supplier_id,
            CAST({supp_name_expr} AS VARCHAR) AS supplier_name,
            CAST({prod_id_expr} AS VARCHAR) AS product_id,
            CAST({prod_name_expr} AS VARCHAR) AS product_name,
            CAST({unit_expr} AS VARCHAR) AS unit_name,
            CAST(COALESCE({qty_expr}, 1.0) AS DOUBLE) AS quantity_base,
            CAST(COALESCE({price_expr_final}, 0) AS DOUBLE) AS unit_price,
            CAST(COALESCE({active_amt_expr}, 0) AS DOUBLE) AS line_amount
        {join_clause}
        WHERE {date_cast} IS NOT NULL;
        """
        drafts.append(v_purchases_sql.strip())
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


def execute_and_fingerprint_purchases(con: duckdb.DuckDBPyConnection) -> Optional[str]:
    """
    Computes fingerprint for v_purchases view.
    """
    try:
        row = con.execute("""
            SELECT 
                COUNT(*), 
                COALESCE(CAST(MIN(purchase_date) AS VARCHAR), ''), 
                COALESCE(CAST(MAX(purchase_date) AS VARCHAR), ''),
                ROUND(COALESCE(SUM(line_amount), 0), 0)
            FROM v_purchases
        """).fetchone()
        if not row:
            return None
        count_p, min_date, max_date, sum_p = row
        if count_p <= 0 or not min_date or not max_date or min_date > max_date:
            return None
        if min_date < "2000-01-01" or max_date > "2030-01-01":
            return None
        if sum_p < 0:
            return None
        return f"{count_p}_{min_date}_{max_date}_{sum_p}"
    except Exception as e:
        logger.debug(f"Purchases fingerprinting failed: {e}")
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
    Executes the view drafting, testing, self-repair, sanity checks, and voting pipeline
    for both sales views (`v_sales`, `v_orders`) and purchase view (`v_purchases`).
    Checks if valid cached views already exist in ctx or DuckDB to skip redundant LLM view drafting.
    """
    # 0. Check if valid canonical views already exist in cache
    if getattr(ctx, "canonical_views", None) and ctx.canonical_views.get("success"):
        return ViewBuildResult(
            success=True,
            v_sales_sql=ctx.canonical_views.get("v_sales_sql"),
            v_orders_sql=ctx.canonical_views.get("v_orders_sql"),
            v_purchases_sql=ctx.canonical_views.get("v_purchases_sql"),
            fingerprint="cached",
        )

    try:
        ctx.con.execute("SELECT 1 FROM v_sales LIMIT 1")
        ctx.con.execute("SELECT 1 FROM v_orders LIMIT 1")
        logger.info(f"Canonical views v_sales and v_orders already exist in database for {ctx.business_id}. Skipping re-drafting.")
        return ViewBuildResult(
            success=True,
            v_sales_sql=ctx.canonical_views.get("v_sales_sql") if getattr(ctx, "canonical_views", None) else None,
            v_orders_sql=ctx.canonical_views.get("v_orders_sql") if getattr(ctx, "canonical_views", None) else None,
            v_purchases_sql=ctx.canonical_views.get("v_purchases_sql") if getattr(ctx, "canonical_views", None) else None,
            fingerprint="cached",
        )
    except Exception:
        pass

    # ------------------ Part 1: Sales Views ------------------
    sales_candidates: List[Tuple[str, str]] = []
    if llm_generator is not None:
        try:
            sales_candidates = llm_generator(ctx)
        except Exception as e:
            logger.warning(f"LLM view generation failed, falling back to heuristics: {e}")
            sales_candidates = generate_rule_based_view_drafts(ctx, k=k)
    else:
        sales_candidates = generate_rule_based_view_drafts(ctx, k=k)

    winning_sales: Optional[Tuple[str, str, int, str]] = None  # (v_sales, v_orders, count, fp)

    if sales_candidates:
        valid_candidates: List[Tuple[str, str, str]] = []  # (v_sales, v_orders, fingerprint)

        for idx, (v_sales, v_orders) in enumerate(sales_candidates):
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

        if valid_candidates:
            fp_counts = Counter(item[2] for item in valid_candidates)
            top_fp, top_count = fp_counts.most_common(1)[0]
            min_required = max(1, int(k * min_agreement_ratio))

            if top_count >= min_required:
                winning = next(c for c in valid_candidates if c[2] == top_fp)
                winning_sales = (winning[0], winning[1], top_count, top_fp)
                ctx.con.execute(winning[0])
                ctx.con.execute(winning[1])
                logger.info(f"Canonical sales views successfully built with agreement {top_count}/{len(sales_candidates)}")

    if not winning_sales:
        ctx.con.execute("DROP VIEW IF EXISTS v_orders; DROP VIEW IF EXISTS v_sales;")

    # ------------------ Part 2: Purchase Views ------------------
    purchase_candidates = generate_purchase_view_drafts(ctx, k=k)
    winning_purchases: Optional[Tuple[str, int, str]] = None  # (v_purchases, count, fp)

    if purchase_candidates:
        valid_p_cands: List[Tuple[str, str]] = []
        for idx, p_sql in enumerate(purchase_candidates):
            try:
                ctx.con.execute(p_sql)
                p_fp = execute_and_fingerprint_purchases(ctx.con)
                if p_fp is not None:
                    valid_p_cands.append((p_sql, p_fp))
            except Exception:
                continue

        if valid_p_cands:
            p_counts = Counter(item[1] for item in valid_p_cands)
            top_p_fp, top_p_count = p_counts.most_common(1)[0]
            min_required = max(1, int(k * min_agreement_ratio))
            if top_p_count >= min_required:
                winning_p = next(c for c in valid_p_cands if c[1] == top_p_fp)
                winning_purchases = (winning_p[0], top_p_count, top_p_fp)
                ctx.con.execute(winning_p[0])
                logger.info(f"Canonical purchase view successfully built with agreement {top_p_count}/{len(purchase_candidates)}")

    if not winning_purchases:
        ctx.con.execute("DROP VIEW IF EXISTS v_purchases;")

    # ------------------ Summary & Decision ------------------
    success = (winning_sales is not None or winning_purchases is not None)
    if success:
        return ViewBuildResult(
            success=True,
            v_sales_sql=winning_sales[0] if winning_sales else None,
            v_orders_sql=winning_sales[1] if winning_sales else None,
            v_purchases_sql=winning_purchases[0] if winning_purchases else None,
            agreement_count=winning_sales[2] if winning_sales else (winning_purchases[1] if winning_purchases else 0),
            total_candidates=len(sales_candidates) if sales_candidates else len(purchase_candidates),
            fingerprint=winning_sales[3] if winning_sales else (winning_purchases[2] if winning_purchases else None),
        )
    else:
        return ViewBuildResult(
            success=False,
            error_message="No reliable canonical view candidates generated (missing core columns from real data)",
        )
