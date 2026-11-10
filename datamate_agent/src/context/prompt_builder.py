"""
Prompt Builder for DataMate Challenge.
Strict static-to-dynamic prompt hierarchy for vLLM KV Prefix Caching hit:
1. SYSTEM: Static sql_rules_system.txt + split's rulebook.md (100% shared across all questions in split).
2. USER Part 1 (Shop Static Prefix): README + RAW SCHEMA (sample rows & column mappings) + CANONICAL VIEWS & MACROS.
3. USER Part 2 (Question Dynamic Suffix): DATE ANCHORS + 4 Few-Shot Examples + QUESTION & Vietnamese abbreviations hint.
4. ASSISTANT Prefill: Always end raw prompt string with 'Notes:\n-'.
"""

import hashlib
import logging
import os
from typing import Any, Dict, List, Optional

from ..data_layer.ingest import BusinessContext
from .date_resolver import DateResolution, DateResolver

logger = logging.getLogger(__name__)


def build_chat_prompt(
    tokenizer: Optional[Any],
    messages: List[Dict[str, str]],
    prefill: str = "Notes:\n-",
) -> str:
    """
    Standardized chat prompt builder across train, inference, and repair.
    Applies tokenizer.apply_chat_template(messages, add_generation_prompt=True) + prefill.
    Falls back to ChatML format if tokenizer is unavailable.
    Always ends raw prompt string with prefill ("Notes:\n-").
    """
    if tokenizer is not None and hasattr(tokenizer, "apply_chat_template"):
        try:
            formatted = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            if prefill:
                if not formatted.endswith(prefill):
                    formatted = formatted + prefill
            return formatted
        except Exception:
            pass

    # ChatML fallback format
    parts = []
    for m in messages:
        role = m.get("role", "user")
        content = m.get("content", "")
        parts.append(f"<|im_start|>{role}\n{content}<|im_end|>")
    parts.append(f"<|im_start|>assistant\n{prefill}" if prefill else "<|im_start|>assistant\n")
    return "\n".join(parts)


FEW_SHOT_EX1 = """
Example 1 (Doanh thu tháng này - number):
Question: "doanh thu tháng này của quán là bao nhiêu?"
Date Anchors: Tháng này: từ 2026-08-01 đến 2026-08-20.
Notes:
- [Entity & Time analysis]: Target is total sales revenue for 'tháng này' (2026-08-01 to 2026-08-20).
- [Logic & Formulas]: Sum line amounts excluding cancelled/returned orders. Round to integer VND.
- [Output Type]: number
TYPE: number
```sql
SELECT ROUND(SUM(thanh_tien), 0) AS answer
FROM don_hang_chi_tiet
WHERE TRY_CAST(ngay AS DATE) BETWEEN '2026-08-01' AND '2026-08-20'
  AND LOWER(trang_thai) NOT IN ('huỷ', 'trả hàng');
```
""".strip()

FEW_SHOT_EX2 = """
Example 2 (Tỉ lệ tăng trưởng doanh thu so với kỳ trước - percent):
Question: "doanh thu tuần này tăng hay giảm bao nhiêu % so với tuần trước?"
Date Anchors: Tuần này: 2026-05-11 đến 2026-05-15. Tuần trước: 2026-05-04 đến 2026-05-10.
Notes:
- [Entity & Time analysis]: Compare revenue of this week vs last week.
- [Logic & Formulas]: Growth formula: ((Rev_this - Rev_last) / Rev_last) * 100. Round to 2 decimals.
- [Output Type]: percent
TYPE: percent
```sql
WITH rev_this AS (
    SELECT COALESCE(SUM(thanh_tien), 0) AS val
    FROM don_hang_chi_tiet
    WHERE TRY_CAST(ngay AS DATE) BETWEEN '2026-05-11' AND '2026-05-15'
      AND LOWER(trang_thai) NOT IN ('huỷ', 'trả hàng')
),
rev_last AS (
    SELECT COALESCE(SUM(thanh_tien), 0) AS val
    FROM don_hang_chi_tiet
    WHERE TRY_CAST(ngay AS DATE) BETWEEN '2026-05-04' AND '2026-05-10'
      AND LOWER(trang_thai) NOT IN ('huỷ', 'trả hàng')
)
SELECT ROUND(((rev_this.val - rev_last.val) / NULLIF(rev_last.val, 0)) * 100.0, 2) AS answer
FROM rev_this, rev_last;
```
""".strip()

