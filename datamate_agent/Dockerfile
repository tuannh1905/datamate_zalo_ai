# ===================================================================
# DataMate Challenge - Offline Docker Environment
# Offline-ready CUDA 12.4 + Python 3.10/3.11 + vLLM + DuckDB
# ===================================================================

FROM vllm/vllm-openai:v0.6.3.post1

# Set non-interactive mode and environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/datamate_agent:${PYTHONPATH}" \
    HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /datamate_agent

# Install Python requirements
COPY requirements.txt /datamate_agent/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, configs, prompts, and scripts
COPY configs/ /datamate_agent/configs/
COPY prompts/ /datamate_agent/prompts/
COPY src/ /datamate_agent/src/
COPY scripts/ /datamate_agent/scripts/
COPY predict.sh /datamate_agent/predict.sh

# Make entrypoint script executable
RUN chmod +x /datamate_agent/predict.sh

# Weights directory is mounted or copied during image finalization:
# COPY weights/ /datamate_agent/weights/
RUN mkdir -p /datamate_agent/weights /result /data

# Default Docker entrypoint
ENTRYPOINT ["/datamate_agent/predict.sh"]
