#!/usr/bin/env python3
"""
scripts/download_dataset.py - Robust Dataset Downloader & Normalizer for Google Colab.

Solves common Colab dataset issues:
1. Google Drive rate limits and 'gdown --folder' failures.
2. Nested folder confusion (e.g., train/train vs train).
3. Scanning all splits (both train and public_test) across Google Drive.
4. Auto-unzipping any .zip archives found on Google Drive.
5. Slow Google Drive FUSE I/O by copying to fast local storage (/content/).
6. Health check & clear status reporting for both train and public_test splits.
"""

import argparse
import fnmatch
import glob
import os
import shutil
import subprocess
import sys
import zipfile
from typing import Optional, List, Dict, Set


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
    """Finds all paths containing target_filename (case-insensitive)."""
    matches = []
    target_lower = target_filename.lower()
    for root, _, files in os.walk(search_dir):
        for f in files:
            if f.lower() == target_lower:
                matches.append(os.path.join(root, f))
    return matches


def find_zip_archives(search_dir: str) -> List[str]:
    """Finds dataset-specific zip files in search_dir (strictly filtered)."""
    zip_files = []
    # Only match exact dataset keywords - never generic '*.zip'
    strict_patterns = ["*train*.zip", "*public*.zip", "*zalo*.zip", "*datamate*.zip"]
    for root, _, files in os.walk(search_dir):
        for f in files:
            f_lower = f.lower()
            if f_lower.endswith(".zip"):
                for pat in strict_patterns:
                    if fnmatch.fnmatch(f_lower, pat):
                        zip_files.append(os.path.join(root, f))
                        break
    return list(set(zip_files))


def auto_restructure_dataset(search_dirs: List[str], target_base: str):
    """
    Scans all search_dirs for train and public_test files and normalizes them into:
      <target_base>/train/train/
        - questions.jsonl, calendar.csv, rulebook.md, answers.jsonl, data/
      <target_base>/public_test/public_test/
        - questions.jsonl, calendar.csv, rulebook.md, data/
    """
    log("Scanning and normalizing dataset directory structure...", "STEP")

    all_q_files = []
    for s_dir in search_dirs:
        if os.path.exists(s_dir):
            all_q_files.extend(find_files_recursive(s_dir, "questions.jsonl"))

    all_q_files = list(set(all_q_files))
    log(f"Found {len(all_q_files)} questions.jsonl file(s): {all_q_files}")

    splits_found: Dict[str, str] = {}
    for qf in all_q_files:
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
            if os.path.exists(src_file):
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

    has_train = False
    has_public = False

    for split_name in ["train", "public_test"]:
        split_dir = os.path.join(target_base, split_name, split_name)
        if not os.path.exists(split_dir):
            if split_name == "train":
                log(f"Split directory not found: {split_dir}", "WARNING")
                log("👉 Lưu ý: Chưa có bộ 'train'. Bạn có thể chạy eval/test trên 'public_test'. "
                    "Nếu muốn huấn luyện (train model), hãy upload thư mục 'train' hoặc 'train.zip' lên Google Drive.", "WARNING")
            else:
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
        else:
            with open(q_path, "r", encoding="utf-8") as f:
                num_q = sum(1 for _ in f)
            num_biz = len([d for d in os.listdir(d_path) if os.path.isdir(os.path.join(d_path, d))])
            log(f"[{split_name}] OK! Questions: {num_q} | Businesses: {num_biz} in '{split_dir}'", "SUCCESS")
            if split_name == "train":
                has_train = True
            elif split_name == "public_test":
                has_public = True

    if has_train and has_public:
        log("Tất cả bộ dữ liệu (train & public_test) đã sẵn sàng 100%!", "SUCCESS")
    elif has_public:
        log("Bộ dữ liệu public_test đã sẵn sàng để kiểm thử và chấm điểm!", "SUCCESS")


def scan_and_extract_drive(drive_mount_root: str, temp_dir: str) -> List[str]:
    """
    Scans Google Drive for any zip files and unzips them.
    Returns list of search candidate directories.
    """
    search_dirs = [drive_mount_root]

    # Look for zip archives and extract
    zips = find_zip_archives(drive_mount_root)
    for z in zips:
        base_name = os.path.splitext(os.path.basename(z))[0]
        ext_target = os.path.join(temp_dir, base_name)
        if not os.path.exists(ext_target):
            try:
                extract_zip(z, ext_target)
                search_dirs.append(ext_target)
            except Exception as e:
                log(f"Failed to extract zip {z}: {e}", "WARNING")
        else:
            search_dirs.append(ext_target)

    return search_dirs


