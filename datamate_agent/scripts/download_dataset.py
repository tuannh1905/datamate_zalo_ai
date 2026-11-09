#!/usr/bin/env python3
"""
scripts/download_dataset.py - Universal Dataset Downloader & Normalizer for Google Colab.

Designed for running across multiple Google Colab accounts without mounting Google Drive:
1. Direct URL / Google Drive link download (single zip or folder).
2. Hugging Face Dataset repository snapshot download.
3. Multi-link support (download train.zip and public_test.zip together).
4. Auto-unzipping, folder restructuring, and dataset health check.
5. Zero dependency on Google Drive mount: works uniformly across any email / account.
"""

import argparse
import fnmatch
import glob
import os
import shutil
import subprocess
import sys
import urllib.request
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
                    "Nếu muốn huấn luyện (train model), hãy tải thêm bộ 'train'.", "WARNING")
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


DEFAULT_DATASET_URLS = [
    # Google Drive verified shared links for Zalo AI DataMate challenge:
    "https://drive.google.com/file/d/1dhbhv0QoXuukOfO3F7sHAX90MOcqwIR7/view?usp=sharing",  # train.zip (~128MB)
    "https://drive.google.com/file/d/1ONecKKdJ9FEbb83LbmUMnfK_YA6iRzU3/view?usp=sharing",  # public_test.zip (~64MB)
]


def download_url_to_file(url: str, dest_path: str):
    """Downloads from direct URL or Google Drive link."""
    url = url.strip()
    if not url:
        return

    # 1. Google Drive link handling
    if "drive.google.com" in url or "docs.google.com" in url:
        try:
            import gdown
        except ImportError:
            run_cmd([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "gdown"])
            import gdown

        if "/drive/folders/" in url or "/folders/" in url:
            log(f"Downloading Google Drive folder: {url} -> {dest_path}", "STEP")
            os.makedirs(dest_path, exist_ok=True)
            gdown.download_folder(url=url, output=dest_path, quiet=False, remaining_ok=True)
        else:
            log(f"Downloading Google Drive file: {url} -> {dest_path}", "STEP")
            os.makedirs(os.path.dirname(os.path.abspath(dest_path)), exist_ok=True)
            gdown.download(url=url, output=dest_path, quiet=False, fuzzy=True)
        return

    # 2. Dropbox link handling
    if "dropbox.com" in url:
        url = url.replace("?dl=0", "?dl=1")
        if "?dl=1" not in url:
            url += "?dl=1"

    # 3. Direct HTTP/HTTPS download
    log(f"Downloading from link: {url} -> {dest_path}", "STEP")
    os.makedirs(os.path.dirname(os.path.abspath(dest_path)), exist_ok=True)
    try:
        # Use curl if available for speed and resumable support
        run_cmd(["curl", "-L", "-C", "-", url, "-o", dest_path])
    except Exception:
        # Fallback to urllib
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, dest_path)
    log(f"Download completed: {dest_path}", "SUCCESS")


def download_hf_dataset(repo_id: str, dest_dir: str, token: Optional[str] = None):
    """Downloads dataset from Hugging Face Hub (fast, no rate-limits, multi-account friendly)."""
    log(f"Downloading from Hugging Face Hub: {repo_id} -> {dest_dir}", "STEP")
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        run_cmd([sys.executable, "-m", "pip", "install", "-q", "huggingface_hub"])
        from huggingface_hub import snapshot_download

    os.makedirs(dest_dir, exist_ok=True)
    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        local_dir=dest_dir,
        token=token,
        local_dir_use_symlinks=False
    )
    log(f"Hugging Face dataset downloaded successfully into: {dest_dir}", "SUCCESS")


