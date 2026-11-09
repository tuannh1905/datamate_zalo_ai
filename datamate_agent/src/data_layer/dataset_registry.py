"""
src/data_layer/dataset_registry.py - Centralized Dataset Registry for DataMate Challenge.

Provides:
- load_registry(path=None): Loads configurations from configs/datasets.yaml
- resolve_dataset(name, require_answers=False): Resolves paths, handles inheritance (extends),
  business ID filtering, question limits, and path auto-detection.
- list_datasets(): Prints status of all configured datasets.
"""

import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import yaml

from src.data_layer.dataset_loader import DatasetPaths

logger = logging.getLogger(__name__)


def find_default_registry_path() -> str:
    """Finds configs/datasets.yaml from env, cwd, or repo structure."""
    if os.environ.get("DATAMATE_DATASETS"):
        cand = os.environ["DATAMATE_DATASETS"]
        if os.path.exists(cand):
            return os.path.abspath(cand)

    cand_paths = [
        "configs/datasets.yaml",
        os.path.join(os.path.dirname(__file__), "../../configs/datasets.yaml"),
        os.path.join(os.path.dirname(__file__), "../configs/datasets.yaml"),
        "/configs/datasets.yaml",
    ]
    for p in cand_paths:
        if os.path.exists(p):
            return os.path.abspath(p)

    return os.path.abspath(cand_paths[1])


def load_registry(path: Optional[str] = None) -> Dict[str, Any]:
    """Loads and returns the raw datasets registry dictionary."""
    reg_path = path or find_default_registry_path()
    if not os.path.exists(reg_path):
        raise FileNotFoundError(f"[DatasetRegistry] Registry file not found at: {reg_path}")

    with open(reg_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if "datasets" not in data:
        raise ValueError(f"[DatasetRegistry] Invalid registry YAML, missing 'datasets' key: {reg_path}")
    return data


def _search_for_questions_root(start_dir: str, target_name: str, max_depth: int = 3) -> Optional[str]:
    """
    Searches up to `max_depth` directory levels starting from start_dir
    to locate a folder that directly contains `questions.jsonl`.
    """
    if not os.path.exists(start_dir):
        return None

    # First check direct child paths matching target_name
    candidates = [
        os.path.join(start_dir, target_name),
        os.path.join(start_dir, target_name, target_name),
        start_dir,
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "questions.jsonl")):
            return os.path.abspath(c)

    # General BFS / walk up to max_depth
    start_depth = start_dir.rstrip(os.sep).count(os.sep)
    for root, dirs, files in os.walk(start_dir):
        cur_depth = root.rstrip(os.sep).count(os.sep) - start_depth
        if cur_depth > max_depth:
            dirs.clear()
            continue
        if "questions.jsonl" in files:
            # If target_name is in path, prefer this
            if target_name in root:
                return os.path.abspath(root)

    return None


def _find_valid_root(declared_root: str, base_dataset_name: str) -> str:
    """
    Checks if declared_root exists. If not, attempts to auto-locate
    the split root folder (looking relative to project roots).
    """
    if os.path.exists(declared_root) and os.path.exists(os.path.join(declared_root, "questions.jsonl")):
        return os.path.abspath(declared_root)

    # Candidate search roots
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    parent_repo = os.path.abspath(os.path.join(repo_dir, ".."))

    search_roots = [
        parent_repo,
        repo_dir,
        os.getcwd(),
        "/content/dataset_gdrive",
        "/data",
    ]

    for s_dir in search_roots:
        found = _search_for_questions_root(s_dir, base_dataset_name, max_depth=3)
        if found:
            logger.warning(
                f"[DatasetRegistry] Declared root '{declared_root}' not found. "
                f"Auto-resolved to: '{found}'"
            )
            return found

    # Fall back to declared_root even if missing, validate() will report clearly
    return os.path.abspath(declared_root)