FEW_SHOT_EX3 = """
Example 3 (Top 3 mặt hàng bán chạy nhất - list):
Question: "top 3 món bán chạy nhất tháng 7/2026 là những món nào?"
Date Anchors: Tháng 7/2026: 2026-07-01 đến 2026-07-31.
Notes:
- [Entity & Time analysis]: Top 3 best selling items in July 2026.
- [Logic & Formulas]: Total quantity base DESC, tie-breaker product_id ASC.
- [Output Type]: list
TYPE: list
```sql
SELECT ten_san_pham
FROM don_hang_chi_tiet
WHERE TRY_CAST(ngay AS DATE) BETWEEN '2026-07-01' AND '2026-07-31'
  AND LOWER(trang_thai) NOT IN ('huỷ', 'trả hàng')
GROUP BY ten_san_pham, ma_san_pham
ORDER BY SUM(so_luong) DESC, ma_san_pham ASC
LIMIT 3;
```
""".strip()

FEW_SHOT_EX4 = """
Example 4 (Câu không trả lời được - unanswerable):
Question: "lợi nhuận ròng của cửa hàng trong tháng 5/2026 là bao nhiêu?"
Date Anchors: Tháng 5/2026: 2026-05-01 đến 2026-05-31.
Notes:
- [Entity & Time analysis]: Net profit requested but database lacks expense ledger/cost tables.
- [Output Type]: unanswerable
TYPE: unanswerable
```sql
SELECT NULL AS answer;
```
""".strip()

FEW_SHOT_EXAMPLES = f"{FEW_SHOT_EX1}\n\n{FEW_SHOT_EX2}\n\n{FEW_SHOT_EX3}\n\n{FEW_SHOT_EX4}"


def select_curated_few_shots(question: str) -> str:
    """
    Selects 2 most relevant few-shots based on question keywords to keep token usage compact.
    """
    q_lower = (question or "").lower()
    if any(w in q_lower for w in ["top", "bán chạy", "xếp hạng", "nhiều nhất", "ít nhất", "bán được bao nhiêu"]):
        return f"{FEW_SHOT_EX3}\n\n{FEW_SHOT_EX4}"
    elif any(w in q_lower for w in ["%", "phần trăm", "tăng", "giảm", "tăng trưởng", "so với"]):
        return f"{FEW_SHOT_EX2}\n\n{FEW_SHOT_EX4}"
    else:
        return f"{FEW_SHOT_EX1}\n\n{FEW_SHOT_EX4}"


def filter_rulebook_for_question(rulebook_text: str, question: Optional[str] = None) -> str:
    """
    Extracts relevant sections of rulebook.md based on question keywords,
    always including core rules (as_of_date, revenue, time, unanswerable),
    while dropping non-SQL sections (file format documentation & grader scoring formulas).
    """
    if not rulebook_text:
        return "Apply standard DataMate business rules: Revenue excludes cancelled & returned orders."

    import re
    sections = re.split(r'\n(?=##\s+\d+\.)', rulebook_text)
    if len(sections) < 3:
        return re.sub(r"\n{3,}", "\n\n", rulebook_text).strip()

    # Core sections always included: Section 0 (Header), Section 1 (Revenue), Section 2 (Time), Section 7 (Unanswerable)
    selected = [sections[0]]
    if len(sections) > 1:
        selected.append(sections[1])  # Doanh thu
    if len(sections) > 2:
        selected.append(sections[2])  # Thời gian
    if len(sections) > 7:
        selected.append(sections[7])  # Không trả lời được

    q_lower = (question or "").lower()

    if question:
        if any(w in q_lower for w in ["xếp hạng", "bán chạy", "top", "nhiều nhất", "ít nhất", "bán được bao nhiêu"]) and len(sections) > 3:
            selected.append(sections[3])
        if any(w in q_lower for w in ["nợ", "công nợ", "tuổi nợ", "trả nợ", "thu nợ"]) and len(sections) > 4:
            selected.append(sections[4])
        if any(w in q_lower for w in ["kho", "tồn", "nhập", "giá vốn", "lãi", "lợi nhuận", "lãi gộp", "lãi ròng"]) and len(sections) > 5:
            selected.append(sections[5])
        if any(w in q_lower for w in ["cà phê", "size", "thuốc", "kê đơn", "hoạt chất", "lô", "hạn dùng", "vật liệu", "đợt giao"]) and len(sections) > 6:
            selected.append(sections[6])
    else:
        for idx in [3, 4, 5, 6]:
            if len(sections) > idx:
                selected.append(sections[idx])

    merged = "\n\n".join(s.strip() for s in selected)
    return re.sub(r"\n{3,}", "\n\n", merged).strip()


