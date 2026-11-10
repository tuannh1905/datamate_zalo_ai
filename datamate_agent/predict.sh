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

# Auto-detect data root if /data has a single child directory containing questions.jsonl
if [ -d "/data" ]; then
    if [ ! -f "${QUESTIONS_PATH}" ]; then
        CANDIDATE=$(find /data -maxdepth 2 -name "questions.jsonl" 2>/dev/null | head -n 1)
        if [ -n "${CANDIDATE}" ]; then
            SPLIT_ROOT="$(dirname "${CANDIDATE}")"
            echo "[predict.sh] Auto-detected split root: ${SPLIT_ROOT}"
            DATA_DIR="${SPLIT_ROOT}/data"
            [ ! -d "${DATA_DIR}" ] && DATA_DIR="${SPLIT_ROOT}"
            QUESTIONS_PATH="${SPLIT_ROOT}/questions.jsonl"
            RULEBOOK_PATH="${SPLIT_ROOT}/rulebook.md"
            CALENDAR_PATH="${SPLIT_ROOT}/calendar.csv"
        fi
    fi
fi

# Verify model weights directory exists (fail early if missing in production Docker mode)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL_DIR="${MODEL_DIR:-${SCRIPT_DIR}/weights/base_model}"
if [ -n "${CHECK_MODEL_DIR:-}" ] && [ ! -d "${MODEL_DIR}" ]; then
    echo "[predict.sh Error] Model directory not found: ${MODEL_DIR}"
    exit 1
fi

RESULT_DIR="${RESULT_DIR:-/result}"
SUBMISSION_PATH="${SUBMISSION_PATH:-/result/submission.jsonl}"
LOG_DIR="${LOG_DIR:-/result/logs}"

mkdir -p "${RESULT_DIR}"
mkdir -p "${LOG_DIR}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH}"
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
export TRANSFORMERS_OFFLINE="${TRANSFORMERS_OFFLINE:-1}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

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