def download_with_gdown_folder(folder_url: str, output_dir: str):
    """Downloads folder using gdown with retry logic."""
    log("Attempting folder download via gdown...", "STEP")
    try:
        import gdown
    except ImportError:
        run_cmd([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "gdown"])
        import gdown

    os.makedirs(output_dir, exist_ok=True)
    log(f"Downloading from {folder_url} -> {output_dir}")
    try:
        gdown.download_folder(url=folder_url, output=output_dir, quiet=False, remaining_ok=True)
    except Exception as e:
        log(f"gdown folder download failed: {e}", "WARNING")
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


def main():
    parser = argparse.ArgumentParser(description="Reliable Dataset Downloader & Normalizer for Colab")
    parser.add_argument("--mode", choices=["auto", "mount", "gdown_folder", "gdown_file", "local_zip", "check_only"],
                        default="auto", help="Download/acquisition mode")
    parser.add_argument("--url", default="https://drive.google.com/drive/folders/1sMB8d47li018WyG_SsXIZJ02jfL8OaLi",
                        help="Google Drive folder or file URL")
    parser.add_argument("--file_id", default=None, help="Google Drive File ID for zip")
    parser.add_argument("--zip_path", default=None, help="Path to local or mounted zip file")
    parser.add_argument("--drive_dir", default=None, help="Specific folder inside Google Drive to scan")
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

    # Check mode AUTO logic
    if args.mode == "auto":
        # Check if Google Drive is mounted
        drive_root = args.drive_dir or "/content/drive/MyDrive"
        if os.path.exists(drive_root):
            args.mode = "mount"
        elif args.zip_path and os.path.exists(args.zip_path):
            args.mode = "local_zip"
        elif args.file_id:
            args.mode = "gdown_file"
        else:
            args.mode = "gdown_folder"

    log(f"Running in mode: {args.mode}", "STEP")

    if args.mode == "mount":
        drive_root = args.drive_dir
        if not drive_root:
            # Check for dedicated competition folders first
            for cand in ["/content/drive/MyDrive/zalo_ai_data", "/content/drive/MyDrive/ZaloAI_DataMate", "/content/drive/MyDrive/DataMate"]:
                if os.path.exists(cand):
                    drive_root = cand
                    log(f"Found dedicated dataset folder in Drive: {drive_root}", "SUCCESS")
                    break
            if not drive_root:
                drive_root = "/content/drive/MyDrive"

        # Check if drive_root already contains questions.jsonl
        existing_q = find_files_recursive(drive_root, "questions.jsonl")
        search_dirs = [drive_root]

        # Only search for and extract zips if questions.jsonl files are missing
        if not existing_q:
            log("No questions.jsonl directly found, checking for dataset zip archives...", "INFO")
            search_dirs = scan_and_extract_drive(drive_root, args.temp_dir)

        auto_restructure_dataset(search_dirs, args.target_base)

    elif args.mode == "local_zip":
        if not args.zip_path or not os.path.exists(args.zip_path):
            raise FileNotFoundError(f"Zip file not found: {args.zip_path}")
        extract_zip(args.zip_path, args.temp_dir)
        auto_restructure_dataset([args.temp_dir], args.target_base)

    elif args.mode == "gdown_file":
        zip_dest = os.path.join(args.temp_dir, "dataset.zip")
        download_with_gdown_file(args.file_id or args.url, zip_dest)
        extract_zip(zip_dest, args.temp_dir)
        auto_restructure_dataset([args.temp_dir], args.target_base)

    elif args.mode == "gdown_folder":
        try:
            download_with_gdown_folder(args.url, args.temp_dir)
            auto_restructure_dataset([args.temp_dir], args.target_base)
        except Exception as e:
            log(f"Failed to download folder automatically: {e}", "ERROR")
            print("\n" + "=" * 65)
            print("🚨 KHẮC PHỤC LỖI TẢI DATASET GOOGLE DRIVE TRÊN COLAB:")
            print("Google Drive thường xuyên chặn / giới hạn tốc độ khi tải cả thư mục.")
            print("👉 CÁCH GIẢI QUYẾT TỐT NHẤT (100% THÀNH CÔNG):")
            print("  1. Upload file 'train.zip' hoặc folder 'train' vào Google Drive.")
            print("  2. Trong Colab, chạy:")
            print("       from google.colab import drive")
            print("       drive.mount('/content/drive')")
            print("       !python scripts/download_dataset.py --mode auto")
            print("=" * 65 + "\n")
            raise

    # Final health check
    validate_and_health_check(args.target_base)


if __name__ == "__main__":
    main()
