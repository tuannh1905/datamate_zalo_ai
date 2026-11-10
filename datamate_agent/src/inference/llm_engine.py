"""
Offline LLM Engine for DataMate Challenge.
Wraps vLLM for high-throughput batch generation with prefix caching,
VRAM auto-detection (Colab T4 / L4), 4-bit quantization, and dynamic LoRA loading,
with seamless fallback to Hugging Face Transformers GPU (4-bit BitsAndBytes)
and CPU mock mode.
"""

import gc
import logging
import os
from typing import Any, Dict, List, Optional, Tuple, Union

# Set PyTorch allocation conf to avoid VRAM fragmentation and virtual memory mapping errors on Colab T4
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "max_split_size_mb:128")

logger = logging.getLogger(__name__)

# Check if PyTorch and CUDA are available
try:
    import torch
    HAS_CUDA = torch.cuda.is_available()
except ImportError:
    torch = None
    HAS_CUDA = False

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
        allow_mock: bool = False,
    ):
        self.model_name_or_path = model_name_or_path
        self.adapter_path = adapter_path
        self.max_model_len = min(max_model_len, 16384) if max_model_len else 16384
        self.allow_mock = allow_mock
        self.llm = None
        self.lora_request = None
        self.is_offline_vllm = False
        self.is_hf_gpu = False
        self.hf_model = None
        self.hf_tokenizer = None

        # 0. Validate adapter path existence if explicitly configured
        if adapter_path:
            if not os.path.exists(adapter_path):
                raise FileNotFoundError(
                    f"[LLMEngine Error] Configured LoRA adapter path does not exist: '{adapter_path}'. "
                    f"Ensure weights/adapters are present or set adapter_path: null."
                )

        # 1. Try vLLM if available
        if HAS_VLLM and (os.path.exists(model_name_or_path) or "/" in model_name_or_path):
            try:
                logger.info(f"Initializing vLLM engine with model: {model_name_or_path}")

                # Auto-detect GPU VRAM
                is_low_vram = False
                vram_gb = 0.0
                if HAS_CUDA and torch.cuda.is_available():
                    try:
                        total_vram = torch.cuda.get_device_properties(0).total_memory
                        vram_gb = total_vram / (1024 ** 3)
                        logger.info(f"[GPU Auto-Detect] Device: {torch.cuda.get_device_name(0)}, Total VRAM: {vram_gb:.2f} GB")
                        if vram_gb < 18.0:
                            is_low_vram = True
                            logger.info(f"[VRAM Guard] VRAM < 18GB (e.g. Colab T4). Forcing dtype='half' and 4-bit quantization.")
                    except Exception as e:
                        logger.warning(f"Failed to check GPU memory: {e}")

                vllm_kwargs: Dict[str, Any] = {
                    "model": model_name_or_path,
                    "tensor_parallel_size": tensor_parallel_size,
                    "gpu_memory_utilization": gpu_memory_utilization,
                    "max_model_len": self.max_model_len,
                    "enable_prefix_caching": True,  # Critical for 14k prefix reuse
                    "trust_remote_code": trust_remote_code,
                    "enable_lora": True,  # Support dynamic LoRA loading
                    "max_lora_rank": 16,
                }

                if is_low_vram:
                    vllm_kwargs["dtype"] = "half"
                    chosen_quant = quantization or "bitsandbytes"
                    vllm_kwargs["quantization"] = chosen_quant
                    if chosen_quant == "bitsandbytes":
                        vllm_kwargs["load_format"] = "bitsandbytes"
                elif quantization:
                    vllm_kwargs["quantization"] = quantization
                    if quantization == "bitsandbytes":
                        vllm_kwargs["load_format"] = "bitsandbytes"

                if enforce_eager:
                    vllm_kwargs["enforce_eager"] = True

                try:
                    self.llm = LLM(**vllm_kwargs)
                except Exception as quant_err:
                    if "quantization" in vllm_kwargs:
                        logger.warning(f"vLLM init with quantization failed ({quant_err}). Retrying with dtype='half' without quantization...")
                        vllm_kwargs.pop("quantization", None)
                        vllm_kwargs.pop("load_format", None)
                        vllm_kwargs["dtype"] = "half"
                        self.llm = LLM(**vllm_kwargs)
                    else:
                        raise quant_err

                self.is_offline_vllm = True

                if adapter_path:
                    try:
                        self.lora_request = LoRARequest("datamate_adapter", 1, adapter_path)
                        logger.info(f"Loaded LoRA adapter into vLLM from: {adapter_path}")
                    except Exception as lora_err:
                        raise RuntimeError(f"Failed to load LoRA adapter into vLLM from '{adapter_path}': {lora_err}")

                logger.info(f"vLLM engine initialized successfully (Model: {model_name_or_path}, Adapter: {adapter_path or 'None'}, Prefix Caching: True).")
            except Exception as e:
                logger.warning(f"Could not initialize vLLM: {e}. Falling back to HuggingFace Transformers...")
                self.llm = None
                self.is_offline_vllm = False

        # 2. If vLLM is not active but CUDA is available, use HuggingFace Transformers + bitsandbytes 4-bit
        if not self.is_offline_vllm and HAS_CUDA and (os.path.exists(model_name_or_path) or "/" in model_name_or_path):
            try:
                from transformers import AutoModelForCausalLM, AutoTokenizer
                logger.info(f"Loading Hugging Face model on GPU: {model_name_or_path}")
                self.hf_tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=trust_remote_code)

                is_ampere_or_later = False
                if torch.cuda.is_available():
                    try:
                        major, _ = torch.cuda.get_device_capability()
                        is_ampere_or_later = (major >= 8)
                    except Exception:
                        pass
                compute_dtype = torch.bfloat16 if is_ampere_or_later else torch.float16

                loaded_successfully = False
                quant_used = "None"
                # Try 4-bit quantization (BitsAndBytes)
                try:
                    from transformers import BitsAndBytesConfig
                    bnb_config = BitsAndBytesConfig(
                        load_in_4bit=True,
                        bnb_4bit_quant_type="nf4",
                        bnb_4bit_compute_dtype=compute_dtype,
                        bnb_4bit_use_double_quant=True,
                    )
                    self.hf_model = AutoModelForCausalLM.from_pretrained(
                        model_name_or_path,
                        quantization_config=bnb_config,
                        device_map="auto",
                        trust_remote_code=trust_remote_code,
                    )
                    loaded_successfully = True
                    quant_used = "BitsAndBytes NF4 (4-bit)"
                    logger.info("Successfully loaded model with BitsAndBytes 4-bit (NF4) quantization.")
                except Exception as bnb_err:
                    logger.warning(f"BitsAndBytes 4-bit load failed or unavailable ({bnb_err}). Trying load_in_4bit=True...")
                    try:
                        self.hf_model = AutoModelForCausalLM.from_pretrained(
                            model_name_or_path,
                            load_in_4bit=True,
                            device_map="auto",
                            trust_remote_code=trust_remote_code,
                        )
                        loaded_successfully = True
                        quant_used = "load_in_4bit=True"
                    except Exception as bnb_err2:
                        logger.warning(f"4-bit load failed ({bnb_err2}). Falling back to native precision...")

                if not loaded_successfully:
                    self.hf_model = AutoModelForCausalLM.from_pretrained(
                        model_name_or_path,
                        torch_dtype=compute_dtype,
                        device_map="auto",
                        trust_remote_code=trust_remote_code,
                    )
                    quant_used = f"Native {compute_dtype}"

                if adapter_path:
                    try:
                        from peft import PeftModel
                        self.hf_model = PeftModel.from_pretrained(self.hf_model, adapter_path)
                        logger.info(f"Loaded PEFT adapter into HuggingFace model from: {adapter_path}")
                    except Exception as peft_err:
                        raise RuntimeError(f"Failed to load PEFT adapter from '{adapter_path}': {peft_err}")

                self.is_hf_gpu = True
                logger.info(
                    f"HuggingFace model initialized successfully (Model: {model_name_or_path}, "
                    f"Adapter: {adapter_path or 'None'}, Quantization: {quant_used})."
                )
            except Exception as e:
                logger.warning(f"Could not load Hugging Face model on GPU: {e}")
                self.is_hf_gpu = False

        if not self.is_offline_vllm and not self.is_hf_gpu:
            if not self.allow_mock:
                raise RuntimeError(
                    f"[LLMEngine Error] Failed to load offline LLM model from '{model_name_or_path}' (adapter: '{adapter_path}'). "
                    f"To enable Fallback Mock Mode for testing/CI, pass '--allow_mock' or allow_mock=True."
                )
            logger.warning("Running in Fallback Mock Mode (--allow_mock enabled).")

    @property
    def tokenizer(self) -> Optional[Any]:
        if self.is_offline_vllm and self.llm is not None:
            try:
                return self.llm.get_tokenizer()
            except Exception:
                pass
        if self.is_hf_gpu and self.hf_tokenizer is not None:
            return self.hf_tokenizer
        return None

    def _prepare_inputs(self, prompt: str, max_tokens: int = 8192) -> Tuple[Dict[str, Any], int]:
        """
        Tokenizes on CPU and safely windows the prompt to avoid quadratic attention OOM on 16GB GPUs.
        """
        inputs = self.hf_tokenizer(prompt, return_tensors="pt")
        total_tokens = inputs["input_ids"].shape[1]
        if total_tokens > max_tokens:
            keep_sys = 6144
            keep_user = max_tokens - keep_sys
            logger.info(
                f"[VRAM Guard] Prompt length ({total_tokens} tokens) exceeds safe threshold ({max_tokens} tokens). "
                f"Windowing on CPU: keeping first {keep_sys} tokens + last {keep_user} tokens."
            )
            input_ids = torch.cat([inputs["input_ids"][:, :keep_sys], inputs["input_ids"][:, -keep_user:]], dim=1)
            attention_mask = torch.cat([inputs["attention_mask"][:, :keep_sys], inputs["attention_mask"][:, -keep_user:]], dim=1)
            del inputs
            inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
            total_tokens = input_ids.shape[1]

        gpu_inputs = {k: v.to(self.hf_model.device) for k, v in inputs.items()}
        del inputs
        return gpu_inputs, total_tokens

    def generate_samples(
        self,
        prompts: Union[str, List[str]],
        n: int = 8,
        temperature: float = 0.7,
        max_tokens: int = 512,
        stop: Optional[List[str]] = None,
    ) -> List[List[str]]:
        """
        Batch Sampling: Generates n candidate samples for a batch of prompts.
        In vLLM, uses a SINGLE SamplingParams(n=n, ...) call so all n SQL drafts
        per question are generated in parallel in one forward pass.
        Returns List[List[str]]: outer list matches input prompts, inner list has n completions.
        """
        prompt_list = [prompts] if isinstance(prompts, str) else prompts
        if not prompt_list:
            return []

        # 1. vLLM parallel generation
        if self.is_offline_vllm and self.llm is not None:
            sampling_params = SamplingParams(
                n=n,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop or ["<|im_end|>"],
            )
            outputs = self.llm.generate(
                prompt_list,
                sampling_params=sampling_params,
                lora_request=self.lora_request,
            )
            results = []
            for out in outputs:
                results.append([cand.text for cand in out.outputs])
            return results

        # 2. HuggingFace fallback
        if self.is_hf_gpu and self.hf_model is not None and self.hf_tokenizer is not None:
            gc.collect()
            if HAS_CUDA and torch is not None:
                torch.cuda.empty_cache()
            all_results = []
            do_sample = temperature > 0.0

            for prompt in prompt_list:
                inputs, prompt_len = self._prepare_inputs(prompt, max_tokens=8192)
                prompt_samples = []
                for _ in range(n):
                    gen_kwargs: Dict[str, Any] = {
                        "max_new_tokens": max_tokens,
                        "do_sample": do_sample,
                        "pad_token_id": self.hf_tokenizer.eos_token_id,
                    }
                    if do_sample:
                        gen_kwargs["temperature"] = temperature
                        gen_kwargs["top_p"] = 0.95
                    with torch.inference_mode():
                        gen_tokens = self.hf_model.generate(**inputs, **gen_kwargs)
                    out_text = self.hf_tokenizer.decode(gen_tokens[0][prompt_len:], skip_special_tokens=True)
                    prompt_samples.append(out_text)
                    del gen_tokens
                    if HAS_CUDA and torch is not None:
                        torch.cuda.empty_cache()
                del inputs
                all_results.append(prompt_samples)
            return all_results

        # 3. CPU / Fallback Mock Mode
        mock_resp = (
            "Notes:\n"
            "- Calculation for total amount.\n"
            "TYPE: number\n"
            "```sql\n"
            "SELECT COALESCE(ROUND(SUM(line_amount), 0), 0) AS answer FROM v_sales WHERE is_valid_sales = TRUE;\n"
            "```"
        )
        return [[mock_resp] * n for _ in prompt_list]

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
        Routes to generate_samples for unified batch sampling.
        """
        samples = self.generate_samples(
            prompts=[prompt],
            n=n,
            temperature=temperature,
            max_tokens=max_new_tokens,
        )
        return samples[0] if samples else []

    def generate_batch(
        self,
        prompts: List[str],
        temperature: float = 0.0,
        top_p: float = 0.95,
        max_new_tokens: int = 1024,
        stop_tokens: Optional[List[str]] = None,
    ) -> List[List[str]]:
        """
        Generates completions for a batch of prompts (1 completion per prompt).
        """
        return self.generate_samples(
            prompts=prompts,
            n=1,
            temperature=temperature,
            max_tokens=max_new_tokens,
            stop=stop_tokens,
        )