def get_merged_dataset_config(name: str, registry: Optional[Dict[str, Any]] = None) -> Tuple[Dict[str, Any], str]:
    """
    Resolves dataset inheritance (extends). Returns (merged_config, base_name).
    """
    if registry is None:
        registry = load_registry()
    datasets = registry.get("datasets", {})
    if name not in datasets:
        valid_names = ", ".join(sorted(datasets.keys()))
        raise ValueError(
            f"[DatasetRegistry] Unknown dataset '{name}'. Available registered datasets: [{valid_names}]"
        )

    config = dict(datasets[name])
    base_name = name

    # Follow inheritance chain
    chain = [name]
    while "extends" in config and config["extends"]:
        parent = config["extends"]
        if parent in chain:
            raise ValueError(f"[DatasetRegistry] Circular 'extends' detected in registry: {' -> '.join(chain + [parent])}")
        chain.append(parent)
        if parent not in datasets:
            raise ValueError(f"[DatasetRegistry] Dataset '{chain[-2]}' extends non-existent dataset '{parent}'")

        parent_cfg = dict(datasets[parent])
        # Update extends to parent's extends before merging other properties
        config["extends"] = parent_cfg.get("extends")
        for k, v in parent_cfg.items():
            if k == "extends":
                continue
            if k not in config or config[k] is None:
                config[k] = v
        base_name = parent

    return config, base_name


