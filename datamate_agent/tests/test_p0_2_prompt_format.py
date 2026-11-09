import os
from src.context.prompt_builder import build_chat_prompt, PromptBuilder


def test_qa_template_no_duplicate_assistant():
    template_path = os.path.join(os.path.dirname(__file__), "../prompts/qa_user_template.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Ensure template does not end with Assistant:\nNotes:\n-
    assert "Assistant:\nNotes:" not in content
    assert content.strip().endswith("Please write your reasoning in Notes, then output the target TYPE and the DuckDB SQL query.")


def test_build_chat_prompt_chatml():
    messages = [
        {"role": "system", "content": "You are a database assistant."},
        {"role": "user", "content": "Calculate total revenue."},
    ]
    prompt = build_chat_prompt(tokenizer=None, messages=messages, prefill="Notes:\n-")
    
    # Verify structure
    assert "<|im_start|>system\nYou are a database assistant.<|im_end|>" in prompt
    assert "<|im_start|>user\nCalculate total revenue.<|im_end|>" in prompt
    assert prompt.endswith("<|im_start|>assistant\nNotes:\n-")
    
    # Count occurrences of "assistant" / "Notes:" to ensure no duplication
    assert prompt.count("<|im_start|>assistant") == 1
    assert prompt.count("Notes:\n-") == 1


def test_sft_sample_alignment():
    # Simulate SFT entry assembly
    system_content = "You are a database assistant."
    user_content = "Calculate total revenue."
    assistant_completion = "Notes:\n- We sum amounts.\nTYPE: number\n```sql\nSELECT 1;\n```"

    sft_messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": assistant_completion},
    ]

    # In SFT training, apply_chat_template without add_generation_prompt
    parts = []
    for m in sft_messages:
        parts.append(f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>")
    full_sft_text = "\n".join(parts)

    response_part = "<|im_start|>assistant\n"
    assert response_part in full_sft_text
    # The text following response_part should start with Notes:\n-
    after_resp = full_sft_text.split(response_part)[1]
    assert after_resp.startswith("Notes:\n-")
