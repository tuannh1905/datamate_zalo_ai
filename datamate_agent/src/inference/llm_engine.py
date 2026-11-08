"""
Offline LLM Engine for DataMate Challenge.
Wraps vLLM for high-throughput batch generation with offline weights,
with seamless fallback to Hugging Face Transformers GPU (4-bit/bfloat16)
and CPU mock mode.
"""

import logging
import os
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)

# Check if PyTorch and CUDA are available
import torch
HAS_CUDA = torch.cuda.is_available()

# Check if vLLM is available
HAS_VLLM = False
if HAS_CUDA:
    try:
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
        self.is_hf_gpu = False
        self.hf_model = None
        self.hf_tokenizer = None

        # 1. Try vLLM if available
        if HAS_VLLM and (os.path.exists(model_name_or_path) or "/" in model_name_or_path):
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
                logger.warning(f"Could not initialize vLLM: {e}")
                self.llm = None
                self.is_offline_vllm = False

        # 2. If vLLM is not active but CUDA is available, use HuggingFace Transformers
        if not self.is_offline_vllm and HAS_CUDA and (os.path.exists(model_name_or_path) or "/" in model_name_or_path):
            try:
                from transformers import AutoModelForCausalLM, AutoTokenizer
                logger.info(f"Loading Hugging Face model on GPU: {model_name_or_path}")
                self.hf_tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=trust_remote_code)
                try:
                    self.hf_model = AutoModelForCausalLM.from_pretrained(
                        model_name_or_path,
                        load_in_4bit=True,
                        device_map="auto",
                        trust_remote_code=trust_remote_code,
                    )
                except Exception:
                    self.hf_model = AutoModelForCausalLM.from_pretrained(
                        model_name_or_path,
                        torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
                        device_map="auto",
                        trust_remote_code=trust_remote_code,
                    )
                
                if adapter_path and os.path.exists(adapter_path):
                    from peft import PeftModel
                    self.hf_model = PeftModel.from_pretrained(self.hf_model, adapter_path)
                    logger.info(f"Loaded PEFT adapter into HuggingFace model from: {adapter_path}")
                
                self.is_hf_gpu = True
            except Exception as e:
                logger.warning(f"Could not load Hugging Face model on GPU: {e}")
                self.is_hf_gpu = False

        if not self.is_offline_vllm and not self.is_hf_gpu:
            logger.info("Running in Fallback Mock Mode (no GPU model loaded).")

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

        if self.is_hf_gpu and self.hf_model is not None and self.hf_tokenizer is not None:
            results = []
            for prompt in prompts:
                inputs = self.hf_tokenizer(prompt, return_tensors="pt").to(self.hf_model.device)
                do_sample = temperature > 0.0
                gen_kwargs: Dict[str, Any] = {
                    "max_new_tokens": max_new_tokens,
                    "do_sample": do_sample,
                    "pad_token_id": self.hf_tokenizer.eos_token_id,
                }
                if do_sample:
                    gen_kwargs["temperature"] = temperature
                    gen_kwargs["top_p"] = top_p
                with torch.no_grad():
                    gen_tokens = self.hf_model.generate(**inputs, **gen_kwargs)
                out_text = self.hf_tokenizer.decode(gen_tokens[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
                results.append([out_text])
            return results

        # CPU / Fallback Mock Mode
        fallback_results = []
        for p in prompts:
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

        if self.is_hf_gpu and self.hf_model is not None and self.hf_tokenizer is not None:
            results = []
            inputs = self.hf_tokenizer(prompt, return_tensors="pt").to(self.hf_model.device)
            do_sample = temperature > 0.0
            for _ in range(n):
                gen_kwargs: Dict[str, Any] = {
                    "max_new_tokens": max_new_tokens,
                    "do_sample": do_sample,
                    "pad_token_id": self.hf_tokenizer.eos_token_id,
                }
                if do_sample:
                    gen_kwargs["temperature"] = temperature
                    gen_kwargs["top_p"] = top_p
                with torch.no_grad():
                    gen_tokens = self.hf_model.generate(**inputs, **gen_kwargs)
                out_text = self.hf_tokenizer.decode(gen_tokens[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
                results.append(out_text)
            return results

        # Fallback Mock Mode
        mock_resp = (
            "Notes:\n"
            "- Calculation for total amount.\n"
            "TYPE: number\n"
            "```sql\n"
            "SELECT COALESCE(ROUND(SUM(line_amount), 0), 0) AS answer FROM v_sales WHERE is_valid_sales = TRUE;\n"
            "```"
        )
        return [mock_resp] * n
