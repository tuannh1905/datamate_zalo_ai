#!/bin/bash
# ===================================================================
# DataMate Agent - Iterative Self-Training Loop (v1 -> v2 -> v3)
# Uses dataset_loader for Google Drive auto-caching (I/O optimization)
# ===================================================================
set -e

DATASET="${DATASET:-train}"
DRIVE_BASE_PATH="${DRIVE_BASE_PATH:-/content/drive/MyDrive/ZaloAI_DataMate}"
LOCAL_CACHE_ROOT="${LOCAL_CACHE_ROOT:-/content/local_data}"

BASE_MODEL="${BASE_MODEL:-./weights/base_model}"
ADAPTER_ROOT="./weights/adapters"
DATA_CACHE="./data_cache"

mkdir -p "${ADAPTER_ROOT}"
mkdir -p "${DATA_CACHE}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$(cd "${SCRIPT_DIR}/.." && pwd):${PYTHONPATH}"

echo "==================================================================="
echo " Starting DataMate Iterative Self-Training Pipeline"
echo " Dataset Split   : ${DATASET}"
echo " Drive Base Path : ${DRIVE_BASE_PATH}"
echo " Local NVMe Cache: ${LOCAL_CACHE_ROOT}"
echo " Base Model      : ${BASE_MODEL}"
echo "==================================================================="

# -------------------------------------------------------------------
# ITERATION 1: Base Model (v0) -> Adapter v1
# -------------------------------------------------------------------
echo "=== [ITERATION 1/3] Generating candidates with Base Model ==="
python3 -m src.training.candidate_gen \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --local_cache_root "${LOCAL_CACHE_ROOT}" \
    --output "${DATA_CACHE}/candidates_v1.jsonl" \
    --model "${BASE_MODEL}"

echo "=== [ITERATION 1/3] Rejection Sampling with Gold Answers ==="
python3 -m src.training.rejection_sampling \
    --candidates "${DATA_CACHE}/candidates_v1.jsonl" \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --output "${DATA_CACHE}/sft_dataset_v1.jsonl" \
    --max_per_q 3

echo "=== [ITERATION 1/3] Fine-tuning Adapter v1 with 4-bit QLoRA ==="
python3 -m src.training.train_qlora \
    --dataset "${DATA_CACHE}/sft_dataset_v1.jsonl" \
    --output_dir "${ADAPTER_ROOT}/v1" \
    --model "${BASE_MODEL}" \
    --epochs 1 \
    --lr 2e-4

# -------------------------------------------------------------------
# ITERATION 2: Model + Adapter v1 -> Adapter v2
# -------------------------------------------------------------------
echo "=== [ITERATION 2/3] Generating candidates with Adapter v1 ==="
python3 -m src.training.candidate_gen \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --local_cache_root "${LOCAL_CACHE_ROOT}" \
    --output "${DATA_CACHE}/candidates_v2.jsonl" \
    --model "${BASE_MODEL}" \
    --adapter "${ADAPTER_ROOT}/v1"

echo "=== [ITERATION 2/3] Rejection Sampling with Gold Answers ==="
python3 -m src.training.rejection_sampling \
    --candidates "${DATA_CACHE}/candidates_v2.jsonl" \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --output "${DATA_CACHE}/sft_dataset_v2.jsonl" \
    --max_per_q 3

echo "=== [ITERATION 2/3] Fine-tuning Adapter v2 with 4-bit QLoRA ==="
python3 -m src.training.train_qlora \
    --dataset "${DATA_CACHE}/sft_dataset_v2.jsonl" \
    --output_dir "${ADAPTER_ROOT}/v2" \
    --model "${BASE_MODEL}" \
    --epochs 1 \
    --lr 1.5e-4

# -------------------------------------------------------------------
# ITERATION 3: Model + Adapter v2 -> Final Adapter v3
# -------------------------------------------------------------------
echo "=== [ITERATION 3/3] Generating candidates with Adapter v2 ==="
python3 -m src.training.candidate_gen \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --local_cache_root "${LOCAL_CACHE_ROOT}" \
    --output "${DATA_CACHE}/candidates_v3.jsonl" \
    --model "${BASE_MODEL}" \
    --adapter "${ADAPTER_ROOT}/v2"

echo "=== [ITERATION 3/3] Rejection Sampling with Gold Answers ==="
python3 -m src.training.rejection_sampling \
    --candidates "${DATA_CACHE}/candidates_v3.jsonl" \
    --dataset "${DATASET}" \
    --drive_base_path "${DRIVE_BASE_PATH}" \
    --output "${DATA_CACHE}/sft_dataset_v3.jsonl" \
    --max_per_q 3

echo "=== [ITERATION 3/3] Fine-tuning Final Adapter v3 ==="
python3 -m src.training.train_qlora \
    --dataset "${DATA_CACHE}/sft_dataset_v3.jsonl" \
    --output_dir "${ADAPTER_ROOT}/v3" \
    --model "${BASE_MODEL}" \
    --epochs 1 \
    --lr 1e-4

echo "==================================================================="
echo " Self-Training Loop Completed! Final Adapter saved to ${ADAPTER_ROOT}/v3"
echo "==================================================================="
