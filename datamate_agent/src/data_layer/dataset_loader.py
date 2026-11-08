"""
Dataset Loader & Google Drive Auto-Caching Module for DataMate Challenge.
Optimizes I/O on Google Colab by copying messy tabular data (CSVs, XLSX, SQLite)
from slow Google Drive (/content/drive/) to fast local NVMe (/content/local_data/).
Provides dataset routing across splits (train, public_test, private_test).
"""

import logging
import os
import shutil
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class DatasetPaths:
    dataset_name: str
    root_dir: str
    data_dir: str
    questions_path: str
    rulebook_path: str
    calendar_path: str
    answers_path: Optional[str] = None
    is_cached: bool = False

    def validate(self) -> None:
        """
        Validates that required files and directories exist.
        """
        if not os.path.exists(self.questions_path):
            raise FileNotFoundError(f"Missing required questions file: {self.questions_path}")
        if not os.path.exists(self.rulebook_path):
            raise FileNotFoundError(f"Missing required rulebook file: {self.rulebook_path}")
        if not os.path.exists(self.calendar_path):
            raise FileNotFoundError(f"Missing required calendar file: {self.calendar_path}")
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError(f"Missing required business data directory: {self.data_dir}")

    def summary(self) -> str:
        return (
            f"Dataset [{self.dataset_name}] Loaded:\n"
            f"  - Active Root   : {self.root_dir} (Cached locally: {self.is_cached})\n"
            f"  - Data Dir      : {self.data_dir}\n"
            f"  - Questions     : {self.questions_path}\n"
            f"  - Rulebook      : {self.rulebook_path}\n"
            f"  - Calendar      : {self.calendar_path}\n"
            f"  - Answers (Gold): {self.answers_path or 'Not provided'}"
        )


def _find_file_or_nested(base_dir: str, filename: str, split_name: Optional[str] = None) -> Optional[str]:
    """
    Looks for a file directly in base_dir, or in base_dir/<split_name>/, or any subfolder.
    """
    # 1. Direct check
    direct = os.path.join(base_dir, filename)
    if os.path.exists(direct):
        return direct

    # 2. Split subfolder check (e.g. train/train/questions.jsonl)
    if split_name:
        nested = os.path.join(base_dir, split_name, filename)
        if os.path.exists(nested):
            return nested

    # 3. Check any direct subdirectory
    if os.path.exists(base_dir):
        for entry in os.listdir(base_dir):
            sub = os.path.join(base_dir, entry)
            if os.path.isdir(sub):
                cand = os.path.join(sub, filename)
                if os.path.exists(cand):
                    return cand

    return None


def _find_dir_or_nested(base_dir: str, dirname: str, split_name: Optional[str] = None) -> Optional[str]:
    """
    Looks for a directory directly in base_dir, or in base_dir/<split_name>/, or any subfolder.
    """
    direct = os.path.join(base_dir, dirname)
    if os.path.exists(direct) and os.path.isdir(direct):
        return direct

    if split_name:
        nested = os.path.join(base_dir, split_name, dirname)
        if os.path.exists(nested) and os.path.isdir(nested):
            return nested

    if os.path.exists(base_dir):
        for entry in os.listdir(base_dir):
            sub = os.path.join(base_dir, entry)
            if os.path.isdir(sub):
                cand = os.path.join(sub, dirname)
                if os.path.exists(cand) and os.path.isdir(cand):
                    return cand

    return None


def is_already_cached(cache_dir: str, dataset_name: str) -> bool:
    """
    Checks if the local cache directory exists and contains key dataset files.
    """
    if not os.path.exists(cache_dir):
        return False

    q_file = _find_file_or_nested(cache_dir, "questions.jsonl", dataset_name)
    c_file = _find_file_or_nested(cache_dir, "calendar.csv", dataset_name)
    d_dir = _find_dir_or_nested(cache_dir, "data", dataset_name)

    return bool(q_file and c_file and d_dir)