def main():
    parser = argparse.ArgumentParser(description="Universal Dataset Downloader & Normalizer for Colab (Link-based, Multi-account)")
    parser.add_argument("--url", action="append", default=[],
                        help="Direct download URL or Google Drive link (can specify multiple times or comma-separated)")
    parser.add_argument("--hf_repo", default=None,
                        help="Hugging Face Dataset repo ID (e.g. username/zalo_dataset)")
    parser.add_argument("--hf_token", default=None,
                        help="Hugging Face API token (if repo is private)")
    parser.add_argument("--mode", choices=["auto", "url", "hf", "mount", "local_zip", "check_only"],
                        default="auto", help="Download mode")
    parser.add_argument("--zip_path", default=None, help="Path to local or mounted zip file")
    parser.add_argument("--drive_dir", default=None, help="Folder inside Google Drive (if mounted)")
    parser.add_argument("--target_base", "--output_dir", dest="target_base", default="/content/dataset_gdrive",
                        help="Target base directory expected by datasets.yaml (alias: --output_dir)")
    parser.add_argument("--temp_dir", default="/content/raw_download",
                        help="Temporary directory for raw downloads/extractions")

    args = parser.parse_args()

    os.makedirs(args.target_base, exist_ok=True)
    os.makedirs(args.temp_dir, exist_ok=True)

    if args.mode == "check_only":
        validate_and_health_check(args.target_base)
        return

    # Collect URLs from arguments or environment variable DATASET_URL
    urls = []
    if args.url:
        for u in args.url:
            for sub_u in u.split(","):
                sub_u = sub_u.strip()
                if sub_u:
                    urls.append(sub_u)
    elif os.environ.get("DATASET_URL"):
        for sub_u in os.environ["DATASET_URL"].split(","):
            sub_u = sub_u.strip()
            if sub_u:
                urls.append(sub_u)

    # Determine mode
    if args.mode == "auto":
        if args.hf_repo:
            args.mode = "hf"
        elif urls:
            args.mode = "url"
        elif args.zip_path and os.path.exists(args.zip_path):
            args.mode = "local_zip"
        elif args.drive_dir and os.path.exists(args.drive_dir):
            args.mode = "mount"
        elif os.path.exists("/content/drive/MyDrive/zalo_ai_data"):
            args.mode = "mount"
        else:
            # Check if dataset is already valid in target_base
            train_q = os.path.join(args.target_base, "train", "train", "questions.jsonl")
            if os.path.exists(train_q):
                args.mode = "check_only"
            else:
                args.mode = "url"

    log(f"Running downloader in mode: [{args.mode}]", "STEP")

    search_dirs = [args.temp_dir]

    if args.mode == "hf":
        if not args.hf_repo:
            raise ValueError("Please provide --hf_repo (e.g. --hf_repo username/zalo_dataset)")
        download_hf_dataset(args.hf_repo, args.temp_dir, args.hf_token)
        search_dirs.append(args.temp_dir)

    elif args.mode == "url":
        if not urls:
            log("No custom URL provided. Using verified default Google Drive dataset links...", "INFO")
            urls = DEFAULT_DATASET_URLS

        for idx, u in enumerate(urls):
            # Check if URL is a zip archive
            is_zip = any(u.lower().endswith(ext) for ext in [".zip", ".tar", ".gz"]) or ("drive.google.com" in u and "/folders/" not in u)
            if is_zip:
                dest_file = os.path.join(args.temp_dir, f"dataset_part_{idx}.zip")
                download_url_to_file(u, dest_file)
                extract_zip(dest_file, os.path.join(args.temp_dir, f"part_{idx}"))
                search_dirs.append(os.path.join(args.temp_dir, f"part_{idx}"))
            else:
                folder_dest = os.path.join(args.temp_dir, f"folder_part_{idx}")
                download_url_to_file(u, folder_dest)
                search_dirs.append(folder_dest)

    elif args.mode == "local_zip":
        if not args.zip_path or not os.path.exists(args.zip_path):
            raise FileNotFoundError(f"Zip file not found: {args.zip_path}")
        extract_zip(args.zip_path, args.temp_dir)
        search_dirs.append(args.temp_dir)

    elif args.mode == "mount":
        drive_root = args.drive_dir or "/content/drive/MyDrive/zalo_ai_data"
        if not os.path.exists(drive_root):
            drive_root = "/content/drive/MyDrive"
        search_dirs.append(drive_root)

    # Restructure & Validate
    auto_restructure_dataset(search_dirs, args.target_base)
    validate_and_health_check(args.target_base)


if __name__ == "__main__":
    main()
