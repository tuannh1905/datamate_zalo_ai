# DataMate Agent: Offline Vietnamese Tabular QA System
### Zalo AI Challenge 2024 / 2025 - Small-Business Tabular QA Track

Hệ thống AI Agent tự hành giải quyết bài toán hỏi đáp trên dữ liệu bảng tiếng Việt hỗn tạp (CSV, Excel đa sheet, cơ sở dữ liệu SQLite) của các hộ kinh doanh cá thể tại Việt Nam.

---

## 🚀 Tính năng Nổi bật

- **Kiến trúc Offline-First:** Vận hành hoàn toàn offline trong môi trường Docker hạn chế tài nguyên, tuân thủ chặt chẽ thể lệ cuộc thi.
- **Tối ưu hóa Metric Penalized Accuracy:** 
  - Cơ chế **Biểu quyết Đa số có Ngưỡng An toàn** ($\tau = 0.5$) qua $k=8$ mẫu truy vấn.
  - Tự động kích hoạt thêm 4 mẫu suy luận sâu (Thinking Samples) khi mức độ đồng thuận thấp.
  - Tự động nộp `type: abstain` ($s_i = 0$) khi không đạt ngưỡng an toàn, triệt tiêu nguy cơ bị trừ điểm oan ($-1$).
- **Vòng lặp Huấn luyện Tự học (Iterative Self-Training):**
  - Vòng lặp 3 chu kỳ ($v_1 \to v_2 \to v_3$) kết hợp **Candidate Generation**, **Rejection Sampling**, và **4-bit QLoRA**.
- **Google Drive Auto-Caching:** 
  - Khắc phục nghẽn cổ chai FUSE I/O trên Google Colab bằng cách tự động sao chép dữ liệu sang bộ nhớ cục bộ NVMe siêu tốc (`/content/local_data/`).
- **Xử lý Đặc thù Kinh doanh Việt Nam:**
  - Chuẩn hóa định dạng tiền tệ (`560,000`, `25.000đ`), ngày tháng đa chuẩn, quy đổi đơn vị (thùng/hộp/cái), lịch Tết âm - dương theo `rulebook.md` và `calendar.csv`.

---

## 📂 Cấu trúc Thư mục

```
datamate_agent/
├── configs/
│   └── config.yaml           # Cấu hình siêu tham số agent & pipeline
├── prompts/
│   ├── sql_rules_system.txt  # System prompt tạo SQL & quy tắc nghiệp vụ
│   ├── view_drafting.txt     # Prompt tạo DuckDB Unified Views
│   ├── qa_user_template.txt  # Mẫu template câu hỏi người dùng
│   └── debt_macros.txt       # Macro xử lý công nợ & thanh toán nợ
├── src/
│   ├── context/              # Date resolver, prompt builder, rulebook parser
│   ├── data_layer/           # Dataset loader, DuckDB ingest, view builder
│   ├── inference/            # LLM engine, execution & majority voting
│   ├── training/             # Candidate generation, rejection sampling, QLoRA
│   ├── evaluator.py          # Hàm chấm điểm chuẩn xác theo thể lệ
│   └── run_inference.py      # Entrypoint chính chạy suy luận
├── scripts/
│   ├── setup_colab.sh        # Cài đặt môi trường GPU trên Colab
│   ├── run_self_training.sh  # Chạy vòng lặp tự huấn luyện 3 chu kỳ
│   └── run_eval.py           # Đánh giá độ chính xác & Penalized Accuracy
├── Dockerfile                # Dockerfile nộp bài chính thức
├── predict.sh                # Entrypoint script cho Docker
└── requirements.txt          # Danh sách thư viện Python
```

---

## 🛠️ Hướng dẫn Chạy trên Google Colab (Huấn luyện & Sinh Mẫu)

### 1. Cài đặt Môi trường
```bash
bash scripts/setup_colab.sh
```

### 2. Tải Dữ liệu từ Google Drive
Dữ liệu cuộc thi (gồm `train` và `public_test`) có thể tải trực tiếp từ Google Drive qua script:
```bash
pip install gdown
gdown --folder "https://drive.google.com/drive/folders/1sMB8d47li018WyG_SsXIZJ02jfL8OaLi" -O ./data_input
```
Hoặc mount Google Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```

### 3. Chạy Vòng lặp Tự huấn luyện (Iterative Self-Training)
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
File kết quả sẽ được xuất tự động ra `/result/submission.jsonl`.
