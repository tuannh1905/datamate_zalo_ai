"""
Candidate Generation Module for DataMate Challenge.
Generates 8 plain + 4 thinking samples per training question using the Student model,
groups by business_id for DuckDB view reuse and prefix caching,
executes them in DuckDB with self-repair, preserves original question order in candidates.jsonl,
and explicitly releases GPU memory and shuts down Ray.
"""

import argparse
import gc
import json
import logging
import os
import time
from typing import Any, Dict, List, Optional

import torch
from tqdm import tqdm

from ..context.prompt_builder import PromptBuilder, build_chat_prompt
from ..data_layer.dataset_loader import group_questions_by_business, load_questions
from ..data_layer.ingest import BusinessContext, load_business_data, resolve_business_dir
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
    allow_mock: bool = False,
) -> None:
    """
    Runs Student model to generate candidate reasoning + SQL solutions for training questions.
    Groups questions by business_id for shop static prefix caching and DuckDB view reuse,
    while writing candidates in original questions order.
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
        allow_mock=allow_mock,
    )

    # Load questions preserving original order
    original_questions = load_questions(questions_path, limit=limit)
    logger.info(f"Loaded {len(original_questions)} questions. Output will be saved to {output_path}")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Group by business_id for shop-centric batching
    biz_groups = group_questions_by_business(original_questions)
    records_by_id: Dict[str, Dict[str, Any]] = {}

    sys_prompt = prompt_builder.build_system_prompt(rulebook_path)

    for b_id, q_list in tqdm(biz_groups.items(), desc="Processing Businesses"):
        b_dir = resolve_business_dir(data_dir, b_id)
        if not b_dir:
            logger.warning(f"Business data directory for '{b_id}' not found under '{data_dir}'. Skipping.")
            continue

        ctx = load_business_data(b_id, b_dir)
        shop_prefix = prompt_builder.build_shop_static_prefix(ctx=ctx)

        voter = ExecutorVoter(
            con=ctx.con,
            llm_engine=llm_engine,
            schema_summary=ctx.get_schema_summary(),
            ctx=ctx,
        )

        for q in q_list:
            q_id = q["id"]
            question_text = q["question"]
            as_of_date = q["as_of_date"]

            q_suffix = prompt_builder.build_question_dynamic_suffix(question_text, as_of_date)
            user_prompt = shop_prefix + "\n\n" + q_suffix

            messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt},
            ]
            full_prompt = build_chat_prompt(
                tokenizer=llm_engine.tokenizer,
                messages=messages,
                prefill="TYPE: ",
            )

            # 1. Generate plain samples in single batch forward pass
            plain_completions = llm_engine.generate_samples(
                prompts=[full_prompt],
                n=num_plain_samples,
                temperature=0.7,
                max_tokens=512,
            )[0]

            # 2. Generate thinking samples in single batch forward pass
            thinking_user_prompt = (
                user_prompt
                + "\n\nThinking Step-by-Step Instructions: Carefully verify all filters, date windows, join conditions, and calculations before outputting TYPE and SQL."
            )
            thinking_messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": thinking_user_prompt},
            ]
            thinking_prompt = build_chat_prompt(
                tokenizer=llm_engine.tokenizer,
                messages=thinking_messages,
                prefill="TYPE: ",
            )
            thinking_completions = llm_engine.generate_samples(
                prompts=[thinking_prompt],
                n=num_thinking_samples,
                temperature=0.6,
                max_tokens=1024,
            )[0]

            sample_records = []

            for idx, comp in enumerate(plain_completions):
                full_text = comp if comp.strip().startswith("TYPE:") else ("TYPE: " + comp.strip())
                cand = voter.process_candidate(
                    sample_id=idx,
                    raw_completion=full_text,
                    orig_question=question_text,
                    is_thinking=False,
                )
                sample_records.append({
                    "sample_id": idx,
                    "is_thinking": False,
                    "completion": full_text,
                    "parsed_type": cand.parsed_type,
                    "parsed_sql": cand.parsed_sql,
                    "success": cand.success,
                    "normalized_value": cand.normalized_value,
                    "vote_key": cand.vote_key,
                    "error": cand.error,
                    "repair_turns": cand.repair_turns,
                })

            for idx, comp in enumerate(thinking_completions):
                full_text = comp if comp.strip().startswith("TYPE:") else ("TYPE: " + comp.strip())
                cand = voter.process_candidate(
                    sample_id=num_plain_samples + idx,
                    raw_completion=full_text,
                    orig_question=question_text,
                    is_thinking=True,
                )
                sample_records.append({
                    "sample_id": num_plain_samples + idx,
                    "is_thinking": True,
                    "completion": full_text,
                    "parsed_type": cand.parsed_type,
                    "parsed_sql": cand.parsed_sql,
                    "success": cand.success,
                    "normalized_value": cand.normalized_value,
                    "vote_key": cand.vote_key,
                    "error": cand.error,
                    "repair_turns": cand.repair_turns,
                })

            records_by_id[q_id] = {
                "id": q_id,
                "business_id": b_id,
                "question": question_text,
                "as_of_date": as_of_date,
                "system_prompt": sys_prompt,
                "user_prompt": user_prompt,
                "samples": sample_records,
            }

    # Write output file in EXACT original question order
    with open(output_path, "w", encoding="utf-8") as out_file:
        for q in original_questions:
            qid = q["id"]
            if qid in records_by_id:
                out_file.write(json.dumps(records_by_id[qid], ensure_ascii=False) + "\n")

    logger.info(f"Finished generating candidates. Saved to {output_path}")

    # Subprocess isolation & memory cleanup
    logger.info("Cleaning up GPU memory and Ray processes...")
    del llm_engine
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    try:
        import ray
        if ray.is_initialized():
            ray.shutdown()
            logger.info("Ray shutdown successfully.")
    except Exception:
        pass


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
    parser.add_argument("--model", default="Qwen/Qwen2.5-Coder-3B-Instruct", help="Model name or path")
    parser.add_argument("--adapter", default=None, help="LoRA adapter path")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions")
    parser.add_argument("--allow_mock", action="store_true", help="Allow fallback mock mode")
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
        allow_mock=args.allow_mock,
    )


if __name__ == "__main__":
    main()
