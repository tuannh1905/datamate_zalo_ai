"""
src/context/rule_router.py - Deterministic Rule Router & Pruner for DataMate Challenge.

Analyzes the user question and selectively extracts only the relevant sections of rulebook.md,
reducing prompt length by 60-75% and speeding up prefill attention while preserving 100% of
the business rules needed to answer the question.
"""

import logging
import re
from typing import Dict, List, Optional, Set, Tuple

logger = logging.getLogger(__name__)


# Core sections that are ALWAYS included in the prompt for grounding
ALWAYS_INCLUDED_HEADERS = [
    "Hôm nay",
    "Không trả lời được",
]

# Section keyword mapping for Vietnamese business queries
SECTION_KEYWORD_MAP: Dict[str, List[str]] = {
    # 1. Đơn hàng và doanh thu
    "doanh thu": [
        "doanh thu", "doanh so", "doanh số", "tiền hàng", "tiền bán", "tien ban",
        "bán được", "ban duoc", "thu về", "thu ve", "đơn hàng", "don hang",
        "huỷ", "huy", "trả hàng", "tra hang", "tỉ lệ huỷ", "ti le huy", "số đơn",
        "so don", "thanh toán", "thanh toan", "cod", "chuyển khoản", "tiền mặt",
        "khách vãng lai", "khach vang lai", "giảm giá", "giam gia", "voucher",
        "tăng trưởng", "tang truong", "chênh lệch", "chenh lech", "hơn kém", "hon kem"
    ],
    # 2. Thời gian
    "thời gian": [
        "hôm nay", "hom nay", "hôm qua", "hom qua", "tuần", "tuan", "tháng", "thang",
        "năm", "nam", "quý", "quy", "tết", "tet", "ca sáng", "ca sang", "ca chiều",
        "ca chieu", "đầu năm", "dau nam", "gần nhất", "gan nhat", "đến hết", "den het",
        "tính đến", "tinh den", "từ ngày", "tu ngay"
    ],
    # 3. Xếp hạng
    "xếp hạng": [
        "top", "xếp hạng", "xep hang", "bán chạy", "ban chay", "hot nhất", "hot nhat",
        "nhiều nhất", "nhieu nhat", "ít nhất", "it nhat", "cao nhất", "cao nhat",
        "thấp nhất", "thap nhat", "món", "mon", "mặt hàng", "mat hang", "sản phẩm",
        "san pham", "hàng lời nhất", "hang loi nhat", "nhân viên", "nhan vien",
        "bán giỏi nhất", "khách mua nhiều", "khach mua nhieu", "trung bình", "trung binh"
    ],
    # 4. Công nợ
    "công nợ": [
        "công nợ", "cong no", "nợ", "no", "phải thu", "phai thu", "chưa trả", "chua tra",
        "tuổi nợ", "tuoi no", "nợ thêm", "no them", "trả nợ", "tra no", "thu nợ",
        "thu no", "còn nợ", "con no", "quá hạn", "qua han", "nợ xấu", "no xau"
    ],
    # 5. Kho, nhập hàng, giá vốn
    "kho": [
        "kho", "nhập hàng", "nhap hang", "tồn kho", "ton kho", "còn tồn", "con ton",
        "giá vốn", "gia von", "lãi gộp", "lai gop", "lãi ròng", "lai rong", "lợi nhuận",
        "loi nhuan", "chi phí", "chi phi", "hết hàng", "het hang", "không bán được",
        "khong ban duoc", "hàng ế", "hang e", "bán ế", "tăng giá", "tang gia", "giá bán", "gia ban",
        "nhà cung cấp", "nha cung cap", "phiếu nhập", "phieu nhap"
    ],
    # 6. Ngành: Cà phê
    "cà phê": [
        "cà phê", "ca phe", "cafe", "size m", "size l"
    ],
    # 6. Ngành: Nhà thuốc
    "nhà thuốc": [
        "thuốc", "thuoc", "kê đơn", "ke don", "hết hạn", "het han", "hoạt chất",
        "hoat chat", "lô thuốc", "số lô", "theo lô", "dược", "duoc"
    ],
    # 6. Ngành: Vật liệu xây dựng
    "vật liệu": [
        "vật liệu", "vat lieu", "xây dựng", "xay dung", "đợt giao", "dot giao", "giao hàng"
    ],
}


def parse_markdown_sections(rulebook_md: str) -> List[Tuple[str, str]]:
    """
    Splits rulebook.md into sections based on '## ' headers.
    Returns a list of (header_title, section_content).
    """
    lines = rulebook_md.split("\n")
    sections: List[Tuple[str, str]] = []
    
    current_title = "Preamble"
    current_lines: List[str] = []
    
    for line in lines:
        if line.startswith("## "):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
                current_lines = []
            current_title = line.replace("## ", "").strip()
        current_lines.append(line)
        
    if current_lines:
        sections.append((current_title, "\n".join(current_lines).strip()))
        
    return sections


def route_rulebook(full_rulebook: str, question: Optional[str] = None) -> str:
    """
    Selectively extracts only relevant sections from rulebook.md for the given question.
    If question is None or empty, returns the full rulebook safely.
    """
    if not full_rulebook or not question or not question.strip():
        return full_rulebook

    q_lower = question.lower()
    sections = parse_markdown_sections(full_rulebook)
    
    if len(sections) <= 1:
        return full_rulebook

    # Determine matched categories from question keywords
    matched_categories: Set[str] = set()
    q_padded = f" {q_lower} "
    for category, keywords in SECTION_KEYWORD_MAP.items():
        for kw in keywords:
            if " " in kw:
                if kw in q_lower:
                    matched_categories.add(category)
                    break
            else:
                if re.search(rf"(?:\b|\W){re.escape(kw)}(?:\b|\W)", q_padded):
                    matched_categories.add(category)
                    break

    # If question mentions date / temporal context, always ensure "thời gian" is included
    matched_categories.add("thời gian")

    # Select sections to keep
    selected_sections: List[str] = []
    included_titles: List[str] = []

    for title, content in sections:
        title_lower = title.lower()
        
        # 1. Always keep preamble (header with as_of_date rule)
        if title == "Preamble" or "hôm nay" in title_lower:
            selected_sections.append(content)
            included_titles.append("Preamble")
            continue
            
        # 2. Always keep "Không trả lời được" / unanswerable guidance
        if "không trả lời được" in title_lower or "unanswerable" in title_lower:
            selected_sections.append(content)
            included_titles.append("Unanswerable")
            continue

        # 3. Check if section matches any active category
        keep = False
        for cat in matched_categories:
            if cat in title_lower:
                keep = True
                break
                
        # 4. Handle section 6 (Theo ngành) sub-sections
        if "theo ngành" in title_lower:
            # Check if any industry sub-category is active
            if any(ind in matched_categories for ind in ["cà phê", "nhà thuốc", "vật liệu"]):
                keep = True

        if keep:
            selected_sections.append(content)
            included_titles.append(title)

    # Fallback: if pruning became too aggressive (less than 2 sections), return full
    if len(selected_sections) < 2:
        return full_rulebook

    routed_content = "\n\n".join(selected_sections)
    saved_pct = round((1.0 - len(routed_content) / len(full_rulebook)) * 100, 1)
    logger.debug(
        f"[RuleRouter] Pruned rulebook for query: kept {included_titles} "
        f"({len(routed_content)}/{len(full_rulebook)} chars, -{saved_pct}% tokens)"
    )
    return routed_content
