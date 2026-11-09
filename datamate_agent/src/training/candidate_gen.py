"""
Candidate Generation Module for DataMate Challenge.
Generates 8 plain + 4 thinking samples per training question using the Student model,
executes them in DuckDB, and saves full trajectories to candidates.jsonl.
"""

import argparse
import json
import logging
import os
import time
from typing import Any, Dict, List, Optional

from tqdm import tqdm

from ..context.prompt_builder import PromptBuilder, build_chat_prompt
from ..data_layer.debt_macros import register_debt_macros
from ..data_layer.ingest import BusinessContext, load_business_data
from ..data_layer.view_builder import build_canonical_views
from ..inference.executor_voter import CandidateExecution, ExecutorVoter
from ..inference.llm_engine import LLMEngine

logger = logging.getLogger(__name__)


def generate_training_candidates(
    questions_path: str,
    data_dir: str,
    rulebook_path: str,
    calendar_path: str,
    output_path: str,
    model_name_or_path: str,
    adapter_path: Optional[str] = None,
    num_plain_samples: int = 8,
    num_thinking_samples: int = 4,
    limit: Optional[int] = None,
) -> None:
    """
    Runs Student model to generate candidate reasoning + SQL solutions for training questions.
    """
    logger.info("Initializing PromptBuilder and LLMEngine...")
    prompt_builder = PromptBuilder(
        system_template_path=os.path.join(os.path.dirname(__file__), "../../prompts/sql_rules_system.txt"),
        user_template_path=os.path.join(os.path.dirname(__file__), "../../prompts/qa_user_template.txt"),
        rulebook_path=rulebook_path,
        calendar_path=calendar_path,
    )

    llm_engine = LLMEngine(
        model_name_or_path=model_name_or_path,
        adapter_path=adapter_path,
    )

    # Load questions
    questions = []
    with open(questions_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                questions.append(json.loads(line))

    if limit:
        questions = questions[:limit]

    logger.info(f"Loaded {len(questions)} questions. Output will be saved to {output_path}")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Cache business contexts to avoid repeated disk reads
    biz_cache: Dict[str, BusinessContext] = {}

    out_file = open(output_path, "w", encoding="utf-8")

    for q in tqdm(questions, desc="Generating Candidates"):
        q_id = q["id"]
        b_id = q["business_id"]
        question_text = q["question"]
        as_of_date = q["as_of_date"]

        # Load business context
        if b_id not in biz_cache:
            b_dir = os.path.join(data_dir, b_id)
            ctx = load_business_data(b_id, b_dir)
            view_res = build_canonical_views(ctx, k=8)
            debt_status = register_debt_macros(ctx, plausibility_check=True)
            biz_cache[b_id] = (ctx, view_res, debt_status)
        else:
            ctx, view_res, debt_status = biz_cache[b_id]

        # Build prompt
        messages = prompt_builder.build_messages(
            question=question_text,
            as_of_date=as_of_date,
            ctx=ctx,
            canonical_sales_sql=view_res.v_sales_sql if view_res.success else None,
            canonical_orders_sql=view_res.v_orders_sql if view_res.success else None,
            has_debt_macros=debt_status.registered,
            runtime_rulebook_path=rulebook_path,
        )

        user_content = messages[1]["content"]
        full_prompt = build_chat_prompt(
            tokenizer=llm_engine.tokenizer,
            messages=messages,
            prefill="Notes:\n-",
        )

        # 1. Generate 8 plain samples (temp 0.1)
        plain_completions = llm_engine.generate_single(
            prompt=full_prompt,
            n=num_plain_samples,
            temperature=0.1,
            max_new_tokens=1024,
        )

        # 2. Generate 4 thinking samples (temp 0.6, max_tokens 2048)
        thinking_completions = llm_engine.generate_single(
            prompt=full_prompt,
            n=num_thinking_samples,
            temperature=0.6,
            max_new_tokens=2048,
        )

        all_completions = plain_completions + thinking_completions

        # Execute and validate each completion
        voter = ExecutorVoter(ctx.con, llm_engine)
        sample_records = []

        for idx, comp in enumerate(all_completions):
            full_text = "Notes:\n-" + comp
            cand = voter.process_candidate(
                sample_id=idx,
                raw_completion=full_text,
                orig_question=question_text,
            )
            sample_records.append({
                "sample_id": idx,
                "is_thinking": (idx >= num_plain_samples),
                "completion": full_text,
                "parsed_type": cand.parsed_type,
                "parsed_sql": cand.parsed_sql,
                "success": cand.success,
                "normalized_value": cand.normalized_value,
                "vote_key": cand.vote_key,
                "error": cand.error,
                "repair_turns": cand.repair_turns,
            })

        record = {
            "id": q_id,
            "business_id": b_id,
            "question": question_text,
            "as_of_date": as_of_date,
            "system_prompt": messages[0]["content"],
            "user_prompt": user_content,
            "samples": sample_records,
        }
        out_file.write(json.dumps(record, ensure_ascii=False) + "\n")
        out_file.flush()

    out_file.close()
    logger.info(f"Finished generating candidates. Saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate SQL candidates for self-training.")
    parser.add_argument("--dataset", default=None, help="Dataset split name: train")
    parser.add_argument("--drive_base_path", default="/content/drive/MyDrive/ZaloAI_DataMate", help="Base directory on Google Drive or local filesystem")
    parser.add_argument("--local_cache_root", default="/content/local_data", help="Fast local NVMe cache directory on Colab")
    parser.add_argument("--questions", default=None, help="Path to questions.jsonl")
    parser.add_argument("--data_dir", default=None, help="Path to data directory")
    parser.add_argument("--rulebook", default=None, help="Path to rulebook.md")
    parser.add_argument("--calendar", default=None, help="Path to calendar.csv")
    parser.add_argument("--output", required=True, help="Path to output candidates.jsonl")
    parser.add_argument("--model", default="Qwen/Qwen2.5-Coder-7B-Instruct", help="Model name or path")
    parser.add_argument("--adapter", default=None, help="LoRA adapter path")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions")
    args = parser.parse_args()

    questions_path = args.questions
    data_dir = args.data_dir
    rulebook_path = args.rulebook
    calendar_path = args.calendar

    if args.dataset:
        from ..data_layer.dataset_loader import load_dataset
        dp = load_dataset(
            dataset=args.dataset,
            drive_base_path=args.drive_base_path,
            local_cache_root=args.local_cache_root,
        )
        questions_path = questions_path or dp.questions_path
        data_dir = data_dir or dp.data_dir
        rulebook_path = rulebook_path or dp.rulebook_path
        calendar_path = calendar_path or dp.calendar_path

    if not questions_path or not data_dir or not rulebook_path or not calendar_path:
        parser.error("Must provide either --dataset or all of (--questions, --data_dir, --rulebook, --calendar)")

    generate_training_candidates(
        questions_path=questions_path,
        data_dir=data_dir,
        rulebook_path=rulebook_path,
        calendar_path=calendar_path,
        output_path=args.output,
        model_name_or_path=args.model,
        adapter_path=args.adapter,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()
