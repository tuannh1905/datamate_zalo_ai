"""
Offline LLM Engine for DataMate Challenge.
Wraps vLLM for high-throughput batch generation with offline weights,
optional LoRA adapter loading, fp8/4-bit quantization, and CPU fallback.
"""

import logging
import os
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)

# Check if vLLM is available
HAS_VLLM = False
try:
    import torch
    if torch.cuda.is_available():
        from vllm import LLM, SamplingParams
        from vllm.lora.request import LoRARequest
        HAS_VLLM = True
except Exception:
    HAS_VLLM = False


class LLMEngine:
    def __init__(
        self,
        model_name_or_path: str,
        adapter_path: Optional[str] = None,
        tensor_parallel_size: int = 1,
        gpu_memory_utilization: float = 0.90,
        max_model_len: int = 16384,
        quantization: Optional[str] = None,
        trust_remote_code: bool = True,
        enforce_eager: bool = False,
    ):
        self.model_name_or_path = model_name_or_path
        self.adapter_path = adapter_path
        self.max_model_len = max_model_len
        self.llm = None
        self.lora_request = None
        self.is_offline_vllm = False

        if HAS_VLLM and os.path.exists(model_name_or_path) or (HAS_VLLM and "/" in model_name_or_path):
            try:
                logger.info(f"Initializing vLLM engine with model: {model_name_or_path}")
                enable_lora = bool(adapter_path and os.path.exists(adapter_path))
                
                vllm_kwargs: Dict[str, Any] = {
                    "model": model_name_or_path,
                    "tensor_parallel_size": tensor_parallel_size,
                    "gpu_memory_utilization": gpu_memory_utilization,
                    "max_model_len": max_model_len,
                    "trust_remote_code": trust_remote_code,
                    "enable_lora": enable_lora,
                }
                if quantization:
                    vllm_kwargs["quantization"] = quantization
                if enforce_eager:
                    vllm_kwargs["enforce_eager"] = True

                self.llm = LLM(**vllm_kwargs)
                self.is_offline_vllm = True

                if enable_lora:
                    self.lora_request = LoRARequest("datamate_adapter", 1, adapter_path)
                    logger.info(f"Loaded LoRA adapter from: {adapter_path}")
            except Exception as e:
                logger.warning(f"Could not initialize vLLM (falling back to mock/CPU mode): {e}")
                self.llm = None
                self.is_offline_vllm = False
        else:
            logger.info("Running in CPU / Fallback Mock Mode (no GPU / vLLM available).")

    def generate_batch(
        self,
        prompts: List[str],
        temperature: float = 0.0,
        top_p: float = 0.95,
        max_new_tokens: int = 1024,
        stop_tokens: Optional[List[str]] = None,
    ) -> List[List[str]]:
        """
        Generates completions for a batch of prompts.
        Returns a list of completions per prompt.
        """
        if self.is_offline_vllm and self.llm is not None:
            sampling_params = SamplingParams(
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_new_tokens,
                stop=stop_tokens or ["```\n\n", "User:", "<|im_end|>"],
            )
            outputs = self.llm.generate(
                prompts,
                sampling_params=sampling_params,
                lora_request=self.lora_request,
            )
            return [[output.outputs[0].text for output in outputs]]

        # CPU / Fallback Mode (useful for offline local testing and mock validation)
        fallback_results = []
        for p in prompts:
            # Deterministic heuristic answer for testing
            mock_resp = (
                "Notes:\n"
                "- Query sales for valid orders.\n"
                "TYPE: number\n"
                "```sql\n"
                "SELECT COALESCE(ROUND(SUM(line_amount), 0), 0) AS answer FROM v_sales WHERE is_valid_sales = TRUE;\n"
                "```"
            )
            fallback_results.append([mock_resp])
        return fallback_results

    def generate_single(
        self,
        prompt: str,
        n: int = 1,
        temperature: float = 0.1,
        top_p: float = 0.95,
        max_new_tokens: int = 1024,
    ) -> List[str]:
        """
        Generates n candidate samples for a single prompt.
        """
        if self.is_offline_vllm and self.llm is not None:
            sampling_params = SamplingParams(
                n=n,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_new_tokens,
                stop=["```\n\n", "<|im_end|>"],
            )
            outputs = self.llm.generate(
                [prompt],
                sampling_params=sampling_params,
                lora_request=self.lora_request,
            )
            return [out.text for out in outputs[0].outputs]

        # Fallback for CPU / mock mode
        results = []
        for i in range(n):
            results.append(
                f"Notes:\n- Sample {i}: calculate sales revenue.\n"
                f"TYPE: number\n"
                f"```sql\n"
                f"SELECT COALESCE(ROUND(SUM(line_amount), 0), 0) AS answer FROM v_sales WHERE is_valid_sales = TRUE;\n"
                f"```"
            )
        return results
