#!/bin/bash
# ===================================================================
# DataMate Challenge - Official Docker & CLI Entrypoint
# Zalo AI Challenge: Offline Vietnamese Tabular QA Agent
# ===================================================================
set -e

echo "=== [DATAMATE AGENT] Starting Inference Pipeline ==="

# Competition default paths
DATA_DIR="${DATA_DIR:-/data}"
QUESTIONS_PATH="${QUESTIONS_PATH:-/data/questions.jsonl}"
RULEBOOK_PATH="${RULEBOOK_PATH:-/data/rulebook.md}"
CALENDAR_PATH="${CALENDAR_PATH:-/data/calendar.csv}"

RESULT_DIR="${RESULT_DIR:-/result}"
SUBMISSION_PATH="${SUBMISSION_PATH:-/result/submission.jsonl}"
LOG_DIR="${LOG_DIR:-/result/logs}"

mkdir -p "${RESULT_DIR}"
mkdir -p "${LOG_DIR}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH}"

# In Docker competition mode, reads directly from /data
# If CLI arguments like --dataset or --drive_base_path are passed, python CLI handles dataset_loader auto-caching
python3 -m src.run_inference \
    --data_dir "${DATA_DIR}" \
    --questions "${QUESTIONS_PATH}" \
    --rulebook "${RULEBOOK_PATH}" \
    --calendar "${CALENDAR_PATH}" \
    --submission "${SUBMISSION_PATH}" \
    --log_dir "${LOG_DIR}" \
    --config "${SCRIPT_DIR}/configs/config.yaml" \
    "$@"

echo "=== [DATAMATE AGENT] Inference Completed Successfully! ==="
