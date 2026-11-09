#!/usr/bin/env python3
"""
scripts/download_dataset.py - Robust Dataset Downloader & Normalizer for Google Colab.

Solves common Colab dataset issues:
1. Google Drive rate limits and 'gdown --folder' failures.
2. Nested folder confusion (e.g., train/train vs train).
3. Slow Google Drive FUSE I/O by copying to fast local storage (/content/).
4. Missing file validation & health check before starting training/inference.
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys
import zipfile
from typing import Optional, List, Tuple


def log(msg: str, status: str = "INFO"):
    icons = {
        "INFO": "ℹ️ ",
        "SUCCESS": "✅ ",
        "WARNING": "⚠️ ",
        "ERROR": "❌ ",
        "STEP": "🚀 "
    }
    icon = icons.get(status, "")
    print(f"{icon}[{status}] {msg}")


def run_cmd(cmd: List[str], check: bool = True) -> int:
    cmd_str = " ".join(cmd)
    log(f"Executing: {cmd_str}")
    res = subprocess.run(cmd)
    if check and res.returncode != 0:
        raise RuntimeError(f"Command failed with return code {res.returncode}: {cmd_str}")
    return res.returncode


def extract_zip(zip_path: str, extract_to: str):
    log(f"Extracting '{zip_path}' to '{extract_to}'...", "STEP")
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    log(f"Extracted successfully: {zip_path}", "SUCCESS")


def find_files_recursive(search_dir: str, target_filename: str) -> List[str]:
    """Finds all paths containing target_filename."""
    matches = []
    for root, _, files in os.walk(search_dir):
        if target_filename in files:
            matches.append(os.path.join(root, target_filename))
    return matches


def find_dirs_recursive(search_dir: str, target_dirname: str) -> List[str]:
    """Finds all directories named target_dirname."""
    matches = []
    for root, dirs, _ in os.walk(search_dir):
        if target_dirname in dirs:
            matches.append(os.path.join(root, target_dirname))
    return matches


def auto_restructure_dataset(raw_dir: str, target_base: str):
    """
    Scans raw_dir for train and public_test files and normalizes them into:
      <target_base>/train/train/
        - questions.jsonl, calendar.csv, rulebook.md, (answers.jsonl), data/
      <target_base>/public_test/public_test/
        - questions.jsonl, calendar.csv, rulebook.md, data/
    """
    log("Scanning and normalizing dataset directory structure...", "STEP")

    # Find all questions.jsonl
    q_files = find_files_recursive(raw_dir, "questions.jsonl")
    log(f"Found {len(q_files)} questions.jsonl file(s): {q_files}")

    splits_found = {}
    for qf in q_files:
        parent = os.path.dirname(qf)
        parent_lower = parent.lower()
        if "public_test" in parent_lower or "public" in parent_lower:
            splits_found["public_test"] = parent
        elif "train" in parent_lower:
            splits_found["train"] = parent
        else:
            # Check if answers.jsonl exists (train has answers)
            if os.path.exists(os.path.join(parent, "answers.jsonl")):
                splits_found["train"] = parent
            else:
                splits_found["public_test"] = parent

    for split_name, source_folder in splits_found.items():
        dest_folder = os.path.join(target_base, split_name, split_name)
        log(f"Normalizing '{split_name}' from '{source_folder}' -> '{dest_folder}'...")
        os.makedirs(dest_folder, exist_ok=True)

        # Copy essential files
        for fname in ["questions.jsonl", "calendar.csv", "rulebook.md", "answers.jsonl"]:
            src_file = os.path.join(source_folder, fname)
            dst_file = os.path.join(dest_folder, fname)
            if os.path.exists(src_file) and not os.path.exists(dst_file):
                log(f"Copying {fname} to {dest_folder}")
                shutil.copy2(src_file, dst_file)

        # Copy or symlink business data directory
        src_data = os.path.join(source_folder, "data")
        dst_data = os.path.join(dest_folder, "data")
        if os.path.exists(src_data) and not os.path.exists(dst_data):
            log(f"Linking/Copying data folder to {dst_data}")
            try:
                os.symlink(src_data, dst_data)
            except (OSError, AttributeError):
                shutil.copytree(src_data, dst_data)


def validate_and_health_check(target_base: str):
    """Checks the dataset integrity and reports item counts."""
    log("Running integrity health check on normalized dataset...", "STEP")
    all_ok = True

    for split_name in ["train", "public_test"]:
        split_dir = os.path.join(target_base, split_name, split_name)
        if not os.path.exists(split_dir):
            log(f"Split directory not found: {split_dir}", "WARNING")
            continue

        q_path = os.path.join(split_dir, "questions.jsonl")
        c_path = os.path.join(split_dir, "calendar.csv")
        r_path = os.path.join(split_dir, "rulebook.md")
        a_path = os.path.join(split_dir, "answers.jsonl")
        d_path = os.path.join(split_dir, "data")

        # Check required files
        missing = []
        if not os.path.exists(q_path): missing.append("questions.jsonl")
        if not os.path.exists(c_path): missing.append("calendar.csv")
        if not os.path.exists(r_path): missing.append("rulebook.md")
        if not os.path.exists(d_path): missing.append("data/")
        if split_name == "train" and not os.path.exists(a_path):
            missing.append("answers.jsonl")

        if missing:
            log(f"[{split_name}] Missing critical files: {missing}", "ERROR")
            all_ok = False
        else:
            # Count questions
            with open(q_path, "r", encoding="utf-8") as f:
                num_q = sum(1 for _ in f)
            num_biz = len([d for d in os.listdir(d_path) if os.path.isdir(os.path.join(d_path, d))])
            log(f"[{split_name}] OK! Questions: {num_q} | Businesses: {num_biz} in '{split_dir}'", "SUCCESS")

    if all_ok:
        log("All dataset splits are verified and ready for training/inference!", "SUCCESS")
    else:
        log("Health check finished with warnings/errors. Please inspect logs above.", "WARNING")


def download_with_gdown_folder(folder_url: str, output_dir: str):
    """Downloads folder using gdown with retry logic."""
    log("Attempting folder download via gdown...", "STEP")
    try:
        import gdown
    except ImportError:
        run_cmd([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "gdown"])
        import gdown

    os.makedirs(output_dir, exist_ok=True)
    # Use gdown.download_folder
    log(f"Downloading from {folder_url} -> {output_dir}")
    try:
        gdown.download_folder(url=folder_url, output=output_dir, quiet=False, remaining_ok=True)
    except Exception as e:
        log(f"gdown folder download failed: {e}", "WARNING")
        log("Tip: Google Drive frequently rate-limits folder downloads. Use Google Drive Mount or single zip download instead.", "WARNING")
        raise


def download_with_gdown_file(file_id_or_url: str, output_path: str):
    """Downloads single file/zip using gdown."""
    try:
        import gdown
    except ImportError:
        run_cmd([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "gdown"])
        import gdown

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    log(f"Downloading file with gdown: {file_id_or_url} -> {output_path}", "STEP")
    gdown.download(file_id_or_url, output=output_path, quiet=False, fuzzy=True)


def search_drive_for_dataset() -> Optional[str]:
    """Looks for dataset files in standard Google Drive mount locations."""
    drive_mount_root = "/content/drive/MyDrive"
    if not os.path.exists(drive_mount_root):
        return None

    # Look for zip archives
    patterns = [
        "**/*train*.zip",
        "**/*DataMate*.zip",
        "**/*zalo*.zip",
        "**/*LifeMate*.zip",
    ]
    for pat in patterns:
        matches = glob.glob(os.path.join(drive_mount_root, pat), recursive=True)
        if matches:
            log(f"Found dataset archive in Google Drive: {matches[0]}", "SUCCESS")
            return matches[0]

    # Look for existing folders containing questions.jsonl
    q_matches = glob.glob(os.path.join(drive_mount_root, "**/questions.jsonl"), recursive=True)
    if q_matches:
        base = os.path.dirname(q_matches[0])
        log(f"Found dataset folder in Google Drive: {base}", "SUCCESS")
        return base

    return None


def main():
    parser = argparse.ArgumentParser(description="Reliable Dataset Downloader & Normalizer for Colab")
    parser.add_argument("--mode", choices=["auto", "mount", "gdown_folder", "gdown_file", "local_zip", "check_only"],
                        default="auto", help="Download/acquisition mode")
    parser.add_argument("--url", default="https://drive.google.com/drive/folders/1sMB8d47li018WyG_SsXIZJ02jfL8OaLi",
                        help="Google Drive folder or file URL")
    parser.add_argument("--file_id", default=None, help="Google Drive File ID for zip")
    parser.add_argument("--zip_path", default=None, help="Path to local or mounted zip file")
    parser.add_argument("--target_base", default="/content/dataset_gdrive",
                        help="Target base directory expected by datasets.yaml")
    parser.add_argument("--temp_dir", default="/content/raw_download",
                        help="Temporary directory for raw downloads/extractions")

    args = parser.parse_args()

    os.makedirs(args.target_base, exist_ok=True)
    os.makedirs(args.temp_dir, exist_ok=True)

    if args.mode == "check_only":
        validate_and_health_check(args.target_base)
        return

    # 1. Check if dataset is already in target_base and valid
    train_q = os.path.join(args.target_base, "train", "train", "questions.jsonl")
    if os.path.exists(train_q):
        log("Existing dataset detected at target base. Verifying...", "INFO")
        try:
            validate_and_health_check(args.target_base)
            log("Dataset is already present and valid! Skipping re-download.", "SUCCESS")
            return
        except Exception:
            log("Existing dataset validation failed. Proceeding with download/refresh.", "WARNING")

    # Mode AUTO logic:
    # 1. First check if Google Drive is mounted and contains zip/data
    # 2. Check if local zip exists
    # 3. Fallback to gdown folder/file
    if args.mode == "auto":
        found_in_drive = search_drive_for_dataset()
        if found_in_drive:
            if found_in_drive.endswith(".zip"):
                args.mode = "local_zip"
                args.zip_path = found_in_drive
            else:
                args.mode = "mount"
                args.zip_path = found_in_drive
        elif args.zip_path and os.path.exists(args.zip_path):
            args.mode = "local_zip"
        elif args.file_id:
            args.mode = "gdown_file"
        else:
            args.mode = "gdown_folder"

    log(f"Running in mode: {args.mode}", "STEP")

    if args.mode == "local_zip" or (args.mode == "mount" and args.zip_path and args.zip_path.endswith(".zip")):
        if not args.zip_path or not os.path.exists(args.zip_path):
            raise FileNotFoundError(f"Zip file not found: {args.zip_path}")
        extract_zip(args.zip_path, args.temp_dir)
        auto_restructure_dataset(args.temp_dir, args.target_base)

    elif args.mode == "mount":
        # Copy from mounted drive directory
        src = args.zip_path or "/content/drive/MyDrive/ZaloAI_DataMate"
        if not os.path.exists(src):
            raise FileNotFoundError(f"Mounted Drive folder not found: {src}")
        auto_restructure_dataset(src, args.target_base)

    elif args.mode == "gdown_file":
        zip_dest = os.path.join(args.temp_dir, "dataset.zip")
        download_with_gdown_file(args.file_id or args.url, zip_dest)
        extract_zip(zip_dest, args.temp_dir)
        auto_restructure_dataset(args.temp_dir, args.target_base)

    elif args.mode == "gdown_folder":
        try:
            download_with_gdown_folder(args.url, args.temp_dir)
            auto_restructure_dataset(args.temp_dir, args.target_base)
        except Exception as e:
            log(f"Failed to download folder automatically: {e}", "ERROR")
            print("\n" + "=" * 65)
            print("🚨 KHẮC PHỤC LỖI TẢI DATASET GOOGLE DRIVE TRÊN COLAB:")
            print("Google Drive thường xuyên chặn / giới hạn tốc độ khi tải cả thư mục.")
            print("👉 CÁCH GIẢI QUYẾT TỐT NHẤT (100% THÀNH CÔNG):")
            print("  1. Mở link Google Drive trên trình duyệt, bấm Tải xuống (Download zip).")
            print("  2. Upload file zip vào Google Drive cá nhân của bạn (ví dụ MyDrive/train.zip).")
            print("  3. Trong Colab, chạy:")
            print("       from google.colab import drive")
            print("       drive.mount('/content/drive')")
            print("       !python scripts/download_dataset.py --mode auto")
            print("=" * 65 + "\n")
            raise

    # Final health check
    validate_and_health_check(args.target_base)


if __name__ == "__main__":
    main()
