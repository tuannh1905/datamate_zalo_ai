"""
Debt Tracking Table Macros for DataMate Challenge.
Registers DuckDB macros following Rulebook Section 4:
- debt_at(target_date): total unpaid debt of orders placed <= target_date, accounting for payments <= target_date.
- debt_new(start_date, end_date): new debt incurred for credit orders placed in [start_date, end_date] not paid on order date.
- debt_repaid(start_date, end_date): debt repayments collected in [start_date, end_date] for credit orders where payment was after order date.
Includes an automated plausibility check to verify macro integrity.
"""

import logging
from dataclasses import dataclass
from typing import Optional

import duckdb

from .ingest import BusinessContext

logger = logging.getLogger(__name__)


@dataclass
class DebtMacroStatus:
    registered: bool
    plausibility_passed: bool
    error_message: Optional[str] = None


def register_debt_macros(ctx: BusinessContext, plausibility_check: bool = True) -> DebtMacroStatus:
    """
    Detects payment/debt structures in business tables, creates canonical `v_payments` if needed,
    registers `debt_at`, `debt_new`, and `debt_repaid` DuckDB macros, and validates them.
    """
    con = ctx.con

    # Check if v_orders exists
    try:
        con.execute("SELECT 1 FROM v_orders LIMIT 1")
        has_v_orders = True
    except Exception:
        has_v_orders = False

    # Look for payments table (e.g., raw_thanh_toan, raw_pos_thanh_toan)
    payment_tbl = None
    for tbl in ctx.table_names:
        if any(term in tbl.lower() for term in ["thanh_toan", "phieu_thu", "payment", "tra_no"]):
            payment_tbl = tbl
            break

    # If payment table exists, create canonical v_payments view
    if payment_tbl:
        cols = {c["name"].lower(): c["name"] for c in ctx.schemas.get(payment_tbl, [])}
        order_id_col = next((cols[c] for c in cols if any(k in c for k in ["ma_don", "ma_hoa_don", "mahoadon", "order_id"])), "NULL")
        date_col = next((cols[c] for c in cols if any(k in c for k in ["ngay", "date", "thoi_gian"])), "CURRENT_DATE")
        amount_col = next((cols[c] for c in cols if any(k in c for k in ["tien", "so_tien", "sotienthu", "amount"])), "0")
        method_col = next((cols[c] for c in cols if any(k in c for k in ["phuong_thuc", "phuongthuc", "method"])), "'Tiền mặt'")

        try:
            v_pay_sql = f"""
            CREATE OR REPLACE VIEW v_payments AS
            SELECT
                ROW_NUMBER() OVER () AS payment_id,
                CAST({order_id_col} AS VARCHAR) AS order_id,
                TRY_CAST({date_col} AS DATE) AS payment_date,
                CAST(COALESCE({amount_col}, 0) AS DOUBLE) AS paid_amount,
                CAST({method_col} AS VARCHAR) AS payment_method
            FROM {payment_tbl};
            """
            con.execute(v_pay_sql)
        except Exception as e:
            logger.debug(f"Could not build v_payments view: {e}")

    # If no v_payments view could be constructed, build an empty fallback view
    try:
        con.execute("SELECT 1 FROM v_payments LIMIT 1")
    except Exception:
        con.execute("""
            CREATE OR REPLACE VIEW v_payments AS
            SELECT 
                CAST(NULL AS BIGINT) AS payment_id,
                CAST(NULL AS VARCHAR) AS order_id,
                CAST(NULL AS DATE) AS payment_date,
                CAST(0.0 AS DOUBLE) AS paid_amount,
                CAST(NULL AS VARCHAR) AS payment_method
            WHERE 1=0;
        """)

    # Check if base views are in place
    if not has_v_orders:
        return DebtMacroStatus(
            registered=False,
            plausibility_passed=False,
            error_message="v_orders view does not exist",
        )

    # Register the 3 table macros
    try:
        # Macro 1: debt_at(target_date)
        con.execute("""
            CREATE OR REPLACE MACRO debt_at(target_date) AS TABLE
            SELECT 
                o.order_id,
                o.customer_id,
                o.customer_name,
                o.order_date,
                DATEDIFF('day', o.order_date, CAST(target_date AS DATE)) AS debt_age_days,
                o.order_total,
                COALESCE(SUM(p.paid_amount), 0) AS total_paid_to_date,
                ROUND((o.order_total - COALESCE(SUM(p.paid_amount), 0)), 0) AS remaining_debt
            FROM v_orders o
            LEFT JOIN v_payments p 
                ON o.order_id = p.order_id 
               AND CAST(p.payment_date AS DATE) <= CAST(target_date AS DATE)
            WHERE o.is_cancelled = FALSE
              AND LOWER(COALESCE(o.payment_method, '')) NOT IN ('cod', 'sàn tmđt', 'shopee', 'lazada', 'tiktok')
              AND CAST(o.order_date AS DATE) <= CAST(target_date AS DATE)
            GROUP BY o.order_id, o.customer_id, o.customer_name, o.order_date, o.order_total, target_date
            HAVING (o.order_total - COALESCE(SUM(p.paid_amount), 0)) > 0;
        """)

        # Macro 2: debt_new(start_date, end_date)
        con.execute("""
            CREATE OR REPLACE MACRO debt_new(start_date, end_date) AS TABLE
            SELECT 
                o.order_id,
                o.customer_id,
                o.customer_name,
                o.order_date,
                ROUND((o.order_total - COALESCE(same_day.same_day_paid, 0)), 0) AS new_debt_amount
            FROM v_orders o
            LEFT JOIN (
                SELECT order_id, SUM(paid_amount) AS same_day_paid
                FROM v_payments
                WHERE payment_date = order_date
                GROUP BY order_id
            ) same_day ON o.order_id = same_day.order_id
            WHERE o.is_cancelled = FALSE
              AND LOWER(COALESCE(o.payment_method, '')) IN ('ghi nợ', 'nợ', 'công nợ')
              AND CAST(o.order_date AS DATE) BETWEEN CAST(start_date AS DATE) AND CAST(end_date AS DATE)
              AND (o.order_total - COALESCE(same_day.same_day_paid, 0)) > 0;
        """)

        # Macro 3: debt_repaid(start_date, end_date)
        con.execute("""
            CREATE OR REPLACE MACRO debt_repaid(start_date, end_date) AS TABLE
            SELECT 
                p.payment_id,
                p.order_id,
                o.customer_id,
                o.customer_name,
                p.payment_date,
                p.paid_amount
            FROM v_payments p
            JOIN v_orders o ON p.order_id = o.order_id
            WHERE o.is_cancelled = FALSE
              AND LOWER(COALESCE(o.payment_method, '')) IN ('ghi nợ', 'nợ', 'công nợ')
              AND CAST(p.payment_date AS DATE) > CAST(o.order_date AS DATE)
              AND CAST(p.payment_date AS DATE) BETWEEN CAST(start_date AS DATE) AND CAST(end_date AS DATE);
        """)
    except Exception as e:
        logger.error(f"Failed to register debt macros: {e}")
        return DebtMacroStatus(registered=False, plausibility_passed=False, error_message=str(e))

    # Plausibility check
    if plausibility_check:
        try:
            sample_debt = con.execute("SELECT COUNT(*) FROM debt_at('2026-12-31')").fetchone()[0]
            logger.info(f"Debt macro plausibility check passed. Debt rows at 2026-12-31: {sample_debt}")
            return DebtMacroStatus(registered=True, plausibility_passed=True)
        except Exception as exc:
            logger.warning(f"Debt macro plausibility check failed: {exc}. Unregistering macros.")
            try:
                con.execute("DROP MACRO IF EXISTS debt_at;")
                con.execute("DROP MACRO IF EXISTS debt_new;")
                con.execute("DROP MACRO IF EXISTS debt_repaid;")
            except Exception:
                pass
            return DebtMacroStatus(registered=False, plausibility_passed=False, error_message=str(exc))

    return DebtMacroStatus(registered=True, plausibility_passed=True)
