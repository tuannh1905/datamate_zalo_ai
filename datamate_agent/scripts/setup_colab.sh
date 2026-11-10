#!/bin/bash
# ===================================================================
# DataMate Agent - Google Colab GPU Environment Setup Script
# Installs LLM tools, Unsloth, DuckDB, OpenPyXL, and downloads weights
# ===================================================================
set -e

echo "=== [1/4] Checking GPU Hardware ==="
nvidia-smi
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"

echo "=== [2/4] Installing Python Dependencies ==="
pip install duckdb openpyxl pandas numpy pyyaml pydantic tqdm python-dateutil
pip install "huggingface-hub>=1.5.0,<2.0"
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git" || echo "Notice: Unsloth install failed, falling back to standard PEFT."
pip install peft accelerate bitsandbytes datasets
pip install -q xformers || echo "Notice: xformers install skipped"

# Optional vLLM installation: only if INSTALL_VLLM=1 is explicitly requested
if [ "${INSTALL_VLLM}" = "1" ]; then
    echo "Installing vLLM as requested (GPU >= 24GB recommended)..."
    pip install "vllm>=0.6.0" || echo "Notice: vLLM install failed, using PyTorch/Unsloth backend."
else
    echo "Notice: vLLM installation skipped by default (set INSTALL_VLLM=1 to enable). Using HuggingFace/Unsloth backend."
fi

echo "=== [3/4] Downloading Base Model Weights (Offline Preparation) ==="
MODEL_ID="Qwen/Qwen2.5-Coder-3B-Instruct"
WEIGHTS_DIR="./weights/base_model"
mkdir -p "${WEIGHTS_DIR}"

python3 -c "
from huggingface_hub import snapshot_download
print(f'Downloading model weights from {MODEL_ID} to {WEIGHTS_DIR}...')
snapshot_download(repo_id='${MODEL_ID}', local_dir='${WEIGHTS_DIR}', local_dir_use_symlinks=False)
print('Model weights downloaded successfully.')
"

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
