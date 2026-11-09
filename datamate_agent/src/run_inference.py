"""
Main Inference Pipeline for DataMate Challenge.
Called by predict.sh inside the competition Docker container.
Ingests business data, generates k=8 SQL samples, handles self-repair and +4 thinking samples,
performs majority voting with tau=0.5 abstain threshold,
and writes `/result/submission.jsonl` and `/result/logs/<id>.json`.
"""

import argparse
import json
import logging
import os
import sys
import time
from collections import defaultdict
from typing import Any, Dict, List, Optional

import yaml
from tqdm import tqdm

from .context.prompt_builder import PromptBuilder, build_chat_prompt
from .data_layer.debt_macros import register_debt_macros
from .data_layer.ingest import BusinessContext, load_business_data, resolve_business_dir
from .data_layer.view_builder import build_canonical_views
from .inference.executor_voter import CandidateExecution, ExecutorVoter, QuestionInferenceResult
from .inference.llm_engine import LLMEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DataMateRunner")


def run_inference_pipeline(
    data_dir: str,
    questions_path: str,
    rulebook_path: str,
    calendar_path: str,
    submission_path: str,
    log_dir: str,
    config_path: Optional[str] = None,
    model_override: Optional[str] = None,
    adapter_override: Optional[str] = None,
    limit: Optional[int] = None,
    allow_mock: bool = False,
) -> None:
    # 1. Load Configuration
    # 1. Load Configuration & Resolve Model/Adapter Paths
    config = {}
    if config_path and os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

    inf_cfg = config.get("inference", {})
    k_samples = inf_cfg.get("num_samples_k", 8)
    thinking_k = inf_cfg.get("num_thinking_samples", 4)
    tau = inf_cfg.get("agreement_threshold_tau", 0.5)

    # Resolution priority: CLI override > Env var > paths.*_dir on disk > config.model
    paths_cfg = config.get("paths", {})
    model_cfg = config.get("model", {})

    model_source = "CLI override"
    model_path = model_override
    if not model_path:
        if os.environ.get("MODEL_DIR") and os.path.exists(os.environ["MODEL_DIR"]):
            model_path = os.environ["MODEL_DIR"]
            model_source = "Env MODEL_DIR"
        elif paths_cfg.get("model_dir") and os.path.exists(paths_cfg["model_dir"]):
            model_path = paths_cfg["model_dir"]
            model_source = f"Local paths.model_dir ({model_path})"
        else:
            model_path = model_cfg.get("base_model_name_or_path", "Qwen/Qwen2.5-Coder-7B-Instruct")
            model_source = "Config base_model_name_or_path"

    adapter_source = "CLI override"
    adapter_path = adapter_override
    if not adapter_path:
        if os.environ.get("ADAPTER_DIR") and os.path.exists(os.environ["ADAPTER_DIR"]):
            adapter_path = os.environ["ADAPTER_DIR"]
            adapter_source = "Env ADAPTER_DIR"
        elif paths_cfg.get("adapter_dir") and os.path.exists(paths_cfg["adapter_dir"]):
            adapter_path = paths_cfg["adapter_dir"]
            adapter_source = f"Local paths.adapter_dir ({adapter_path})"
        else:
            adapter_path = model_cfg.get("adapter_path", None)
            adapter_source = "Config adapter_path"

    logger.info(f"Loaded Base Model : {model_path} (Source: {model_source})")
    logger.info(f"Loaded Adapter    : {adapter_path or 'None'} (Source: {adapter_source})")

    # 2. Setup Output Directories
    os.makedirs(os.path.dirname(os.path.abspath(submission_path)), exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    # 3. Initialize Engine and PromptBuilder
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys_prompt_file = os.path.join(base_dir, "prompts", "sql_rules_system.txt")
    user_prompt_file = os.path.join(base_dir, "prompts", "qa_user_template.txt")

    logger.info("Initializing PromptBuilder with dynamic rulebook...")
    if rulebook_path and os.path.exists(rulebook_path):
        import hashlib
        with open(rulebook_path, "rb") as f:
            rb_sha1 = hashlib.sha1(f.read()).hexdigest()
        logger.info(f"Active Split Rulebook: '{rulebook_path}' (SHA1: {rb_sha1})")

    prompt_builder = PromptBuilder(
        system_template_path=sys_prompt_file,
        user_template_path=user_prompt_file,
        rulebook_path=rulebook_path,
        calendar_path=calendar_path,
    )

    llm_engine = LLMEngine(
        model_name_or_path=model_path,
        adapter_path=adapter_path,
        allow_mock=allow_mock,
    )

    # 4. Load Questions and Group by Business
    questions: List[Dict[str, Any]] = []
    with open(questions_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                questions.append(json.loads(line))

    if limit:
        questions = questions[:limit]

    logger.info(f"Total questions to process: {len(questions)}")
    biz_questions = defaultdict(list)
    for q in questions:
        biz_questions[q["business_id"]].append(q)

    # 5. Execute Per-Business Batch Processing
    submission_file = open(submission_path, "w", encoding="utf-8")
    total_processed = 0
    total_abstain = 0
    start_total_time = time.time()

    for b_id, q_list in biz_questions.items():
        b_dir = resolve_business_dir(data_dir, b_id)
        if not b_dir:
            logger.warning(f"Business data directory for '{b_id}' not found under '{data_dir}'. Abstaining {len(q_list)} queries.")
            for q in q_list:
                q_id = q["id"]
                sub_dict = {"id": q_id, "type": "abstain"}
                submission_file.write(json.dumps(sub_dict, ensure_ascii=False) + "\n")
                submission_file.flush()

                log_path = os.path.join(log_dir, f"{q_id}.json")
                log_data = {
                    "id": q_id,
                    "business_id": b_id,
                    "final_type": "abstain",
                    "final_answer": None,
                    "elapsed_seconds": 0.0,
                    "abstain_reason": f"Business directory '{b_id}' could not be resolved under '{data_dir}'",
                    "candidates": [],
                }
                with open(log_path, "w", encoding="utf-8") as f_log:
                    json.dump(log_data, f_log, ensure_ascii=False, indent=2)

                total_abstain += 1
                total_processed += 1
            continue

        logger.info(f"--- Loading Business [{b_id}] ({len(q_list)} queries) ---")
        ctx = load_business_data(b_id, b_dir)

        # Build canonical views & macros
        view_res = build_canonical_views(ctx, k=8)
        debt_status = register_debt_macros(ctx, plausibility_check=True)

        voter = ExecutorVoter(
            con=ctx.con,
            llm_engine=llm_engine,
            agreement_threshold_tau=tau,
            schema_summary=ctx.get_schema_summary(),
        )

        for q in q_list:
            q_id = q["id"]
            q_text = q["question"]
            as_of_date = q["as_of_date"]
            q_start_time = time.time()

            # Assemble prompt
            messages = prompt_builder.build_messages(
                question=q_text,
                as_of_date=as_of_date,
                ctx=ctx,
                canonical_sales_sql=view_res.v_sales_sql if view_res.success else None,
                canonical_orders_sql=view_res.v_orders_sql if view_res.success else None,
                has_debt_macros=debt_status.registered,
                runtime_rulebook_path=rulebook_path,
            )

            # Assemble standardized chat prompt with prefill
            full_prompt = build_chat_prompt(
                tokenizer=llm_engine.tokenizer,
                messages=messages,
                prefill="Notes:\n-",
            )

            # Generate initial k=8 plain samples
            plain_outputs = llm_engine.generate_single(
                prompt=full_prompt,
                n=k_samples,
                temperature=0.1,
                max_new_tokens=1024,
            )

            candidates: List[CandidateExecution] = []
            for idx, comp in enumerate(plain_outputs):
                full_text = "Notes:\n-" + comp
                cand = voter.process_candidate(
                    sample_id=idx,
                    raw_completion=full_text,
                    orig_question=q_text,
                )
                candidates.append(cand)

            # Check intermediate agreement
            valid_keys = [c.vote_key for c in candidates if c.success and c.vote_key]
            from collections import Counter
            top_share = (Counter(valid_keys).most_common(1)[0][1] / len(candidates)) if valid_keys else 0.0

            # If low agreement, trigger +4 thinking samples
            if top_share < tau and thinking_k > 0:
                logger.debug(f"Question {q_id}: Agreement {top_share:.2f} < tau={tau}. Triggering +{thinking_k} thinking samples.")
                thinking_outputs = llm_engine.generate_single(
                    prompt=full_prompt,
                    n=thinking_k,
                    temperature=0.6,
                    max_new_tokens=2048,
                )
                for idx, comp in enumerate(thinking_outputs):
                    full_text = "Notes:\n-" + comp
                    cand = voter.process_candidate(
                        sample_id=k_samples + idx,
                        raw_completion=full_text,
                        orig_question=q_text,
                    )
                    candidates.append(cand)

            q_elapsed = time.time() - q_start_time

            # Majority Vote & Abstain Decision
            result = voter.vote_and_decide(
                question_id=q_id,
                business_id=b_id,
                candidates=candidates,
                elapsed=q_elapsed,
            )

            if result.final_type == "abstain":
                total_abstain += 1

            # Write submission entry
            sub_dict = result.to_submission_dict()
            submission_file.write(json.dumps(sub_dict, ensure_ascii=False) + "\n")
            submission_file.flush()

            # Write per-question log to /result/logs/<id>.json
            log_path = os.path.join(log_dir, f"{q_id}.json")
            with open(log_path, "w", encoding="utf-8") as f_log:
                json.dump(result.to_log_dict(), f_log, ensure_ascii=False, indent=2)

            total_processed += 1

    submission_file.close()
    total_elapsed = time.time() - start_total_time
    logger.info(
        f"Inference Completed! Total Questions: {total_processed} | Abstains: {total_abstain} | "
        f"Total Time: {total_elapsed:.2f}s | Avg/Question: {total_elapsed / max(1, total_processed):.2f}s"
    )


def main():
    parser = argparse.ArgumentParser(description="Run DataMate Offline Inference Pipeline.")
    parser.add_argument("--list_datasets", action="store_true", help="List all datasets registered in configs/datasets.yaml")
    # Dataset routing & Drive caching parameters
    parser.add_argument("--dataset", default=None, help="Dataset split name: train, public_test, private_test, train_mini, etc.")
    parser.add_argument("--drive_base_path", default="/content/drive/MyDrive/ZaloAI_DataMate", help="Base directory on Google Drive or local filesystem")
    parser.add_argument("--local_cache_root", default="/content/local_data", help="Fast local NVMe cache directory on Colab")
    
    # Direct path options (Docker environment defaults to /data)
    parser.add_argument("--data_dir", default="/data", help="Path to data directory")
    parser.add_argument("--questions", default="/data/questions.jsonl", help="Path to questions.jsonl")
    parser.add_argument("--rulebook", default="/data/rulebook.md", help="Path to rulebook.md")
    parser.add_argument("--calendar", default="/data/calendar.csv", help="Path to calendar.csv")
    parser.add_argument("--submission", default="/result/submission.jsonl", help="Path to output submission.jsonl")
    parser.add_argument("--log_dir", default="/result/logs", help="Path to logs directory")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--model", default=None, help="Model name or path override")
    parser.add_argument("--adapter", default=None, help="Adapter path override")
    parser.add_argument("--limit", type=int, default=None, help="Limit questions for quick testing")
    parser.add_argument("--allow_mock", action="store_true", help="Allow fallback mock LLM mode for testing/CI")
    args = parser.parse_args()

    if args.list_datasets:
        from .data_layer.dataset_registry import list_datasets
        list_datasets()
        return

    data_dir = args.data_dir
    questions_path = args.questions
    rulebook_path = args.rulebook
    calendar_path = args.calendar

    # If --dataset is specified, route through dataset_registry (or dataset_loader fallback)
    if args.dataset:
        try:
            from .data_layer.dataset_registry import resolve_dataset
            dp = resolve_dataset(args.dataset)
        except Exception as e:
            logger.warning(f"Dataset registry could not resolve '{args.dataset}' ({e}). Falling back to dataset_loader...")
            from .data_layer.dataset_loader import load_dataset
            dp = load_dataset(
                dataset=args.dataset,
                drive_base_path=args.drive_base_path,
                local_cache_root=args.local_cache_root,
            )
        data_dir = dp.data_dir
        questions_path = dp.questions_path
        rulebook_path = dp.rulebook_path
        calendar_path = dp.calendar_path

    run_inference_pipeline(
        data_dir=data_dir,
        questions_path=questions_path,
        rulebook_path=rulebook_path,
        calendar_path=calendar_path,
        submission_path=args.submission,
        log_dir=args.log_dir,
        config_path=args.config,
        model_override=args.model,
        adapter_override=args.adapter,
        limit=args.limit,
        allow_mock=args.allow_mock,
    )


if __name__ == "__main__":
    main()
