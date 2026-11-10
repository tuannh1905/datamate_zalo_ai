"""
Main Inference Pipeline for DataMate Challenge.
Called by predict.sh inside the competition Docker container.
Groups questions by business_id for DuckDB view reuse and vLLM prefix caching,
runs n=8 parallel batch sampling, self-repairs errors, triggers +4 thinking samples
on agreement < 0.5, and outputs submission.jsonl in exact original question order.
"""

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional

import yaml

from .context.prompt_builder import PromptBuilder, build_chat_prompt
from .data_layer.dataset_loader import group_questions_by_business, load_questions
from .data_layer.debt_macros import register_debt_macros
from .data_layer.ingest import BusinessContext, load_business_data, resolve_business_dir
from .data_layer.view_builder import build_canonical_views
from .inference.executor_voter import CandidateExecution, ExecutorVoter, QuestionInferenceResult
from .inference.llm_engine import LLMEngine
from .inference.verifier import verify_candidate_execution

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
    k_override: Optional[int] = None,
    cache_dir: Optional[str] = None,
) -> None:
    # 1. Load Configuration & Resolve Model/Adapter Paths
    config = {}
    if config_path and os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

    inf_cfg = config.get("inference", {})
    exec_cfg = config.get("execution", {})

    k_samples = k_override if k_override is not None else inf_cfg.get("num_samples_k", 8)
    thinking_k = inf_cfg.get("num_thinking_samples", 4)
    tau = inf_cfg.get("agreement_threshold_tau", 0.5)
    sql_timeout = exec_cfg.get("sql_timeout_seconds", 5.0)

    logger.info(f"Inference Mode: k_samples={k_samples}, thinking_k={thinking_k}, tau={tau}, sql_timeout={sql_timeout}s")

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
            model_path = model_cfg.get("base_model_name_or_path", "Qwen/Qwen2.5-Coder-3B-Instruct")
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

    if adapter_path and not os.path.exists(adapter_path):
        if adapter_source in ["CLI override", "Env ADAPTER_DIR", "Config adapter_path"]:
            raise FileNotFoundError(
                f"[Configuration Error] Configured LoRA adapter path does not exist: '{adapter_path}' (Source: {adapter_source}). "
                "Failing fast to prevent running an unintended base model."
            )

    logger.info(f"Loaded Base Model : {model_path} (Source: {model_source})")
    logger.info(f"Loaded Adapter    : {adapter_path or 'None'} (Source: {adapter_source})")

    # 2. Setup Output Directories
    os.makedirs(os.path.dirname(os.path.abspath(submission_path)), exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    # 3. Initialize PromptBuilder and LLMEngine
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys_prompt_file = os.path.join(base_dir, "prompts", "sql_rules_system.txt")
    user_prompt_file = os.path.join(base_dir, "prompts", "qa_user_template.txt")

    logger.info("Initializing PromptBuilder with dynamic rulebook...")
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

    # 4. Load Questions preserving original order, then group by business_id
    original_questions = load_questions(questions_path, limit=limit)
    logger.info(f"Total questions loaded: {len(original_questions)}")
    biz_questions = group_questions_by_business(original_questions)
    logger.info(f"Grouped into {len(biz_questions)} distinct businesses for batch execution.")

    # 5. Process Businesses
    results_by_id: Dict[str, QuestionInferenceResult] = {}
    total_processed = 0
    total_abstain = 0
    start_total_time = time.time()

    for b_id, q_list in biz_questions.items():
        b_dir = resolve_business_dir(data_dir, b_id)
        if not b_dir:
            logger.warning(f"Business data directory for '{b_id}' not found under '{data_dir}'. Abstaining {len(q_list)} queries.")
            for q in q_list:
                q_id = q["id"]
                res = QuestionInferenceResult(
                    question_id=q_id,
                    business_id=b_id,
                    final_type="abstain",
                    final_answer=None,
                    confidence=0.0,
                    total_samples=0,
                    agreement_count=0,
                    elapsed_time=0.0,
                    reason=f"DATASET_NOT_FOUND: Business directory '{b_id}' could not be resolved under '{data_dir}'",
                )
                results_by_id[q_id] = res

                # Write individual log
                log_path = os.path.join(log_dir, f"{q_id}.json")
                log_data = res.to_log_dict()
                log_data.update({
                    "question": q.get("question", ""),
                    "as_of_date": q.get("as_of_date", ""),
                    "model_name": model_path,
                    "adapter_name": adapter_path or "None",
                })
                with open(log_path, "w", encoding="utf-8") as f_log:
                    json.dump(log_data, f_log, ensure_ascii=False, indent=2)

                total_abstain += 1
                total_processed += 1
            continue

        logger.info(f"--- Loading Business [{b_id}] ({len(q_list)} queries) ---")
        ctx = load_business_data(b_id, b_dir, cache_dir=cache_dir)

        # Build / retrieve canonical views and debt macros
        view_res = build_canonical_views(ctx, k=8)
        debt_status = register_debt_macros(ctx, plausibility_check=True)

        voter = ExecutorVoter(
            con=ctx.con,
            llm_engine=llm_engine,
            agreement_threshold_tau=tau,
            sql_timeout_seconds=sql_timeout,
            schema_summary=ctx.get_schema_summary(),
        )

        # Build Shop Static Prefix (100% shared across all questions of this shop)
        shop_prefix = prompt_builder.build_shop_static_prefix(
            ctx=ctx,
            canonical_sales_sql=view_res.v_sales_sql if view_res.success else None,
            canonical_orders_sql=view_res.v_orders_sql if view_res.success else None,
            canonical_purchases_sql=view_res.v_purchases_sql if view_res.success else None,
            has_debt_macros=debt_status.registered,
        )
        sys_prompt = prompt_builder.build_system_prompt(rulebook_path)

        for q in q_list:
            q_id = q["id"]
            q_text = q["question"]
            as_of_date = q["as_of_date"]
            q_start_time = time.time()

            # Dynamic question suffix
            q_suffix = prompt_builder.build_question_dynamic_suffix(q_text, as_of_date)
            user_prompt = shop_prefix + "\n\n" + q_suffix

            messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt},
            ]
            full_prompt = build_chat_prompt(
                tokenizer=llm_engine.tokenizer,
                messages=messages,
                prefill="Notes:\n-",
            )

            # Generate initial plain samples (k_samples, default 8) via single batch call
            initial_outputs = llm_engine.generate_samples(
                prompts=[full_prompt],
                n=k_samples,
                temperature=0.7 if k_samples > 1 else 0.0,
                max_tokens=512,
            )[0]

            candidates: List[CandidateExecution] = []
            for idx, comp in enumerate(initial_outputs):
                full_comp = comp if comp.startswith("Notes:\n-") else ("Notes:\n-" + comp)
                cand = voter.process_candidate(
                    sample_id=idx,
                    raw_completion=full_comp,
                    orig_question=q_text,
                    is_thinking=False,
                )
                candidates.append(cand)

            # Check intermediate top agreement
            valid_candidates = [c for c in candidates if c.success and c.vote_key is not None]
            group_counts = Counter((c.parsed_type, c.vote_key) for c in valid_candidates)
            top_count = group_counts.most_common(1)[0][1] if group_counts else 0
            initial_share = top_count / k_samples

            # Trigger +4 thinking samples if agreement < tau and thinking_k is configured
            if k_samples >= 4 and initial_share < tau and thinking_k > 0:
                logger.info(
                    f"Question [{q_id}]: Initial agreement {top_count}/{k_samples} ({initial_share:.2f}) < tau={tau}. "
                    f"Triggering +{thinking_k} thinking samples..."
                )
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
                    prefill="Notes:\n-",
                )
                thinking_outputs = llm_engine.generate_samples(
                    prompts=[thinking_prompt],
                    n=thinking_k,
                    temperature=0.6,
                    max_tokens=1024,
                )[0]

                for idx, comp in enumerate(thinking_outputs):
                    full_comp = comp if comp.startswith("Notes:\n-") else ("Notes:\n-" + comp)
                    cand = voter.process_candidate(
                        sample_id=k_samples + idx,
                        raw_completion=full_comp,
                        orig_question=q_text,
                        is_thinking=True,
                    )
                    candidates.append(cand)

            q_elapsed = time.time() - q_start_time

            # Majority Vote & Abstain Decision
            result = voter.vote_and_decide(
                question_id=q_id,
                business_id=b_id,
                candidates=candidates,
                elapsed=q_elapsed,
                denominator=len(candidates),
            )
            results_by_id[q_id] = result

            if result.final_type == "abstain":
                total_abstain += 1

            # Write individual log to /result/logs/<id>.json
            log_data = result.to_log_dict()
            log_data.update({
                "question": q_text,
                "as_of_date": as_of_date,
                "model_name": model_path,
                "adapter_name": adapter_path or "None",
                "resolved_business_dir": b_dir,
                "k_samples": k_samples,
                "tau": tau,
            })
            log_path = os.path.join(log_dir, f"{q_id}.json")
            with open(log_path, "w", encoding="utf-8") as f_log:
                json.dump(log_data, f_log, ensure_ascii=False, indent=2)

            total_processed += 1

    # 6. Write final submission.jsonl in EXACT original question order
    logger.info(f"Writing final submission.jsonl preserving original question order to: {submission_path}")
    with open(submission_path, "w", encoding="utf-8") as f_sub:
        for q in original_questions:
            qid = q["id"]
            if qid in results_by_id:
                sub_dict = results_by_id[qid].to_submission_dict()
            else:
                sub_dict = {"id": qid, "type": "abstain"}
            f_sub.write(json.dumps(sub_dict, ensure_ascii=False) + "\n")

    total_elapsed = time.time() - start_total_time
    logger.info(
        f"Inference Completed! Total Questions: {total_processed} | Abstains: {total_abstain} | "
        f"Total Time: {total_elapsed:.2f}s | Avg/Question: {total_elapsed / max(1, total_processed):.2f}s"
    )


