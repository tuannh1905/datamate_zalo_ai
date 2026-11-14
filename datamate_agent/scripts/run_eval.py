"""
Local Validation and Scoring Script for DataMate Challenge.
Supports dataset routing and Google Drive auto-caching via dataset_loader.
Example Colab CLI:
    python scripts/run_eval.py --dataset train --drive_base_path /content/drive/MyDrive/DataMate
"""

import argparse
import json
import logging
import os
import sys

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data_layer.dataset_loader import load_dataset
from src.evaluator import evaluate_predictions
from src.run_inference import run_inference_pipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DataMateEval")


def main():
    parser = argparse.ArgumentParser(description="Evaluate DataMate pipeline with dataset routing and auto-caching.")
    
    # Dataset routing arguments
    parser.add_argument("--list_datasets", action="store_true", help="List all datasets registered in configs/datasets.yaml")
    parser.add_argument("--dataset", default=None, help="Dataset split name: train, public_test, private_test, train_mini, etc.")
    parser.add_argument("--drive_base_path", default="/content/drive/MyDrive/ZaloAI_DataMate", help="Base directory on Google Drive or local filesystem")
    parser.add_argument("--local_cache_root", default="/content/local_data", help="Fast local NVMe cache directory on Colab")
    
    # Direct path overrides (optional)
    parser.add_argument("--submission", default=None, help="Path to submission.jsonl (defaults to ./result/submission.jsonl)")
    parser.add_argument("--answers", default=None, help="Explicit path to answers.jsonl (defaults to dataset answers.jsonl)")
    
    # Inference execution options
    parser.add_argument("--run_inference", action="store_true", help="Force running inference before evaluation")
    parser.add_argument("--allow_mock", action="store_true", help="Allow fallback mock mode for testing/CI without GPU")
    parser.add_argument("--model", default=None, help="Model name or path override")
    parser.add_argument("--adapter", default=None, help="Adapter path override")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions for quick testing")
    parser.add_argument("--k", type=int, default=None, help="Number of samples per question (defaults to config: 1)")
    parser.add_argument("--verbose", action="store_true", help="Print details on incorrect answers")
    
    args = parser.parse_args()

    # Resolve default config path if not provided
    default_cfg = os.path.abspath(os.path.join(os.path.dirname(__file__), "../configs/config.yaml"))
    config_path = args.config or (default_cfg if os.path.exists(default_cfg) else None)

    if args.list_datasets:
        from src.data_layer.dataset_registry import list_datasets
        list_datasets()
        return

    # Determine submission path
    submission_path = args.submission or os.path.abspath(os.path.join(os.path.dirname(__file__), "../result/submission.jsonl"))
    log_dir = os.path.abspath(os.path.join(os.path.dirname(submission_path), "logs"))

    answers_path = args.answers

    # If --dataset is specified, route through dataset_registry (fallback to dataset_loader)
    if args.dataset:
        try:
            from src.data_layer.dataset_registry import resolve_dataset
            dataset_paths = resolve_dataset(args.dataset)
        except Exception as e:
            logger.warning(f"Dataset registry fallback to dataset_loader for '{args.dataset}': {e}")
            dataset_paths = load_dataset(
                dataset=args.dataset,
                drive_base_path=args.drive_base_path,
                local_cache_root=args.local_cache_root,
            )
        
        if not answers_path:
            answers_path = dataset_paths.answers_path

        # If submission file doesn't exist or --run_inference is requested, run inference
        if args.run_inference or not os.path.exists(submission_path):
            logger.info(f"Generating predictions for dataset [{args.dataset}]...")
            run_inference_pipeline(
                data_dir=dataset_paths.data_dir,
                questions_path=dataset_paths.questions_path,
                rulebook_path=dataset_paths.rulebook_path,
                calendar_path=dataset_paths.calendar_path,
                submission_path=submission_path,
                log_dir=log_dir,
                config_path=config_path,
                model_override=args.model,
                adapter_override=args.adapter,
                limit=args.limit,
                allow_mock=args.allow_mock,
                k_override=args.k,
            )

    if not os.path.exists(submission_path):
        logger.error(f"Submission file not found at: {submission_path}. Use --run_inference to generate it.")
        sys.exit(1)

    if not answers_path or not os.path.exists(answers_path):
        logger.warning(f"No gold answers.jsonl found for evaluation (answers_path: {answers_path}).")
        logger.info(f"Predictions successfully generated and written to: {submission_path}")
        return

    # Load predictions
    predictions = []
    with open(submission_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                predictions.append(json.loads(line))

    # Load gold answers
    gold_dict = {}
    with open(answers_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                item = json.loads(line)
                gold_dict[item["id"]] = item

    # P0-11: When evaluating a subset (via --limit or partial predictions), filter gold_dict by evaluated IDs
    pred_ids = {p["id"] for p in predictions if "id" in p}
    if args.limit or len(pred_ids) < len(gold_dict):
        filtered_gold = {qid: gold for qid, gold in gold_dict.items() if qid in pred_ids}
        if filtered_gold:
            logger.info(f"P0-11: Evaluating {len(filtered_gold)} questions (filtered from total {len(gold_dict)} gold references).")
            gold_dict = filtered_gold

    results = evaluate_predictions(predictions, gold_dict)

    print("\n" + "=" * 60)
    print("           DATAMATE CHALLENGE - EVALUATION REPORT")
    print("=" * 60)
    print(f" Dataset Split              : {args.dataset or 'Custom'}")
    print(f" Submission File            : {submission_path}")
    print(f" Total Reference Questions  : {results['total']}")
    print(f" Correct Answers (+1)       : {results['correct']} ({results['correct'] / results['total'] * 100:.2f}%)")
    print(f" Wrong Answers (-1)         : {results['wrong']} ({results['wrong'] / results['total'] * 100:.2f}%)")
    print(f" Abstains (0)               : {results['abstain']} ({results['abstain'] / results['total'] * 100:.2f}%)")
    print(f" Answered Accuracy          : {results['accuracy'] * 100:.2f}%")
    print("-" * 60)
    print(f" Penalized Accuracy (PA)    : {results['penalized_accuracy']:+.4f}")
    print("=" * 60 + "\n")

    if args.verbose:
        pred_map = {p["id"]: p for p in predictions}
        print("Incorrect predictions breakdown:")
        for d in results.get("details", []):
            if d["score"] == -1:
                qid = d["id"]
                p = pred_map.get(qid, {})
                g = gold_dict.get(qid, {})
                print(f" [WRONG] ID: {qid} | Pred Type: {p.get('type')} | Pred Ans: {p.get('answer')} | Gold Type: {g.get('type')} | Gold Ans: {g.get('answer')}")


if __name__ == "__main__":
    main()
