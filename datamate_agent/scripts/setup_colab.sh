#!/bin/bash
# ===================================================================
# DataMate Agent - Google Colab GPU Environment Setup Script
# Installs LLM tools, Unsloth, DuckDB, OpenPyXL, and downloads weights
# ===================================================================
set -e

echo "=== [1/4] Checking GPU Hardware ==="
nvidia-smi

echo "=== [2/4] Installing Python Dependencies ==="
pip install duckdb openpyxl pandas numpy pyyaml pydantic tqdm python-dateutil
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install peft accelerate bitsandbytes datasets

# Attempt vllm install if available for this Python/CUDA version
pip install "vllm>=0.6.0" || echo "Notice: vLLM not available for this Python version, will use HuggingFace/Unsloth backend."

echo "=== [3/4] Downloading Base Model Weights (Offline Preparation) ==="
MODEL_ID="Qwen/Qwen2.5-Coder-7B-Instruct"
WEIGHTS_DIR="./weights/base_model"
mkdir -p "${WEIGHTS_DIR}"

pip install -U "huggingface_hub[cli]"
huggingface-cli download "${MODEL_ID}" --local-dir "${WEIGHTS_DIR}" --local-dir-use-symlinks False

echo "=== [4/4] Verifying Environment ==="
python3 -c "
import duckdb, torch, openpyxl
print('✓ DuckDB Version:', duckdb.__version__)
print('✓ CUDA Available:', torch.cuda.is_available(), 'Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')
try:
    import vllm
    print('✓ vLLM Version:', vllm.__version__)
except ImportError:
    print('✓ vLLM not installed, using native PyTorch/Unsloth backend')
print('✓ OpenPyXL Installed')
print('✓ Environment is ready!')
"

echo "=== Colab Environment Setup Completed Successfully! ==="