def main():
    parser = argparse.ArgumentParser(description="Run DataMate Offline Inference Pipeline.")
    parser.add_argument("--list_datasets", action="store_true", help="List all datasets registered in configs/datasets.yaml")
    parser.add_argument("--dataset", default=None, help="Dataset split name: train, public_test, private_test, train_mini, etc.")
    parser.add_argument("--drive_base_path", default="/content/drive/MyDrive/ZaloAI_DataMate", help="Base directory on Google Drive or local filesystem")
    parser.add_argument("--local_cache_root", default="/content/local_data", help="Fast local NVMe cache directory on Colab")
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
    parser.add_argument("--k", type=int, default=None, help="Override k_samples")
    args = parser.parse_args()

    if args.list_datasets:
        from .data_layer.dataset_registry import list_datasets
        list_datasets()
        return

    data_dir = args.data_dir
    questions_path = args.questions
    rulebook_path = args.rulebook
    calendar_path = args.calendar

    if args.dataset:
        try:
            from .data_layer.dataset_registry import resolve_dataset
            dp = resolve_dataset(args.dataset)
        except Exception as e:
            logger.warning(f"Dataset registry fallback to dataset_loader for '{args.dataset}': {e}")
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
        k_override=args.k,
    )


if __name__ == "__main__":
    main()
