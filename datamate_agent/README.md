# DataMate Agent: Offline Vietnamese Tabular QA System
### Zalo AI Challenge 2024 / 2025 - Small-Business Tabular QA Track

Hệ thống AI Agent tự hành giải quyết bài toán hỏi đáp trên dữ liệu bảng tiếng Việt hỗn tạp (CSV, Excel đa sheet, cơ sở dữ liệu SQLite) của các hộ kinh doanh cá thể tại Việt Nam.

---

## 🚀 Tính năng Nổi bật & Cải tiến Toàn diện

- **Kiến trúc Offline-First:** Vận hành hoàn toàn offline trong môi trường Docker hạn chế tài nguyên (`HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`), tuân thủ chặt chẽ thể lệ cuộc thi.
- **Dataset Registry Thống nhất (`configs/datasets.yaml`):**
  - Quản lý tập dữ liệu qua một file cấu hình duy nhất: `train`, `public_test`, `private_test`, `train_fit`, `train_holdout`, và `train_mini`.
  - Cơ chế kế thừa `extends`, tự động lọc câu hỏi theo business IDs (`include_business_ids`, `exclude_business_ids`, `limit`) vào `data_cache/` mà không can thiệp vào dữ liệu gốc.
  - Tự động dò tìm thư mục gốc (3 cấp) khi cấu hình đường dẫn bị lệch.
- **Tối ưu hóa Metric Penalized Accuracy:** 
  - Cơ chế **Biểu quyết Đa số có Ngưỡng An toàn** ($\tau = 0.5$) qua $k=8$ mẫu truy vấn.
  - Tự động nộp `type: abstain` ($s_i = 0$) khi không đạt ngưỡng an toàn hoặc dữ liệu thiếu/lỗi, triệt tiêu nguy cơ bị trừ điểm oan ($-1$).
  - Đảm bảo 100% dòng nộp bài tuân thủ schema cuộc thi qua `validate_submission_item()`.
- **DuckDB Dynamic View Builder & Join Tự động:**
  - Tự động nhận diện cấu trúc quan hệ (Header-Detail như `don_hang` + `chi_tiet_don`, hoặc bảng tra cứu `san_pham`, `khach_hang`) và thực hiện kết nối bảng chuẩn xác.
  - Loại bỏ hoàn toàn mặc định sai `ELSE 'hoàn thành'`, giữ nguyên tên trạng thái gốc đối với các trạng thái chưa biết.
  - Chỉ chấp nhận dựng view canonical khi tất cả các cột cốt lõi (ngày, sản phẩm, số lượng, thành tiền) được ánh xạ từ dữ liệu thật (không dùng hằng số giả lập).
  - Tự động fallback về truy vấn bảng gốc khi view không đủ tin cậy.
- **Phân giải Thời gian Đa chuẩn (`DateResolver`):**
  - Chuẩn hóa văn bản không dấu trước khi so khớp regex (`remove_accents`), nhận diện cả tiếng Việt có dấu và không dấu ("tháng 7 năm 2026", "thang 7 nam 2026", "7 ngay gan nhat", "quy 2 nam nay").
  - Xử lý các câu hỏi so sánh hai mốc thời gian ("hôm nay so với hôm qua", "tuần này so với tuần trước", "cùng kỳ").
  - An toàn tuyệt đối: bọc toàn bộ khối tính toán trong `try/except`, không bao giờ bị sập do tháng/ngày không hợp lệ (ví dụ: tháng 13).
- **Vòng lặp Huấn luyện Tự học (Iterative Self-Training):**
  - Vòng lặp 3 chu kỳ ($v_1 \to v_2 \to v_3$) kết hợp **Candidate Generation**, **Rejection Sampling**, và **4-bit QLoRA**.
  - Huấn luyện trên tập `train_fit` và đánh giá khách quan trên tập hold-out (`train_holdout`), loại bỏ triệt để hiện tượng rò rỉ dữ liệu (data leakage).
- **Hệ thống Kiểm thử Toàn diện:**
  - 47 unit tests hoàn chỉnh trong `tests/`, bao phủ mọi khía cạnh: parser số, NFKD tiếng Việt, subtotal, SQL CTE, date resolver, evaluator, registry.

---

## 📂 Cấu trúc Thư mục

```
datamate_agent/
├── configs/
│   ├── config.yaml           # Cấu hình siêu tham số agent & pipeline
│   └── datasets.yaml         # Dataset Registry cấu hình toàn bộ các split
├── prompts/
│   ├── sql_rules_system.txt  # System prompt DuckDB SQL rules (decoupled)
│   ├── view_drafting.txt     # Template sinh canonical views
│   └── qa_user_template.txt  # Mẫu template câu hỏi người dùng
├── src/
│   ├── context/              # Date resolver (không dấu, quý, so sánh), prompt builder
│   ├── data_layer/           # Dataset registry, DuckDB ingest, relational view builder
│   ├── inference/            # LLM engine, execution voter, SQL timeout & safety
│   ├── training/             # Candidate generation, rejection sampling, train_qlora
│   ├── evaluator.py          # Bộ chấm điểm Penalized Accuracy (Proxy Evaluator)
│   └── run_inference.py      # Entrypoint chính chạy suy luận
├── tests/                    # 47 unit tests kiểm chứng hệ thống
├── reports/                  # Data profile train & public_test
├── scripts/
│   ├── setup_colab.sh        # Cài đặt môi trường GPU trên Colab
│   ├── run_self_training.sh  # Chạy vòng lặp tự huấn luyện 3 chu kỳ
│   ├── run_eval.py           # Đánh giá Penalized Accuracy
│   └── inspect_data.py       # Script profiling dữ liệu
├── Dockerfile                # Dockerfile nộp bài chính thức
├── predict.sh                # Entrypoint script cho Docker
├── requirements.txt          # Thư viện Python chung
├── requirements-docker.txt   # Thư viện Python riêng cho Docker (bảo toàn ABI torch/vllm)
└── CHANGES.md                # Nhật ký thay đổi và kiểm chứng chi tiết
```

---

## 🛠️ Hướng dẫn Sử dụng

### 1. Kiểm tra Danh sách Dataset
```bash
python -m src.data_layer.dataset_registry --list_datasets
```

### 2. Chạy Kiểm thử Toàn bộ Hệ thống
```bash
pytest -q
```

### 3. Đánh giá Nhanh trên `train_mini`
```bash
python scripts/run_eval.py --dataset train_mini --run_inference --limit 5
```

### 4. Chạy Suy luận trên `public_test`
```bash
python -m src.run_inference --dataset public_test --limit 20
```

### 5. Chạy Tự huấn luyện trên `train_fit` và Đo trên `train_holdout`
```bash
bash scripts/run_self_training.sh
```

---

## 🐳 Hướng dẫn Chạy Offline với Docker (Chấm thi)

### 1. Build Docker Image
```bash
docker build -t datamate_agent .
```

### 2. Chạy Suy luận Offline
```bash
docker run --gpus all --rm \
    --network none \
    -v /path/to/public_test:/data:ro \
    -v /path/to/result:/result \
    datamate_agent
```
File kết quả sẽ được xuất tự động ra `/result/submission.jsonl` và các file log chi tiết tại `/result/logs/<id>.json`.