def filter_questions_and_answers(
    src_questions: str,
    src_answers: Optional[str],
    cache_dir: str,
    dataset_name: str,
    include_biz: Optional[List[str]] = None,
    exclude_biz: Optional[List[str]] = None,
    limit: Optional[int] = None,
) -> Tuple[str, Optional[str]]:
    """
    Filters questions and answers by business IDs and/or limit.
    Writes result to data_cache/<dataset_name>/questions.jsonl and answers.jsonl.
    Never modifies source files.
    """
    os.makedirs(cache_dir, exist_ok=True)
    out_q_path = os.path.join(cache_dir, "questions.jsonl")
    out_a_path = os.path.join(cache_dir, "answers.jsonl") if src_answers and os.path.exists(src_answers) else None

    include_set = set(include_biz) if include_biz else None
    exclude_set = set(exclude_biz) if exclude_biz else None

    kept_ids = set()
    kept_q_rows = []

    with open(src_questions, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue
            item = json.loads(line_str)
            biz = item.get("business_id")
            qid = item.get("id")

            if include_set and biz not in include_set:
                continue
            if exclude_set and biz in exclude_set:
                continue

            kept_q_rows.append(line_str)
            if qid:
                kept_ids.add(qid)

            if limit is not None and len(kept_q_rows) >= limit:
                break

    with open(out_q_path, "w", encoding="utf-8") as f:
        for q in kept_q_rows:
            f.write(q + "\n")

    if out_a_path and src_answers and os.path.exists(src_answers):
        kept_a_rows = []
        with open(src_answers, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if not line_str:
                    continue
                item = json.loads(line_str)
                if item.get("id") in kept_ids:
                    kept_a_rows.append(line_str)
        with open(out_a_path, "w", encoding="utf-8") as f:
            for a in kept_a_rows:
                f.write(a + "\n")

    logger.info(
        f"[DatasetRegistry] Filtered dataset '{dataset_name}': {len(kept_q_rows)} questions saved to {out_q_path}"
    )
    return out_q_path, out_a_path


def resolve_dataset(
    name: str,
    registry_path: Optional[str] = None,
    require_answers: bool = False,
    cache_root: str = "./data_cache",
) -> DatasetPaths:
    """
    Resolves a registered dataset name into an active, validated DatasetPaths object.
    Supports inheritance, business exclusion/inclusion, limits, and sanity checks.
    """
    registry = load_registry(registry_path)
    cfg, base_name = get_merged_dataset_config(name, registry)

    raw_root = cfg.get("root", "")
    root_dir = _find_valid_root(raw_root, base_name)

    # Relative paths resolve relative to root_dir
    def _res(p: Optional[str]) -> Optional[str]:
        if not p:
            return None
        return p if os.path.isabs(p) else os.path.abspath(os.path.join(root_dir, p))

    data_dir = _res(cfg.get("data_dir", "data")) or ""
    questions_path = _res(cfg.get("questions", "questions.jsonl")) or ""
    answers_path = _res(cfg.get("answers"))
    rulebook_path = _res(cfg.get("rulebook", "rulebook.md")) or ""
    calendar_path = _res(cfg.get("calendar", "calendar.csv")) or ""

    # Check filtering requirements (extends or explicit filters)
    inc_biz = cfg.get("include_business_ids")
    exc_biz = cfg.get("exclude_business_ids")
    limit = cfg.get("limit")

    if inc_biz or exc_biz or limit is not None:
        sub_cache = os.path.abspath(os.path.join(cache_root, name))
        questions_path, answers_path = filter_questions_and_answers(
            src_questions=questions_path,
            src_answers=answers_path,
            cache_dir=sub_cache,
            dataset_name=name,
            include_biz=inc_biz,
            exclude_biz=exc_biz,
            limit=limit,
        )

    # Validate essential files
    if not os.path.exists(questions_path):
        raise FileNotFoundError(f"[DatasetRegistry] Questions file not found: {questions_path}")
    if not os.path.exists(rulebook_path):
        raise FileNotFoundError(f"[DatasetRegistry] Rulebook file not found: {rulebook_path}")
    if not os.path.exists(calendar_path):
        raise FileNotFoundError(f"[DatasetRegistry] Calendar file not found: {calendar_path}")
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"[DatasetRegistry] Business data directory not found: {data_dir}")

    # Check at least one business directory
    subdirs = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    if not subdirs:
        raise FileNotFoundError(f"[DatasetRegistry] Data directory '{data_dir}' contains no business folders!")

    if require_answers:
        if not answers_path or not os.path.exists(answers_path):
            raise FileNotFoundError(
                f"[DatasetRegistry] Dataset '{name}' requires answers.jsonl for training, but none found at: {answers_path}"
            )

    # Statistics reporting
    try:
        with open(questions_path, "r", encoding="utf-8") as f:
            q_lines = [json.loads(line) for line in f if line.strip()]
        total_q = len(q_lines)
        referenced_biz = {q.get("business_id") for q in q_lines if q.get("business_id")}
        existing_biz_set = set(subdirs)
        missing_biz = referenced_biz - existing_biz_set

        print(f"\n==================== DATASET REGISTRY: {name} ====================")
        print(f"  • Root Directory       : {root_dir}")
        print(f"  • Data Directory       : {data_dir} ({len(subdirs)} businesses present)")
        print(f"  • Questions            : {questions_path} ({total_q:,} questions)")
        print(f"  • Rulebook             : {rulebook_path}")
        print(f"  • Calendar             : {calendar_path}")
        print(f"  • Answers (Gold)       : {answers_path or 'None (test split)'}")
        if missing_biz:
            print(f"  ⚠️ Warning: {len(missing_biz)} referenced business IDs missing on disk: {sorted(missing_biz)[:5]}...")
        print("==================================================================\n")
    except Exception as e:
        logger.debug(f"[DatasetRegistry] Could not compute full stats: {e}")

    return DatasetPaths(
        dataset_name=name,
        root_dir=root_dir,
        data_dir=data_dir,
        questions_path=questions_path,
        rulebook_path=rulebook_path,
        calendar_path=calendar_path,
        answers_path=answers_path,
        is_cached=False,
    )


def list_datasets(registry_path: Optional[str] = None) -> None:
    """Lists all datasets defined in registry and their status."""
    registry = load_registry(registry_path)
    datasets = registry.get("datasets", {})
    print("\nAvailable Datasets in Registry:")
    print(f"{'Dataset Name':<16} | {'Extends':<10} | {'Status':<12} | {'Declared Root'}")
    print("-" * 80)
    for name, cfg in datasets.items():
        ext = cfg.get("extends") or "-"
        raw_root = cfg.get("root", "")
        # Resolve base root if extends
        curr = cfg
        while not raw_root and curr.get("extends"):
            curr = datasets.get(curr["extends"], {})
            raw_root = curr.get("root", "")

        status = "EXISTS" if os.path.exists(raw_root) else "AUTO-DETECT"
        print(f"{name:<16} | {ext:<10} | {status:<12} | {raw_root}")
    print("-" * 80 + "\n")


if __name__ == "__main__":
    if "--list" in sys.argv or "--list_datasets" in sys.argv:
        list_datasets()
    else:
        name = sys.argv[1] if len(sys.argv) > 1 else "train_mini"
        paths = resolve_dataset(name)
        print(paths.summary())