class PromptBuilder:
    def __init__(
        self,
        system_template_path: str,
        user_template_path: str,
        rulebook_path: Optional[str] = None,
        calendar_path: Optional[str] = None,
    ):
        self.system_template_path = system_template_path
        self.user_template_path = user_template_path
        self.rulebook_path = rulebook_path
        self.calendar_path = calendar_path
        self.date_resolver = DateResolver(calendar_path)

        # Load system template
        if os.path.exists(system_template_path):
            with open(system_template_path, "r", encoding="utf-8") as f:
                self.system_template = f.read()
        else:
            self.system_template = "You are DuckDB SQL Expert.\n{rulebook_content}"

        # Load user template
        if os.path.exists(user_template_path):
            with open(user_template_path, "r", encoding="utf-8") as f:
                self.user_template = f.read()
        else:
            self.user_template = "{question}"

    def get_rulebook_content(self, runtime_rulebook_path: Optional[str] = None) -> str:
        """
        Dynamically reads rulebook.md at runtime and logs SHA1 checksum.
        """
        path = runtime_rulebook_path or self.rulebook_path
        if path and os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    sha1 = hashlib.sha1(f.read()).hexdigest()
                logger.info(f"Loaded Runtime Rulebook from '{path}' (SHA1: {sha1})")
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                try:
                    with open(path, "r", encoding="latin1") as f:
                        content = f.read()
                except Exception:
                    content = ""
            if content:
                import re
                cleaned = re.sub(r"\n{3,}", "\n\n", content).strip()
                return cleaned
        return "Apply standard DataMate business rules: Revenue excludes cancelled & returned orders."

    def build_system_prompt(
        self,
        runtime_rulebook_path: Optional[str] = None,
        question: Optional[str] = None,
    ) -> str:
        """
        Builds static SYSTEM prompt: sql_rules_system.txt + split's rulebook.md.
        Filters out non-SQL documentation (file formats & grader formulas).
        If question is provided, extracts topic-relevant business rules.
        """
        raw_rulebook = self.get_rulebook_content(runtime_rulebook_path)
        rulebook_text = filter_rulebook_for_question(raw_rulebook, question)
        return self.system_template.format(rulebook_content=rulebook_text)

    def build_shop_static_prefix(
        self,
        ctx: BusinessContext,
        canonical_sales_sql: Optional[str] = None,
        canonical_orders_sql: Optional[str] = None,
        canonical_purchases_sql: Optional[str] = None,
        has_debt_macros: bool = False,
    ) -> str:
        """
        USER Part 1 (Shop Static Prefix):
        - README.md
        - RAW SCHEMA (with sample rows & original->clean column mappings)
        - CANONICAL VIEWS (v_sales, v_orders) & DEBT MACROS.
        100% shared across all questions of the same business_id.
        """
        readme = ctx.readme_text.strip()
        if len(readme) > 600:
            readme = readme[:600] + "\n...[truncated]"
        if not readme:
            readme = "No README provided."

        schema_summary = ctx.get_schema_summary()

        views_section = []
        if canonical_sales_sql and canonical_orders_sql:
            views_section.append("Canonical Views Available:")
            views_section.append("`v_sales`: Standardized order item sales (order_id, order_date, status, is_valid_sales, customer_id, customer_name, product_id, product_name, unit_name, quantity_base, unit_price, line_amount)")
            views_section.append("`v_orders`: Standardized order headers (order_id, order_date, status, is_cancelled, is_returned, is_valid_sales, customer_id, customer_name, payment_method, order_total)")
        if canonical_purchases_sql:
            if not views_section:
                views_section.append("Canonical Views Available:")
            views_section.append("`v_purchases`: Standardized purchase items (purchase_id, purchase_date, status, is_valid_purchase, supplier_id, supplier_name, product_id, product_name, unit_name, quantity_base, unit_price, line_amount)")
        if has_debt_macros:
            views_section.append("Debt Macros Available:")
            views_section.append("- `debt_at('YYYY-MM-DD')`: Table macro of remaining debts at given date")
            views_section.append("- `debt_new('start', 'end')`: Table macro of new debts incurred in period")
            views_section.append("- `debt_repaid('start', 'end')`: Table macro of debt repayments collected in period")
        canonical_str = "\n".join(views_section) if views_section else "No canonical views built; query raw tables directly."

        prefix_parts = [
            "===================================================================",
            "1. BUSINESS OVERVIEW (README)",
            "===================================================================",
            f"Business ID: {ctx.business_id}",
            readme,
            "",
            "===================================================================",
            "2. DATABASE SCHEMA & SAMPLE DATA",
            "===================================================================",
            "The DuckDB database contains the following tables:",
            schema_summary,
            "",
            "===================================================================",
            "3. CANONICAL VIEWS & MACROS (IF CONSTRUCTED)",
            "===================================================================",
            canonical_str,
        ]
        return "\n".join(prefix_parts)

    def build_question_dynamic_suffix(
        self,
        question: str,
        as_of_date: str,
    ) -> str:
        """
        USER Part 2 (Question Dynamic Suffix):
        - DATE ANCHORS (today = as_of_date, resolved windows for tuần này, tuần rồi, tháng này, Tết, etc.)
        - RULEBOOK CONSTRAINTS
        - 4 Few-Shot SQL Examples
        - QUESTION & Vietnamese abbreviations hint.
        """
        date_res = self.date_resolver.resolve(question, as_of_date)
        date_explanation = date_res.explanation

        suffix_parts = [
            "===================================================================",
            "4. DATE ANCHORS & TIME WINDOW RESOLUTION",
            "===================================================================",
            f"- Today (as_of_date): {as_of_date}",
            "- Target Date Context:",
            date_explanation,
            "",
            "===================================================================",
            "5. RULEBOOK CONSTRAINTS & HINTS",
            "===================================================================",
            "- The Business Rulebook provided in the system prompt is the authoritative single source of truth for all metric calculations, status filtering, date definitions, ranking ties, and rounding conventions.",
            "- If the required columns or tables do not exist in the database to answer the question, output TYPE: unanswerable.",
            "- Ensure all queries are valid DuckDB SQL syntax.",
            "- When canonical views (`v_sales`, `v_orders`) are available, you may query them; otherwise query raw tables directly.",
            "",
            "===================================================================",
            "6. FEW-SHOT EXAMPLES (SIMILAR QUESTIONS)",
            "===================================================================",
            select_curated_few_shots(question),
            "",
            "===================================================================",
            "7. CURRENT QUESTION & HINTS",
            "===================================================================",
            f'Question: "{question}"',
            f"As-of Date: {as_of_date}",
            "",
            "Vietnamese abbreviations hint:",
            "- 'doanh thu', 'dt' = sales revenue",
            "- 'đơn', 'đh', 'hd', 'hóa đơn' = orders / invoices",
            "- 'kh', 'khách' = customer",
            "- 'sp', 'hàng', 'món' = product / item",
            "- 'ncc' = supplier",
            "- 'cn', 'nợ' = debt / credit",
            "- 'sl' = quantity",
            "- 'km', 'ck' = discount / promotion",
            "",
            "Please write your reasoning in Notes, then output the target TYPE and the DuckDB SQL query.",
        ]
        return "\n".join(suffix_parts)

    def build_user_prompt(
        self,
        question: str,
        as_of_date: str,
        ctx: BusinessContext,
        canonical_sales_sql: Optional[str] = None,
        canonical_orders_sql: Optional[str] = None,
        canonical_purchases_sql: Optional[str] = None,
        has_debt_macros: bool = False,
    ) -> str:
        """
        Assembles full user prompt with strict static-prefix then dynamic-suffix ordering.
        """
        shop_prefix = self.build_shop_static_prefix(
            ctx=ctx,
            canonical_sales_sql=canonical_sales_sql,
            canonical_orders_sql=canonical_orders_sql,
            canonical_purchases_sql=canonical_purchases_sql,
            has_debt_macros=has_debt_macros,
        )
        question_suffix = self.build_question_dynamic_suffix(
            question=question,
            as_of_date=as_of_date,
        )
        return shop_prefix + "\n\n" + question_suffix

    def build_messages(
        self,
        question: str,
        as_of_date: str,
        ctx: BusinessContext,
        canonical_sales_sql: Optional[str] = None,
        canonical_orders_sql: Optional[str] = None,
        canonical_purchases_sql: Optional[str] = None,
        has_debt_macros: bool = False,
        runtime_rulebook_path: Optional[str] = None,
    ) -> List[Dict[str, str]]:
        """
        Creates OpenAI/vLLM format message list with strict static-to-dynamic prompt hierarchy.
        """
        sys_prompt = self.build_system_prompt(runtime_rulebook_path)
        user_prompt = self.build_user_prompt(
            question=question,
            as_of_date=as_of_date,
            ctx=ctx,
            canonical_sales_sql=canonical_sales_sql,
            canonical_orders_sql=canonical_orders_sql,
            canonical_purchases_sql=canonical_purchases_sql,
            has_debt_macros=has_debt_macros,
        )

        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt},
        ]
        return messages
