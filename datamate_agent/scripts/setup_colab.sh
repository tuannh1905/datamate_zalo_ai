#!/bin/bash
# ===================================================================
# DataMate Agent - Google Colab GPU Environment Setup Script
# Installs vLLM, Unsloth, DuckDB, OpenPyXL, and downloads model weights
# ===================================================================
set -e

echo "=== [1/4] Checking GPU Hardware ==="
nvidia-smi

echo "=== [2/4] Installing Python Dependencies ==="
pip install --upgrade pip
pip install duckdb openpyxl pandas numpy pyyaml pydantic tqdm python-dateutil
pip install vllm>=0.6.0
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps "xformers<0.0.28" "trl<0.9.0" peft accelerate bitsandbytes datasets

echo "=== [3/4] Downloading Base Model Weights (Offline Preparation) ==="
MODEL_ID="Qwen/Qwen2.5-Coder-7B-Instruct"
WEIGHTS_DIR="./weights/base_model"
mkdir -p "${WEIGHTS_DIR}"

pip install -U "huggingface_hub[cli]"
huggingface-cli download "${MODEL_ID}" --local-dir "${WEIGHTS_DIR}" --local-dir-use-symlinks False

echo "=== [4/4] Verifying Environment ==="
python3 -c "
import duckdb, torch, vllm, openpyxl
print('✓ DuckDB Version:', duckdb.__version__)
print('✓ CUDA Available:', torch.cuda.is_available(), 'Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')
print('✓ vLLM Version:', vllm.__version__)
print('✓ OpenPyXL Installed')
"

echo "=== Colab Environment Setup Completed Successfully! ==="
