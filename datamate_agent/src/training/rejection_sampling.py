"""
Rejection Sampling Module for DataMate Challenge.
Scores candidate trajectories against `answers.jsonl` using `evaluator.py`,
filters out incorrect answers (-1) and errors,
keeps ONLY verified positive solutions (+1),
and formats them into SFT dataset for QLoRA training.
"""

import argparse
import json
import logging
import os
from typing import Any, Dict, List, Optional, Set

from ..evaluator import score_single_prediction

logger = logging.getLogger(__name__)


def run_rejection_sampling(
    candidates_path: str,
    answers_path: str,
    output_sft_path: str,
    teacher_fallback_hook: Optional[Any] = None,
    max_samples_per_question: int = 3,
) -> Dict[str, Any]:
    """
    Filters candidates: keeps only samples that achieve exact match score (+1).
    Outputs clean instruction fine-tuning dataset formatted for Unsloth / Hugging Face.
    """
    # 1. Load Gold Answers
    gold_dict: Dict[str, Dict[str, Any]] = {}
    with open(answers_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                item = json.loads(line)
                gold_dict[item["id"]] = item

    logger.info(f"Loaded {len(gold_dict)} reference answers from {answers_path}")

    # 2. Process Candidates
    total_questions = 0
    solved_questions = 0
    total_positive_trajectories = 0
    unsolved_questions = []

    os.makedirs(os.path.dirname(os.path.abspath(output_sft_path)), exist_ok=True)
    out_file = open(output_sft_path, "w", encoding="utf-8")

    with open(candidates_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cand_record = json.loads(line)
            total_questions += 1
            q_id = cand_record["id"]

            if q_id not in gold_dict:
                continue

            gold = gold_dict[q_id]
            samples = cand_record.get("samples", [])

            # Filter for successful samples matching gold answer
            accepted_samples = []
            seen_sql: Set[str] = set()

            for s in samples:
                if not s.get("success"):
                    continue

                pred = {
                    "id": q_id,
                    "type": s.get("parsed_type"),
                    "answer": s.get("normalized_value"),
                }

                score, status = score_single_prediction(pred, gold)
                if score == 1:
                    clean_sql = (s.get("parsed_sql") or "").strip()
                    if clean_sql not in seen_sql:
                        seen_sql.add(clean_sql)
                        accepted_samples.append(s)

            if accepted_samples:
                solved_questions += 1
                # Limit to top diverse accepted samples
                chosen_samples = accepted_samples[:max_samples_per_question]
                total_positive_trajectories += len(chosen_samples)

                for sample in chosen_samples:
                    sft_entry = {
                        "id": q_id,
                        "business_id": cand_record.get("business_id"),
                        "messages": [
                            {"role": "system", "content": cand_record["system_prompt"]},
                            {"role": "user", "content": cand_record["user_prompt"]},
                            {"role": "assistant", "content": sample["completion"]},
                        ],
                    }
                    out_file.write(json.dumps(sft_entry, ensure_ascii=False) + "\n")
            else:
                unsolved_questions.append(q_id)
                # Teacher / Self-distillation hook for hard questions
                if teacher_fallback_hook is not None:
                    teacher_solution = teacher_fallback_hook(cand_record, gold)
                    if teacher_solution:
                        sft_entry = {
                            "id": q_id,
                            "business_id": cand_record.get("business_id"),
                            "messages": [
                                {"role": "system", "content": cand_record["system_prompt"]},
                                {"role": "user", "content": cand_record["user_prompt"]},
                                {"role": "assistant", "content": teacher_solution},
                            ],
                        }
                        out_file.write(json.dumps(sft_entry, ensure_ascii=False) + "\n")
                        total_positive_trajectories += 1
                        solved_questions += 1

    out_file.close()

    solve_rate = (solved_questions / total_questions) * 100 if total_questions > 0 else 0.0
    stats = {
        "total_questions": total_questions,
        "solved_questions": solved_questions,
        "solve_rate_pct": round(solve_rate, 2),
        "total_positive_trajectories": total_positive_trajectories,
        "unsolved_count": len(unsolved_questions),
    }

    logger.info(f"Rejection Sampling Summary: {stats}")
    return stats


def main():
    parser = argparse.ArgumentParser(description="Perform rejection sampling on candidate generations.")
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl")
    parser.add_argument("--dataset", default=None, help="Dataset split name: train")
    parser.add_argument("--drive_base_path", default="/content/drive/MyDrive/ZaloAI_DataMate", help="Base directory on Google Drive or local filesystem")
    parser.add_argument("--answers", default=None, help="Path to gold answers.jsonl")
    parser.add_argument("--output", required=True, help="Path to output sft_dataset.jsonl")
    parser.add_argument("--max_per_q", type=int, default=3, help="Max accepted samples per question")
    args = parser.parse_args()

    answers_path = args.answers
    if args.dataset and not answers_path:
        from ..data_layer.dataset_loader import load_dataset
        dp = load_dataset(dataset=args.dataset, drive_base_path=args.drive_base_path)
        answers_path = dp.answers_path

    if not answers_path:
        parser.error("Must provide either --answers or --dataset")

    run_rejection_sampling(
        candidates_path=args.candidates,
        answers_path=answers_path,
        output_sft_path=args.output,
        max_samples_per_question=args.max_per_q,
    )


if __name__ == "__main__":
    main()