def load_dataset(
    dataset: str,
    drive_base_path: str = "/content/drive/MyDrive/ZaloAI_DataMate",
    local_cache_root: str = "/content/local_data",
    force_cache: bool = False,
) -> DatasetPaths:
    """
    Loads dataset split from drive_base_path.
    If on Google Drive (/content/drive/), automatically copies data to fast local NVMe storage.
    Returns resolved DatasetPaths object.
    """
    # 1. Determine Source Path
    source_path = os.path.join(drive_base_path, dataset)

    if not os.path.exists(source_path):
        # Also check if drive_base_path already IS the dataset folder
        if os.path.basename(os.path.normpath(drive_base_path)) == dataset and os.path.exists(drive_base_path):
            source_path = drive_base_path
        else:
            raise FileNotFoundError(
                f"\n[DatasetLoader Error] Source dataset path does not exist:\n  --> '{source_path}'\n"
                f"Please ensure:\n"
                f"  1. If running on Google Colab, mount Google Drive before running:\n"
                f"       from google.colab import drive\n"
                f"       drive.mount('/content/drive')\n"
                f"  2. Verify '--drive_base_path' ({drive_base_path}) and '--dataset' ({dataset}) match your Drive folders.\n"
                f"     Example: /content/drive/MyDrive/ZaloAI_DataMate/{dataset}\n"
            )

    # 2. Check if caching is required (Google Drive path or forced)
    is_drive = (
        source_path.startswith("/content/drive")
        or "/content/drive/" in source_path
        or "\\content\\drive" in source_path
        or force_cache
    )

    is_cached = False
    active_dir = source_path

    if is_drive:
        target_cache_dir = os.path.join(local_cache_root, dataset)
        if is_already_cached(target_cache_dir, dataset):
            logger.info(f"[DatasetLoader] Dataset '{dataset}' is already cached at fast local NVMe: {target_cache_dir}")
            active_dir = target_cache_dir
            is_cached = True
        else:
            logger.info(f"[DatasetLoader] I/O Optimization: Copying '{dataset}' from Drive ({source_path}) to fast local NVMe ({target_cache_dir})...")
            os.makedirs(target_cache_dir, exist_ok=True)
            try:
                shutil.copytree(source_path, target_cache_dir, dirs_exist_ok=True)
                logger.info(f"[DatasetLoader] Copy completed! Pipeline will query fast local path.")
                active_dir = target_cache_dir
                is_cached = True
            except Exception as e:
                logger.warning(f"[DatasetLoader] Warning during copy: {e}. Falling back to source path.")
                active_dir = source_path
                is_cached = False
    else:
        logger.info(f"[DatasetLoader] Reading directly from local path: {active_dir}")

    # 3. Locate Key Files (supporting both flat and nested structures)
    questions_file = _find_file_or_nested(active_dir, "questions.jsonl", dataset)
    rulebook_file = _find_file_or_nested(active_dir, "rulebook.md", dataset)
    calendar_file = _find_file_or_nested(active_dir, "calendar.csv", dataset)
    answers_file = _find_file_or_nested(active_dir, "answers.jsonl", dataset)
    data_directory = _find_dir_or_nested(active_dir, "data", dataset)

    # Fallbacks if some files are direct
    if not questions_file:
        questions_file = os.path.join(active_dir, "questions.jsonl")
    if not rulebook_file:
        rulebook_file = os.path.join(active_dir, "rulebook.md")
    if not calendar_file:
        calendar_file = os.path.join(active_dir, "calendar.csv")
    if not data_directory:
        data_directory = os.path.join(active_dir, "data")

    paths = DatasetPaths(
        dataset_name=dataset,
        root_dir=active_dir,
        data_dir=data_directory,
        questions_path=questions_file,
        rulebook_path=rulebook_file,
        calendar_path=calendar_file,
        answers_path=answers_file,
        is_cached=is_cached,
    )

    paths.validate()
    logger.info(paths.summary())
    return paths
