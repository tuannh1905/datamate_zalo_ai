import json
import os
import pytest
from src.data_layer.dataset_registry import (
    get_merged_dataset_config,
    list_datasets,
    load_registry,
    resolve_dataset,
)


def test_load_registry():
    reg = load_registry()
    assert "datasets" in reg
    assert "train" in reg["datasets"]
    assert "public_test" in reg["datasets"]
    assert "train_fit" in reg["datasets"]
    assert "train_holdout" in reg["datasets"]
    assert "train_mini" in reg["datasets"]


def test_extends_inheritance():
    cfg, base_name = get_merged_dataset_config("train_mini")
    assert base_name == "train"
    # Inherited from train
    assert cfg.get("questions") == "questions.jsonl"
    assert cfg.get("rulebook") == "rulebook.md"
    # Specific to train_mini
    assert cfg.get("include_business_ids") == ["biz_101", "biz_102"]
    assert cfg.get("limit") == 20


def test_missing_dataset_raises_error():
    with pytest.raises(ValueError) as exc:
        resolve_dataset("non_existent_dataset_name")
    assert "Unknown dataset" in str(exc.value)


def test_resolve_dataset_filtering(tmp_path):
    # Resolving train_mini filters questions to cache_root/train_mini/questions.jsonl
    paths = resolve_dataset("train_mini", cache_root=str(tmp_path))
    assert os.path.exists(paths.questions_path)
    assert os.path.exists(paths.rulebook_path)
    assert os.path.exists(paths.calendar_path)

    # Check that filtered questions only contain biz_101 and biz_102
    with open(paths.questions_path, "r", encoding="utf-8") as f:
        questions = [json.loads(line) for line in f if line.strip()]

    assert len(questions) <= 20
    for q in questions:
        assert q["business_id"] in ["biz_101", "biz_102"]
