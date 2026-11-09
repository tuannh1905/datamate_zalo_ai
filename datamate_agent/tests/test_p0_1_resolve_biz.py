import os
import shutil
import tempfile
import pytest
from src.data_layer.ingest import resolve_business_dir


def test_resolve_business_dir_direct():
    with tempfile.TemporaryDirectory() as tmpdir:
        biz_dir = os.path.join(tmpdir, "biz_001")
        os.makedirs(biz_dir, exist_ok=True)
        res = resolve_business_dir(tmpdir, "biz_001")
        assert res == os.path.abspath(biz_dir)


def test_resolve_business_dir_nested_data():
    with tempfile.TemporaryDirectory() as tmpdir:
        biz_dir = os.path.join(tmpdir, "data", "biz_002")
        os.makedirs(biz_dir, exist_ok=True)
        res = resolve_business_dir(tmpdir, "biz_002")
        assert res == os.path.abspath(biz_dir)


def test_resolve_business_dir_one_level_down():
    with tempfile.TemporaryDirectory() as tmpdir:
        # e.g. /data/split_root/data/biz_003
        biz_dir = os.path.join(tmpdir, "split_root", "data", "biz_003")
        os.makedirs(biz_dir, exist_ok=True)
        res = resolve_business_dir(tmpdir, "biz_003")
        assert res == os.path.abspath(biz_dir)


def test_resolve_business_dir_missing():
    with tempfile.TemporaryDirectory() as tmpdir:
        res = resolve_business_dir(tmpdir, "biz_nonexistent")
        assert res is None
