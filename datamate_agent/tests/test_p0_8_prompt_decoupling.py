import os
import hashlib
from src.context.prompt_builder import FEW_SHOT_EXAMPLES, PromptBuilder


def test_sql_rules_system_decoupled():
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "sql_rules_system.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Hardcoded domain rules must NOT be in Section 1
    assert "ROUND(pct, 2)" not in content
    assert "Vietnamese Dong (VND) is an integer currency" not in content
    assert "ties broken by item code / ID ascending" not in content
    assert "{rulebook_content}" in content
    assert "AUTHORITATIVE SOURCE OF TRUTH" in content


def test_qa_user_template_decoupled():
    template_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "qa_user_template.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Section 5 must not have hardcoded train assumptions
    assert "BEFORE order-level voucher" not in content
    assert "authoritative single source of truth" in content.lower()


def test_few_shot_examples_decoupled():
    # Must not reference specific "Rulebook Section X"
    assert "Rulebook Section" not in FEW_SHOT_EXAMPLES


def test_rulebook_sha1_logging(tmp_path, caplog):
    import logging
    rulebook_file = tmp_path / "rulebook.md"
    rulebook_text = "# Test Rulebook Content"
    rulebook_file.write_text(rulebook_text, encoding="utf-8")

    expected_sha1 = hashlib.sha1(rulebook_text.encode("utf-8")).hexdigest()

    builder = PromptBuilder(
        system_template_path="dummy_sys",
        user_template_path="dummy_user",
        rulebook_path=str(rulebook_file),
    )

    with caplog.at_level(logging.INFO):
        content = builder.get_rulebook_content()
        assert content == rulebook_text
        assert expected_sha1 in caplog.text
