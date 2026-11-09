# Data Profile Report: `train`
Total Businesses: 30

## Business `biz_101`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_101  Một file phẳng, mỗi dòng một bản ghi (một dòng hàng trong đơn).  ## File - `ban_hang.csv` (csv)  ## Cột trong `ban_hang.csv` - **Giá bán**: đơn giá - **Kết quả**: trạng thái đơn - **Nội dung**: tên hàng - **Ngày tháng**: ngày bán - **Đơn vị (tính)**: đơn vị tính - **so_luong**: số lượng - **Thanh tien**: thành tiền sau giảm - **Quy ra ĐV lẻ**: số lượng đã đổi ra đơn vị cơ bản - **Mã hóa đơn**: mã đơn - **Đối tác**: tên khách (Khách lẻ nếu không lưu)  ## Quy ước - Dữ liệu có đế
- **Files on disk (2):** README.md, ban_hang.csv

### Tables / Sheets Detail:
#### Table `ban_hang.csv`
- **Rows:** 56,501 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Giá bán, Kết quả, Nội dung, Ngày tháng, Đơn vị (tính), so_luong, Thanh tien, Quy ra ĐV lẻ, Mã hóa đơn, Đối tác
  - *Date cols:* None
  - *Amount/Qty cols:* ['so_luong', 'Thanh tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá bán": "560,000", "Kết quả": "Xong", "Nội dung": "Bột ngọt Ajinomoto 400g", "Ngày tháng": "1 thg 6 2025", "Đơn vị (tính)": "thùng", "so_luong": "1", "Thanh tien": "560,000", "Quy ra ĐV lẻ": "20"}
{"Giá bán": "4,000", "Kết quả": "Xong", "Nội dung": "Mì 3 Miền tôm hùm", "Ngày tháng": "1 thg 6 2025", "Đơn vị (tính)": "gói", "so_luong": "1", "Thanh tien": "4,000", "Quy ra ĐV lẻ": "1"}
{"Giá bán": "4,000", "Kết quả": "Xong", "Nội dung": "Trứng gà so", "Ngày tháng": "1 thg 6 2025", "Đơn vị (tính)": "quả", "so_luong": "1", "Thanh tien": "4,000", "Quy ra ĐV lẻ": "1"}
```

---

## Business `biz_102`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_102  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…). File đơn hàng mỗi dòng một sản phẩm, thông tin đơn lặp lại ở mọi dòng của đơn; file này không có mã sản phẩm, nối với các danh sách sản phẩm qua tên sản phẩm. Ngày dạng dd/mm/yyyy.  File `DonHang_ChiTiet.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DonHang_ChiTiet.xlsx` (xlsx) - `DanhSachQuyDoi.xlsx` (
- **Files on disk (3):** DanhSachQuyDoi.xlsx, DonHang_ChiTiet.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DanhSachQuyDoi.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên sản phẩm, Đơn vị quy đổi, Tỉ lệ quy đổi, Đơn vị cơ bản
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên sản phẩm": "Coca Cola 330ml", "Đơn vị quy đổi": "lốc", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "lon"}
{"Tên sản phẩm": "Coca Cola 330ml", "Đơn vị quy đổi": "thùng", "Tỉ lệ quy đổi": "24", "Đơn vị cơ bản": "lon"}
{"Tên sản phẩm": "Pepsi 330ml", "Đơn vị quy đổi": "lốc", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "lon"}
```

#### Table `DonHang_ChiTiet.xlsx :: T01_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Sơn Hải", "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "38,000", "Tổng tiền": "38,000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Gạo thơm Jasmine", "Số lượng sản phẩm": "1", "Giá sản phẩm": "20000", "Tổng tiền": "20000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Sữa TH true MILK 180ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "8,500", "Tổng tiền": "8,500"}
```

#### Table `DonHang_ChiTiet.xlsx :: T02_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD002712", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hứa Minh Linh", "Tên sản phẩm": "Bia Heineken 330ml", "Số lượng sản phẩm": "3", "Giá sản phẩm": "21,000", "Tổng tiền": "63000"}
{"Mã đơn hàng": "ORD002712", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hứa Minh Linh", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "10000", "Tổng tiền": "10,000"}
{"Mã đơn hàng": "ORD002712", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hứa Minh Linh", "Tên sản phẩm": "Sữa tươi Vinamilk 180ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "8,400", "Tổng tiền": "16800"}
```

#### Table `DonHang_ChiTiet.xlsx :: T03_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD005079", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Ngô Thảo Quân", "Tên sản phẩm": "Dầu ăn Tường An 1L", "Số lượng sản phẩm": "2", "Giá sản phẩm": "52000", "Tổng tiền": "104,000"}
{"Mã đơn hàng": "ORD005079", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Ngô Thảo Quân", "Tên sản phẩm": "Trứng gà so", "Số lượng sản phẩm": "1", "Giá sản phẩm": "4,000", "Tổng tiền": "4000"}
{"Mã đơn hàng": "ORD005080", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đinh Khánh Bình", "Tên sản phẩm": "Bánh quy Cosy 200g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "440000", "Tổng tiền": "440000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T04_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD006966", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Yakult 65ml", "Số lượng sản phẩm": "4 chai", "Giá sản phẩm": "6500", "Tổng tiền": "26000"}
{"Mã đơn hàng": "ORD006967", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Kiều Thanh Giang", "Tên sản phẩm": "Nước suối Aquafina 500ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "5000", "Tổng tiền": "5,000"}
{"Mã đơn hàng": "ORD006968", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "10,000", "Tổng tiền": "10,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T05_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD008735", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Nguyễn Bảo Đức", "Tên sản phẩm": "Sữa đặc Ông Thọ 380g", "Số lượng sản phẩm": "1 hộp", "Giá sản phẩm": "25,000", "Tổng tiền": "25,000"}
{"Mã đơn hàng": "ORD008736", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hứa Trang An", "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "38,000", "Tổng tiền": "38,000"}
{"Mã đơn hàng": "ORD008737", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Bia Sài Gòn Special 330ml", "Số lượng sản phẩm": "2 lon", "Giá sản phẩm": "15,000", "Tổng tiền": "30000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T06_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD010611", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hủy", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Nước tương Maggi 700ml", "Số lượng sản phẩm": "3", "Giá sản phẩm": "30,000", "Tổng tiền": "90000"}
{"Mã đơn hàng": "ORD010611", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hủy", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Red Bull 250ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "12500", "Tổng tiền": "25,000"}
{"Mã đơn hàng": "ORD010612", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hủy", "Tên khách hàng": "Trương Hiếu Châu", "Tên sản phẩm": "Snack Lay's vị tự nhiên 56g", "Số lượng sản phẩm": "2", "Giá sản phẩm": "12000", "Tổng tiền": "24000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T07_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD012340", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Trịnh Khoa An", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "2", "Giá sản phẩm": "135,000", "Tổng tiền": "270,000"}
{"Mã đơn hàng": "ORD012341", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Bánh Chocopie 12 cái", "Số lượng sản phẩm": "1", "Giá sản phẩm": "55,000", "Tổng tiền": "55000"}
{"Mã đơn hàng": "ORD012341", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "38,000", "Tổng tiền": "76000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T08_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD014188", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Kem đánh răng P/S 180g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "30000", "Tổng tiền": "30000"}
{"Mã đơn hàng": "ORD014188", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Nước suối Aquafina 500ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "5000", "Tổng tiền": "5000"}
{"Mã đơn hàng": "ORD014188", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Red Bull 250ml", "Số lượng sản phẩm": "1 lon", "Giá sản phẩm": "12,500", "Tổng tiền": "12,500"}
```

#### Table `DonHang_ChiTiet.xlsx :: T09_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD016021", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Bột giặt OMO 3kg", "Số lượng sản phẩm": "1", "Giá sản phẩm": "135,000", "Tổng tiền": "135,000"}
{"Mã đơn hàng": "ORD016021", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Khăn giấy Tempo 10 gói", "Số lượng sản phẩm": "1 lốc", "Giá sản phẩm": "40,000", "Tổng tiền": "40000"}
{"Mã đơn hàng": "ORD016022", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lương Quân Mai", "Tên sản phẩm": "Gạo ST25", "Số lượng sản phẩm": "5 kg", "Giá sản phẩm": "32,000", "Tổng tiền": "160000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T10_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD017776", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Thuốc lá Vinataba", "Số lượng sản phẩm": "1", "Giá sản phẩm": "26,000", "Tổng tiền": "26000"}
{"Mã đơn hàng": "ORD017777", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hồ Giang Tâm", "Tên sản phẩm": "Bia Tiger 330ml", "Số lượng sản phẩm": "3", "Giá sản phẩm": "18,000", "Tổng tiền": "54000"}
{"Mã đơn hàng": "ORD017778", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hủy", "Tên khách hàng": "Phạm Bình Bình", "Tên sản phẩm": "Hạt nêm Knorr 400g", "Số lượng sản phẩm": "2 gói", "Giá sản phẩm": "32,000", "Tổng tiền": "64,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T11_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD019645", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Red Bull 250ml", "Số lượng sản phẩm": "1 lon", "Giá sản phẩm": "12500", "Tổng tiền": "12500"}
{"Mã đơn hàng": "ORD019646", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Từ Phong An", "Tên sản phẩm": "Muối I-ốt 500g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "126,000", "Tổng tiền": "126000"}
{"Mã đơn hàng": "ORD019646", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Từ Phong An", "Tên sản phẩm": "Red Bull 250ml", "Số lượng sản phẩm": "1 lon", "Giá sản phẩm": "12500", "Tổng tiền": "12500"}
```

#### Table `DonHang_ChiTiet.xlsx :: T12_2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD021413", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Hồng Bảo", "Tên sản phẩm": "Đường Biên Hòa 1kg", "Số lượng sản phẩm": "1", "Giá sản phẩm": "26,000", "Tổng tiền": "26,000"}
{"Mã đơn hàng": "ORD021413", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Hồng Bảo", "Tên sản phẩm": "Yakult 65ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "6500", "Tổng tiền": "6,500"}
{"Mã đơn hàng": "ORD021413", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Hồng Bảo", "Tên sản phẩm": "Nước suối Lavie 1.5L", "Số lượng sản phẩm": "1 thùng", "Giá sản phẩm": "126,000", "Tổng tiền": "126000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T01_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD023196", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lương Anh Hồng", "Tên sản phẩm": "Băng vệ sinh Diana 8 miếng", "Số lượng sản phẩm": "4", "Giá sản phẩm": "23000", "Tổng tiền": "92000"}
{"Mã đơn hàng": "ORD023196", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lương Anh Hồng", "Tên sản phẩm": "Gạo ST25", "Số lượng sản phẩm": "1 kg", "Giá sản phẩm": "32000", "Tổng tiền": "32,000"}
{"Mã đơn hàng": "ORD023196", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lương Anh Hồng", "Tên sản phẩm": "Pin Panasonic AA", "Số lượng sản phẩm": "4 vỉ", "Giá sản phẩm": "20000", "Tổng tiền": "80000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T02_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD025066", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Giang Hoàng Quang", "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "2 chai", "Giá sản phẩm": "40000", "Tổng tiền": "80,000"}
{"Mã đơn hàng": "ORD025066", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Giang Hoàng Quang", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "1 gói", "Giá sản phẩm": "4,500", "Tổng tiền": "4500"}
{"Mã đơn hàng": "ORD025067", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Chung Đức Bích", "Tên sản phẩm": "Đường Biên Hòa 1kg", "Số lượng sản phẩm": "1", "Giá sản phẩm": "26,000", "Tổng tiền": "26,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T03_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD027955", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hủy", "Tên khách hàng": "Dương Duy Hồng", "Tên sản phẩm": "Nước rửa chén Sunlight 750g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "29500", "Tổng tiền": "29500"}
{"Mã đơn hàng": "ORD027956", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Bùi Trang Minh", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "10000", "Tổng tiền": "10000"}
{"Mã đơn hàng": "ORD027957", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Huỳnh Anh Thảo", "Tên sản phẩm": "Giấy vệ sinh Pulppy 10 cuộn", "Số lượng sản phẩm": "1 lốc", "Giá sản phẩm": "68,000", "Tổng tiền": "68000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T04_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD029780", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Trứng gà so", "Số lượng sản phẩm": "4 quả", "Giá sản phẩm": "4,000", "Tổng tiền": "16,000"}
{"Mã đơn hàng": "ORD029780", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "2", "Giá sản phẩm": "4,500", "Tổng tiền": "9,000"}
{"Mã đơn hàng": "ORD029780", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "40,000", "Tổng tiền": "40000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T05_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD031512", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Ngân Tâm", "Tên sản phẩm": "Mì Omachi sườn hầm", "Số lượng sản phẩm": "10", "Giá sản phẩm": "8000", "Tổng tiền": "80,000"}
{"Mã đơn hàng": "ORD031512", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Ngân Tâm", "Tên sản phẩm": "Trứng gà so", "Số lượng sản phẩm": "1 quả", "Giá sản phẩm": "4,000", "Tổng tiền": "4000"}
{"Mã đơn hàng": "ORD031513", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Nước suối Aquafina 500ml", "Số lượng sản phẩm": "2 chai", "Giá sản phẩm": "5,000", "Tổng tiền": "10000"}
```

#### Table `DonHang_ChiTiet.xlsx :: T06_2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD033260", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Giấy vệ sinh Pulppy 10 cuộn", "Số lượng sản phẩm": "1", "Giá sản phẩm": "71,500", "Tổng tiền": "71,500"}
{"Mã đơn hàng": "ORD033261", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Mì Omachi sườn hầm", "Số lượng sản phẩm": "3", "Giá sản phẩm": "8000", "Tổng tiền": "24,000"}
{"Mã đơn hàng": "ORD033261", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Nước tương Maggi 700ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "360,000", "Tổng tiền": "360000"}
```

---

## Business `biz_103`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_103  File Excel xuất từ phần mềm bán hàng. File đơn hàng mỗi dòng một sản phẩm.  File `DonHang_ChiTiet.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DonHang_ChiTiet.xlsx` (xlsx) - `DanhSachQuyDoi.xlsx` (xlsx)  ## Cột trong `DonHang_ChiTiet.xlsx` - **Mã đơn hàng**: mã đơn - **Ngày đặt hàng**: ngày bán - **Trạng thái đơn hàng**: trạng thái đơn - **Tên khách hàng**: tên khách (Khách lẻ nếu không lưu) - **Tên sản phẩm**: tên hàng - **Số lượng sản phẩm**: số lư
- **Files on disk (3):** DanhSachQuyDoi.xlsx, DonHang_ChiTiet.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DanhSachQuyDoi.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên sản phẩm, Đơn vị quy đổi, Tỉ lệ quy đổi, Đơn vị cơ bản
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên sản phẩm": "Coca Cola 330ml", "Đơn vị quy đổi": "lốc", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "lon"}
{"Tên sản phẩm": "Coca Cola 330ml", "Đơn vị quy đổi": "thùng", "Tỉ lệ quy đổi": "24", "Đơn vị cơ bản": "lon"}
{"Tên sản phẩm": "Pepsi 330ml", "Đơn vị quy đổi": "lốc", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "lon"}
```

#### Table `DonHang_ChiTiet.xlsx :: 04.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Doãn Dũng Bình", "Tên sản phẩm": "Dầu ăn Tường An 1L", "Số lượng sản phẩm": "3 chai", "Giá sản phẩm": "52000", "Tổng tiền": "156000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Bánh Chocopie 12 cái", "Số lượng sản phẩm": "3", "Giá sản phẩm": "55,000", "Tổng tiền": "165,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Sữa đặc Ông Thọ 380g", "Số lượng sản phẩm": "2", "Giá sản phẩm": "25,000", "Tổng tiền": "50,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 05.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD001099", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Doãn Dũng Bình", "Tên sản phẩm": "Đường Biên Hòa 1kg", "Số lượng sản phẩm": "4", "Giá sản phẩm": "26000", "Tổng tiền": "104,000"}
{"Mã đơn hàng": "ORD001100", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Gạo thơm Jasmine", "Số lượng sản phẩm": "2", "Giá sản phẩm": "20000", "Tổng tiền": "40,000"}
{"Mã đơn hàng": "ORD001101", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Nước lau sàn Sunlight 1L", "Số lượng sản phẩm": "1", "Giá sản phẩm": "35000", "Tổng tiền": "35,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 06.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD002225", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Võ Hà Dương", "Tên sản phẩm": "Bánh Chocopie 12 cái", "Số lượng sản phẩm": "1 hộp", "Giá sản phẩm": "55,000", "Tổng tiền": "55,000"}
{"Mã đơn hàng": "ORD002226", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Snack Oishi tôm cay 40g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "6,000", "Tổng tiền": "6,000"}
{"Mã đơn hàng": "ORD002227", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Dầu ăn Tường An 1L", "Số lượng sản phẩm": "3", "Giá sản phẩm": "52,000", "Tổng tiền": "156,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 07.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD003296", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "1 gói", "Giá sản phẩm": "4500", "Tổng tiền": "4,500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Coca Cola 330ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "10,500", "Tổng tiền": "10500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Nước mắm Nam Ngư 750ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "38000", "Tổng tiền": "38000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 08.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD004402", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Quách Long Cường", "Tên sản phẩm": "Bánh Oreo 133g", "Số lượng sản phẩm": "4 gói", "Giá sản phẩm": "15,000", "Tổng tiền": "60000"}
{"Mã đơn hàng": "ORD004403", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Vương Hương Hoa", "Tên sản phẩm": "Xúc xích Vissan 5 cây", "Số lượng sản phẩm": "1", "Giá sản phẩm": "25,000", "Tổng tiền": "25,000"}
{"Mã đơn hàng": "ORD004404", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Bùi Hương Hạnh", "Tên sản phẩm": "Mì 3 Miền tôm hùm", "Số lượng sản phẩm": "1", "Giá sản phẩm": "4000", "Tổng tiền": "4000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 09.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD005537", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Hồ Hạnh Tâm", "Tên sản phẩm": "Sữa tắm Lifebuoy 850g", "Số lượng sản phẩm": "2 chai", "Giá sản phẩm": "120000", "Tổng tiền": "240,000"}
{"Mã đơn hàng": "ORD005538", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Đặng Huy Quang", "Tên sản phẩm": "Bia Sài Gòn Special 330ml", "Số lượng sản phẩm": "3", "Giá sản phẩm": "15,000", "Tổng tiền": "45000"}
{"Mã đơn hàng": "ORD005539", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Đặng Huy Quang", "Tên sản phẩm": "Snack Lay's vị tự nhiên 56g", "Số lượng sản phẩm": "2 gói", "Giá sản phẩm": "12500", "Tổng tiền": "25000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 10.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD006665", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Lâm Phương Trung", "Tên sản phẩm": "Xà bông Lifebuoy 90g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "12,000", "Tổng tiền": "12000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Bia Tiger 330ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "18000", "Tổng tiền": "18,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Nước suối Aquafina 500ml", "Số lượng sản phẩm": "5", "Giá sản phẩm": "5200", "Tổng tiền": "26000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 11.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD007809", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "hủy đơn", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "10", "Giá sản phẩm": "4,500", "Tổng tiền": "45,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Gạo ST25", "Số lượng sản phẩm": "1 kg", "Giá sản phẩm": "32000", "Tổng tiền": "32000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Pepsi 330ml", "Số lượng sản phẩm": "1 lon", "Giá sản phẩm": "10,000", "Tổng tiền": "10,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 12.2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD008992", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "4", "Giá sản phẩm": "10,000", "Tổng tiền": "40000"}
{"Mã đơn hàng": "ORD008993", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Hồ Hạnh Tâm", "Tên sản phẩm": "Mì Omachi sườn hầm", "Số lượng sản phẩm": "1", "Giá sản phẩm": "8,000", "Tổng tiền": "8000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Trà xanh 0 độ 455ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "10,000", "Tổng tiền": "10000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 01.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD010100", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Nước lau sàn Sunlight 1L", "Số lượng sản phẩm": "1", "Giá sản phẩm": "37,000", "Tổng tiền": "37,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Trứng gà so", "Số lượng sản phẩm": "3 quả", "Giá sản phẩm": "4,000", "Tổng tiền": "12,000"}
{"Mã đơn hàng": "ORD010101", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "2", "Giá sản phẩm": "4,500", "Tổng tiền": "9,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 02.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD011307", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "đã lấy", "Tên khách hàng": "Đinh Huy Bích", "Tên sản phẩm": "Bia Sài Gòn Special 330ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "15000", "Tổng tiền": "30,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Bàn chải Colgate", "Số lượng sản phẩm": "1 cái", "Giá sản phẩm": "15000", "Tổng tiền": "15000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Nước rửa chén Sunlight 750g", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "28,000", "Tổng tiền": "28000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 03.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD013179", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "10", "Giá sản phẩm": "10,000", "Tổng tiền": "100,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Bàn chải Colgate", "Số lượng sản phẩm": "1", "Giá sản phẩm": "15,000", "Tổng tiền": "15,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Mì Omachi sườn hầm", "Số lượng sản phẩm": "4", "Giá sản phẩm": "8000", "Tổng tiền": "32,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 04.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD014354", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Tăng Hoàng Đức", "Tên sản phẩm": "Sữa đặc Ông Thọ 380g", "Số lượng sản phẩm": "2", "Giá sản phẩm": "25000", "Tổng tiền": "50,000"}
{"Mã đơn hàng": "ORD014355", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sữa tươi Vinamilk 180ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "8400", "Tổng tiền": "8400"}
{"Mã đơn hàng": "ORD014356", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sữa TH true MILK 180ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "8500", "Tổng tiền": "8,500"}
```

#### Table `DonHang_ChiTiet.xlsx :: 05.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD015519", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Trần Đức Hải", "Tên sản phẩm": "Đậu phộng rang muối 200g", "Số lượng sản phẩm": "1 gói", "Giá sản phẩm": "20,000", "Tổng tiền": "20000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Đường Biên Hòa 1kg", "Số lượng sản phẩm": "2", "Giá sản phẩm": "26,000", "Tổng tiền": "52000"}
{"Mã đơn hàng": "ORD015520", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Trần Dũng Hoàng", "Tên sản phẩm": "Dầu ăn Tường An 1L", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "52,000", "Tổng tiền": "52,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 06.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD016662", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sữa tắm Lifebuoy 850g", "Số lượng sản phẩm": "3 chai", "Giá sản phẩm": "120000", "Tổng tiền": "360000"}
{"Mã đơn hàng": "ORD016663", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Đỗ Duy Khánh", "Tên sản phẩm": "Coca Cola 330ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "11,000", "Tổng tiền": "10,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Red Bull 250ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "72,000", "Tổng tiền": "72,000"}
```

#### Table `DonHang_ChiTiet.xlsx :: 07.2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD017760", "Ngày đặt hàng": "01/07/2026", "Trạng thái đơn hàng": "Thành công", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Mì Hảo Hảo tôm chua cay", "Số lượng sản phẩm": "2 gói", "Giá sản phẩm": "4,500", "Tổng tiền": "9,000"}
{"Mã đơn hàng": "ORD017761", "Ngày đặt hàng": "01/07/2026", "Trạng thái đơn hàng": "Đã hủy đơn", "Tên khách hàng": "Đinh Mai Đức", "Tên sản phẩm": "Sting dâu 330ml", "Số lượng sản phẩm": "10", "Giá sản phẩm": "10500", "Tổng tiền": "100,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Xà bông Lifebuoy 90g", "Số lượng sản phẩm": "1 cục", "Giá sản phẩm": "12,000", "Tổng tiền": "11,000"}
```

---

## Business `biz_104`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_104  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…). File đơn hàng mỗi dòng một sản phẩm, thông tin đơn lặp lại ở mọi dòng của đơn; file này không có mã sản phẩm, nối với các danh sách sản phẩm qua tên sản phẩm. Ngày dạng dd/mm/yyyy.  ## File - `DonHang_ChiTiet.xlsx` (xlsx) - `DanhSachQuyDoi.xlsx` (xlsx)  ## Cột trong `DonHang_ChiTiet.xlsx` - **Mã đơn hàng**: mã đơn - **Ngày đặt h
- **Files on disk (3):** DanhSachQuyDoi.xlsx, DonHang_ChiTiet.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DanhSachQuyDoi.xlsx :: Sheet1`
- **Rows:** 2 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên sản phẩm, Đơn vị quy đổi, Tỉ lệ quy đổi, Đơn vị cơ bản
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên sản phẩm": "Bánh croissant", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "cái"}
{"Tên sản phẩm": "Bánh tiramisu", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "6", "Đơn vị cơ bản": "cái"}
```

#### Table `DonHang_ChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Bạch Quang Hoa", "Tên sản phẩm": "Sinh tố xoài (M)", "Số lượng sản phẩm": "2", "Giá sản phẩm": "42000", "Tổng tiền": "84000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Trà sữa ô long (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "51000", "Tổng tiền": "51,000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Sữa tươi trân châu đường đen (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "45,000", "Tổng tiền": "45000"}
```

---

## Business `biz_105`
- **Structure Archetype:** Multi-table Relational (21 tables)
- **README (truncated 500 chars):** # Dữ liệu biz_105  Sổ bán hàng ghi tay chuyển sang Excel, mỗi tháng một sheet.  ## File - `SoBanHang_1.xlsx` (xlsx) - `SoBanHang_2026.xlsx` (xlsx) - `DanhMuc.xlsx` (xlsx) - `TonKho.xlsx` (xlsx) - `SoNhapHang.xlsx` (xlsx) - `BangGia.xlsx` (xlsx)  ## Cột trong `SoBanHang_1.xlsx` - **Hàng**: tên hàng - **so_luong**: số lượng - **Unit**: đơn vị tính - **Trị giá**: thành tiền sau giảm - **Status**: trạng thái đơn - **Giá lẻ**: đơn giá - **Giờ**: giờ đặt đơn (dòng trả hàng: lúc trả) - **Mã hóa đơn**:
- **Files on disk (7):** BangGia.xlsx, DanhMuc.xlsx, README.md, SoBanHang_1.xlsx, SoBanHang_2026.xlsx, SoNhapHang.xlsx, TonKho.xlsx

### Tables / Sheets Detail:
#### Table `BangGia.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Ngày áp dụng, ten_hang, Giá mới, Giá cũ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày áp dụng": "2025-02-01 00:00:00", "ten_hang": "Cà phê đen (M)", "Giá mới": "25.000đ", "Giá cũ": null}
{"Ngày áp dụng": "2025-02-01 00:00:00", "ten_hang": "Cà phê đen (L)", "Giá mới": "31.000đ", "Giá cũ": null}
{"Ngày áp dụng": "2025-02-01 00:00:00", "ten_hang": "Cà phê sữa (M)", "Giá mới": "29.000đ", "Giá cũ": null}
```

#### Table `DanhMuc.xlsx :: Sheet1`
- **Rows:** 2 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên món, Đơn vị gốc, ĐV nhập, Hệ số
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên món": "Bánh croissant", "Đơn vị gốc": "cái", "ĐV nhập": "hộp", "Hệ số": "6"}
{"Tên món": "Bánh tiramisu", "Đơn vị gốc": "cái", "ĐV nhập": "hộp", "Hệ số": "6"}
```

#### Table `SoBanHang_1.xlsx :: Thang 02 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Đá xay cookie (M)", "col_1": "1", "col_2": "ly", "Tiền": "55.000đ", "col_4": "đã lấy", "col_5": "55.000đ", "Đơn": "2025-02-01 06:00:25"}
{"Hàng": "Cà phê đen (M)", "col_1": "1", "col_2": "ly", "Tiền": "25.000đ", "col_4": "đã lấy", "col_5": "25k", "Đơn": "2025-02-01 06:00:25"}
```

#### Table `SoBanHang_1.xlsx :: Thang 03 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Espresso (single)", "col_1": "1", "col_2": "ly", "Tiền": "35.000đ", "col_4": "đã lấy", "col_5": "35.000đ", "Đơn": "2025-03-01 06:01:04"}
{"Hàng": "Espresso (single)", "col_1": "1", "col_2": "ly", "Tiền": "35.000đ", "col_4": "đã xong", "col_5": "35.000đ", "Đơn": "2025-03-01 06:03:07"}
```

#### Table `SoBanHang_1.xlsx :: Thang 04 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Bạc xỉu (L)", "col_1": "1", "col_2": "ly", "Tiền": "38.000đ", "col_4": "đã xong", "col_5": "38.000đ", "Đơn": "2025-04-01 06:06:05"}
{"Hàng": "Trà vải (M)", "col_1": "2", "col_2": "ly", "Tiền": "78.000đ", "col_4": "đã xong", "col_5": "39.000đ", "Đơn": "2025-04-01 06:06:05"}
```

#### Table `SoBanHang_1.xlsx :: Thang 05 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Matcha latte (M)", "col_1": "1", "col_2": "ly", "Tiền": "49k", "col_4": "đã xong", "col_5": "49.000đ", "Đơn": "2025-05-01 06:03:16"}
{"Hàng": "Trà chanh (M)", "col_1": "1", "col_2": "ly", "Tiền": "24.000đ", "col_4": "đã xong", "col_5": "25.000đ", "Đơn": "2025-05-01 06:05:50"}
```

#### Table `SoBanHang_1.xlsx :: Thang 06 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Sinh tố bơ (M)", "col_1": "-1", "col_2": "ly", "Tiền": "-45k", "col_4": "Đổi trả", "col_5": "45.000đ", "Đơn": "2025-06-01 16:09:26"}
{"Hàng": "Nước ép cam (L)", "col_1": "1", "col_2": "ly", "Tiền": "45k", "col_4": "đã xong", "col_5": "45.000đ", "Đơn": "2025-06-01 06:06:50"}
```

#### Table `SoBanHang_1.xlsx :: Thang 07 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê sữa (M)", "col_1": "-1", "col_2": "ly", "Tiền": "-30.500đ", "col_4": "hàng trả về", "col_5": "30.500đ", "Đơn": "2025-07-01 10:05:37"}
{"Hàng": "Trà đào cam sả (M)", "col_1": "1", "col_2": "ly", "Tiền": "39.000đ", "col_4": "đã lấy", "col_5": "39.000đ", "Đơn": "2025-07-01 06:04:41"}
```

#### Table `SoBanHang_1.xlsx :: Thang 08 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê đen (L)", "col_1": "1", "col_2": "ly", "Tiền": "31k", "col_4": "đã xong", "col_5": "31.000đ", "Đơn": "2025-08-01 06:05:00"}
{"Hàng": "Topping Trân châu đen", "col_1": "1", "col_2": "phần", "Tiền": "7.000đ", "col_4": "đã lấy", "col_5": "7k", "Đơn": "2025-08-01 06:13:30"}
```

#### Table `SoBanHang_1.xlsx :: Thang 09 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê đen (L)", "col_1": "1", "col_2": "ly", "Tiền": "31.000đ", "col_4": "đã lấy", "col_5": "31.000đ", "Đơn": "2025-09-01 06:11:34"}
{"Hàng": "Trà sữa trân châu (M)", "col_1": "1", "col_2": "ly", "Tiền": "42k", "col_4": "đã lấy", "col_5": "42.000đ", "Đơn": "2025-09-01 06:11:34"}
```

#### Table `SoBanHang_1.xlsx :: Thang 10 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê sữa (M)", "col_1": "-1", "col_2": "ly", "Tiền": "-30.500đ", "col_4": "Trả hàng", "col_5": "30.500đ", "Đơn": "2025-10-01 14:10:46"}
{"Hàng": "Cappuccino (L)", "col_1": "1", "col_2": "ly", "Tiền": "53.500đ", "col_4": "đã lấy", "col_5": "53.500đ", "Đơn": "2025-10-01 06:10:04"}
```

#### Table `SoBanHang_1.xlsx :: Thang 11 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Trà chanh (M)", "col_1": "1", "col_2": "ly", "Tiền": "25.000đ", "col_4": "đã xong", "col_5": "25.000đ", "Đơn": "2025-11-01 06:01:54"}
{"Hàng": "Sinh tố bơ (M)", "col_1": "1", "col_2": "ly", "Tiền": "45k", "col_4": "đã xong", "col_5": "45.000đ", "Đơn": "2025-11-01 06:01:54"}
```

#### Table `SoBanHang_1.xlsx :: Thang 12 2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Hồng trà sữa (M)", "col_1": "2", "col_2": "ly", "Tiền": "78.000đ", "col_4": "đã lấy", "col_5": "39.000đ", "Đơn": "2025-12-01 06:05:06"}
{"Hàng": "Trà sữa trân châu (L)", "col_1": "1", "col_2": "ly", "Tiền": "48k", "col_4": "đã lấy", "col_5": "48k", "Đơn": "2025-12-01 06:05:06"}
```

#### Table `SoBanHang_1.xlsx :: Thang 01 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê sữa (M)", "col_1": "-1", "col_2": "ly", "Tiền": "-30.500đ", "col_4": "hàng trả về", "col_5": "30.500đ", "Đơn": "2026-01-01 14:58:08"}
{"Hàng": "Cà phê đen (M)", "col_1": "1", "col_2": "ly", "Tiền": "25k", "col_4": "đã xong", "col_5": "25k", "Đơn": "2026-01-01 06:03:16"}
```

#### Table `SoBanHang_2026.xlsx :: Thang 02 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cappuccino (L)", "col_1": "-1", "col_2": "ly", "Tiền": "-53.500đ", "col_4": "Đổi trả", "col_5": "53.500đ", "Đơn": "2026-02-01 08:47:28"}
{"Hàng": "Trà chanh (M)", "col_1": "3", "col_2": "ly", "Tiền": "75.000đ", "col_4": "đã xong", "col_5": "25.000đ", "Đơn": "2026-02-01 06:04:33"}
```

#### Table `SoBanHang_2026.xlsx :: Thang 03 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Hồng trà sữa (M)", "col_1": "-1", "col_2": "ly", "Tiền": "-39.000đ", "col_4": "Trả hàng", "col_5": "39k", "Đơn": "2026-03-01 19:10:13"}
{"Hàng": "Topping Pudding trứng", "col_1": "1", "col_2": "phần", "Tiền": "10.500đ", "col_4": "đã lấy", "col_5": "10.500đ", "Đơn": "2026-03-01 06:03:00"}
```

#### Table `SoBanHang_2026.xlsx :: Thang 04 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Hồng trà sữa (L)", "col_1": "-1", "col_2": "ly", "Tiền": "-45.000đ", "col_4": "hàng trả về", "col_5": "45k", "Đơn": "2026-04-01 15:00:37"}
{"Hàng": "Cà phê đen (M)", "col_1": "1", "col_2": "ly", "Tiền": "25.000đ", "col_4": "đã lấy", "col_5": "25k", "Đơn": "2026-04-01 06:01:03"}
```

#### Table `SoBanHang_2026.xlsx :: Thang 05 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Cà phê sữa (M)", "col_1": "1", "col_2": "ly", "Tiền": "30.500đ", "col_4": "đã xong", "col_5": "30.500đ", "Đơn": "2026-05-01 06:07:33"}
{"Hàng": "Bánh croissant", "col_1": "1", "col_2": "cái", "Tiền": "37.000đ", "col_4": "đã xong", "col_5": "37.000đ", "Đơn": "2026-05-01 06:07:33"}
```

#### Table `SoBanHang_2026.xlsx :: Thang 06 2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Hàng, col_1, col_2, Tiền, col_4, col_5, Đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Hàng", "col_1": "so_luong", "col_2": "Unit", "Tiền": "Trị giá", "col_4": "Status", "col_5": "Giá lẻ", "Đơn": "Giờ"}
{"Hàng": "Trà đào cam sả (L)", "col_1": "-1", "col_2": "ly", "Tiền": "-45k", "col_4": "Trả hàng", "col_5": "45.000đ", "Đơn": "2026-06-01 10:50:42"}
{"Hàng": "Trà đào cam sả (L)", "col_1": "1", "col_2": "ly", "Tiền": "45k", "col_4": "đã xong", "col_5": "45.000đ", "Đơn": "2026-06-01 06:21:35"}
```

#### Table `SoNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Số phiếu, Ngày nhập, Ghi chu, Thành tiền, Nhà cung cấp, Tên mặt hàng, Giá nhập, ĐVT, SL nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số phiếu": "PN00001", "Ngày nhập": "2025-02-01 00:00:00", "Ghi chu": "nhập đầu kỳ", "Thành tiền": "2131200", "Nhà cung cấp": "Cty Hoàng Bình", "Tên mặt hàng": "Cà phê đen (M)", "Giá nhập": "7200", "ĐVT": "ly"}
{"Số phiếu": "PN00001", "Ngày nhập": "2025-02-01 00:00:00", "Ghi chu": "nhập đầu kỳ", "Thành tiền": "1317200", "Nhà cung cấp": "Cty Hoàng Bình", "Tên mặt hàng": "Cà phê đen (L)", "Giá nhập": "8900", "ĐVT": "ly"}
{"Số phiếu": "PN00001", "Ngày nhập": "2025-02-01 00:00:00", "Ghi chu": "nhập đầu kỳ", "Thành tiền": "3219000", "Nhà cung cấp": "Cty Hoàng Bình", "Tên mặt hàng": "Cà phê sữa (M)", "Giá nhập": "8700", "ĐVT": "ly"}
```

#### Table `TonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Hàng hóa, Đơn vị tính, Tồn cuối
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng hóa": "Cà phê đen (M)", "Đơn vị tính": "ly", "Tồn cuối": "197"}
{"Hàng hóa": "Cà phê đen (L)", "Đơn vị tính": "ly", "Tồn cuối": "132"}
{"Hàng hóa": "Cà phê sữa (M)", "Đơn vị tính": "ly", "Tồn cuối": "173"}
```

---

## Business `biz_106`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_106  File máy POS xuất ra.  ## File - `DanhSachHoaDon.xlsx` (xlsx) - `DanhSachHoaDonChiTiet_1.xlsx` (xlsx) - `DanhSachHoaDonChiTiet_2.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DanhSachKhachHang.xlsx` (xlsx) - `BaoCaoTonKho.xlsx` (xlsx) - `DanhSachNhapHang.xlsx` (xlsx) - `DanhSachChiTietNhapHang.xlsx` (xlsx) - `SoQuy.xlsx` (xlsx) - `DanhSachDonViTinh.xlsx` (xlsx)  ## Quy ước - Dữ liệu có đến hết 14/09/2026. - **Công nợ**: mỗi lần khách trả tiền cho một đơn là một dòng, **Giá t
- **Files on disk (11):** BaoCaoTonKho.xlsx, DanhSachChiTietNhapHang.xlsx, DanhSachDonViTinh.xlsx, DanhSachHoaDon.xlsx, DanhSachHoaDonChiTiet_1.xlsx, DanhSachHoaDonChiTiet_2.xlsx, DanhSachKhachHang.xlsx, DanhSachNhapHang.xlsx, DanhSachSanPham.xlsx, README.md, SoQuy.xlsx

### Tables / Sheets Detail:
#### Table `BaoCaoTonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Cà phê đen (M)", "ĐVT": "ly", "Tồn cuối kỳ": "132"}
{"Mã hàng": "SP0002", "Tên hàng": "Cà phê đen (L)", "ĐVT": "ly", "Tồn cuối kỳ": "41"}
{"Mã hàng": "SP0003", "Tên hàng": "Cà phê sữa (M)", "ĐVT": "ly", "Tồn cuối kỳ": "278"}
```

#### Table `DanhSachChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "ly", "Số lượng": "237", "Đơn giá": "7,100"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "ly", "Số lượng": "119", "Đơn giá": "8,200"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "ly", "Số lượng": "296", "Đơn giá": "8,900"}
```

#### Table `DanhSachDonViTinh.xlsx :: Sheet1`
- **Rows:** 2 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, ĐVT, Quy đổi, Giá bán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0049", "ĐVT": "hộp", "Quy đổi": "6", "Giá bán": "222000"}
{"Mã hàng": "SP0050", "ĐVT": "hộp", "Quy đổi": "6", "Giá bán": "270000"}
```

#### Table `DanhSachHoaDon.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Tổng sau giảm giá, Khách đã trả, Phương thức thanh toán, Trạng thái, Thời gian tạo, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "01/02/2025", "Mã KH": "KH0043", "Khách hàng": "Triệu Hằng Hiếu", "Tổng tiền hàng": "90,000", "Giảm giá": "0", "Tổng sau giảm giá": "90,000", "Khách đã trả": "90,000"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "01/02/2025", "Mã KH": "KH0091", "Khách hàng": "Doãn Dũng Thanh", "Tổng tiền hàng": "55,000", "Giảm giá": "0", "Tổng sau giảm giá": "55,000", "Khách đã trả": "55,000"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "45689", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "132,000", "Giảm giá": "0", "Tổng sau giảm giá": "132,000", "Khách đã trả": "132,000"}
```

#### Table `DanhSachHoaDonChiTiet_1.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, STT, Mã hàng, Tên hàng, Đơn vị tính, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, Giá vốn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "STT": "1", "Mã hàng": "SP0026", "Tên hàng": "Hồng trà sữa (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "45,000", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD000001", "STT": "2", "Mã hàng": "SP0038", "Tên hàng": "Nước ép cam (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "45,000", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD000002", "STT": "1", "Mã hàng": "SP0030", "Tên hàng": "Matcha latte (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "55,000", "Giảm giá": "0"}
```

#### Table `DanhSachHoaDonChiTiet_2.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, STT, Mã hàng, Tên hàng, Đơn vị tính, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, Giá vốn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD060893", "STT": "1", "Mã hàng": "SP0005", "Tên hàng": "Bạc xỉu (M)", "Đơn vị tính": "ly", "Số lượng": "3", "Đơn giá": "33,500", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD060894", "STT": "1", "Mã hàng": "SP0033", "Tên hàng": "Sinh tố bơ (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "47,000", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD060895", "STT": "1", "Mã hàng": "SP0037", "Tên hàng": "Nước ép cam (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "39,000", "Giảm giá": "0"}
```

#### Table `DanhSachKhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (14):** Email, Mã khách hàng, Trạng thái, Tên công ty, Ngày sinh, Tổng điểm, Điểm tích lũy, Ghi chú, Số CMND/CCCD, Tên khách hàng, Mã số thuế, Người tạo, Điện thoại, Loại hình khách
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Email": null, "Mã khách hàng": "KH0001", "Trạng thái": "Đang hoạt động", "Tên công ty": null, "Ngày sinh": null, "Tổng điểm": "0", "Điểm tích lũy": "0", "Ghi chú": null}
{"Email": null, "Mã khách hàng": "KH0002", "Trạng thái": "Đang hoạt động", "Tên công ty": null, "Ngày sinh": null, "Tổng điểm": "0", "Điểm tích lũy": "0", "Ghi chú": null}
{"Email": null, "Mã khách hàng": "KH0003", "Trạng thái": "Đang hoạt động", "Tên công ty": null, "Ngày sinh": null, "Tổng điểm": "0", "Điểm tích lũy": "0", "Ghi chú": null}
```

#### Table `DanhSachNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/02/2025", "Mã NCC": "NCC005", "Cần trả NCC": "56,356,700", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "19/02/2025", "Mã NCC": "NCC004", "Cần trả NCC": "1,105,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "20/02/2025", "Mã NCC": "NCC001", "Cần trả NCC": "972,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (23):** Hình ảnh (url1,url2...), Vị trí kệ, Ghi chú, Được bán trực tiếp, Nhóm hàng(3 Cấp), Mã barcode, Mã hàng, Thương hiệu, Tồn lớn nhất, Tên hàng, Mã HH Liên quan, Thuộc tính, Giá bán, Mô tả sản phẩm, Loại hàng hóa...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hình ảnh (url1,url2...)": null, "Vị trí kệ": null, "Ghi chú": null, "Được bán trực tiếp": "1", "Nhóm hàng(3 Cấp)": "cà phê", "Mã barcode": "8937889784207", "Mã hàng": "SP0001", "Thương hiệu": null}
{"Hình ảnh (url1,url2...)": null, "Vị trí kệ": null, "Ghi chú": null, "Được bán trực tiếp": "1", "Nhóm hàng(3 Cấp)": "cà phê", "Mã barcode": "8932826184317", "Mã hàng": "SP0002", "Thương hiệu": null}
{"Hình ảnh (url1,url2...)": null, "Vị trí kệ": null, "Ghi chú": null, "Được bán trực tiếp": "1", "Nhóm hàng(3 Cấp)": "cà phê", "Mã barcode": "8933390411380", "Mã hàng": "SP0003", "Thương hiệu": null}
```

#### Table `SoQuy.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã phiếu, Thời gian, Mã hóa đơn, Phương thức thanh toán, Giá trị
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã phiếu": "PAY000001", "Thời gian": "2025-02-01 06:03:42", "Mã hóa đơn": "ORD000001", "Phương thức thanh toán": "Tiền mặt", "Giá trị": "90.000đ"}
{"Mã phiếu": "PAY000002", "Thời gian": "2025-02-01 06:38:13", "Mã hóa đơn": "ORD000002", "Phương thức thanh toán": "Tiền mặt", "Giá trị": "55.000đ"}
{"Mã phiếu": "PAY000003", "Thời gian": "2025-02-01 06:42:18", "Mã hóa đơn": "ORD000003", "Phương thức thanh toán": "Tiền mặt", "Giá trị": "132.000đ"}
```

---

## Business `biz_107`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_107  Sổ bán hàng chủ tiệm tự ghi trên Excel, một sheet: mỗi dòng một mặt hàng khách mua, không ghi mã đơn, không ghi tên khách.  ## File - `SoBanHang.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **Trạng thái xử lý**: trạng thái đơn - **Tổng tiền**: thành tiền sau giảm - **ngay_ban**: ngày bán - **Số lượng**: số lượng - **Nội dung**: tên hàng - **don_gia**: đơn giá - **Đơn vị (tính)**: đơn vị tính - **Số lượng lẻ**: số lượng đã đổi ra đơn vị cơ bản  ## Quy ước - Dữ liệu có đến hết
- **Files on disk (2):** README.md, SoBanHang.xlsx

### Tables / Sheets Detail:
#### Table `SoBanHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Trạng thái xử lý, Tổng tiền, ngay_ban, Số lượng, Nội dung, don_gia, Đơn vị (tính), Số lượng lẻ
  - *Date cols:* ['ngay_ban']
  - *Amount/Qty cols:* ['don_gia']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Trạng thái xử lý": "Đã hoàn thành", "Tổng tiền": "22,000", "ngay_ban": "45717", "Số lượng": "1 hộp", "Nội dung": "Cá hộp 3 Cô Gái 155g", "don_gia": "22,000", "Đơn vị (tính)": "hộp", "Số lượng lẻ": "1"}
{"Trạng thái xử lý": "Đã hoàn thành", "Tổng tiền": "10,000", "ngay_ban": "45717", "Số lượng": "1", "Nội dung": "Trà xanh 0 độ 455ml", "don_gia": "10,000", "Đơn vị (tính)": "chai", "Số lượng lẻ": "1"}
{"Trạng thái xử lý": "Đã hoàn thành", "Tổng tiền": "25,000", "ngay_ban": "45717", "Số lượng": "5 chai", "Nội dung": "Nước suối Aquafina 500ml", "don_gia": "5,000", "Đơn vị (tính)": "chai", "Số lượng lẻ": "5"}
```

---

## Business `biz_108`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_108  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…), nối với nhau qua mã. Ngày dạng dd/mm/yyyy.  ## File - `DanhSachHoaDon.xlsx` (xlsx) - `DanhSachHoaDonChiTiet.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DanhSachKhachHang.xlsx` (xlsx) - `BaoCaoTonKho.xlsx` (xlsx) - `DanhSachNhapHang.xlsx` (xlsx) - `DanhSachChiTietNhapHang.xlsx` (xlsx)  ## Cột trong `DanhSachHoaDon.xlsx` - **M
- **Files on disk (8):** BaoCaoTonKho.xlsx, DanhSachChiTietNhapHang.xlsx, DanhSachHoaDon.xlsx, DanhSachHoaDonChiTiet.xlsx, DanhSachKhachHang.xlsx, DanhSachNhapHang.xlsx, DanhSachSanPham.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BaoCaoTonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Coca Cola 330ml", "ĐVT": "lon", "Tồn cuối kỳ": "192"}
{"Mã hàng": "SP0002", "Tên hàng": "Pepsi 330ml", "ĐVT": "lon", "Tồn cuối kỳ": "142"}
{"Mã hàng": "SP0003", "Tên hàng": "Sting dâu 330ml", "ĐVT": "chai", "Tồn cuối kỳ": "140"}
```

#### Table `DanhSachChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "thùng", "Số lượng": "8", "Đơn giá": "208,800"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "thùng", "Số lượng": "6", "Đơn giá": "194,400"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "thùng", "Số lượng": "8", "Đơn giá": "192,000"}
```

#### Table `DanhSachHoaDon.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (14):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ, Kênh bán, Người bán, Trạng thái HĐĐT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "01/01/2025", "Mã KH": "KH0055", "Khách hàng": "Đoàn Hùng Hiếu", "Tổng tiền hàng": "213,000", "Giảm giá": "0", "Khách đã trả": "213,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "01/01/2025", "Mã KH": "KH0180", "Khách hàng": "Lưu Phương Hải", "Tổng tiền hàng": "36,000", "Giảm giá": "0", "Khách đã trả": "36,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "01/01/2025", "Mã KH": "KH0109", "Khách hàng": "Trương Giang Ngọc", "Tổng tiền hàng": "18,000", "Giảm giá": "0", "Khách đã trả": "18,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDonChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Mã hóa đơn, Mã hàng, Tên hàng, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, Đơn vị tính, STT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0033", "Tên hàng": "Xúc xích Vissan 5 cây", "Số lượng": "2", "Đơn giá": "25,000", "Giảm giá": "0", "Thành tiền": "50,000", "Số lượng quy đổi": "2"}
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0021", "Tên hàng": "Gạo thơm Jasmine", "Số lượng": "2", "Đơn giá": "20,000", "Giảm giá": "0", "Thành tiền": "40,000", "Số lượng quy đổi": "2"}
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0008", "Tên hàng": "Bia Tiger 330ml", "Số lượng": "1", "Đơn giá": "18,000", "Giảm giá": "0", "Thành tiền": "18,000", "Số lượng quy đổi": "1"}
```

#### Table `DanhSachKhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (16):** Đối tượng KH, Tổng điểm, Trạng thái, Mã số thuế, Mã khách hàng, Tên khách hàng, Điện thoại, Ngày sinh, Nhóm khách hàng, Địa chỉ, Người tạo, Giới tính, CCCD, Tên công ty, Điểm hiện tại...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đối tượng KH": "Cá nhân", "Tổng điểm": "0", "Trạng thái": "Đang hoạt động", "Mã số thuế": null, "Mã khách hàng": "KH0001", "Tên khách hàng": "Hồ Minh Dương (0933201672)", "Điện thoại": "0933201672", "Ngày sinh": null}
{"Đối tượng KH": "Cá nhân", "Tổng điểm": "0", "Trạng thái": "Đang hoạt động", "Mã số thuế": null, "Mã khách hàng": "KH0002", "Tên khách hàng": "Tô Nam Long 0919331756", "Điện thoại": "0919331756", "Ngày sinh": null}
{"Đối tượng KH": "Cá nhân", "Tổng điểm": "0", "Trạng thái": "Đang hoạt động", "Mã số thuế": null, "Mã khách hàng": "KH0003", "Tên khách hàng": "Hoàng Hoàng Duy", "Điện thoại": "0975706068", "Ngày sinh": null}
```

#### Table `DanhSachNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/01/2025", "Mã NCC": "NCC001", "Cần trả NCC": "131,789,600", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "04/01/2025", "Mã NCC": "NCC001", "Cần trả NCC": "4,200,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "08/01/2025", "Mã NCC": "NCC002", "Cần trả NCC": "816,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Mã hàng, Tên hàng, Bảo hành, Nhóm hàng(3 Cấp), Mô tả chi tiết, Trọng lượng, Vị trí, Hình ảnh (url1,url2...), Mã barcode, Loại hàng hóa, Thuộc tính, Mẫu ghi chú, Giá bán, Được bán trực tiếp, Ghi chú...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Coca Cola 330ml", "Bảo hành": null, "Nhóm hàng(3 Cấp)": "nước giải khát", "Mô tả chi tiết": null, "Trọng lượng": null, "Vị trí": null, "Hình ảnh (url1,url2...)": null}
{"Mã hàng": "SP0002", "Tên hàng": "Pepsi 330ml", "Bảo hành": null, "Nhóm hàng(3 Cấp)": "nước giải khát", "Mô tả chi tiết": null, "Trọng lượng": null, "Vị trí": null, "Hình ảnh (url1,url2...)": null}
{"Mã hàng": "SP0003", "Tên hàng": "Sting dâu 330ml", "Bảo hành": null, "Nhóm hàng(3 Cấp)": "nước giải khát", "Mô tả chi tiết": null, "Trọng lượng": null, "Vị trí": null, "Hình ảnh (url1,url2...)": null}
```

---

## Business `biz_109`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_109  File máy POS xuất ra.  Các danh sách `DanhSachHoaDon`, `DanhSachSanPham`, `DanhSachKhachHang`, `BaoCaoTonKho`, `DanhSachNhapHang`, `DanhSachChiTietNhapHang`, `SoQuy`, `DanhSachDonViTinh` nằm chung file `DuLieuBanHang.xlsx`, mỗi danh sách một sheet.  ## File - `DuLieuBanHang.xlsx` (xlsx) - `DanhSachHoaDonChiTiet.xlsx` (xlsx)  ## Quy ước - Dữ liệu có đến hết 05/08/2026. - **Công nợ**: mỗi lần khách trả tiền cho một đơn là một dòng, **Giá trị** là số tiền trả lần đó; **Tổng sau g
- **Files on disk (3):** DanhSachHoaDonChiTiet.xlsx, DuLieuBanHang.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DanhSachHoaDonChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, STT, Mã hàng, Tên hàng, Đơn vị tính, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, Giá vốn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "STT": "1", "Mã hàng": "SP0006", "Tên hàng": "Nước suối Aquafina 500ml", "Đơn vị tính": "thùng", "Số lượng": "2", "Đơn giá": "120,000", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD000001", "STT": "2", "Mã hàng": "SP0014", "Tên hàng": "Sữa Chua Vinamilk Có Đường", "Đơn vị tính": "hộp", "Số lượng": "1", "Đơn giá": "6,000", "Giảm giá": "0"}
{"Mã hóa đơn": "ORD000001", "STT": "3", "Mã hàng": "SP0009", "Tên hàng": "Bia Sài Gòn Special 330ml", "Đơn vị tính": "lon", "Số lượng": "1", "Đơn giá": "15,000", "Giảm giá": "0"}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachHoaDon`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (14):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Tổng sau giảm giá, Khách đã trả, Phương thức thanh toán, Trạng thái, Thời gian tạo, Kênh bán, Người bán, Trạng thái HĐĐT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "45658", "Mã KH": null, "Khách hàng": "kl", "Tổng tiền hàng": "301,000", "Giảm giá": "10,000", "Tổng sau giảm giá": "291,000", "Khách đã trả": "291,000"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "45658", "Mã KH": null, "Khách hàng": "lẻ", "Tổng tiền hàng": "400,500", "Giảm giá": "10,000", "Tổng sau giảm giá": "390,500", "Khách đã trả": "390,500"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "01/01/2025", "Mã KH": "KH0058", "Khách hàng": "Giang Thu Cường", "Tổng tiền hàng": "106,000", "Giảm giá": "0", "Tổng sau giảm giá": "106,000", "Khách đã trả": "106,000"}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachSanPham`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Tồn lớn nhất, Nhóm hàng(3 Cấp), Vị trí, Mã hàng, Trọng lượng, Thuộc tính, Tên hàng, Mẫu ghi chú, Giá bán, Hình ảnh (url1,url2...), Bảo hành, Định mức tồn tối thiểu, Giá vốn, Thương hiệu, Được bán trực tiếp...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tồn lớn nhất": "999999999", "Nhóm hàng(3 Cấp)": "nước giải khát", "Vị trí": null, "Mã hàng": "SP0001", "Trọng lượng": null, "Thuộc tính": null, "Tên hàng": "Coca Cola 330ml", "Mẫu ghi chú": null}
{"Tồn lớn nhất": "999999999", "Nhóm hàng(3 Cấp)": "nước giải khát", "Vị trí": null, "Mã hàng": "SP0002", "Trọng lượng": null, "Thuộc tính": null, "Tên hàng": "Pepsi 330ml", "Mẫu ghi chú": null}
{"Tồn lớn nhất": "999999999", "Nhóm hàng(3 Cấp)": "nước giải khát", "Vị trí": null, "Mã hàng": "SP0003", "Trọng lượng": null, "Thuộc tính": null, "Tên hàng": "Sting dâu 330ml", "Mẫu ghi chú": null}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachKhachHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (13):** Mã khách hàng, Tổng điểm, Tên khách hàng, Điện thoại, MST, Trạng thái, Loại hình khách, Người tạo, Ghi chú KH, Tên công ty, Nhóm khách hàng, Ngày tạo, Sinh nhật
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã khách hàng": "KH0001", "Tổng điểm": "0", "Tên khách hàng": "Đinh Khoa Châu", "Điện thoại": "0918010418", "MST": null, "Trạng thái": "Đang hoạt động", "Loại hình khách": "Cá nhân", "Người tạo": "admin"}
{"Mã khách hàng": "KH0002", "Tổng điểm": "0", "Tên khách hàng": "Lê Bảo Ngọc", "Điện thoại": "0359041900", "MST": null, "Trạng thái": "Đang hoạt động", "Loại hình khách": "Cá nhân", "Người tạo": "admin"}
{"Mã khách hàng": "KH0003", "Tổng điểm": "0", "Tên khách hàng": "Kiều Trang Phúc", "Điện thoại": "0700175052", "MST": null, "Trạng thái": "Đang hoạt động", "Loại hình khách": "Cá nhân", "Người tạo": "admin"}
```

#### Table `DuLieuBanHang.xlsx :: BaoCaoTonKho`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Coca Cola 330ml", "ĐVT": "lon", "Tồn cuối kỳ": "145"}
{"Mã hàng": "SP0002", "Tên hàng": "PEPSI 330ML", "ĐVT": "lon", "Tồn cuối kỳ": "76"}
{"Mã hàng": "SP0003", "Tên hàng": "Sting Dâu 330ml", "ĐVT": "chai", "Tồn cuối kỳ": "89"}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachNhapHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/01/2025", "Mã NCC": "NCC004", "Cần trả NCC": "145,823,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "03/01/2025", "Mã NCC": "NCC001", "Cần trả NCC": "1,200,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "05/01/2025", "Mã NCC": "NCC005", "Cần trả NCC": "1,280,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachChiTietNhapHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "thùng", "Số lượng": "8", "Đơn giá": "204,000"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "thùng", "Số lượng": "7", "Đơn giá": "201,600"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "thùng", "Số lượng": "8", "Đơn giá": "204,000"}
```

#### Table `DuLieuBanHang.xlsx :: SoQuy`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã phiếu, Thời gian, Mã hóa đơn, Phương thức thanh toán, Giá trị
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã phiếu": "PAY000001", "Thời gian": "2025-01-01 06:09:10", "Mã hóa đơn": "ORD000001", "Phương thức thanh toán": "Chuyển khoản", "Giá trị": "291000"}
{"Mã phiếu": "PAY000002", "Thời gian": "2025-01-01 06:13:15", "Mã hóa đơn": "ORD000002", "Phương thức thanh toán": "Tiền mặt", "Giá trị": "390500"}
{"Mã phiếu": "PAY000003", "Thời gian": "2025-01-01 07:48:26", "Mã hóa đơn": "ORD000004", "Phương thức thanh toán": "Tiền mặt", "Giá trị": "814000"}
```

#### Table `DuLieuBanHang.xlsx :: DanhSachDonViTinh`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, ĐVT, Quy đổi, Giá bán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "ĐVT": "lốc", "Quy đổi": "6", "Giá bán": "60000"}
{"Mã hàng": "SP0001", "ĐVT": "thùng", "Quy đổi": "24", "Giá bán": "240000"}
{"Mã hàng": "SP0002", "ĐVT": "lốc", "Quy đổi": "6", "Giá bán": "63000"}
```

---

## Business `biz_110`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_110  Danh sách hoá đơn, một file CSV: mỗi dòng một đơn hàng (hoá đơn), không có chi tiết mặt hàng trong đơn.  ## File - `danh_sach_hoa_don.csv` (csv)  ## Cột trong `danh_sach_hoa_don.csv` - **Tien hang**: tiền hàng của đơn: cộng thành tiền các mặt hàng, trước giảm giá của đơn, chưa gồm phí giao - **TongTien**: số khách phải trả cho cả đơn (đã tính giảm giá của đơn và phí giao) - **Mã bill**: mã đơn - **Bên mua**: tên khách (Khách lẻ nếu không lưu) - **Ngày giao dịch**: ngày bán - *
- **Files on disk (2):** README.md, danh_sach_hoa_don.csv

### Tables / Sheets Detail:
#### Table `danh_sach_hoa_don.csv`
- **Rows:** 29,317 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Tien hang, TongTien, Mã bill, Bên mua, Ngày giao dịch, Status, Da tra, Chưa trả
  - *Date cols:* None
  - *Amount/Qty cols:* ['Tien hang']
  - *Status cols:* ['Status']
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tien hang": "35,000", "TongTien": "35,000", "Mã bill": "ORD000001", "Bên mua": "Khách lẻ", "Ngày giao dịch": "01/05/2025", "Status": "Hoàn thành", "Da tra": "35,000", "Chưa trả": "0"}
{"Tien hang": "81,000", "TongTien": "81,000", "Mã bill": "ORD000002", "Bên mua": "Mai Khoa Bình", "Ngày giao dịch": "01/05/2025", "Status": "Hoàn thành", "Da tra": "81,000", "Chưa trả": "0"}
{"Tien hang": "80,000", "TongTien": "80,000", "Mã bill": "ORD000003", "Bên mua": "kl", "Ngày giao dịch": "01/05/2025", "Status": "Hoàn thành", "Da tra": "80,000", "Chưa trả": "0"}
```

---

## Business `biz_111`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_111  Dữ liệu bán hàng của tiệm, gồm vài file nối với nhau qua mã.  ## File - `don_hang.csv` (csv) - `chi_tiet_don.csv` (csv) - `san_pham.csv` (csv) - `khach_hang.csv` (csv) - `thanh_toan.csv` (csv)  ## Cột trong `don_hang.csv` - **Số KH**: mã khách (trống nếu khách lẻ) - **Xử lý**: trạng thái đơn - **NgayBan**: ngày bán - **Bán qua**: kênh bán - **Còn lại**: còn nợ - **Khách trả**: đã thanh toán - **Tổng bill**: tổng tiền đơn - **Phương thức TT**: hình thức thanh toán của đơn: cash
- **Files on disk (6):** README.md, chi_tiet_don.csv, don_hang.csv, khach_hang.csv, san_pham.csv, thanh_toan.csv

### Tables / Sheets Detail:
#### Table `chi_tiet_don.csv`
- **Rows:** 106,585 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** SL quy đổi, Thứ tự, Giá đơn vị, SL, T.Tiền, ID SP, Ma don, Đơn vị (tính)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"SL quy đổi": "1", "Thứ tự": "1", "Giá đơn vị": "7000", "SL": "1", "T.Tiền": "7000", "ID SP": "SP0046", "Ma don": "ORD000001", "Đơn vị (tính)": "phần"}
{"SL quy đổi": "1", "Thứ tự": "1", "Giá đơn vị": "32000", "SL": "1", "T.Tiền": "32000", "ID SP": "SP0005", "Ma don": "ORD000002", "Đơn vị (tính)": "ly"}
{"SL quy đổi": "1", "Thứ tự": "1", "Giá đơn vị": "42000", "SL": "1 ly", "T.Tiền": "42000", "ID SP": "SP0021", "Ma don": "ORD000003", "Đơn vị (tính)": "ly"}
```

#### Table `don_hang.csv`
- **Rows:** 66,469 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Số KH, Xử lý, NgayBan, Bán qua, Còn lại, Khách trả, Tổng bill, Phương thức TT, Mã chứng từ
  - *Date cols:* ['NgayBan']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số KH": "KH0114", "Xử lý": "completed", "NgayBan": "1 thg 1 2025", "Bán qua": "zalo_oa", "Còn lại": "0", "Khách trả": "22000", "Tổng bill": "22000", "Phương thức TT": "transfer"}
{"Số KH": "KH0078", "Xử lý": "completed", "NgayBan": "1 thg 1 2025", "Bán qua": "store", "Còn lại": "0", "Khách trả": "32000", "Tổng bill": "32000", "Phương thức TT": "ewallet"}
{"Số KH": "KH0065", "Xử lý": "completed", "NgayBan": "45658", "Bán qua": "store", "Còn lại": "0", "Khách trả": "67000", "Tổng bill": "67000", "Phương thức TT": "cash"}
```

#### Table `khach_hang.csv`
- **Rows:** 200 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (15):** ma_kh, Điểm tích lũy, Nhóm, Trạng thái, Email, Ghi chú KH, Mã số thuế, Loại hình khách, Ngày sinh, CCCD, Phone, Người tạo, Addr, Khách lẻ/sỉ, Tổng điểm
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"ma_kh": "KH0001", "Điểm tích lũy": "0", "Nhóm": "thân thiết", "Trạng thái": "Đang hoạt động", "Email": "nan", "Ghi chú KH": "nan", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân"}
{"ma_kh": "KH0002", "Điểm tích lũy": "0", "Nhóm": "lẻ", "Trạng thái": "Đang hoạt động", "Email": "nan", "Ghi chú KH": "nan", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân"}
{"ma_kh": "KH0003", "Điểm tích lũy": "0", "Nhóm": "lẻ", "Trạng thái": "Đang hoạt động", "Email": "nan", "Ghi chú KH": "nan", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân"}
```

#### Table `san_pham.csv`
- **Rows:** 50 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Thuộc tính, Được bán trực tiếp, Mã barcode, SKU, Hình ảnh, Giá, Đơn vị, Loại hàng hóa, Thương hiệu, Nhom hang, Trọng lượng, Vị trí, Mẫu ghi chú, Mô tả sản phẩm, Bảo hành...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Thuộc tính": "nan", "Được bán trực tiếp": "1", "Mã barcode": "nan", "SKU": "SP0001", "Hình ảnh": "nan", "Giá": "25000", "Đơn vị": "ly", "Loại hàng hóa": "Hàng hóa"}
{"Thuộc tính": "nan", "Được bán trực tiếp": "1", "Mã barcode": "nan", "SKU": "SP0002", "Hình ảnh": "nan", "Giá": "31000", "Đơn vị": "ly", "Loại hàng hóa": "Hàng hóa"}
{"Thuộc tính": "nan", "Được bán trực tiếp": "1", "Mã barcode": "nan", "SKU": "SP0003", "Hình ảnh": "nan", "Giá": "29000", "Đơn vị": "ly", "Loại hàng hóa": "Hàng hóa"}
```

#### Table `thanh_toan.csv`
- **Rows:** 66,195 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Thời gian thu, Phương thức, Tiền, Mã phiếu thu, Số HĐ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Thời gian thu": "2025-01-01 06:03:59", "Phương thức": "transfer", "Tiền": "22000", "Mã phiếu thu": "PAY000001", "Số HĐ": "ORD000001"}
{"Thời gian thu": "2025-01-01 06:56:27", "Phương thức": "ewallet", "Tiền": "32000", "Mã phiếu thu": "PAY000002", "Số HĐ": "ORD000002"}
{"Thời gian thu": "2025-01-01 07:04:26", "Phương thức": "cash", "Tiền": "67000", "Mã phiếu thu": "PAY000003", "Số HĐ": "ORD000003"}
```

---

## Business `biz_112`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_112  File Excel xuất từ phần mềm bán hàng. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng.  File `So_chi_tiet_ban_hang_1.xlsx`, `So_chi_tiet_ban_hang_2026.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `So_chi_tiet_ban_hang_1.xlsx` (xlsx) - `So_chi_tiet_ban_hang_2026.xlsx` (xlsx) - `Danh sách hàng hóa.xlsx` (xlsx)  ## Cột trong `So_chi_tiet_ban_hang_1.xlsx` - **Ngày**: ngày bán - **Mã đơn hàng**: mã đơn - **Tên hàng hóa**: tên
- **Files on disk (4):** Danh sách hàng hóa.xlsx, README.md, So_chi_tiet_ban_hang_1.xlsx, So_chi_tiet_ban_hang_2026.xlsx

### Tables / Sheets Detail:
#### Table `Danh sách hàng hóa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (16):** Mã hàng hóa, Mã vạch EAN, Tồn nhỏ nhất, Trọng lượng, Ghi chú, Loại hàng hóa, Mã HH Liên quan, Mô tả sản phẩm, Bảo hành, Tên hàng hóa, Vị trí, Nhóm hàng hóa, Đơn vị tính, Giá bán, Tồn lớn nhất...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng hóa": "SP0001", "Mã vạch EAN": null, "Tồn nhỏ nhất": "0", "Trọng lượng": null, "Ghi chú": null, "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mô tả sản phẩm": null}
{"Mã hàng hóa": "SP0002", "Mã vạch EAN": null, "Tồn nhỏ nhất": "0", "Trọng lượng": null, "Ghi chú": null, "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mô tả sản phẩm": null}
{"Mã hàng hóa": "SP0003", "Mã vạch EAN": null, "Tồn nhỏ nhất": "0", "Trọng lượng": null, "Ghi chú": null, "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mô tả sản phẩm": null}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T04_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Trà đào cam sả (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Cà phê đen (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "25,000.0000", "Thành tiền": "25,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Cà phê muối (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T05_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD004069", "Tên hàng hóa": "Topping Pudding trứng", "Đơn vị tính": "phần", "Số lượng": "1 phần", "Đơn giá": "10,000.0000", "Thành tiền": "10,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD004069", "Tên hàng hóa": "Sữa tươi trân châu đường đen (L)", "Đơn vị tính": "ly", "Số lượng": "3 ly", "Đơn giá": "51,000.0000", "Thành tiền": "153,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD004070", "Tên hàng hóa": "Nước ép dưa hấu (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "41,000.0000", "Thành tiền": "41,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T06_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD008372", "Tên hàng hóa": "Trà sữa trân châu (M)", "Đơn vị tính": "ly", "Số lượng": "2 ly", "Đơn giá": "46,000.0000", "Thành tiền": "92,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD008373", "Tên hàng hóa": "Cà phê đen (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "25,000.0000", "Thành tiền": "25,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD008373", "Tên hàng hóa": "Hồng trà sữa (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T07_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD012686", "Tên hàng hóa": "Sữa tươi trân châu đường đen (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD012687", "Tên hàng hóa": "Nước ép cam (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD012688", "Tên hàng hóa": "Hồng trà sữa (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T08_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD017014", "Tên hàng hóa": "Bạc xỉu (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "32,000.0000", "Thành tiền": "30,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD017014", "Tên hàng hóa": "Cà phê sữa (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD017015", "Tên hàng hóa": "Cà phê đen (M)", "Đơn vị tính": "ly", "Số lượng": "2", "Đơn giá": "25,000.0000", "Thành tiền": "50,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T09_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD021667", "Tên hàng hóa": "Cold brew (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "51,000.0000", "Thành tiền": "51,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD021668", "Tên hàng hóa": "Cappuccino (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD021669", "Tên hàng hóa": "Matcha latte (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "55,000.0000", "Thành tiền": "55,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T10_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD025990", "Tên hàng hóa": "Hồng trà sữa (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD025990", "Tên hàng hóa": "Trà vải (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD025990", "Tên hàng hóa": "Sữa tươi trân châu đường đen (L)", "Đơn vị tính": "ly", "Số lượng": "2 ly", "Đơn giá": "51,000.0000", "Thành tiền": "102,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T11_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD030434", "Tên hàng hóa": "Nước ép cam (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD030434", "Tên hàng hóa": "Trà sữa ô long (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD030435", "Tên hàng hóa": "Cà phê sữa (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "29,000.0000", "Thành tiền": "29,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T12_2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD034960", "Tên hàng hóa": "Trà sữa trân châu (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "48,500.0000", "Thành tiền": "48,500.0000", "Trạng thái": "xong"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD034960", "Tên hàng hóa": "Cà phê đen (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "25,000.0000", "Thành tiền": "25,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD034960", "Tên hàng hóa": "Bạc xỉu (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "33,500.0000", "Thành tiền": "33,500.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T01_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD039496", "Tên hàng hóa": "Soda chanh dây (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "41,000.0000", "Thành tiền": "41,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD039496", "Tên hàng hóa": "Đá xay cookie (M)", "Đơn vị tính": "ly", "Số lượng": "2", "Đơn giá": "55,000.0000", "Thành tiền": "110,000.0000", "Trạng thái": "xong"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD039496", "Tên hàng hóa": "Espresso (single)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "xong"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T02_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD044112", "Tên hàng hóa": "Trà đào cam sả (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "39,000.0000", "Thành tiền": "39,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD044113", "Tên hàng hóa": "Cà phê đen (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "32,500.0000", "Thành tiền": "32,500.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD044113", "Tên hàng hóa": "Sữa tươi trân châu đường đen (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "47,000.0000", "Thành tiền": "47,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T03_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD047407", "Tên hàng hóa": "Cold brew (M)", "Đơn vị tính": "ly", "Số lượng": "2 ly", "Đơn giá": "45,000.0000", "Thành tiền": "90,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD047407", "Tên hàng hóa": "Nước ép cam (M)", "Đơn vị tính": "ly", "Số lượng": "2 ly", "Đơn giá": "41,000.0000", "Thành tiền": "82,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD047408", "Tên hàng hóa": "Sữa tươi trân châu đường đen (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "47,000.0000", "Thành tiền": "47,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T04_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD052113", "Tên hàng hóa": "Topping Trân châu đen", "Đơn vị tính": "phần", "Số lượng": "1", "Đơn giá": "7,000.0000", "Thành tiền": "7,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD052114", "Tên hàng hóa": "Topping Trân châu đen", "Đơn vị tính": "phần", "Số lượng": "1", "Đơn giá": "7,000.0000", "Thành tiền": "7,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD052114", "Tên hàng hóa": "Cà phê muối (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "43,000.0000", "Thành tiền": "43,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: T05_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD056664", "Tên hàng hóa": "Trà chanh (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "25,000.0000", "Thành tiền": "25,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD056665", "Tên hàng hóa": "Bánh croissant", "Đơn vị tính": "cái", "Số lượng": "1 cái", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD056666", "Tên hàng hóa": "Topping Pudding trứng", "Đơn vị tính": "phần", "Số lượng": "1", "Đơn giá": "10,000.0000", "Thành tiền": "10,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_2026.xlsx :: T06_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD061542", "Tên hàng hóa": "Sinh tố xoài (L)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "50,500.0000", "Thành tiền": "50,500.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD061542", "Tên hàng hóa": "Trà sữa trân châu (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "48,500.0000", "Thành tiền": "48,500.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD061543", "Tên hàng hóa": "Bạc xỉu (M)", "Đơn vị tính": "ly", "Số lượng": "1 ly", "Đơn giá": "33,500.0000", "Thành tiền": "33,500.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_2026.xlsx :: T07_2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD065973", "Tên hàng hóa": "Cà phê sữa (M)", "Đơn vị tính": "ly", "Số lượng": "2 ly", "Đơn giá": "29,000.0000", "Thành tiền": "58,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD065974", "Tên hàng hóa": "Đá xay cookie (M)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "55,000.0000", "Thành tiền": "55,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD065975", "Tên hàng hóa": "Cold brew (L)", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "51,000.0000", "Thành tiền": "51,000.0000", "Trạng thái": "Đã hoàn thành"}
```

---

## Business `biz_113`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_113  Sổ bán hàng chủ tiệm tự ghi trên Excel, một sheet: mỗi dòng một mặt hàng khách mua, không ghi mã đơn, không ghi tên khách.  ## File - `SoBanHang.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **DonVi**: đơn vị tính - **Ngày mua**: ngày bán - **Số lượng lẻ**: số lượng đã đổi ra đơn vị cơ bản - **thanh_tien**: thành tiền sau giảm - **Đơn giá bán**: đơn giá - **SL bán**: số lượng - **Ghi chú TT**: trạng thái đơn - **Mặt hàng**: tên hàng  ## Quy ước - Dữ liệu có đến hết 09/08/2026.
- **Files on disk (2):** README.md, SoBanHang.xlsx

### Tables / Sheets Detail:
#### Table `SoBanHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** DonVi, Ngày mua, Số lượng lẻ, thanh_tien, Đơn giá bán, SL bán, Ghi chú TT, Mặt hàng
  - *Date cols:* None
  - *Amount/Qty cols:* ['thanh_tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"DonVi": "bộ", "Ngày mua": "01/02/2025", "Số lượng lẻ": "1", "thanh_tien": "250,000", "Đơn giá bán": "250,000", "SL bán": "1", "Ghi chú TT": "xong", "Mặt hàng": "Bộ van dây gas Namilux"}
{"DonVi": "bình", "Ngày mua": "01/02/2025", "Số lượng lẻ": "3", "thanh_tien": "216,000", "Đơn giá bán": "72,000", "SL bán": "3", "Ghi chú TT": "xong", "Mặt hàng": "Nước kiềm Ion Life 19L"}
{"DonVi": "cái", "Ngày mua": "01/02/2025", "Số lượng lẻ": "2", "thanh_tien": "90,000", "Đơn giá bán": "45,000", "SL bán": "2", "Ghi chú TT": "xong", "Mặt hàng": "Bóng LED bulb Rạng Đông A60 9W"}
```

---

## Business `biz_114`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_114  Một file phẳng, mỗi dòng một bản ghi (một dòng hàng trong đơn).  ## File - `ban_hang.csv` (csv)  ## Cột trong `ban_hang.csv` - **Giá bán lẻ**: đơn giá - **Đơn vị tính**: đơn vị tính - **Mã GD**: mã đơn - **Quy ra ĐV lẻ**: số lượng đã đổi ra đơn vị cơ bản - **Sluong**: số lượng - **Sản phẩm**: tên hàng - **Tổng**: thành tiền sau giảm - **Tên khách**: tên khách (Khách lẻ nếu không lưu) - **Ngày**: ngày bán - **trang_thai**: trạng thái đơn  ## Quy ước - Dữ liệu có đến hết 21/06/2
- **Files on disk (2):** README.md, ban_hang.csv

### Tables / Sheets Detail:
#### Table `ban_hang.csv`
- **Rows:** 26,119 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Giá bán lẻ, Đơn vị tính, Mã GD, Quy ra ĐV lẻ, Sluong, Sản phẩm, Tổng, Tên khách, Ngày, trang_thai
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* ['trang_thai']
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá bán lẻ": "1270000", "Đơn vị tính": "cuộn", "Mã GD": "ORD000001", "Quy ra ĐV lẻ": "2", "Sluong": "2", "Sản phẩm": "Dây điện Cadivi CV 2.5 cuộn 100m", "Tổng": "2540000", "Tên khách": "Tăng Chi Trang"}
{"Giá bán lẻ": "1,200,000", "Đơn vị tính": "xe 4m3", "Mã GD": "ORD000001", "Quy ra ĐV lẻ": "8", "Sluong": "2 xe 4m3", "Sản phẩm": "Đá mi bụi", "Tổng": "2,400,000", "Tên khách": "Tăng Chi Trang"}
{"Giá bán lẻ": "300,000", "Đơn vị tính": "thùng", "Mã GD": "ORD000002", "Quy ra ĐV lẻ": "1", "Sluong": "1 thùng", "Sản phẩm": "Gạch lát nền Prime 60x60 thùng 4 viên", "Tổng": "300,000", "Tên khách": "Khách lẻ"}
```

---

## Business `biz_115`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_115  File Excel xuất từ phần mềm bán hàng, mỗi báo cáo, danh sách một file. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng của đơn; sổ không có mã hàng, nối với danh sách hàng hóa qua tên hàng hóa. Ngày dạng dd/mm/yyyy.  File `So_chi_tiet_ban_hang.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `So_chi_tiet_ban_hang.xlsx` (xlsx) - `Danh sách hàng hóa.xlsx` (xlsx) - `Bảng kê phiếu giao hàng.xlsx` (xlsx) - `Chi tiết công nợ theo
- **Files on disk (5):** Bảng kê phiếu giao hàng.xlsx, Chi tiết công nợ theo hạn.xlsx, Danh sách hàng hóa.xlsx, README.md, So_chi_tiet_ban_hang.xlsx

### Tables / Sheets Detail:
#### Table `Bảng kê phiếu giao hàng.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày giao hàng, Mã đơn hàng, Lần giao, Tên hàng hóa, Đơn vị tính, Số lượng giao, Biển số xe, Người giao hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày giao hàng": "01/02/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Thép Pomina D10 cây 11.7m", "Đơn vị tính": "cây", "Số lượng giao": "1", "Biển số xe": "61C-750.95", "Người giao hàng": "Hồ Linh"}
{"Ngày giao hàng": "01/02/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Dây điện Cadivi CV 1.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng giao": "1", "Biển số xe": "61C-750.95", "Người giao hàng": "Hồ Linh"}
{"Ngày giao hàng": "01/02/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Sơn Dulux Weathershield Powerflexx 5L", "Đơn vị tính": "thùng", "Số lượng giao": "1", "Biển số xe": "61C-750.95", "Người giao hàng": "Hồ Linh"}
```

#### Table `Chi tiết công nợ theo hạn.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn hàng, Số ngày được nợ, Hạn thanh toán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Số ngày được nợ": "30", "Hạn thanh toán": "03/03/2025"}
{"Mã đơn hàng": "ORD000011", "Số ngày được nợ": "60", "Hạn thanh toán": "02/04/2025"}
{"Mã đơn hàng": "ORD000019", "Số ngày được nợ": "30", "Hạn thanh toán": "03/03/2025"}
```

#### Table `Danh sách hàng hóa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (15):** Mã hàng hóa, Được bán trực tiếp, Thương hiệu, Tên hàng hóa, Nhóm hàng hóa, Vị trí, Mẫu ghi chú, Loại hàng hóa, Ghi chú, Đơn vị tính, Bảo hành, Giá vốn, Mô tả sản phẩm, Định mức tồn tối thiểu, Trọng lượng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng hóa": "SP0001", "Được bán trực tiếp": "1", "Thương hiệu": null, "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg", "Nhóm hàng hóa": "xi măng", "Vị trí": null, "Mẫu ghi chú": null, "Loại hàng hóa": "Hàng hóa"}
{"Mã hàng hóa": "SP0002", "Được bán trực tiếp": "1", "Thương hiệu": null, "Tên hàng hóa": "Xi măng INSEE Power-S bao 50kg", "Nhóm hàng hóa": "xi măng", "Vị trí": null, "Mẫu ghi chú": null, "Loại hàng hóa": "Hàng hóa"}
{"Mã hàng hóa": "SP0003", "Được bán trực tiếp": "1", "Thương hiệu": null, "Tên hàng hóa": "Cát xây tô", "Nhóm hàng hóa": "cát đá", "Vị trí": null, "Mẫu ghi chú": null, "Loại hàng hóa": "Hàng hóa"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 02.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Thép Pomina D10 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "1 cây", "Đơn giá": "115,000.0000", "Thành tiền": "115,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Dây điện Cadivi CV 1.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "1", "Đơn giá": "790,000.0000", "Thành tiền": "790,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Sơn Dulux Weathershield Powerflexx 5L", "Đơn vị tính": "thùng", "Số lượng": "1", "Đơn giá": "1,550,000.0000", "Thành tiền": "1,550,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 03.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000685", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "5 viên", "Đơn giá": "1,300.0000", "Thành tiền": "6,500.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000685", "Tên hàng hóa": "Gas Petrolimex 12kg", "Đơn vị tính": "bình", "Số lượng": "2 bình", "Đơn giá": "520,000.0000", "Thành tiền": "1,040,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000686", "Tên hàng hóa": "Dây điện Cadivi CV 2.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "1", "Đơn giá": "1,270,000.0000", "Thành tiền": "1,270,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 04.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD001608", "Tên hàng hóa": "Đá 1x2", "Đơn vị tính": "m3", "Số lượng": "5", "Đơn giá": "380,000.0000", "Thành tiền": "1,900,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD001609", "Tên hàng hóa": "Băng keo điện Nano 20 yard", "Đơn vị tính": "cuộn", "Số lượng": "2", "Đơn giá": "9,000.0000", "Thành tiền": "18,000.0000", "Trạng thái": "Đã hủy"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD001609", "Tên hàng hóa": "Nước tinh khiết Bidrico 20L", "Đơn vị tính": "bình", "Số lượng": "1 bình", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "Đã hủy"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 05.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD002496", "Tên hàng hóa": "Keo dán ống PVC Bình Minh 200g", "Đơn vị tính": "lon", "Số lượng": "1", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD002497", "Tên hàng hóa": "Ống PVC Bình Minh D32 cây 4m", "Đơn vị tính": "cây", "Số lượng": "2", "Đơn giá": "65,000.0000", "Thành tiền": "130,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD002498", "Tên hàng hóa": "Gas Petrolimex 12kg", "Đơn vị tính": "bình", "Số lượng": "10", "Đơn giá": "520,000.0000", "Thành tiền": "5,200,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 06.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD003402", "Tên hàng hóa": "Sơn lót Jotun Jotashield chống kiềm 5L", "Đơn vị tính": "thùng", "Số lượng": "1", "Đơn giá": "720,000.0000", "Thành tiền": "720,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD003402", "Tên hàng hóa": "Xi măng INSEE Power-S bao 50kg", "Đơn vị tính": "bao", "Số lượng": "3", "Đơn giá": "100,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD003402", "Tên hàng hóa": "Thép Pomina D10 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "5", "Đơn giá": "115,000.0000", "Thành tiền": "575,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 07.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD004250", "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg", "Đơn vị tính": "bao", "Số lượng": "1 bao", "Đơn giá": "105,000.0000", "Thành tiền": "105,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD004251", "Tên hàng hóa": "Đinh 5 phân", "Đơn vị tính": "kg", "Số lượng": "1", "Đơn giá": "20,000.0000", "Thành tiền": "20,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD004251", "Tên hàng hóa": "Công tắc 1 chiều Panasonic Wide kèm mặt", "Đơn vị tính": "bộ", "Số lượng": "1", "Đơn giá": "35,000.0000", "Thành tiền": "35,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 08.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD005123", "Tên hàng hóa": "Ống PVC Bình Minh D32 cây 4m", "Đơn vị tính": "cây", "Số lượng": "1", "Đơn giá": "65,000.0000", "Thành tiền": "65,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD005124", "Tên hàng hóa": "Bộ van dây gas Namilux", "Đơn vị tính": "bộ", "Số lượng": "5", "Đơn giá": "250,000.0000", "Thành tiền": "1,250,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD005124", "Tên hàng hóa": "Lưới B40 mạ kẽm khổ 1.5m", "Đơn vị tính": "m", "Số lượng": "2", "Đơn giá": "50,500.0000", "Thành tiền": "101,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 09.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD005970", "Tên hàng hóa": "Máy bơm nước Panasonic GP-129JXK 125W", "Đơn vị tính": "cái", "Số lượng": "1 cái", "Đơn giá": "1,250,000.0000", "Thành tiền": "1,250,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD005970", "Tên hàng hóa": "Bóng LED bulb Rạng Đông A60 9W", "Đơn vị tính": "cái", "Số lượng": "1", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD005971", "Tên hàng hóa": "Bộ van dây gas Namilux", "Đơn vị tính": "bộ", "Số lượng": "2", "Đơn giá": "250,000.0000", "Thành tiền": "500,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 10.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD006855", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "2", "Đơn giá": "1,300.0000", "Thành tiền": "2,600.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD006856", "Tên hàng hóa": "Bột trét Jotun nội thất 40kg", "Đơn vị tính": "bao", "Số lượng": "3", "Đơn giá": "315,000.0000", "Thành tiền": "945,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD006857", "Tên hàng hóa": "Công tắc 1 chiều Panasonic Wide kèm mặt", "Đơn vị tính": "bộ", "Số lượng": "2", "Đơn giá": "35,000.0000", "Thành tiền": "70,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 11.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD007734", "Tên hàng hóa": "Thước thủy nhôm Total 60cm", "Đơn vị tính": "cái", "Số lượng": "1", "Đơn giá": "100,000.0000", "Thành tiền": "100,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD007734", "Tên hàng hóa": "Băng keo điện Nano 20 yard", "Đơn vị tính": "cuộn", "Số lượng": "2 cuộn", "Đơn giá": "9,000.0000", "Thành tiền": "18,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD007735", "Tên hàng hóa": "Bộ đèn tuýp LED T8 1.2m 18W Rạng Đông", "Đơn vị tính": "bộ", "Số lượng": "2", "Đơn giá": "155,000.0000", "Thành tiền": "294,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 12.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD008594", "Tên hàng hóa": "Ổ cắm đôi 3 chấu Panasonic Wide WEV1582S", "Đơn vị tính": "cái", "Số lượng": "1 cái", "Đơn giá": "68,000.0000", "Thành tiền": "68,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD008594", "Tên hàng hóa": "Thép Pomina D10 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "3", "Đơn giá": "121,000.0000", "Thành tiền": "363,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD008595", "Tên hàng hóa": "Keo chà ron Weber 1kg", "Đơn vị tính": "gói", "Số lượng": "2 gói", "Đơn giá": "40,000.0000", "Thành tiền": "80,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 01.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD009492", "Tên hàng hóa": "Kẽm buộc 1mm", "Đơn vị tính": "kg", "Số lượng": "1", "Đơn giá": "22,000.0000", "Thành tiền": "22,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD009493", "Tên hàng hóa": "Gas Saigon Petro 12kg", "Đơn vị tính": "bình", "Số lượng": "2", "Đơn giá": "560,000.0000", "Thành tiền": "1,064,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD009493", "Tên hàng hóa": "Nước khoáng Lavie 19L", "Đơn vị tính": "bình", "Số lượng": "1 bình", "Đơn giá": "68,000.0000", "Thành tiền": "68,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 02.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD010347", "Tên hàng hóa": "Sơn Maxilite trong nhà 18L", "Đơn vị tính": "thùng", "Số lượng": "3 thùng", "Đơn giá": "827,000.0000", "Thành tiền": "2,481,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD010348", "Tên hàng hóa": "Gas Saigon Petro 12kg", "Đơn vị tính": "bình", "Số lượng": "1", "Đơn giá": "560,000.0000", "Thành tiền": "560,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD010349", "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg", "Đơn vị tính": "bao", "Số lượng": "1", "Đơn giá": "105,000.0000", "Thành tiền": "105,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 03.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD010914", "Tên hàng hóa": "Băng keo điện Nano 20 yard", "Đơn vị tính": "cuộn", "Số lượng": "2", "Đơn giá": "9,000.0000", "Thành tiền": "18,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD010914", "Tên hàng hóa": "Nước tinh khiết Bidrico 20L", "Đơn vị tính": "bình", "Số lượng": "3 bình", "Đơn giá": "47,000.0000", "Thành tiền": "141,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD010915", "Tên hàng hóa": "Keo dán gạch Weber.tai fix xám 25kg", "Đơn vị tính": "bao", "Số lượng": "2 bao", "Đơn giá": "331,000.0000", "Thành tiền": "662,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 04.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD011763", "Tên hàng hóa": "Nước kiềm Ion Life 19L", "Đơn vị tính": "bình", "Số lượng": "1 bình", "Đơn giá": "72,000.0000", "Thành tiền": "72,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD011764", "Tên hàng hóa": "Cát xây tô", "Đơn vị tính": "xe 4m3", "Số lượng": "1", "Đơn giá": "1,200,000.0000", "Thành tiền": "1,200,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD011764", "Tên hàng hóa": "Keo dán gạch Weber.tai fix xám 25kg", "Đơn vị tính": "bao", "Số lượng": "2", "Đơn giá": "331,000.0000", "Thành tiền": "662,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: 05.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD012554", "Tên hàng hóa": "Gạch ốp tường Viglacera 30x60 thùng 8 vi", "Đơn vị tính": "thùng", "Số lượng": "1", "Đơn giá": "280,000.0000", "Thành tiền": "280,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD012555", "Tên hàng hóa": "Ổ cắm đôi 3 chấu Panasonic Wide WEV1582S", "Đơn vị tính": "cái", "Số lượng": "2", "Đơn giá": "68,000.0000", "Thành tiền": "136,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD012556", "Tên hàng hóa": "Gas Petrolimex 12kg", "Đơn vị tính": "bình", "Số lượng": "3 bình", "Đơn giá": "520,000.0000", "Thành tiền": "1,560,000.0000", "Trạng thái": "Đã hoàn thành"}
```

---

## Business `biz_116`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_116  File Excel xuất từ phần mềm bán hàng, mỗi báo cáo, danh sách một file hoặc một sheet. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng của đơn; sổ không có mã hàng, nối với danh sách hàng hóa qua tên hàng hóa. Ngày dạng dd/mm/yyyy.  Các danh sách `So_chi_tiet_ban_hang`, `Danh sách hàng hóa`, `Bảng kê phiếu giao hàng`, `Chi tiết công nợ theo hạn` nằm chung file `Bao_cao_ban_hang.xlsx`, mỗi danh sách một sheet.  ## File - `Bao_cao_ban_hang.xlsx` (xl
- **Files on disk (2):** Bao_cao_ban_hang.xlsx, README.md

### Tables / Sheets Detail:
#### Table `Bao_cao_ban_hang.xlsx :: So_chi_tiet_ban_hang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Gạch thẻ đặc 4x8x18", "Đơn vị tính": "viên", "Số lượng": "1", "Đơn giá": "1,500.0000", "Thành tiền": "1,500.0000", "Trạng thái": "ok"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Dây điện Cadivi VCmd 2x2.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "1", "Đơn giá": "2,760,000.0000", "Thành tiền": "2,760,000.0000", "Trạng thái": "ok"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Đinh 5 phân", "Đơn vị tính": "kg", "Số lượng": "1 kg", "Đơn giá": "20,000.0000", "Thành tiền": "20,000.0000", "Trạng thái": "ok"}
```

#### Table `Bao_cao_ban_hang.xlsx :: Danh sách hàng hóa`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Bảo hành, Mã hàng hóa, Tên hàng hóa, Hình ảnh (url1,url2...), Thuộc tính, Mẫu ghi chú, Mô tả sản phẩm, Nhóm hàng hóa, Đơn vị tính, Trọng lượng, Tồn nhỏ nhất, Mã HH Liên quan, Ghi chú, Được bán trực tiếp, Giá vốn...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Bảo hành": null, "Mã hàng hóa": "SP0001", "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg", "Hình ảnh (url1,url2...)": null, "Thuộc tính": null, "Mẫu ghi chú": null, "Mô tả sản phẩm": null, "Nhóm hàng hóa": "xi măng"}
{"Bảo hành": null, "Mã hàng hóa": "SP0002", "Tên hàng hóa": "Xi măng INSEE Power-S bao 50kg", "Hình ảnh (url1,url2...)": null, "Thuộc tính": null, "Mẫu ghi chú": null, "Mô tả sản phẩm": null, "Nhóm hàng hóa": "xi măng"}
{"Bảo hành": null, "Mã hàng hóa": "SP0003", "Tên hàng hóa": "Cát xây tô", "Hình ảnh (url1,url2...)": null, "Thuộc tính": null, "Mẫu ghi chú": null, "Mô tả sản phẩm": null, "Nhóm hàng hóa": "cát đá"}
```

#### Table `Bao_cao_ban_hang.xlsx :: Bảng kê phiếu giao hàng`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày giao hàng, Mã đơn hàng, Lần giao, Tên hàng hóa, Đơn vị tính, Số lượng giao, Biển số xe, Người giao hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày giao hàng": "02/05/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Gạch thẻ đặc 4x8x18", "Đơn vị tính": "viên", "Số lượng giao": "1", "Biển số xe": "51D-961.15", "Người giao hàng": "Chung Nam"}
{"Ngày giao hàng": "02/05/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Dây điện Cadivi VCmd 2x2.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng giao": "1", "Biển số xe": "51D-961.15", "Người giao hàng": "Chung Nam"}
{"Ngày giao hàng": "02/05/2025", "Mã đơn hàng": "ORD000001", "Lần giao": "1", "Tên hàng hóa": "Đinh 5 phân", "Đơn vị tính": "kg", "Số lượng giao": "1", "Biển số xe": "51D-961.15", "Người giao hàng": "Chung Nam"}
```

#### Table `Bao_cao_ban_hang.xlsx :: Chi tiết công nợ theo hạn`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn hàng, Số ngày được nợ, Hạn thanh toán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Số ngày được nợ": "30", "Hạn thanh toán": "31/05/2025"}
{"Mã đơn hàng": "ORD000003", "Số ngày được nợ": "30", "Hạn thanh toán": "31/05/2025"}
{"Mã đơn hàng": "ORD000009", "Số ngày được nợ": "30", "Hạn thanh toán": "31/05/2025"}
```

---

## Business `biz_117`
- **Structure Archetype:** Multi-table Relational (23 tables)
- **README (truncated 500 chars):** # Dữ liệu biz_117  Sổ bán hàng ghi tay chuyển sang Excel, mỗi tháng một sheet.  ## File - `SoBanHang.xlsx` (xlsx) - `DanhMuc.xlsx` (xlsx) - `TonKho.xlsx` (xlsx) - `SoGiaoHang.xlsx` (xlsx) - `SoHanNo.xlsx` (xlsx) - `SoNhapHang.xlsx` (xlsx) - `BangGia.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **Giờ**: giờ đặt đơn (dòng trả hàng: lúc trả) - **Mã phiếu**: mã đơn - **TenKH**: tên khách (Khách lẻ nếu không lưu) - **Ngày lập**: ngày bán - **Tiền**: thành tiền sau giảm - **Ghi chú TT**: trạng thái đ
- **Files on disk (8):** BangGia.xlsx, DanhMuc.xlsx, README.md, SoBanHang.xlsx, SoGiaoHang.xlsx, SoHanNo.xlsx, SoNhapHang.xlsx, TonKho.xlsx

### Tables / Sheets Detail:
#### Table `BangGia.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Ngày áp dụng, Giá cũ, Giá mới, TenHang
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày áp dụng": "45658", "Giá cũ": null, "Giá mới": "105.000đ", "TenHang": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Ngày áp dụng": "45781", "Giá cũ": "105.000đ", "Giá mới": "110.000đ", "TenHang": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Ngày áp dụng": "45846", "Giá cũ": "110.000đ", "Giá mới": "115.500đ", "TenHang": "Xi măng Hà Tiên PCB40 bao 50kg"}
```

#### Table `DanhMuc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Hàng, ĐV lớn, ĐV nhỏ, Hệ số QĐ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Xi măng Hà Tiên PCB40 bao 50kg", "ĐV lớn": "tấn", "ĐV nhỏ": "bao", "Hệ số QĐ": "20"}
{"Hàng": "Xi măng INSEE Power-S bao 50kg", "ĐV lớn": "tấn", "ĐV nhỏ": "bao", "Hệ số QĐ": "20"}
{"Hàng": "Cát xây tô", "ĐV lớn": "xe 4m3", "ĐV nhỏ": "m3", "Hệ số QĐ": "4"}
```

#### Table `SoBanHang.xlsx :: Tháng 01-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-01-01 06:13:20", "col_1": "ORD000001", "col_2": "Triệu Đức Duy", "col_3": "1/1", "Tiền": "1tr440", "col_5": "Thành công", "col_6": "720.000đ", "Hàng": "thùng"}
{"Đơn": "2025-01-01 06:17:24", "col_1": "ORD000002", "col_2": "lẻ", "col_3": "1/1", "Tiền": "300.000đ", "col_5": "Đã hoàn thành", "col_6": "300.000đ", "Hàng": "bao"}
```

#### Table `SoBanHang.xlsx :: Tháng 02-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-02-01 06:07:13", "col_1": "ORD000696", "col_2": "Khách lẻ", "col_3": "45689", "Tiền": "825.000đ", "col_5": "Thành công", "col_6": "165.000đ", "Hàng": "cây"}
{"Đơn": "2025-02-01 06:07:13", "col_1": "ORD000696", "col_2": "Khách lẻ", "col_3": "1 thg 2 2025", "Tiền": "1tr050", "col_5": "Thành công", "col_6": "350.000đ", "Hàng": "m3"}
```

#### Table `SoBanHang.xlsx :: Tháng 03-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-03-01 06:12:27", "col_1": "ORD001397", "col_2": "Đỗ Dương Phong", "col_3": "45717", "Tiền": "300.000đ", "col_5": "đã lấy", "col_6": "300.000đ", "Hàng": "m3"}
{"Đơn": "2025-03-01 06:12:27", "col_1": "ORD001397", "col_2": "Đỗ Dương Phong", "col_3": "45717", "Tiền": "144.000đ", "col_5": "đã lấy", "col_6": "72.000đ", "Hàng": "bình"}
```

#### Table `SoBanHang.xlsx :: Tháng 04-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-04-01 15:07:04", "col_1": "ORD002250", "col_2": "Dương Phúc Hương", "col_3": "1/4", "Tiền": "-15.300đ", "col_5": "trả lại", "col_6": "15.300đ", "Hàng": "kg"}
{"Đơn": "2025-04-01 07:07:31", "col_1": "ORD002318", "col_2": "Đặng Hà Khoa", "col_3": "45748", "Tiền": "520.000đ", "col_5": "đã lấy", "col_6": "520.000đ", "Hàng": "bình"}
```

#### Table `SoBanHang.xlsx :: Tháng 05-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-05-01 06:10:21", "col_1": "ORD003180", "col_2": "khách lẻ", "col_3": "01/05/2025", "Tiền": "790.000đ", "col_5": "Thành công", "col_6": "790.000đ", "Hàng": "cuộn"}
{"Đơn": "2025-05-01 06:12:53", "col_1": "ORD003181", "col_2": "kl", "col_3": "1 thg 5 2025", "Tiền": "295.000đ", "col_5": "Thành công", "col_6": "295.000đ", "Hàng": "cây"}
```

#### Table `SoBanHang.xlsx :: Tháng 06-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-06-01 06:25:17", "col_1": "ORD004106", "col_2": "khách lẻ", "col_3": "01/06/2025", "Tiền": "180.000đ", "col_5": "Thành công", "col_6": "90.000đ", "Hàng": "cây"}
{"Đơn": "2025-06-01 06:25:17", "col_1": "ORD004106", "col_2": "khách lẻ", "col_3": "45809", "Tiền": "155.000đ", "col_5": "Thành công", "col_6": "155.000đ", "Hàng": "bộ"}
```

#### Table `SoBanHang.xlsx :: Tháng 07-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-07-01 07:34:30", "col_1": "ORD005051", "col_2": "lẻ", "col_3": "45839", "Tiền": "295.000đ", "col_5": "đã lấy", "col_6": "295.000đ", "Hàng": "cây"}
{"Đơn": "2025-07-01 07:34:30", "col_1": "ORD005051", "col_2": "lẻ", "col_3": "1/7", "Tiền": "220.000đ", "col_5": "đã lấy", "col_6": "110.000đ", "Hàng": "bao"}
```

#### Table `SoBanHang.xlsx :: Tháng 08-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-08-01 07:14:37", "col_1": "ORD005961", "col_2": "lẻ", "col_3": "1 thg 8 2025", "Tiền": "20.000đ", "col_5": "Thành công", "col_6": "20.000đ", "Hàng": "kg"}
{"Đơn": "2025-08-01 07:17:45", "col_1": "ORD005962", "col_2": "Quách Hạnh Nam", "col_3": "45870", "Tiền": "85.000đ", "col_5": "Thành công", "col_6": "85.000đ", "Hàng": "m"}
```

#### Table `SoBanHang.xlsx :: Tháng 09-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-09-01 06:16:23", "col_1": "ORD006881", "col_2": "lẻ", "col_3": "45901", "Tiền": "1tr995", "col_5": "đã lấy", "col_6": "399.000đ", "Hàng": "m3"}
{"Đơn": "2025-09-01 06:16:23", "col_1": "ORD006881", "col_2": "lẻ", "col_3": "01/09/2025", "Tiền": "825.000đ", "col_5": "đã lấy", "col_6": "165.000đ", "Hàng": "cây"}
```

#### Table `SoBanHang.xlsx :: Tháng 10-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-10-01 06:02:30", "col_1": "ORD007788", "col_2": "Tạ Ngọc Hoa", "col_3": "01/10/2025", "Tiền": "155.000đ", "col_5": "đã lấy", "col_6": "155.000đ", "Hàng": "bộ"}
{"Đơn": "2025-10-01 06:27:13", "col_1": "ORD007789", "col_2": "Phạm Hoa Hạnh", "col_3": "1/10", "Tiền": "300.000đ", "col_5": "Đã hoàn thành", "col_6": "100.000đ", "Hàng": "cái"}
```

#### Table `SoBanHang.xlsx :: Tháng 11-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-11-01 06:16:00", "col_1": "ORD008699", "col_2": "kl", "col_3": "01/11/2025", "Tiền": "2tr", "col_5": "Thành công", "col_6": "100.000đ", "Hàng": "bao"}
{"Đơn": "2025-11-01 06:16:00", "col_1": "ORD008699", "col_2": "kl", "col_3": "01/11/2025", "Tiền": "300.000đ", "col_5": "Thành công", "col_6": "300.000đ", "Hàng": "m3"}
```

#### Table `SoBanHang.xlsx :: Tháng 12-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2025-12-01 06:04:05", "col_1": "ORD009591", "col_2": "khách lẻ", "col_3": "01/12/2025", "Tiền": "47.000đ", "col_5": "Thành công", "col_6": "47.000đ", "Hàng": "bình"}
{"Đơn": "2025-12-01 06:04:05", "col_1": "ORD009591", "col_2": "khách lẻ", "col_3": "01/12/2025", "Tiền": "115.000đ", "col_5": "Thành công", "col_6": "115.000đ", "Hàng": "cây"}
```

#### Table `SoBanHang.xlsx :: Tháng 01-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2026-01-01 18:57:42", "col_1": "ORD010355", "col_2": "lẻ", "col_3": "1/1", "Tiền": "-1.400đ", "col_5": "Đã trả hàng", "col_6": "1.400đ", "Hàng": "viên"}
{"Đơn": "2026-01-01 06:49:39", "col_1": "ORD010533", "col_2": "Đinh Hải Hương", "col_3": "1 thg 1 2026", "Tiền": "347.500đ", "col_5": "Thành công", "col_6": "347.500đ", "Hàng": "thùng"}
```

#### Table `SoBanHang.xlsx :: Tháng 02-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2026-02-01 06:15:58", "col_1": "ORD011587", "col_2": "lẻ", "col_3": "1/2", "Tiền": "310.000đ", "col_5": "Thành công", "col_6": "155.000đ", "Hàng": "bộ"}
{"Đơn": "2026-02-01 06:15:58", "col_1": "ORD011587", "col_2": "lẻ", "col_3": "1/2", "Tiền": "110.000đ", "col_5": "Thành công", "col_6": "55.000đ", "Hàng": "bình"}
```

#### Table `SoBanHang.xlsx :: Tháng 03-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2026-03-01 06:16:20", "col_1": "ORD012251", "col_2": "Khách lẻ", "col_3": "46082", "Tiền": "130.000đ", "col_5": "Thành công", "col_6": "65.000đ", "Hàng": "bình"}
{"Đơn": "2026-03-01 06:29:34", "col_1": "ORD012252", "col_2": "Bạch An Hoàng", "col_3": "1 thg 3 2026", "Tiền": "2.800đ", "col_5": "Đã hoàn thành", "col_6": "1.400đ", "Hàng": "viên"}
```

#### Table `SoBanHang.xlsx :: Tháng 04-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2026-04-01 06:01:33", "col_1": "ORD013291", "col_2": "Bùi Long Thắng", "col_3": "1/4", "Tiền": "504.000đ", "col_5": "Thành công", "col_6": "252.000đ", "Hàng": "m3"}
{"Đơn": "2026-04-01 06:01:33", "col_1": "ORD013291", "col_2": "Bùi Long Thắng", "col_3": "1/4", "Tiền": "230.000đ", "col_5": "Thành công", "col_6": "115.000đ", "Hàng": "cây"}
```

#### Table `SoBanHang.xlsx :: Tháng 05-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn, col_1, col_2, col_3, Tiền, col_5, col_6, Hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Giờ", "col_1": "Mã phiếu", "col_2": "TenKH", "col_3": "Ngày lập", "Tiền": "Tiền", "col_5": "Ghi chú TT", "col_6": "Giá", "Hàng": "DonVi"}
{"Đơn": "2026-05-01 06:37:35", "col_1": "ORD014314", "col_2": "Quách Hiếu Hoa", "col_3": "1 thg 5 2026", "Tiền": "575.000đ", "col_5": "đã lấy", "col_6": "115.000đ", "Hàng": "cây"}
{"Đơn": "2026-05-01 06:37:35", "col_1": "ORD014314", "col_2": "Quách Hiếu Hoa", "col_3": "1 thg 5 2026", "Tiền": "68.000đ", "col_5": "đã lấy", "col_6": "68.000đ", "Hàng": "cái"}
```

#### Table `SoGiaoHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** ĐV gốc, Biển số xe, Mã bill, Lượt giao, SL thực giao, Tên hàng, Ngày chở, Người chở
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"ĐV gốc": "cây", "Biển số xe": "61C-873.50", "Mã bill": "ORD000006", "Lượt giao": "1", "SL thực giao": "3", "Tên hàng": "Thép Pomina D12 cây 11.7m", "Ngày chở": "2 thg 1 2025", "Người chở": "Chung Ngân"}
{"ĐV gốc": "viên", "Biển số xe": "61C-873.50", "Mã bill": "ORD000007", "Lượt giao": "1", "SL thực giao": "8", "Tên hàng": "Gạch ống 8x8x18 Tuynel", "Ngày chở": "2 thg 1 2025", "Người chở": "Chung Ngân"}
{"ĐV gốc": "cái", "Biển số xe": "61C-873.50", "Mã bill": "ORD000007", "Lượt giao": "1", "SL thực giao": "1", "Tên hàng": "Bay thợ hồ Total 160mm", "Ngày chở": "2 thg 1 2025", "Người chở": "Chung Ngân"}
```

#### Table `SoHanNo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** So hoa don, Hạn nợ (ngày), Han tra
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"So hoa don": "ORD000001", "Hạn nợ (ngày)": "30", "Han tra": "31/01/2025"}
{"So hoa don": "ORD000004", "Hạn nợ (ngày)": "30", "Han tra": "45688"}
{"So hoa don": "ORD000008", "Hạn nợ (ngày)": "30", "Han tra": "45688"}
```

#### Table `SoNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Số phiếu, Product, Ngày nhập, ĐVT, Thành tiền, Nội dung, Nhà cung cấp, SL nhập, Giá nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số phiếu": "PN00001", "Product": "Xi măng Hà Tiên PCB40 bao 50kg", "Ngày nhập": "45658", "ĐVT": "tấn", "Thành tiền": "16,56tr", "Nội dung": "nhập đầu kỳ", "Nhà cung cấp": "Cty Châu Linh", "SL nhập": "9"}
{"Số phiếu": "PN00001", "Product": "Xi măng INSEE Power-S bao 50kg", "Ngày nhập": "01/01/2025", "ĐVT": "tấn", "Thành tiền": "9tr960", "Nội dung": "nhập đầu kỳ", "Nhà cung cấp": "Cty Châu Linh", "SL nhập": "6"}
{"Số phiếu": "PN00001", "Product": "Cát xây tô", "Ngày nhập": "01/01/2025", "ĐVT": "xe 4m3", "Thành tiền": "35,56tr", "Nội dung": "nhập đầu kỳ", "Nhà cung cấp": "Cty Châu Linh", "SL nhập": "35"}
```

#### Table `TonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Tồn thực, Đơn vị, Product
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tồn thực": "169", "Đơn vị": "bao", "Product": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Tồn thực": "36", "Đơn vị": "bao", "Product": "Xi măng INSEE Power-S bao 50kg"}
{"Tồn thực": "78", "Đơn vị": "m3", "Product": "Cát xây tô"}
```

---

## Business `biz_118`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_118  File Excel xuất từ phần mềm bán hàng. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng.  File `So_chi_tiet_ban_hang.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `So_chi_tiet_ban_hang.xlsx` (xlsx) - `Danh sách hàng hóa.xlsx` (xlsx) - `Bảng kê phiếu giao hàng.xlsx` (xlsx) - `Chi tiết công nợ theo hạn.xlsx` (xlsx)  ## Cột trong `So_chi_tiet_ban_hang.xlsx` - **Ngày**: ngày bán - **Mã đơn hàng**: mã đơn - **Tên hàng hóa**: tên
- **Files on disk (5):** Bảng kê phiếu giao hàng.xlsx, Chi tiết công nợ theo hạn.xlsx, Danh sách hàng hóa.xlsx, README.md, So_chi_tiet_ban_hang.xlsx

### Tables / Sheets Detail:
#### Table `Bảng kê phiếu giao hàng.xlsx :: Sheet1`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày giao hàng, Mã đơn hàng, Lần giao, Tên hàng hóa, Đơn vị tính, Số lượng giao, Biển số xe, Người giao hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày giao hàng": "02/02/2025", "Mã đơn hàng": "ORD000002", "Lần giao": "1", "Tên hàng hóa": "Kẽm buộc 1mm", "Đơn vị tính": "kg", "Số lượng giao": "1", "Biển số xe": "51C-327.66", "Người giao hàng": "Ông Hương"}
{"Ngày giao hàng": "03/02/2025", "Mã đơn hàng": "ORD000002", "Lần giao": "2", "Tên hàng hóa": "Kẽm buộc 1mm", "Đơn vị tính": "kg", "Số lượng giao": "1", "Biển số xe": "51D-233.15", "Người giao hàng": "Châu Giang"}
{"Ngày giao hàng": "06/02/2025", "Mã đơn hàng": "ORD000002", "Lần giao": "3", "Tên hàng hóa": "Cát xây tô", "Đơn vị tính": "m3", "Số lượng giao": "1", "Biển số xe": "51C-327.66", "Người giao hàng": "Ông Hương"}
```

#### Table `Chi tiết công nợ theo hạn.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn hàng, Số ngày được nợ, Hạn thanh toán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000005", "Số ngày được nợ": "30", "Hạn thanh toán": "03/03/2025"}
{"Mã đơn hàng": "ORD000006", "Số ngày được nợ": "60", "Hạn thanh toán": "02/04/2025"}
{"Mã đơn hàng": "ORD000007", "Số ngày được nợ": "30", "Hạn thanh toán": "03/03/2025"}
```

#### Table `Danh sách hàng hóa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (16):** Hình ảnh (url1,url2...), Vị trí, Trọng lượng, Bảo hành, Mã hàng hóa, Mã barcode, Mô tả sản phẩm, Tên hàng hóa, Loại hàng hóa, Nhóm hàng hóa, Đơn vị tính, Mã HH Liên quan, Tồn lớn nhất, Ghi chú, Mẫu ghi chú...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hình ảnh (url1,url2...)": null, "Vị trí": null, "Trọng lượng": null, "Bảo hành": null, "Mã hàng hóa": "SP0001", "Mã barcode": null, "Mô tả sản phẩm": null, "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Hình ảnh (url1,url2...)": null, "Vị trí": null, "Trọng lượng": null, "Bảo hành": null, "Mã hàng hóa": "SP0002", "Mã barcode": "8939792877748", "Mô tả sản phẩm": null, "Tên hàng hóa": "Xi măng INSEE Power-S bao 50kg"}
{"Hình ảnh (url1,url2...)": null, "Vị trí": null, "Trọng lượng": null, "Bảo hành": null, "Mã hàng hóa": "SP0003", "Mã barcode": null, "Mô tả sản phẩm": null, "Tên hàng hóa": "Cát xây tô"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T02-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Ống PVC Bình Minh D32 cây 4m", "Đơn vị tính": "cây", "Số lượng": "2", "Đơn giá": "65,000.0000", "Thành tiền": "130,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000002", "Tên hàng hóa": "Cát xây tô", "Đơn vị tính": "m3", "Số lượng": "1", "Đơn giá": "300,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000002", "Tên hàng hóa": "Kẽm buộc 1mm", "Đơn vị tính": "kg", "Số lượng": "3", "Đơn giá": "20,000.0000", "Thành tiền": "60,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T03-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000935", "Tên hàng hóa": "Thép cuộn phi 6 Hòa Phát", "Đơn vị tính": "kg", "Số lượng": "1", "Đơn giá": "16,500.0000", "Thành tiền": "16,500.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000935", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "10 viên", "Đơn giá": "1,300.0000", "Thành tiền": "13,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/03/2025", "Mã đơn hàng": "ORD000935", "Tên hàng hóa": "Xi măng INSEE Power-S bao 50kg", "Đơn vị tính": "bao", "Số lượng": "3 bao", "Đơn giá": "100,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T04-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD002130", "Tên hàng hóa": "Gạch thẻ đặc 4x8x18", "Đơn vị tính": "viên", "Số lượng": "1 viên", "Đơn giá": "1,500.0000", "Thành tiền": "1,500.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD002130", "Tên hàng hóa": "Gas Petrolimex 12kg", "Đơn vị tính": "bình", "Số lượng": "3", "Đơn giá": "520,000.0000", "Thành tiền": "1,560,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/04/2025", "Mã đơn hàng": "ORD002131", "Tên hàng hóa": "Thép cuộn phi 8 Hòa Phát", "Đơn vị tính": "kg", "Số lượng": "1", "Đơn giá": "15,300.0000", "Thành tiền": "15,300.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T05-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD003265", "Tên hàng hóa": "Thép Pomina D14 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "1", "Đơn giá": "225,000.0000", "Thành tiền": "225,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD003266", "Tên hàng hóa": "Đá 4x6", "Đơn vị tính": "m3", "Số lượng": "2", "Đơn giá": "350,000.0000", "Thành tiền": "700,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/05/2025", "Mã đơn hàng": "ORD003266", "Tên hàng hóa": "Gạch thẻ đặc 4x8x18", "Đơn vị tính": "viên", "Số lượng": "3", "Đơn giá": "1,500.0000", "Thành tiền": "4,500.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T06-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD004457", "Tên hàng hóa": "Bột trét Jotun nội thất 40kg", "Đơn vị tính": "bao", "Số lượng": "1", "Đơn giá": "300,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD004457", "Tên hàng hóa": "Xi măng Hà Tiên PCB40 bao 50kg", "Đơn vị tính": "bao", "Số lượng": "1", "Đơn giá": "105,000.0000", "Thành tiền": "105,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/06/2025", "Mã đơn hàng": "ORD004458", "Tên hàng hóa": "Keo dán gạch Weber.tai fix xám 25kg", "Đơn vị tính": "bao", "Số lượng": "3 bao", "Đơn giá": "300,000.0000", "Thành tiền": "900,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T07-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD005587", "Tên hàng hóa": "Bột trét Jotun nội thất 40kg", "Đơn vị tính": "bao", "Số lượng": "2 bao", "Đơn giá": "300,000.0000", "Thành tiền": "600,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD005588", "Tên hàng hóa": "Gas Saigon Petro 12kg", "Đơn vị tính": "bình", "Số lượng": "1", "Đơn giá": "560,000.0000", "Thành tiền": "560,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/07/2025", "Mã đơn hàng": "ORD005589", "Tên hàng hóa": "Thép Pomina D12 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "2", "Đơn giá": "173,000.0000", "Thành tiền": "346,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T08-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD006729", "Tên hàng hóa": "Nước khoáng Lavie 19L", "Đơn vị tính": "bình", "Số lượng": "5", "Đơn giá": "65,000.0000", "Thành tiền": "325,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD006729", "Tên hàng hóa": "Tấm thạch cao Gyproc 9mm 1.2x2.4m", "Đơn vị tính": "tấm", "Số lượng": "5", "Đơn giá": "110,000.0000", "Thành tiền": "550,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/08/2025", "Mã đơn hàng": "ORD006729", "Tên hàng hóa": "Thép cuộn phi 6 Hòa Phát", "Đơn vị tính": "kg", "Số lượng": "2 kg", "Đơn giá": "16,500.0000", "Thành tiền": "33,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T09-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD007864", "Tên hàng hóa": "Thép Pomina D12 cây 11.7m", "Đơn vị tính": "cây", "Số lượng": "5 cây", "Đơn giá": "181,500.0000", "Thành tiền": "907,500.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD007864", "Tên hàng hóa": "Công tắc 1 chiều Panasonic Wide kèm mặt", "Đơn vị tính": "bộ", "Số lượng": "2", "Đơn giá": "41,000.0000", "Thành tiền": "82,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/09/2025", "Mã đơn hàng": "ORD007864", "Tên hàng hóa": "Ống PVC Bình Minh D32 cây 4m", "Đơn vị tính": "cây", "Số lượng": "1 cây", "Đơn giá": "65,000.0000", "Thành tiền": "65,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T10-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD009020", "Tên hàng hóa": "Lưới B40 mạ kẽm khổ 1.5m", "Đơn vị tính": "m", "Số lượng": "3 m", "Đơn giá": "50,500.0000", "Thành tiền": "151,500.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD009020", "Tên hàng hóa": "Công tắc 1 chiều Panasonic Wide kèm mặt", "Đơn vị tính": "bộ", "Số lượng": "1 bộ", "Đơn giá": "41,000.0000", "Thành tiền": "41,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/10/2025", "Mã đơn hàng": "ORD009020", "Tên hàng hóa": "Keo dán ống PVC Bình Minh 200g", "Đơn vị tính": "lon", "Số lượng": "2", "Đơn giá": "35,000.0000", "Thành tiền": "70,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T11-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD010130", "Tên hàng hóa": "Dây điện Cadivi VCmd 2x2.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "1", "Đơn giá": "2,898,000.0000", "Thành tiền": "2,898,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD010130", "Tên hàng hóa": "Đá mi bụi", "Đơn vị tính": "m3", "Số lượng": "1", "Đơn giá": "300,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/11/2025", "Mã đơn hàng": "ORD010131", "Tên hàng hóa": "Bóng LED bulb Rạng Đông A60 9W", "Đơn vị tính": "cái", "Số lượng": "1", "Đơn giá": "47,000.0000", "Thành tiền": "47,000.0000", "Trạng thái": "đã xong"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T12-2025`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD011220", "Tên hàng hóa": "Keo dán gạch Weber.tai fix xám 25kg", "Đơn vị tính": "bao", "Số lượng": "1 bao", "Đơn giá": "300,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "hủy"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD011220", "Tên hàng hóa": "Thép cuộn phi 8 Hòa Phát", "Đơn vị tính": "kg", "Số lượng": "2", "Đơn giá": "16,000.0000", "Thành tiền": "32,000.0000", "Trạng thái": "hủy"}
{"Ngày": "01/12/2025", "Mã đơn hàng": "ORD011220", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "3", "Đơn giá": "1,300.0000", "Thành tiền": "3,900.0000", "Trạng thái": "hủy"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T01-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD012360", "Tên hàng hóa": "Chống thấm Kova CT-11A tường 20kg", "Đơn vị tính": "thùng", "Số lượng": "1", "Đơn giá": "2,150,000.0000", "Thành tiền": "2,150,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD012360", "Tên hàng hóa": "Đinh 5 phân", "Đơn vị tính": "kg", "Số lượng": "1", "Đơn giá": "20,000.0000", "Thành tiền": "20,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/01/2026", "Mã đơn hàng": "ORD012361", "Tên hàng hóa": "Gas Petrolimex 12kg", "Đơn vị tính": "bình", "Số lượng": "3", "Đơn giá": "520,000.0000", "Thành tiền": "1,560,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T02-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD013485", "Tên hàng hóa": "Thép cuộn phi 8 Hòa Phát", "Đơn vị tính": "kg", "Số lượng": "2", "Đơn giá": "16,000.0000", "Thành tiền": "32,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD013485", "Tên hàng hóa": "Bộ van dây gas Namilux", "Đơn vị tính": "bộ", "Số lượng": "1", "Đơn giá": "250,000.0000", "Thành tiền": "250,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/02/2026", "Mã đơn hàng": "ORD013486", "Tên hàng hóa": "Keo dán gạch Weber.tai fix xám 25kg", "Đơn vị tính": "bao", "Số lượng": "1", "Đơn giá": "300,000.0000", "Thành tiền": "300,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T03-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD014180", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "1", "Đơn giá": "1,300.0000", "Thành tiền": "1,300.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD014180", "Tên hàng hóa": "Lưới B40 mạ kẽm khổ 1.5m", "Đơn vị tính": "m", "Số lượng": "2", "Đơn giá": "50,500.0000", "Thành tiền": "101,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/03/2026", "Mã đơn hàng": "ORD014180", "Tên hàng hóa": "Kẽm buộc 1mm", "Đơn vị tính": "kg", "Số lượng": "2", "Đơn giá": "20,000.0000", "Thành tiền": "40,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T04-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD015285", "Tên hàng hóa": "Ống PVC Bình Minh D50 cây 4m", "Đơn vị tính": "cây", "Số lượng": "1", "Đơn giá": "125,000.0000", "Thành tiền": "125,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD015286", "Tên hàng hóa": "Nước tinh khiết Vihawa 20L", "Đơn vị tính": "bình", "Số lượng": "2", "Đơn giá": "58,000.0000", "Thành tiền": "116,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/04/2026", "Mã đơn hàng": "ORD015286", "Tên hàng hóa": "Gạch ốp tường Viglacera 30x60 thùng 8 vi", "Đơn vị tính": "thùng", "Số lượng": "1 thùng", "Đơn giá": "280,000.0000", "Thành tiền": "280,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T05-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD016345", "Tên hàng hóa": "Keo dán ống PVC Bình Minh 200g", "Đơn vị tính": "lon", "Số lượng": "2 lon", "Đơn giá": "35,000.0000", "Thành tiền": "70,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD016345", "Tên hàng hóa": "Gạch lát nền Prime 60x60 thùng 4 viên", "Đơn vị tính": "thùng", "Số lượng": "2 thùng", "Đơn giá": "315,000.0000", "Thành tiền": "630,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/05/2026", "Mã đơn hàng": "ORD016345", "Tên hàng hóa": "Ổ cắm đôi 3 chấu Panasonic Wide WEV1582S", "Đơn vị tính": "cái", "Số lượng": "1 cái", "Đơn giá": "68,000.0000", "Thành tiền": "68,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T06-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD017429", "Tên hàng hóa": "Ổ cắm đôi 3 chấu Panasonic Wide WEV1582S", "Đơn vị tính": "cái", "Số lượng": "1 cái", "Đơn giá": "68,000.0000", "Thành tiền": "68,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD017429", "Tên hàng hóa": "Sơn lót Jotun Jotashield chống kiềm 5L", "Đơn vị tính": "thùng", "Số lượng": "2", "Đơn giá": "720,000.0000", "Thành tiền": "1,440,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/06/2026", "Mã đơn hàng": "ORD017429", "Tên hàng hóa": "Ống PVC Bình Minh D32 cây 4m", "Đơn vị tính": "cây", "Số lượng": "20 cây", "Đơn giá": "65,000.0000", "Thành tiền": "1,300,000.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T07-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD018425", "Tên hàng hóa": "Nước khoáng Lavie 19L", "Đơn vị tính": "bình", "Số lượng": "1", "Đơn giá": "68,000.0000", "Thành tiền": "68,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD018425", "Tên hàng hóa": "Sơn lót Jotun Jotashield chống kiềm 5L", "Đơn vị tính": "thùng", "Số lượng": "1", "Đơn giá": "720,000.0000", "Thành tiền": "720,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/07/2026", "Mã đơn hàng": "ORD018425", "Tên hàng hóa": "Gạch thẻ đặc 4x8x18", "Đơn vị tính": "viên", "Số lượng": "1", "Đơn giá": "1,600.0000", "Thành tiền": "1,600.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T08-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/08/2026", "Mã đơn hàng": "ORD019467", "Tên hàng hóa": "Nước tinh khiết Bidrico 20L", "Đơn vị tính": "bình", "Số lượng": "1 bình", "Đơn giá": "45,000.0000", "Thành tiền": "45,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/08/2026", "Mã đơn hàng": "ORD019467", "Tên hàng hóa": "Gạch ống 8x8x18 Tuynel", "Đơn vị tính": "viên", "Số lượng": "1 viên", "Đơn giá": "1,300.0000", "Thành tiền": "1,300.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/08/2026", "Mã đơn hàng": "ORD019467", "Tên hàng hóa": "Ngói Đồng Nai 22 viên/m2", "Đơn vị tính": "viên", "Số lượng": "3 viên", "Đơn giá": "13,500.0000", "Thành tiền": "40,500.0000", "Trạng thái": "Đã giao"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: T09-2026`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2026", "Mã đơn hàng": "ORD020526", "Tên hàng hóa": "Băng keo điện Nano 20 yard", "Đơn vị tính": "cuộn", "Số lượng": "1", "Đơn giá": "9,000.0000", "Thành tiền": "9,000.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/09/2026", "Mã đơn hàng": "ORD020526", "Tên hàng hóa": "Dây điện Cadivi CV 1.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "5", "Đơn giá": "914,500.0000", "Thành tiền": "4,572,500.0000", "Trạng thái": "Đã giao"}
{"Ngày": "01/09/2026", "Mã đơn hàng": "ORD020526", "Tên hàng hóa": "Dây điện Cadivi VCmd 2x2.5 cuộn 100m", "Đơn vị tính": "cuộn", "Số lượng": "2", "Đơn giá": "3,043,000.0000", "Thành tiền": "6,086,000.0000", "Trạng thái": "Đã giao"}
```

---

## Business `biz_119`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_119  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…), nối với nhau qua mã. Ngày dạng dd/mm/yyyy.  File `DanhSachHoaDon.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DanhSachHoaDon.xlsx` (xlsx) - `DanhSachHoaDonChiTiet.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DanhSachKhachHang.xlsx` (xlsx) - `BaoCaoTonKho.xlsx` (xlsx) - `DanhSachNhapHang.xlsx` (xlsx)
- **Files on disk (11):** BaoCaoTonKho.xlsx, DanhSachChiTietNhapHang.xlsx, DanhSachHoaDon.xlsx, DanhSachHoaDonChiTiet.xlsx, DanhSachHoaDonChiTietLo.xlsx, DanhSachKhachHang.xlsx, DanhSachLoHang.xlsx, DanhSachNhapHang.xlsx, DanhSachSanPham.xlsx, DanhSachThuoc.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BaoCaoTonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Panadol Extra Hộp 15 Vỉ X 12 Viên", "ĐVT": "viên", "Tồn cuối kỳ": "80"}
{"Mã hàng": "SP0002", "Tên hàng": "Hapacol 250 hộp 24 gói", "ĐVT": "gói", "Tồn cuối kỳ": "165"}
{"Mã hàng": "SP0003", "Tên hàng": "Panadol 500mg hộp 10 vỉ x 12 viên", "ĐVT": "viên", "Tồn cuối kỳ": "58"}
```

#### Table `DanhSachChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá, Lô, Hạn sử dụng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "hộp", "Số lượng": "2", "Đơn giá": "180,000", "Lô": "W2501882", "Hạn sử dụng": "2025-04-26 00:00:00"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "hộp", "Số lượng": "8", "Đơn giá": "36,000", "Lô": "W2501754", "Hạn sử dụng": "2026-09-30 00:00:00"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "hộp", "Số lượng": "2", "Đơn giá": "96,000", "Lô": "M2501906", "Hạn sử dụng": "2025-05-17 00:00:00"}
```

#### Table `DanhSachHoaDon.xlsx :: T01-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "01/01/2025", "Mã KH": "KH0144", "Khách hàng": "Hồ Ngọc Châu", "Tổng tiền hàng": "8,800", "Giảm giá": "0", "Khách đã trả": "8,800", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "01/01/2025", "Mã KH": "KH0206", "Khách hàng": "Phạm Sơn Đức", "Tổng tiền hàng": "5,200", "Giảm giá": "0", "Khách đã trả": "20,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "01/01/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "53,400", "Giảm giá": "0", "Khách đã trả": "53,400", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T02-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD002070", "Thời gian": "01/02/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "13,200", "Giảm giá": "0", "Khách đã trả": "13,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD002071", "Thời gian": "01/02/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,600", "Giảm giá": "0", "Khách đã trả": "1,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD002072", "Thời gian": "01/02/2025", "Mã KH": "KH0267", "Khách hàng": "Chung Hoa Linh", "Tổng tiền hàng": "6,700", "Giảm giá": "0", "Khách đã trả": "6,700", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T03-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD003893", "Thời gian": "01/03/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "5,500", "Giảm giá": "0", "Khách đã trả": "20,500", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD003894", "Thời gian": "01/03/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "117,000", "Giảm giá": "0", "Khách đã trả": "117,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD003895", "Thời gian": "01/03/2025", "Mã KH": "KH0177", "Khách hàng": "Từ Nam Bích", "Tổng tiền hàng": "265,100", "Giảm giá": "0", "Khách đã trả": "265,100", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T04-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD005925", "Thời gian": "01/04/2025", "Mã KH": "KH0214", "Khách hàng": "Vương Loan Bảo", "Tổng tiền hàng": "800", "Giảm giá": "0", "Khách đã trả": "800", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD005926", "Thời gian": "01/04/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "100,000", "Giảm giá": "0", "Khách đã trả": "115,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD005927", "Thời gian": "01/04/2025", "Mã KH": "KH0174", "Khách hàng": "Bùi Anh Long", "Tổng tiền hàng": "6,500", "Giảm giá": "0", "Khách đã trả": "6,500", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T05-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD007877", "Thời gian": "01/05/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,500", "Giảm giá": "0", "Khách đã trả": "1,500", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD007878", "Thời gian": "01/05/2025", "Mã KH": "KH0010", "Khách hàng": "Lâm Trung Hồng", "Tổng tiền hàng": "170,900", "Giảm giá": "0", "Khách đã trả": "170,900", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD007879", "Thời gian": "01/05/2025", "Mã KH": "KH0146", "Khách hàng": "Thái Bảo Linh", "Tổng tiền hàng": "79,600", "Giảm giá": "0", "Khách đã trả": "79,600", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T06-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD009883", "Thời gian": "01/06/2025", "Mã KH": "KH0028", "Khách hàng": "Vũ Ngọc Thanh", "Tổng tiền hàng": "65,000", "Giảm giá": "0", "Khách đã trả": "65,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD009884", "Thời gian": "01/06/2025", "Mã KH": "KH0045", "Khách hàng": "Hồ Khoa Đức", "Tổng tiền hàng": "12,600", "Giảm giá": "0", "Khách đã trả": "12,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD009885", "Thời gian": "01/06/2025", "Mã KH": "KH0004", "Khách hàng": "Luong Huy Hai", "Tổng tiền hàng": "55,000", "Giảm giá": "0", "Khách đã trả": "55,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T07-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD011763", "Thời gian": "01/07/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "8,000", "Giảm giá": "0", "Khách đã trả": "8,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD011764", "Thời gian": "01/07/2025", "Mã KH": "KH0099", "Khách hàng": "Đinh Quân Ngọc", "Tổng tiền hàng": "3,300", "Giảm giá": "0", "Khách đã trả": "3,300", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD011765", "Thời gian": "01/07/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "101,200", "Giảm giá": "0", "Khách đã trả": "101,200", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T08-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD013675", "Thời gian": "01/08/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "22,000", "Giảm giá": "0", "Khách đã trả": "22,000", "Trạng thái": "Đã trả hàng"}
{"Mã hóa đơn": "ORD013676", "Thời gian": "01/08/2025", "Mã KH": "KH0135", "Khách hàng": "Kiều Chi Hùng", "Tổng tiền hàng": "2,300", "Giảm giá": "0", "Khách đã trả": "2,300", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD013677", "Thời gian": "01/08/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "261,000", "Giảm giá": "0", "Khách đã trả": "261,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T09-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD015601", "Thời gian": "01/09/2025", "Mã KH": "KH0188", "Khách hàng": "Tăng Duy Châu", "Tổng tiền hàng": "284,600", "Giảm giá": "0", "Khách đã trả": "284,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD015602", "Thời gian": "01/09/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "40,000", "Giảm giá": "0", "Khách đã trả": "40,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD015603", "Thời gian": "01/09/2025", "Mã KH": "KH0165", "Khách hàng": "Hoàng Hải Chi", "Tổng tiền hàng": "3,000", "Giảm giá": "0", "Khách đã trả": "3,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T10-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD017468", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "500", "Giảm giá": "0", "Khách đã trả": "15,500", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD017469", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "49,000", "Giảm giá": "0", "Khách đã trả": "49,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD017470", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "17,400", "Giảm giá": "0", "Khách đã trả": "17,400", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T11-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD019296", "Thời gian": "01/11/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "104,600", "Giảm giá": "0", "Khách đã trả": "104,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD019297", "Thời gian": "01/11/2025", "Mã KH": "KH0055", "Khách hàng": "Tống Cường Minh", "Tổng tiền hàng": "80,000", "Giảm giá": "0", "Khách đã trả": "80,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD019298", "Thời gian": "01/11/2025", "Mã KH": "KH0076", "Khách hàng": "Đinh Chi Phúc", "Tổng tiền hàng": "120,000", "Giảm giá": "0", "Khách đã trả": "120,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T12-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD021060", "Thời gian": "01/12/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "227,000", "Giảm giá": "0", "Khách đã trả": "227,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD021061", "Thời gian": "01/12/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "313,200", "Giảm giá": "10,000", "Khách đã trả": "303,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD021062", "Thời gian": "01/12/2025", "Mã KH": "KH0289", "Khách hàng": "Đinh Thanh Huy", "Tổng tiền hàng": "1,500", "Giảm giá": "0", "Khách đã trả": "1,500", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T01-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD022894", "Thời gian": "01/01/2026", "Mã KH": "KH0206", "Khách hàng": "Phạm Sơn Đức", "Tổng tiền hàng": "192,000", "Giảm giá": "0", "Khách đã trả": "192,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD022895", "Thời gian": "01/01/2026", "Mã KH": "KH0013", "Khách hàng": "Đàm Hùng Hoa", "Tổng tiền hàng": "150,200", "Giảm giá": "0", "Khách đã trả": "150,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD022896", "Thời gian": "01/01/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "303,000", "Giảm giá": "10,000", "Khách đã trả": "293,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T02-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD024648", "Thời gian": "01/02/2026", "Mã KH": "KH0042", "Khách hàng": "Doãn Khoa Anh", "Tổng tiền hàng": "8,200", "Giảm giá": "0", "Khách đã trả": "8,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD024649", "Thời gian": "01/02/2026", "Mã KH": "KH0126", "Khách hàng": "Dương Mai Khánh", "Tổng tiền hàng": "17,000", "Giảm giá": "0", "Khách đã trả": "17,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD024650", "Thời gian": "01/02/2026", "Mã KH": "KH0038", "Khách hàng": "Châu Trung Bình", "Tổng tiền hàng": "2,600", "Giảm giá": "0", "Khách đã trả": "2,600", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T03-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD026394", "Thời gian": "01/03/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "25,900", "Giảm giá": "0", "Khách đã trả": "25,900", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD026395", "Thời gian": "01/03/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "174,000", "Giảm giá": "0", "Khách đã trả": "174,000", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD026396", "Thời gian": "01/03/2026", "Mã KH": "KH0140", "Khách hàng": "Hứa Loan Dũng", "Tổng tiền hàng": "3,400", "Giảm giá": "0", "Khách đã trả": "3,400", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T04-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD028122", "Thời gian": "01/04/2026", "Mã KH": "KH0281", "Khách hàng": "Phạm Tâm Bích", "Tổng tiền hàng": "1,600", "Giảm giá": "0", "Khách đã trả": "1,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD028123", "Thời gian": "01/04/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "3,200", "Giảm giá": "0", "Khách đã trả": "18,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD028124", "Thời gian": "01/04/2026", "Mã KH": "KH0298", "Khách hàng": "Bùi Chi Duy", "Tổng tiền hàng": "5,000", "Giảm giá": "0", "Khách đã trả": "5,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T05-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD029811", "Thời gian": "01/05/2026", "Mã KH": "KH0063", "Khách hàng": "Võ Châu Giang", "Tổng tiền hàng": "5,900", "Giảm giá": "0", "Khách đã trả": "5,900", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD029812", "Thời gian": "01/05/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "92,600", "Giảm giá": "0", "Khách đã trả": "92,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD029813", "Thời gian": "01/05/2026", "Mã KH": "KH0016", "Khách hàng": "Ông Nhung Thảo", "Tổng tiền hàng": "2,200", "Giảm giá": "0", "Khách đã trả": "2,200", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T06-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD031575", "Thời gian": "01/06/2026", "Mã KH": "KH0268", "Khách hàng": "Doãn Dũng An", "Tổng tiền hàng": "45,200", "Giảm giá": "0", "Khách đã trả": "45,200", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD031576", "Thời gian": "01/06/2026", "Mã KH": "KH0157", "Khách hàng": "Lâm Trang Cường", "Tổng tiền hàng": "16,400", "Giảm giá": "0", "Khách đã trả": "31,400", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD031577", "Thời gian": "01/06/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "265,000", "Giảm giá": "0", "Khách đã trả": "265,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDon.xlsx :: T07-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD033305", "Thời gian": "01/07/2026", "Mã KH": "KH0142", "Khách hàng": "Lưu Mai Thắng", "Tổng tiền hàng": "92,600", "Giảm giá": "0", "Khách đã trả": "92,600", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD033306", "Thời gian": "01/07/2026", "Mã KH": "KH0015", "Khách hàng": "Hoàng Khoa Hùng", "Tổng tiền hàng": "174,400", "Giảm giá": "0", "Khách đã trả": "174,400", "Trạng thái": "Hoàn thành"}
{"Mã hóa đơn": "ORD033307", "Thời gian": "01/07/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "16,000", "Giảm giá": "0", "Khách đã trả": "16,000", "Trạng thái": "Hoàn thành"}
```

#### Table `DanhSachHoaDonChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã hóa đơn, Mã hàng, Tên hàng, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, STT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0004", "Tên hàng": "Tiffy Dey hộp 25 vỉ x 4 viên", "Số lượng": "2", "Đơn giá": "4,400", "Giảm giá": "0", "Thành tiền": "8,800", "Số lượng quy đổi": "8"}
{"Mã hóa đơn": "ORD000002", "Mã hàng": "SP0029", "Tên hàng": "Alaxan hộp 25 vỉ x 4 viên", "Số lượng": "1", "Đơn giá": "5,200", "Giảm giá": "0", "Thành tiền": "5,200", "Số lượng quy đổi": "4"}
{"Mã hóa đơn": "ORD000003", "Mã hàng": "SP0005", "Tên hàng": "Nước muối sinh lý Natri clorid 0,9% Vĩnh", "Số lượng": "4", "Đơn giá": "10,000", "Giảm giá": "0", "Thành tiền": "40,000", "Số lượng quy đổi": "4"}
```

#### Table `DanhSachHoaDonChiTietLo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã hóa đơn, STT, Lô, Số lượng (ĐVT cơ bản), Số lượng trả (ĐVT cơ bản)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "STT": "1", "Lô": "X2501948", "Số lượng (ĐVT cơ bản)": "8", "Số lượng trả (ĐVT cơ bản)": "0"}
{"Mã hóa đơn": "ORD000002", "STT": "1", "Lô": "F2501832", "Số lượng (ĐVT cơ bản)": "4", "Số lượng trả (ĐVT cơ bản)": "0"}
{"Mã hóa đơn": "ORD000003", "STT": "1", "Lô": "X2501996", "Số lượng (ĐVT cơ bản)": "4", "Số lượng trả (ĐVT cơ bản)": "0"}
```

#### Table `DanhSachKhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Công ty, Tổng điểm, Mã khách hàng, Ghi chú KH, Ngày sinh, Tên khách hàng, Người tạo, Đối tượng KH, Điểm tích lũy, Điện thoại, MST, Địa chỉ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Công ty": null, "Tổng điểm": "0", "Mã khách hàng": "KH0001", "Ghi chú KH": null, "Ngày sinh": null, "Tên khách hàng": "Đào Hà Phúc", "Người tạo": "admin", "Đối tượng KH": "Cá nhân"}
{"Công ty": null, "Tổng điểm": "0", "Mã khách hàng": "KH0002", "Ghi chú KH": null, "Ngày sinh": null, "Tên khách hàng": "Dương Hạnh Đạt", "Người tạo": "admin", "Đối tượng KH": "Cá nhân"}
{"Công ty": null, "Tổng điểm": "0", "Mã khách hàng": "KH0003", "Ghi chú KH": null, "Ngày sinh": null, "Tên khách hàng": "Tăng Phúc Hoàng", "Người tạo": "admin", "Đối tượng KH": "Cá nhân"}
```

#### Table `DanhSachLoHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã nhập hàng, Mã hàng, Lô, Hạn sử dụng, Số lượng (ĐVT cơ bản)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00039", "Mã hàng": "SP0001", "Lô": "A2502949", "Hạn sử dụng": "29/07/2025", "Số lượng (ĐVT cơ bản)": "360"}
{"Mã nhập hàng": "PN00124", "Mã hàng": "SP0001", "Lô": "B2505889", "Hạn sử dụng": "08/02/2027", "Số lượng (ĐVT cơ bản)": "360"}
{"Mã nhập hàng": "PN00258", "Mã hàng": "SP0001", "Lô": "B2509833", "Hạn sử dụng": "09/07/2028", "Số lượng (ĐVT cơ bản)": "360"}
```

#### Table `DanhSachNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/01/2025", "Mã NCC": "NCC002", "Cần trả NCC": "94,231,600", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "02/01/2025", "Mã NCC": "NCC001", "Cần trả NCC": "687,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "05/01/2025", "Mã NCC": "NCC005", "Cần trả NCC": "811,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (20):** Trọng lượng, Mã hàng, Loại hàng hóa, Tên hàng, Tồn nhỏ nhất, Bảo hành, Ghi chú, Được bán trực tiếp, Mẫu ghi chú, Nhóm hàng(3 Cấp), Vị trí kệ, Mô tả chi tiết, Thuộc tính, Hình ảnh (url1,url2...), Giá bán...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Trọng lượng": null, "Mã hàng": "SP0001", "Loại hàng hóa": "Hàng hóa", "Tên hàng": "Panadol Extra hộp 15 vỉ x 12 viên", "Tồn nhỏ nhất": "0", "Bảo hành": null, "Ghi chú": null, "Được bán trực tiếp": "1"}
{"Trọng lượng": null, "Mã hàng": "SP0002", "Loại hàng hóa": "Hàng hóa", "Tên hàng": "Hapacol 250 hộp 24 gói", "Tồn nhỏ nhất": "0", "Bảo hành": null, "Ghi chú": null, "Được bán trực tiếp": "1"}
{"Trọng lượng": null, "Mã hàng": "SP0003", "Loại hàng hóa": "Hàng hóa", "Tên hàng": "Panadol 500mg hộp 10 vỉ x 12 viên", "Tồn nhỏ nhất": "0", "Bảo hành": null, "Ghi chú": null, "Được bán trực tiếp": "1"}
```

#### Table `DanhSachThuoc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã hàng, Hoạt chất, Thuốc kê đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Hoạt chất": "Paracetamol + Cafein", "Thuốc kê đơn": "False"}
{"Mã hàng": "SP0002", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
{"Mã hàng": "SP0003", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
```

---

## Business `biz_120`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_120  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…), nối với nhau qua mã. Ngày dạng dd/mm/yyyy.  File `DanhSachHoaDon.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DanhSachHoaDon.xlsx` (xlsx) - `DanhSachHoaDonChiTiet.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DanhSachKhachHang.xlsx` (xlsx) - `BaoCaoTonKho.xlsx` (xlsx) - `DanhSachNhapHang.xlsx` (xlsx)
- **Files on disk (11):** BaoCaoTonKho.xlsx, DanhSachChiTietNhapHang.xlsx, DanhSachHoaDon.xlsx, DanhSachHoaDonChiTiet.xlsx, DanhSachHoaDonChiTietLo.xlsx, DanhSachKhachHang.xlsx, DanhSachLoHang.xlsx, DanhSachNhapHang.xlsx, DanhSachSanPham.xlsx, DanhSachThuoc.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BaoCaoTonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "PANADOL EXTRA HỘP 15 VỈ X 12 VIÊN", "ĐVT": "viên", "Tồn cuối kỳ": "392"}
{"Mã hàng": "SP0002", "Tên hàng": "Hapacol 250 hộp 24 gói", "ĐVT": "gói", "Tồn cuối kỳ": "0"}
{"Mã hàng": "SP0003", "Tên hàng": "Panadol 500mg hộp 10 vỉ x 12 viên", "ĐVT": "viên", "Tồn cuối kỳ": "105"}
```

#### Table `DanhSachChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá, Lô, Hạn sử dụng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "hộp", "Số lượng": "2", "Đơn giá": "198,000", "Lô": "T2501293", "Hạn sử dụng": "2025-04-17 00:00:00"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "hộp", "Số lượng": "10", "Đơn giá": "38,400", "Lô": "E2501838", "Hạn sử dụng": "2025-03-17 00:00:00"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "hộp", "Số lượng": "2", "Đơn giá": "96,000", "Lô": "B2501356", "Hạn sử dụng": "2027-06-16 00:00:00"}
```

#### Table `DanhSachHoaDon.xlsx :: 01.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "01/01/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "12,900", "Giảm giá": "0", "Khách đã trả": "12,900", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "01/01/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "114,000", "Giảm giá": "0", "Khách đã trả": "114,000", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "01/01/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,600", "Giảm giá": "0", "Khách đã trả": "1,600", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 02.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD002585", "Thời gian": "01/02/2025", "Mã KH": "KH0008", "Khách hàng": "Thái Minh Giang", "Tổng tiền hàng": "122,500", "Giảm giá": "0", "Khách đã trả": "122,500", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD002586", "Thời gian": "01/02/2025", "Mã KH": "KH0131", "Khách hàng": "Đỗ Thanh An", "Tổng tiền hàng": "5,600", "Giảm giá": "0", "Khách đã trả": "5,600", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD002587", "Thời gian": "01/02/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "101,800", "Giảm giá": "0", "Khách đã trả": "101,800", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 03.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD005044", "Thời gian": "01/03/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "110,000", "Giảm giá": "0", "Khách đã trả": "110,000", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD005045", "Thời gian": "01/03/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "8,000", "Giảm giá": "0", "Khách đã trả": "8,000", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD005046", "Thời gian": "01/03/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "36,000", "Giảm giá": "0", "Khách đã trả": "36,000", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 04.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD007804", "Thời gian": "01/04/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "4,800", "Giảm giá": "0", "Khách đã trả": "0", "Trạng thái": "hủy đơn"}
{"Mã hóa đơn": "ORD007805", "Thời gian": "01/04/2025", "Mã KH": "KH0305", "Khách hàng": "Đoàn Phong Hương", "Tổng tiền hàng": "110,000", "Giảm giá": "0", "Khách đã trả": "110,000", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD007806", "Thời gian": "01/04/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,104,500", "Giảm giá": "10,000", "Khách đã trả": "1,094,500", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 05.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD010381", "Thời gian": "01/05/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "2,100", "Giảm giá": "0", "Khách đã trả": "2,100", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD010382", "Thời gian": "01/05/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "49,300", "Giảm giá": "0", "Khách đã trả": "49,300", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD010383", "Thời gian": "01/05/2025", "Mã KH": "KH0295", "Khách hàng": "Tống Bình Ngọc", "Tổng tiền hàng": "122,000", "Giảm giá": "0", "Khách đã trả": "122,000", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 06.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD013079", "Thời gian": "01/06/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "27,800", "Giảm giá": "0", "Khách đã trả": "42,800", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD013080", "Thời gian": "01/06/2025", "Mã KH": "KH0337", "Khách hàng": "La Sơn Lan", "Tổng tiền hàng": "2,600", "Giảm giá": "0", "Khách đã trả": "17,600", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD013081", "Thời gian": "01/06/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "65,000", "Giảm giá": "0", "Khách đã trả": "65,000", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 07.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD015732", "Thời gian": "01/07/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "3,900", "Giảm giá": "0", "Khách đã trả": "3,900", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD015733", "Thời gian": "01/07/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "240,500", "Giảm giá": "0", "Khách đã trả": "240,500", "Trạng thái": "ok"}
{"Mã hóa đơn": "ORD015734", "Thời gian": "01/07/2025", "Mã KH": "KH0307", "Khách hàng": "Mai Hiếu Thu", "Tổng tiền hàng": "43,500", "Giảm giá": "0", "Khách đã trả": "58,500", "Trạng thái": "ok"}
```

#### Table `DanhSachHoaDon.xlsx :: 08.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD018515", "Thời gian": "01/08/2025", "Mã KH": "KH0067", "Khách hàng": "Diệp Duy Hải", "Tổng tiền hàng": "16,000", "Giảm giá": "0", "Khách đã trả": "16,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD018516", "Thời gian": "01/08/2025", "Mã KH": "KH0110", "Khách hàng": "Thân Quân Hà", "Tổng tiền hàng": "76,800", "Giảm giá": "0", "Khách đã trả": "76,800", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD018517", "Thời gian": "01/08/2025", "Mã KH": "KH0018", "Khách hàng": "Kiều Hùng Lan", "Tổng tiền hàng": "3,300", "Giảm giá": "0", "Khách đã trả": "3,300", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 09.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD021224", "Thời gian": "01/09/2025", "Mã KH": "KH0042", "Khách hàng": "Trần Tâm Ngân", "Tổng tiền hàng": "152,000", "Giảm giá": "0", "Khách đã trả": "152,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD021225", "Thời gian": "01/09/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "5,800", "Giảm giá": "0", "Khách đã trả": "5,800", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD021226", "Thời gian": "01/09/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,200", "Giảm giá": "0", "Khách đã trả": "1,200", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 10.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD024021", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "3,000", "Giảm giá": "0", "Khách đã trả": "3,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD024022", "Thời gian": "01/10/2025", "Mã KH": "KH0078", "Khách hàng": "Giang Phong Trung", "Tổng tiền hàng": "4,500", "Giảm giá": "0", "Khách đã trả": "4,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD024023", "Thời gian": "01/10/2025", "Mã KH": "KH0277", "Khách hàng": "Đàm Hà Duy", "Tổng tiền hàng": "164,300", "Giảm giá": "0", "Khách đã trả": "164,300", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 11.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD026806", "Thời gian": "01/11/2025", "Mã KH": "KH0348", "Khách hàng": "Dương Ngọc Bình", "Tổng tiền hàng": "99,000", "Giảm giá": "0", "Khách đã trả": "99,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD026807", "Thời gian": "01/11/2025", "Mã KH": "KH0171", "Khách hàng": "Lương Thu Đức", "Tổng tiền hàng": "60,000", "Giảm giá": "0", "Khách đã trả": "60,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD026808", "Thời gian": "01/11/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "13,000", "Giảm giá": "0", "Khách đã trả": "13,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 12.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD029626", "Thời gian": "01/12/2025", "Mã KH": "KH0231", "Khách hàng": "Đào Nam Huy", "Tổng tiền hàng": "2,100", "Giảm giá": "0", "Khách đã trả": "2,100", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD029627", "Thời gian": "01/12/2025", "Mã KH": "KH0023", "Khách hàng": "Châu Hương Khoa", "Tổng tiền hàng": "10,500", "Giảm giá": "0", "Khách đã trả": "10,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD029628", "Thời gian": "01/12/2025", "Mã KH": "KH0291", "Khách hàng": "Đoàn Khoa Đạt", "Tổng tiền hàng": "18,000", "Giảm giá": "0", "Khách đã trả": "18,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 01.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD032510", "Thời gian": "01/01/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "87,000", "Giảm giá": "0", "Khách đã trả": "87,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD032511", "Thời gian": "01/01/2026", "Mã KH": "KH0016", "Khách hàng": "Ông Bình Nam", "Tổng tiền hàng": "16,000", "Giảm giá": "0", "Khách đã trả": "16,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD032512", "Thời gian": "01/01/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "151,700", "Giảm giá": "0", "Khách đã trả": "151,700", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 02.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD035513", "Thời gian": "01/02/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "16,800", "Giảm giá": "0", "Khách đã trả": "16,800", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD035514", "Thời gian": "01/02/2026", "Mã KH": "KH0225", "Khách hàng": "Phan Hà Lan", "Tổng tiền hàng": "11,000", "Giảm giá": "0", "Khách đã trả": "11,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD035515", "Thời gian": "01/02/2026", "Mã KH": "KH0230", "Khách hàng": "Đinh Ngọc Minh", "Tổng tiền hàng": "122,800", "Giảm giá": "0", "Khách đã trả": "0", "Trạng thái": "Huỷ đơn"}
```

#### Table `DanhSachHoaDon.xlsx :: 03.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD038330", "Thời gian": "01/03/2026", "Mã KH": "KH0115", "Khách hàng": "Tô Hoa Ngân", "Tổng tiền hàng": "28,000", "Giảm giá": "0", "Khách đã trả": "28,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD038331", "Thời gian": "01/03/2026", "Mã KH": "KH0240", "Khách hàng": "Hoàng Linh Bảo", "Tổng tiền hàng": "178,000", "Giảm giá": "0", "Khách đã trả": "178,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD038332", "Thời gian": "01/03/2026", "Mã KH": "KH0074", "Khách hàng": "Lâm Phong Phúc", "Tổng tiền hàng": "8,900", "Giảm giá": "0", "Khách đã trả": "8,900", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 04.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD041331", "Thời gian": "01/04/2026", "Mã KH": "KH0209", "Khách hàng": "Hà Hải Dương", "Tổng tiền hàng": "17,500", "Giảm giá": "0", "Khách đã trả": "17,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD041332", "Thời gian": "01/04/2026", "Mã KH": "KH0328", "Khách hàng": "Đào Hiếu Duy", "Tổng tiền hàng": "5,400", "Giảm giá": "0", "Khách đã trả": "5,400", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD041333", "Thời gian": "01/04/2026", "Mã KH": "KH0303", "Khách hàng": "Đinh Long Thanh", "Tổng tiền hàng": "4,100", "Giảm giá": "0", "Khách đã trả": "4,100", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 05.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD044240", "Thời gian": "01/05/2026", "Mã KH": "KH0043", "Khách hàng": "Trần Long Dương", "Tổng tiền hàng": "4,200", "Giảm giá": "0", "Khách đã trả": "4,200", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD044241", "Thời gian": "01/05/2026", "Mã KH": "KH0202", "Khách hàng": "Doãn Long Quang", "Tổng tiền hàng": "11,200", "Giảm giá": "0", "Khách đã trả": "11,200", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD044242", "Thời gian": "01/05/2026", "Mã KH": "KH0200", "Khách hàng": "Ngô Bình Hà", "Tổng tiền hàng": "8,300", "Giảm giá": "0", "Khách đã trả": "8,300", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 06.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Còn nợ, Kênh bán, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD047294", "Thời gian": "01/06/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "94,500", "Giảm giá": "0", "Khách đã trả": "94,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD047295", "Thời gian": "01/06/2026", "Mã KH": "KH0248", "Khách hàng": "Doãn Quân Huy", "Tổng tiền hàng": "1,400", "Giảm giá": "0", "Khách đã trả": "1,400", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD047296", "Thời gian": "01/06/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "522,000", "Giảm giá": "10,000", "Khách đã trả": "512,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDonChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Mã hóa đơn, Mã hàng, Tên hàng, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0070", "Tên hàng": "Bisolvon 8mg hộp 3 vỉ x 10 viên", "Số lượng": "1", "Đơn giá": "2,100", "Giảm giá": "0", "Thành tiền": "2,100", "Số lượng quy đổi": "1"}
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0039", "Tên hàng": "Efticol 0,9% lốc 10 lọ x 10ml", "Số lượng": "4", "Đơn giá": "2,700", "Giảm giá": "0", "Thành tiền": "10,800", "Số lượng quy đổi": "4"}
{"Mã hóa đơn": "ORD000002", "Mã hàng": "SP0066", "Tên hàng": "Boganic Traphaco hộp 5 vỉ x 20 viên", "Số lượng": "1", "Đơn giá": "800", "Giảm giá": "0", "Thành tiền": "800", "Số lượng quy đổi": "1"}
```

#### Table `DanhSachHoaDonChiTietLo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã hóa đơn, STT, Lô, Số lượng (ĐVT cơ bản), Số lượng trả (ĐVT cơ bản)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "STT": "1", "Lô": "O2501749", "Số lượng (ĐVT cơ bản)": "1", "Số lượng trả (ĐVT cơ bản)": "0"}
{"Mã hóa đơn": "ORD000001", "STT": "2", "Lô": "M2501980", "Số lượng (ĐVT cơ bản)": "4", "Số lượng trả (ĐVT cơ bản)": "0"}
{"Mã hóa đơn": "ORD000002", "STT": "1", "Lô": "T2501295", "Số lượng (ĐVT cơ bản)": "1", "Số lượng trả (ĐVT cơ bản)": "0"}
```

#### Table `DanhSachKhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Mã khách hàng, Ghi chú, Mã số thuế, Tên khách hàng, Người tạo, CCCD, Ngày sinh, E-mail, Đối tượng KH, Tên công ty, Điện thoại, Địa chỉ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã khách hàng": "KH0001", "Ghi chú": null, "Mã số thuế": null, "Tên khách hàng": "Tăng Bình Huy", "Người tạo": "admin", "CCCD": null, "Ngày sinh": null, "E-mail": null}
{"Mã khách hàng": "KH0002", "Ghi chú": null, "Mã số thuế": null, "Tên khách hàng": "Ngô Hùng Nhung", "Người tạo": "admin", "CCCD": null, "Ngày sinh": "15/02/2000", "E-mail": null}
{"Mã khách hàng": "KH0003", "Ghi chú": null, "Mã số thuế": null, "Tên khách hàng": "Tăng Minh Anh", "Người tạo": "admin", "CCCD": null, "Ngày sinh": null, "E-mail": null}
```

#### Table `DanhSachLoHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã nhập hàng, Mã hàng, Lô, Hạn sử dụng, Số lượng (ĐVT cơ bản)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00121", "Mã hàng": "SP0001", "Lô": "A2505314", "Hạn sử dụng": "14/05/2026", "Số lượng (ĐVT cơ bản)": "360"}
{"Mã nhập hàng": "PN00134", "Mã hàng": "SP0001", "Lô": "A2505854", "Hạn sử dụng": "31/07/2025", "Số lượng (ĐVT cơ bản)": "360"}
{"Mã nhập hàng": "PN00381", "Mã hàng": "SP0001", "Lô": "A2601477", "Hạn sử dụng": "25/03/2026", "Số lượng (ĐVT cơ bản)": "360"}
```

#### Table `DanhSachNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/01/2025", "Mã NCC": "NCC002", "Cần trả NCC": "211,648,300", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "02/01/2025", "Mã NCC": "NCC004", "Cần trả NCC": "180,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "03/01/2025", "Mã NCC": "NCC001", "Cần trả NCC": "200,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Trọng lượng, Mã hàng, Định mức tồn tối thiểu, Tên hàng, Mô tả chi tiết, Nhóm hàng(3 Cấp), Mẫu ghi chú, Định mức tồn tối đa, Được bán trực tiếp, Bảo hành, Mã HH Liên quan, Giá bán, Loại hàng hóa, ĐVT, Giá vốn...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Trọng lượng": null, "Mã hàng": "SP0001", "Định mức tồn tối thiểu": "0", "Tên hàng": "Panadol Extra hộp 15 vỉ x 12 viên", "Mô tả chi tiết": null, "Nhóm hàng(3 Cấp)": "giảm đau hạ sốt", "Mẫu ghi chú": null, "Định mức tồn tối đa": "999999999"}
{"Trọng lượng": null, "Mã hàng": "SP0002", "Định mức tồn tối thiểu": "0", "Tên hàng": "Hapacol 250 hộp 24 gói", "Mô tả chi tiết": null, "Nhóm hàng(3 Cấp)": "giảm đau hạ sốt", "Mẫu ghi chú": null, "Định mức tồn tối đa": "999999999"}
{"Trọng lượng": null, "Mã hàng": "SP0003", "Định mức tồn tối thiểu": "0", "Tên hàng": "Panadol 500mg hộp 10 vỉ x 12 viên", "Mô tả chi tiết": null, "Nhóm hàng(3 Cấp)": "giảm đau hạ sốt", "Mẫu ghi chú": null, "Định mức tồn tối đa": "999999999"}
```

#### Table `DanhSachThuoc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã hàng, Hoạt chất, Thuốc kê đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Hoạt chất": "Paracetamol + Cafein", "Thuốc kê đơn": "False"}
{"Mã hàng": "SP0002", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
{"Mã hàng": "SP0003", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
```

---

## Business `biz_121`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_121  File Excel xuất từ phần mềm bán hàng. File đơn hàng mỗi dòng một sản phẩm.  Các danh sách `DanhSachQuyDoi`, `DanhSachSanPham`, `DonNhapHang`, `DonNhapHang_ChiTiet`, `DonHang_Lo`, `DanhSachThuoc` nằm chung file `DuLieuXuat.xlsx`, mỗi danh sách một sheet.  ## File - `DonHang_ChiTiet.xlsx` (xlsx) - `DuLieuXuat.xlsx` (xlsx)  ## Cột trong `DonHang_ChiTiet.xlsx` - **Mã đơn hàng**: mã đơn - **Ngày đặt hàng**: ngày bán - **Trạng thái đơn hàng**: trạng thái đơn - **Tên khách hàng**: tê
- **Files on disk (3):** DonHang_ChiTiet.xlsx, DuLieuXuat.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DonHang_ChiTiet.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lâm Ngọc Ngọc", "Tên sản phẩm": "Amoxicillin 500mg Domesco hộp 10 vỉ x 10", "Số lượng sản phẩm": "1", "Giá sản phẩm": "100,000", "Tổng tiền": "100000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lê Phương Hoàng", "Tên sản phẩm": "Hapacol 150 hộp 24 gói", "Số lượng sản phẩm": "2", "Giá sản phẩm": "1,600", "Tổng tiền": "3200"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Hagifen 400mg DHG hộp 10 vỉ x 10 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "6000", "Tổng tiền": "6,000"}
```

#### Table `DuLieuXuat.xlsx :: DanhSachQuyDoi`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên sản phẩm, Đơn vị quy đổi, Tỉ lệ quy đổi, Đơn vị cơ bản
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Đơn vị quy đổi": "vỉ", "Tỉ lệ quy đổi": "12", "Đơn vị cơ bản": "viên"}
{"Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "180", "Đơn vị cơ bản": "viên"}
{"Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "24", "Đơn vị cơ bản": "gói"}
```

#### Table `DuLieuXuat.xlsx :: DanhSachSanPham`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Vị trí, Ghi chú, Mã SKU, Bảo hành, Thương hiệu, Mẫu ghi chú, Tên sản phẩm, Trọng lượng, Mã barcode, Đơn vị, Mã HH Liên quan, Tồn lớn nhất, Hình ảnh (url1,url2...), Thuộc tính, Mô tả chi tiết...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Vị trí": null, "Ghi chú": null, "Mã SKU": "SP0001", "Bảo hành": null, "Thương hiệu": null, "Mẫu ghi chú": null, "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Trọng lượng": null}
{"Vị trí": null, "Ghi chú": null, "Mã SKU": "SP0002", "Bảo hành": null, "Thương hiệu": null, "Mẫu ghi chú": null, "Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Trọng lượng": null}
{"Vị trí": null, "Ghi chú": null, "Mã SKU": "SP0003", "Bảo hành": null, "Thương hiệu": null, "Mẫu ghi chú": null, "Tên sản phẩm": "Panadol 500mg hộp 10 vỉ x 12 viên", "Trọng lượng": null}
```

#### Table `DuLieuXuat.xlsx :: DonNhapHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn nhập, Ngày nhập, Mã nhà cung cấp
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn nhập": "PN00001", "Ngày nhập": "01/03/2025", "Mã nhà cung cấp": "NCC001"}
{"Mã đơn nhập": "PN00002", "Ngày nhập": "03/03/2025", "Mã nhà cung cấp": "NCC004"}
{"Mã đơn nhập": "PN00003", "Ngày nhập": "04/03/2025", "Mã nhà cung cấp": "NCC002"}
```

#### Table `DuLieuXuat.xlsx :: DonNhapHang_ChiTiet`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã đơn nhập, Mã SKU, Mã lô, Hạn sử dụng, Số lượng nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn nhập": "PN00204", "Mã SKU": "SP0001", "Mã lô": "A2509923", "Hạn sử dụng": "08/03/2027", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00331", "Mã SKU": "SP0001", "Mã lô": "A2601643", "Hạn sử dụng": "01/07/2028", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00353", "Mã SKU": "SP0001", "Mã lô": "A2602894", "Hạn sử dụng": "03/01/2028", "Số lượng nhập": "360"}
```

#### Table `DuLieuXuat.xlsx :: DonHang_Lo`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã đơn hàng, Mã lô, Số lượng, Số lượng trả
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Mã lô": "Y2503213", "Số lượng": "100", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000002", "Mã lô": "R2503152", "Số lượng": "2", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000002", "Mã lô": "Q2503369", "Số lượng": "10", "Số lượng trả": "0"}
```

#### Table `DuLieuXuat.xlsx :: DanhSachThuoc`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã SKU, Hoạt chất, Thuốc kê đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã SKU": "SP0001", "Hoạt chất": "Paracetamol + Cafein", "Thuốc kê đơn": "False"}
{"Mã SKU": "SP0002", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
{"Mã SKU": "SP0003", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
```

---

## Business `biz_122`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_122  File Excel xuất từ phần mềm bán hàng. File đơn hàng mỗi dòng một sản phẩm.  File `DonHang_ChiTiet_1.xlsx`, `DonHang_ChiTiet_2026.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DonHang_ChiTiet_1.xlsx` (xlsx) - `DonHang_ChiTiet_2026.xlsx` (xlsx) - `DanhSachQuyDoi.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DonNhapHang.xlsx` (xlsx) - `DonNhapHang_ChiTiet.xlsx` (xlsx) - `DonHang_Lo_1.xlsx` (xlsx) - `DonHang_Lo_2.xlsx` (xlsx) - `DanhSachThuoc.xlsx` (xls
- **Files on disk (10):** DanhSachQuyDoi.xlsx, DanhSachSanPham.xlsx, DanhSachThuoc.xlsx, DonHang_ChiTiet_1.xlsx, DonHang_ChiTiet_2026.xlsx, DonHang_Lo_1.xlsx, DonHang_Lo_2.xlsx, DonNhapHang.xlsx, DonNhapHang_ChiTiet.xlsx, README.md

### Tables / Sheets Detail:
#### Table `DanhSachQuyDoi.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Tên sản phẩm, Đơn vị quy đổi, Tỉ lệ quy đổi, Đơn vị cơ bản
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Đơn vị quy đổi": "vỉ", "Tỉ lệ quy đổi": "12", "Đơn vị cơ bản": "viên"}
{"Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "180", "Đơn vị cơ bản": "viên"}
{"Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "24", "Đơn vị cơ bản": "gói"}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Ghi chú, Mô tả sản phẩm, Tồn lớn nhất, Vị trí, Mã SKU, Mã HH Liên quan, Thương hiệu, Thuộc tính, Tên sản phẩm, Hình ảnh, Trọng lượng, Mã vạch EAN, Bảo hành, Đơn vị, Định mức tồn tối thiểu...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ghi chú": null, "Mô tả sản phẩm": null, "Tồn lớn nhất": "999999999", "Vị trí": null, "Mã SKU": "SP0001", "Mã HH Liên quan": null, "Thương hiệu": null, "Thuộc tính": null}
{"Ghi chú": null, "Mô tả sản phẩm": null, "Tồn lớn nhất": "999999999", "Vị trí": null, "Mã SKU": "SP0002", "Mã HH Liên quan": null, "Thương hiệu": null, "Thuộc tính": null}
{"Ghi chú": null, "Mô tả sản phẩm": null, "Tồn lớn nhất": "999999999", "Vị trí": null, "Mã SKU": "SP0003", "Mã HH Liên quan": null, "Thương hiệu": null, "Thuộc tính": null}
```

#### Table `DanhSachThuoc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã SKU, Hoạt chất, Thuốc kê đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã SKU": "SP0001", "Hoạt chất": "Paracetamol + Cafein", "Thuốc kê đơn": "False"}
{"Mã SKU": "SP0002", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
{"Mã SKU": "SP0003", "Hoạt chất": "Paracetamol", "Thuốc kê đơn": "False"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T01-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tăng Hiếu Hương", "Tên sản phẩm": "Lorastad 10mg Stella hộp 10 vỉ x 10 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "800", "Tổng tiền": "1.600đ"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Enterogermina 2 tỷ/5ml hộp 20 ống", "Số lượng sản phẩm": "1", "Giá sản phẩm": "9,200", "Tổng tiền": "9200"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Tiffy Dey hộp 25 vỉ x 4 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "1100", "Tổng tiền": "2.200đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T02-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD002909", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hoàng Giang Quân", "Tên sản phẩm": "Gaviscon hộp 24 gói x 10ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "8000", "Tổng tiền": "16000"}
{"Mã đơn hàng": "ORD002910", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đàm Loan Trang", "Tên sản phẩm": "Zyrtec 10mg hộp 1 vỉ x 10 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "75000", "Tổng tiền": "150000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Enterogermina 2 tỷ/5ml hộp 20 ống", "Số lượng sản phẩm": "1", "Giá sản phẩm": "184000", "Tổng tiền": "184k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T03-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD005502", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "10", "Giá sản phẩm": "5,300", "Tổng tiền": "53000"}
{"Mã đơn hàng": "ORD005503", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đinh Hằng Minh", "Tên sản phẩm": "Dầu gió xanh Con Ó chai 12ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "49,000", "Tổng tiền": "98k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Nước muối sinh lý Natri clorid 0,9% Vĩnh", "Số lượng sản phẩm": "2", "Giá sản phẩm": "10000", "Tổng tiền": "20k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T04-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD008310", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Savi Losartan 50mg hộp 3 vỉ x 10 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "14,000", "Tổng tiền": "28k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Viên ngậm Eugica gói 15 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "15,000", "Tổng tiền": "30000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Enterogermina 2 tỷ/5ml hộp 20 ống", "Số lượng sản phẩm": "1", "Giá sản phẩm": "9,700", "Tổng tiền": "9.700đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T05-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD011018", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lê Minh Duy", "Tên sản phẩm": "Que thử thai Quickstick hộp 1 cái", "Số lượng sản phẩm": "1", "Giá sản phẩm": "25,000", "Tổng tiền": "25k"}
{"Mã đơn hàng": "ORD011019", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Povidine 10% chai 90ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "18000", "Tổng tiền": "18k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Cao Sao Vàng TW3 hộp 3g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "5000", "Tổng tiền": "5000"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T06-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD013979", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Povidine 10% chai 90ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "18,000", "Tổng tiền": "36000"}
{"Mã đơn hàng": "ORD013980", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hồ Nam Hiếu", "Tên sản phẩm": "Lorastad 10mg Stella Hộp 10 Vỉ X 10 Viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "800", "Tổng tiền": "800"}
{"Mã đơn hàng": "ORD013981", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Otrivin 0,1% xịt mũi chai 10ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "61000", "Tổng tiền": "122000"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T07-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD016861", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hồ Hồng Hùng", "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Số lượng sản phẩm": "3", "Giá sản phẩm": "1400", "Tổng tiền": "4200"}
{"Mã đơn hàng": "ORD016862", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hà Dũng Tâm", "Tên sản phẩm": "Vitamin C 500mg Quapharco hộp 10 vỉ x 10", "Số lượng sản phẩm": "1", "Giá sản phẩm": "500", "Tổng tiền": "500đ"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Biosubtyl-II hộp 25 gói", "Số lượng sản phẩm": "3", "Giá sản phẩm": "2100", "Tổng tiền": "6.300đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T08-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD019762", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Gaviscon hộp 24 gói x 10ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "192000", "Tổng tiền": "192k"}
{"Mã đơn hàng": "ORD019763", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Enervon hộp 10 vỉ x 10 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "23,000", "Tổng tiền": "23k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Clarityne 10mg hộp 1 vỉ x 10 viên", "Số lượng sản phẩm": "4", "Giá sản phẩm": "6700", "Tổng tiền": "26.800đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T09-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD022683", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Siro ăn ngon Ích Nhi Plus chai 100ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "65,000", "Tổng tiền": "65000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "2", "Giá sản phẩm": "5300", "Tổng tiền": "10.600đ"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Hagifen 400mg DHG hộp 10 vỉ x 10 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "600", "Tổng tiền": "1.200đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T10-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD025664", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đặng Đức Chi", "Tên sản phẩm": "Bio-acimin Gold men vi sinh hộp 30 gói", "Số lượng sản phẩm": "2", "Giá sản phẩm": "5,300", "Tổng tiền": "10600"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Cao Sao Vàng TW3 hộp 3g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "5000", "Tổng tiền": "5k"}
{"Mã đơn hàng": "ORD025665", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tăng Thanh Ngân", "Tên sản phẩm": "Alaxan hộp 25 vỉ x 4 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "1300", "Tổng tiền": "1300"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T11-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD028649", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lâm Bảo Thắng", "Tên sản phẩm": "Betadine Gargle súc họng chai 125ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "75,000", "Tổng tiền": "75k"}
{"Mã đơn hàng": "ORD028650", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Otrivin 0,1% xịt mũi chai 10ml", "Số lượng sản phẩm": "4", "Giá sản phẩm": "61,000", "Tổng tiền": "244k"}
{"Mã đơn hàng": "ORD028651", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Clorpheniramin 4mg DHG hộp 10 vỉ x 20 vi", "Số lượng sản phẩm": "1", "Giá sản phẩm": "2000", "Tổng tiền": "2k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T12-2025`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD031652", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hà Trang Minh", "Tên sản phẩm": "Pharmaton Essential hộp 30 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "210000", "Tổng tiền": "210k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Decolgen Forte hộp 30 vỉ x 4 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "1,300", "Tổng tiền": "1300"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Cetirizin 10mg Domesco hộp 10 vỉ x 10 vi", "Số lượng sản phẩm": "2", "Giá sản phẩm": "6,000", "Tổng tiền": "12k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T01-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD034693", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tô Duy Mai", "Tên sản phẩm": "Cao Sao Vàng TW3 hộp 3g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "5,000", "Tổng tiền": "5k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Magne-B6 Corbière hộp 5 vỉ x 10 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "2,200", "Tổng tiền": "2200"}
{"Mã đơn hàng": "ORD034694", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lương Hà Bảo", "Tên sản phẩm": "Enterogermina 2 tỷ/5ml hộp 20 ống", "Số lượng sản phẩm": "10", "Giá sản phẩm": "9700", "Tổng tiền": "97k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T02-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD037777", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Diệp Minh Linh", "Tên sản phẩm": "Decolgen Forte hộp 30 vỉ x 4 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "1,300", "Tổng tiền": "1300"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Siro ho Bổ phế Nam Hà Chỉ Khái Lộ chai 1", "Số lượng sản phẩm": "2", "Giá sản phẩm": "58000", "Tổng tiền": "116000"}
{"Mã đơn hàng": "ORD037778", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Povidine 10% chai 90ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "18,000", "Tổng tiền": "18k"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T03-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD040699", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Fugacar 500mg hộp 1 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "22000", "Tổng tiền": "22000"}
{"Mã đơn hàng": "ORD040700", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Trương Hải Thu", "Tên sản phẩm": "Phosphalugel hộp 26 gói", "Số lượng sản phẩm": "3", "Giá sản phẩm": "4,700", "Tổng tiền": "14.100đ"}
{"Mã đơn hàng": "ORD040701", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đỗ Trang Hằng", "Tên sản phẩm": "Biosubtyl-II hộp 25 gói", "Số lượng sản phẩm": "6", "Giá sản phẩm": "2,100", "Tổng tiền": "12.600đ"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T04-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD043847", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đặng Minh Thắng", "Tên sản phẩm": "Cetirizin 10mg Domesco hộp 10 vỉ x 10 vi", "Số lượng sản phẩm": "1", "Giá sản phẩm": "6,000", "Tổng tiền": "6000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Berocca Performance viên sủi tuýp 10 viê", "Số lượng sản phẩm": "10", "Giá sản phẩm": "8,300", "Tổng tiền": "83k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Voltaren Emulgel 1% tuýp 20g", "Số lượng sản phẩm": "1", "Giá sản phẩm": "69,000", "Tổng tiền": "69000"}
```

#### Table `DonHang_ChiTiet_1.xlsx :: T05-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD046958", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Prednisolon 5mg Boston chai 500 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "500", "Tổng tiền": "500đ"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Siro ăn ngon Ích Nhi Plus chai 100ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "65000", "Tổng tiền": "130000"}
{"Mã đơn hàng": "ORD046959", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Telfast HD 180mg hộp 3 vỉ x 10 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "9,800", "Tổng tiền": "9.800đ"}
```

#### Table `DonHang_ChiTiet_2026.xlsx :: T06-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD050167", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Amoxicillin 500mg Domesco hộp 10 vỉ x 10", "Số lượng sản phẩm": "10", "Giá sản phẩm": "1000", "Tổng tiền": "10k"}
{"Mã đơn hàng": "ORD050168", "Ngày đặt hàng": "01/06/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Efticol 0,9% lốc 10 lọ x 10ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "28000", "Tổng tiền": "28k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Fugacar 500mg hộp 1 viên", "Số lượng sản phẩm": "2", "Giá sản phẩm": "22000", "Tổng tiền": "44k"}
```

#### Table `DonHang_ChiTiet_2026.xlsx :: T07-2026`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD053267", "Ngày đặt hàng": "01/07/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Bạch Thắng Huy", "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "106000", "Tổng tiền": "106k"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "50,400", "Tổng tiền": "50.400đ"}
{"Mã đơn hàng": "ORD053268", "Ngày đặt hàng": "01/07/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Châu Phong Quân", "Tên sản phẩm": "Tiffy Dey hộp 25 vỉ x 4 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "120000", "Tổng tiền": "120000"}
```

#### Table `DonHang_Lo_1.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã đơn hàng, Mã lô, Số lượng, Số lượng trả
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Mã lô": "J2501674", "Số lượng": "2", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000001", "Mã lô": "X2501549", "Số lượng": "1", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000002", "Mã lô": "W2501411", "Số lượng": "2", "Số lượng trả": "0"}
```

#### Table `DonHang_Lo_2.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã đơn hàng, Mã lô, Số lượng, Số lượng trả
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD052057", "Mã lô": "C2605930", "Số lượng": "2", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD052058", "Mã lô": "A2606201", "Số lượng": "1", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD052059", "Mã lô": "Y2606355", "Số lượng": "1", "Số lượng trả": "0"}
```

#### Table `DonNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn nhập, Ngày nhập, Mã nhà cung cấp
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn nhập": "PN00001", "Ngày nhập": "01/01/2025", "Mã nhà cung cấp": "NCC001"}
{"Mã đơn nhập": "PN00002", "Ngày nhập": "04/01/2025", "Mã nhà cung cấp": "NCC002"}
{"Mã đơn nhập": "PN00003", "Ngày nhập": "05/01/2025", "Mã nhà cung cấp": "NCC001"}
```

#### Table `DonNhapHang_ChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã đơn nhập, Mã SKU, Mã lô, Hạn sử dụng, Số lượng nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn nhập": "PN00101", "Mã SKU": "SP0001", "Mã lô": "B2504124", "Hạn sử dụng": "18/07/2026", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00441", "Mã SKU": "SP0001", "Mã lô": "B2603530", "Hạn sử dụng": "20/10/2027", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00066", "Mã SKU": "SP0001", "Mã lô": "C2503471", "Hạn sử dụng": "01/08/2025", "Số lượng nhập": "360"}
```

---

## Business `biz_123`
- **Structure Archetype:** SQLite Database (17 tables in pos.sqlite)
- **README (truncated 500 chars):** # Dữ liệu biz_123  File máy POS xuất ra.  ## File - `pos.sqlite` (sqlite)  ## Bảng `chi_nhanh`, `nhan_vien`, `khach_hang`, `nha_cung_cap`, `san_pham`, `don_vi_sp`, `phieu_nhap`, `chi_tiet_nhap`, `don_hang`, `chi_tiet_don`, `thanh_toan`, `tra_hang`, `the_kho`, `lich_su_gia`, `lo_hang`, `chi_tiet_don_lo`, `thong_tin_thuoc`  Mã đơn nối `don_hang` với `chi_tiet_don`. Ngày giờ dạng text.  ## Quy ước - Dữ liệu có đến hết 28/06/2026. - **Dòng hàng**: `chi_tiet_don.TriGia` là thành tiền của dòng (đã trừ
- **Files on disk (2):** README.md, pos.sqlite

### Tables / Sheets Detail:
#### Table `pos.sqlite :: chi_nhanh`
- **Rows:** 1 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** IDCuaHang, MaChiNhanh, TenGoi, DiaChiLienHe, NgayKhaiTruong
  - *Date cols:* ['NgayKhaiTruong']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaChiNhanh": "CN1", "TenGoi": "Nhà thuốc Lan", "DiaChiLienHe": "126 Lê Đức Thọ", "NgayKhaiTruong": "2021-08-15"}
```

#### Table `pos.sqlite :: nhan_vien`
- **Rows:** 3 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaNhanVien, TenGoi, MaChiNhanh, ChucVu, NgayNhanViec, NgayThoiViec
  - *Date cols:* ['NgayNhanViec', 'NgayThoiViec']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaNhanVien": "NV001", "TenGoi": "La Thu Quân", "MaChiNhanh": "CN1", "ChucVu": "owner", "NgayNhanViec": "2024-01-31", "NgayThoiViec": null}
{"IDCuaHang": "biz_123", "MaNhanVien": "NV002", "TenGoi": "Phùng Thu Trang", "MaChiNhanh": "CN1", "ChucVu": "cashier", "NgayNhanViec": "2024-03-24", "NgayThoiViec": null}
{"IDCuaHang": "biz_123", "MaNhanVien": "NV003", "TenGoi": "Bùi Dũng Lan", "MaChiNhanh": "CN1", "ChucVu": "sales", "NgayNhanViec": "2022-08-28", "NgayThoiViec": null}
```

#### Table `pos.sqlite :: khach_hang`
- **Rows:** 300 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** trang_thai_kh, cccd, IDCuaHang, diem_hien_tai, MaKhachHang, ghi_chu_kh, ngay_sinh, email, TenGoi, SoDienThoai, NamNu, nguoi_tao, LoaiKhachHang, cong_ty, tong_diem...
  - *Date cols:* ['ngay_sinh']
  - *Amount/Qty cols:* None
  - *Status cols:* ['trang_thai_kh']
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"trang_thai_kh": "Đang hoạt động", "cccd": null, "IDCuaHang": "biz_123", "diem_hien_tai": "0", "MaKhachHang": "KH0001", "ghi_chu_kh": null, "ngay_sinh": null, "email": null}
{"trang_thai_kh": "Đang hoạt động", "cccd": null, "IDCuaHang": "biz_123", "diem_hien_tai": "0", "MaKhachHang": "KH0002", "ghi_chu_kh": null, "ngay_sinh": "27/06/1972", "email": null}
{"trang_thai_kh": "Đang hoạt động", "cccd": null, "IDCuaHang": "biz_123", "diem_hien_tai": "0", "MaKhachHang": "KH0003", "ghi_chu_kh": null, "ngay_sinh": "12/02/1991", "email": null}
```

#### Table `pos.sqlite :: nha_cung_cap`
- **Rows:** 5 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** IDCuaHang, MaNhaCungCap, TenGoi, SoDienThoai, DiaChiLienHe
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaNhaCungCap": "NCC001", "TenGoi": "Cty Trịnh Thắng", "SoDienThoai": "0351807815", "DiaChiLienHe": "608 Mai Chí Thọ"}
{"IDCuaHang": "biz_123", "MaNhaCungCap": "NCC002", "TenGoi": "Cty Tăng Giang", "SoDienThoai": "0939278825", "DiaChiLienHe": "997 Tỉnh Lộ 10"}
{"IDCuaHang": "biz_123", "MaNhaCungCap": "NCC003", "TenGoi": "Cty Chung Khoa", "SoDienThoai": "0938341869", "DiaChiLienHe": "71 Tên Lửa"}
```

#### Table `pos.sqlite :: san_pham`
- **Rows:** 80 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (22):** hinh_anh, ma_vach_ean, bao_hanh, ban_truc_tiep, IDCuaHang, MaHangHoa, ghi_chu_hh, vi_tri, TenGoi, DanhMuc, loai_hang_hoa, ton_nho_nhat, thuong_hieu, DonViCoSo, GiaBanLe...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"hinh_anh": null, "ma_vach_ean": "8937439774399", "bao_hanh": null, "ban_truc_tiep": "1", "IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "ghi_chu_hh": null, "vi_tri": null}
{"hinh_anh": null, "ma_vach_ean": null, "bao_hanh": null, "ban_truc_tiep": "1", "IDCuaHang": "biz_123", "MaHangHoa": "SP0002", "ghi_chu_hh": null, "vi_tri": null}
{"hinh_anh": null, "ma_vach_ean": "8930259999492", "bao_hanh": null, "ban_truc_tiep": "1", "IDCuaHang": "biz_123", "MaHangHoa": "SP0003", "ghi_chu_hh": null, "vi_tri": null}
```

#### Table `pos.sqlite :: don_vi_sp`
- **Rows:** 83 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** IDCuaHang, MaHangHoa, DonViTinh, HeSoQuyDoi, GiaDonVi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "DonViTinh": "hộp", "HeSoQuyDoi": "180", "GiaDonVi": "252000"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "DonViTinh": "vỉ", "HeSoQuyDoi": "12", "GiaDonVi": "16800"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0002", "DonViTinh": "hộp", "HeSoQuyDoi": "24", "GiaDonVi": "48000"}
```

#### Table `pos.sqlite :: phieu_nhap`
- **Rows:** 540 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** IDCuaHang, MaPhieuNhap, MaNhaCungCap, MaChiNhanh, NgayNhapKho, TinhTrang, TongGiaTriNhap, DienGiai
  - *Date cols:* ['NgayNhapKho']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00001", "MaNhaCungCap": "NCC003", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-01-01", "TinhTrang": "received", "TongGiaTriNhap": "171276600", "DienGiai": "nhập đầu kỳ"}
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00002", "MaNhaCungCap": "NCC001", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-01-02", "TinhTrang": "received", "TongGiaTriNhap": "200000", "DienGiai": null}
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00003", "MaNhaCungCap": "NCC003", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-01-03", "TinhTrang": "received", "TongGiaTriNhap": "120000", "DienGiai": null}
```

#### Table `pos.sqlite :: chi_tiet_nhap`
- **Rows:** 2,953 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** IDCuaHang, MaPhieuNhap, SoThuTu, MaHangHoa, DonViTinh, SL, DonGiaNhap, MaLo, HanSuDung
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00001", "SoThuTu": "1", "MaHangHoa": "SP0001", "DonViTinh": "hộp", "SL": "2", "DonGiaNhap": "198000", "MaLo": "U2501782"}
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00001", "SoThuTu": "2", "MaHangHoa": "SP0002", "DonViTinh": "hộp", "SL": "9", "DonGiaNhap": "36000", "MaLo": "I2501228"}
{"IDCuaHang": "biz_123", "MaPhieuNhap": "PN00001", "SoThuTu": "3", "MaHangHoa": "SP0003", "DonViTinh": "hộp", "SL": "2", "DonGiaNhap": "96000", "MaLo": "O2501135"}
```

#### Table `pos.sqlite :: don_hang`
- **Rows:** 33,630 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (22):** IDCuaHang, MaHoaDon, MaChiNhanh, MaKhachHang, MaNhanVien, MaCaLam, KenhBanHang, ThoiGianLap, NgayLap, TinhTrang, TongTienHang, ChietKhau, PhiVanChuyen, ThueGTGT, TongThanhToan...
  - *Date cols:* ['NgayLap']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000001", "MaChiNhanh": "CN1", "MaKhachHang": "KH0109", "MaNhanVien": "NV002", "MaCaLam": "CA202501011", "KenhBanHang": "store", "ThoiGianLap": "2025-01-01 06:03:04"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000002", "MaChiNhanh": "CN1", "MaKhachHang": "KH0045", "MaNhanVien": "NV002", "MaCaLam": "CA202501011", "KenhBanHang": "store", "ThoiGianLap": "2025-01-01 06:28:42"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000003", "MaChiNhanh": "CN1", "MaKhachHang": "KH0283", "MaNhanVien": "NV002", "MaCaLam": "CA202501011", "KenhBanHang": "store", "ThoiGianLap": "2025-01-01 06:42:54"}
```

#### Table `pos.sqlite :: chi_tiet_don`
- **Rows:** 64,149 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** IDCuaHang, MaHoaDon, SoThuTu, MaHangHoa, DonViTinh, SL, SLQuyDoi, GiaDonVi, ChietKhau, TriGia, GiaVonLucBan
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000001", "SoThuTu": "1", "MaHangHoa": "SP0080", "DonViTinh": "hộp", "SL": "1", "SLQuyDoi": "1", "GiaDonVi": "371000"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000001", "SoThuTu": "2", "MaHangHoa": "SP0038", "DonViTinh": "chai", "SL": "3", "SLQuyDoi": "3", "GiaDonVi": "58000"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000002", "SoThuTu": "1", "MaHangHoa": "SP0058", "DonViTinh": "chai", "SL": "1", "SLQuyDoi": "1", "GiaDonVi": "65000"}
```

#### Table `pos.sqlite :: thanh_toan`
- **Rows:** 33,816 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaPhieuThu, MaHoaDon, NgayGioThu, SoTienThu, PhuongThuc, DienGiai
  - *Date cols:* ['NgayGioThu']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaPhieuThu": "PAY000001", "MaHoaDon": "ORD000001", "NgayGioThu": "2025-01-01 06:03:04", "SoTienThu": "535000", "PhuongThuc": "transfer", "DienGiai": null}
{"IDCuaHang": "biz_123", "MaPhieuThu": "PAY000002", "MaHoaDon": "ORD000002", "NgayGioThu": "2025-01-01 06:28:42", "SoTienThu": "65000", "PhuongThuc": "cash", "DienGiai": null}
{"IDCuaHang": "biz_123", "MaPhieuThu": "PAY000003", "MaHoaDon": "ORD000003", "NgayGioThu": "2025-01-01 06:42:54", "SoTienThu": "131200", "PhuongThuc": "transfer", "DienGiai": null}
```

#### Table `pos.sqlite :: tra_hang`
- **Rows:** 273 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaPhieuTra, MaHoaDon, NgayGioTra, NguyenNhan, TienHoanTra, CachHoanTien
  - *Date cols:* ['NgayGioTra']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaPhieuTra": "TH00001", "MaHoaDon": "ORD000047", "NgayGioTra": "2025-01-05 08:52:25", "NguyenNhan": "gần hết hạn", "TienHoanTra": "1200", "CachHoanTien": "cash"}
{"IDCuaHang": "biz_123", "MaPhieuTra": "TH00002", "MaHoaDon": "ORD000265", "NgayGioTra": "2025-01-06 18:36:32", "NguyenNhan": "gần hết hạn", "TienHoanTra": "80400", "CachHoanTien": "cash"}
{"IDCuaHang": "biz_123", "MaPhieuTra": "TH00003", "MaHoaDon": "ORD000278", "NgayGioTra": "2025-01-10 12:52:10", "NguyenNhan": "hàng lỗi", "TienHoanTra": "800", "CachHoanTien": "cash"}
```

#### Table `pos.sqlite :: the_kho`
- **Rows:** 65,514 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** IDCuaHang, MaGiaoDichKho, MaHangHoa, MaChiNhanh, NgayGioPhatSinh, LoaiGiaoDich, SLQuyDoi, KieuChungTu, MaChungTu, TonCuoi
  - *Date cols:* ['NgayGioPhatSinh']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaGiaoDichKho": "MV0000001", "MaHangHoa": "SP0001", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-01-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "360", "KieuChungTu": "purchase"}
{"IDCuaHang": "biz_123", "MaGiaoDichKho": "MV0000002", "MaHangHoa": "SP0002", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-01-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "216", "KieuChungTu": "purchase"}
{"IDCuaHang": "biz_123", "MaGiaoDichKho": "MV0000003", "MaHangHoa": "SP0003", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-01-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "240", "KieuChungTu": "purchase"}
```

#### Table `pos.sqlite :: lich_su_gia`
- **Rows:** 109 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** IDCuaHang, MaHangHoa, NgayApDung, GiaBanLe
  - *Date cols:* ['NgayApDung']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "NgayApDung": "2025-01-01", "GiaBanLe": "1400"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0002", "NgayApDung": "2025-01-01", "GiaBanLe": "2000"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0003", "NgayApDung": "2025-01-01", "GiaBanLe": "1000"}
```

#### Table `pos.sqlite :: lo_hang`
- **Rows:** 2,953 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaHangHoa, MaLo, MaPhieuNhap, HanSuDung, SLNhapQuyDoi, DonGiaNhap
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "MaLo": "B2506748", "MaPhieuNhap": "PN00164", "HanSuDung": "2027-04-15", "SLNhapQuyDoi": "360", "DonGiaNhap": "1000"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "MaLo": "B2601174", "MaPhieuNhap": "PN00365", "HanSuDung": "2026-06-26", "SLNhapQuyDoi": "360", "DonGiaNhap": "1000"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "MaLo": "B2604235", "MaPhieuNhap": "PN00473", "HanSuDung": "2028-01-07", "SLNhapQuyDoi": "180", "DonGiaNhap": "1000"}
```

#### Table `pos.sqlite :: chi_tiet_don_lo`
- **Rows:** 64,422 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** IDCuaHang, MaHoaDon, SoThuTu, MaLo, SLQuyDoi, SLTraQuyDoi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000001", "SoThuTu": "1", "MaLo": "J2501289", "SLQuyDoi": "1", "SLTraQuyDoi": "0"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000001", "SoThuTu": "2", "MaLo": "E2501445", "SLQuyDoi": "3", "SLTraQuyDoi": "0"}
{"IDCuaHang": "biz_123", "MaHoaDon": "ORD000002", "SoThuTu": "1", "MaLo": "N2501218", "SLQuyDoi": "1", "SLTraQuyDoi": "0"}
```

#### Table `pos.sqlite :: thong_tin_thuoc`
- **Rows:** 80 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** IDCuaHang, MaHangHoa, ThanhPhanChinh, BanTheoDon
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0001", "ThanhPhanChinh": "Paracetamol + Cafein", "BanTheoDon": "0"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0002", "ThanhPhanChinh": "Paracetamol", "BanTheoDon": "0"}
{"IDCuaHang": "biz_123", "MaHangHoa": "SP0003", "ThanhPhanChinh": "Paracetamol", "BanTheoDon": "0"}
```

---

## Business `biz_124`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_124  Chủ tiệm gửi dữ liệu từ ba nguồn: file Excel xuất từ phần mềm bán hàng (tên file bắt đầu BanHang_, mỗi danh sách một file, danh sách dài tách thành nhiều file đánh số _1, _2…), sổ chủ tiệm tự ghi trên Excel (SoTay_), và file tồn kho CSV. Các file nối với nhau qua mã hoá đơn, mã hàng; sổ tay không có mã hàng, nối qua tên hàng. Tên cột mỗi file đặt theo cách của tiệm.  ## File - `BanHang_HoaDon.xlsx` (xlsx) - `BanHang_ChiTietHoaDon.xlsx` (xlsx) - `BanHang_PhieuThu.xlsx` (xlsx) -
- **Files on disk (14):** BanHang_BanTheoLo.xlsx, BanHang_ChiTietHoaDon.xlsx, BanHang_DonViQuyDoi.xlsx, BanHang_HangHoa.xlsx, BanHang_HoaDon.xlsx, BanHang_KhachHang.xlsx, BanHang_LichSuGia.xlsx, BanHang_LoHang.xlsx, BanHang_PhieuThu.xlsx, BanHang_Thuoc.xlsx, README.md, SoTay_ChiPhi.xlsx, SoTay_NhapHang.xlsx, ton_kho.csv

### Tables / Sheets Detail:
#### Table `BanHang_BanTheoLo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Lô, SL quy ra lẻ, SL trả (ĐVT cơ bản), No., Mã hóa đơn
  - *Date cols:* None
  - *Amount/Qty cols:* ['No.']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Lô": "H2501745", "SL quy ra lẻ": "1", "SL trả (ĐVT cơ bản)": "1", "No.": "1", "Mã hóa đơn": "ORD000001"}
{"Lô": "Y2501823", "SL quy ra lẻ": "20", "SL trả (ĐVT cơ bản)": "0", "No.": "1", "Mã hóa đơn": "ORD000002"}
{"Lô": "D2501692", "SL quy ra lẻ": "10", "SL trả (ĐVT cơ bản)": "0", "No.": "2", "Mã hóa đơn": "ORD000002"}
```

#### Table `BanHang_ChiTietHoaDon.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Giá vốn lúc bán, SL cơ bản, Khuyến mãi, Giá niêm yết, Thanh tien, Mã giao dịch, Chi tiết hàng, Slg, TT dòng, Ma hang, Đ.vị
  - *Date cols:* None
  - *Amount/Qty cols:* ['Thanh tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá vốn lúc bán": "61,000", "SL cơ bản": "1", "Khuyến mãi": "0", "Giá niêm yết": "75,000", "Thanh tien": "75,000", "Mã giao dịch": "ORD000001", "Chi tiết hàng": "Betadine Gargle súc họng chai 125ml", "Slg": "1"}
{"Giá vốn lúc bán": "86,000", "SL cơ bản": "20", "Khuyến mãi": "0", "Giá niêm yết": "106,000", "Thanh tien": "106,000", "Mã giao dịch": "ORD000002", "Chi tiết hàng": "Yumangel Hộp 20 Gói", "Slg": "1"}
{"Giá vốn lúc bán": "1,100", "SL cơ bản": "10", "Khuyến mãi": "0", "Giá niêm yết": "1,300", "Thanh tien": "13,000", "Mã giao dịch": "ORD000002", "Chi tiết hàng": "Decolgen Forte hộp 30 vỉ x 4 viên", "Slg": "10"}
```

#### Table `BanHang_DonViQuyDoi.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Đơn vị, Bằng, Giá bán theo đơn vị quy đổi, Mã sp
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn vị": "hộp", "Bằng": "180", "Giá bán theo đơn vị quy đổi": "270000", "Mã sp": "SP0001"}
{"Đơn vị": "vỉ", "Bằng": "12", "Giá bán theo đơn vị quy đổi": "18000", "Mã sp": "SP0001"}
{"Đơn vị": "hộp", "Bằng": "24", "Giá bán theo đơn vị quy đổi": "48000", "Mã sp": "SP0002"}
```

#### Table `BanHang_HangHoa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (16):** Định mức tồn tối thiểu, Giá vốn hiện tại, Thương hiệu, Thuộc tính, Phân loại, Món, Được bán trực tiếp, Mã HH Liên quan, ma_sp, Mô tả sản phẩm, Mẫu ghi chú, Giá, Ghi chú, Đơn vị, Trọng lượng...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* ['ma_sp']
- **Sample 3 rows:**
```json
{"Định mức tồn tối thiểu": "0", "Giá vốn hiện tại": "1100", "Thương hiệu": null, "Thuộc tính": null, "Phân loại": "giảm đau hạ sốt", "Món": "Panadol Extra hộp 15 vỉ x 12 viên", "Được bán trực tiếp": "1", "Mã HH Liên quan": null}
{"Định mức tồn tối thiểu": "0", "Giá vốn hiện tại": "1600", "Thương hiệu": null, "Thuộc tính": null, "Phân loại": "giảm đau hạ sốt", "Món": "Hapacol 250 hộp 24 gói", "Được bán trực tiếp": "1", "Mã HH Liên quan": null}
{"Định mức tồn tối thiểu": "0", "Giá vốn hiện tại": "800", "Thương hiệu": null, "Thuộc tính": null, "Phân loại": "giảm đau hạ sốt", "Món": "Panadol 500mg hộp 10 vỉ x 12 viên", "Được bán trực tiếp": "1", "Mã HH Liên quan": null}
```

#### Table `BanHang_HoaDon.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (14):** Đã thu, Tên KH, Trạng thái, Giờ tạo đơn, Mã NV bán, Phương thức TT, Ngày bán, Nguồn đơn, Còn nợ, Mã KH mua, Tiền hàng trước giảm, Tong tien, Order ID, CK
  - *Date cols:* None
  - *Amount/Qty cols:* ['Tong tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đã thu": "75,000", "Tên KH": "Tạ Bảo Duy", "Trạng thái": "Đổi trả", "Giờ tạo đơn": "2025-01-01 06:09:58", "Mã NV bán": "NV002", "Phương thức TT": "Tiền mặt", "Ngày bán": "1 thg 1 2025", "Nguồn đơn": "store"}
{"Đã thu": "119,000", "Tên KH": "Từ Thắng Hải", "Trạng thái": "Đã giao", "Giờ tạo đơn": "2025-01-01 07:00:31", "Mã NV bán": "NV002", "Phương thức TT": "Tiền mặt", "Ngày bán": "1 thg 1 2025", "Nguồn đơn": "store"}
{"Đã thu": "18,000", "Tên KH": "Khách lẻ", "Trạng thái": "Đã giao", "Giờ tạo đơn": "2025-01-01 07:26:25", "Mã NV bán": "NV002", "Phương thức TT": "Tiền mặt", "Ngày bán": "01/01/2025", "Nguồn đơn": "store"}
```

#### Table `BanHang_KhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (15):** Điểm tích lũy, Công ty, Hạng, E-mail, MST, Ngày sinh, CCCD, Trạng thái, ten_kh, Người tạo, Ghi chú, Tổng điểm, Loại hình khách, Số điện thoại, Customer ID
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Điểm tích lũy": "0", "Công ty": null, "Hạng": "thân thiết", "E-mail": null, "MST": null, "Ngày sinh": null, "CCCD": null, "Trạng thái": "Đang hoạt động"}
{"Điểm tích lũy": "0", "Công ty": null, "Hạng": "sỉ", "E-mail": null, "MST": null, "Ngày sinh": null, "CCCD": null, "Trạng thái": "Đang hoạt động"}
{"Điểm tích lũy": "0", "Công ty": null, "Hạng": "lẻ", "E-mail": null, "MST": null, "Ngày sinh": null, "CCCD": null, "Trạng thái": "Đang hoạt động"}
```

#### Table `BanHang_LichSuGia.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã sản phẩm, Giá mới, Ngày áp dụng, Sản phẩm, Giá cũ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã sản phẩm": "SP0001", "Giá mới": "1400", "Ngày áp dụng": "2025-01-01 00:00:00", "Sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Giá cũ": null}
{"Mã sản phẩm": "SP0001", "Giá mới": "1500", "Ngày áp dụng": "2025-12-17 00:00:00", "Sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Giá cũ": "1400"}
{"Mã sản phẩm": "SP0002", "Giá mới": "2000", "Ngày áp dụng": "2025-01-01 00:00:00", "Sản phẩm": "Hapacol 250 hộp 24 gói", "Giá cũ": null}
```

#### Table `BanHang_LoHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** HSD, Mã món, SL nhập (ĐVT cơ bản), Mã phiếu nhập, Lô
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"HSD": "30/01/2027", "Mã món": "SP0001", "SL nhập (ĐVT cơ bản)": "360", "Mã phiếu nhập": "PN00142", "Lô": "A2505116"}
{"HSD": "08/04/2027", "Mã món": "SP0001", "SL nhập (ĐVT cơ bản)": "360", "Mã phiếu nhập": "PN00405", "Lô": "A2602802"}
{"HSD": "13/07/2027", "Mã món": "SP0001", "SL nhập (ĐVT cơ bản)": "360", "Mã phiếu nhập": "PN00185", "Lô": "B2507439"}
```

#### Table `BanHang_PhieuThu.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Số tiền thu, Mã bill, Phiếu thu, Thời gian thu, PTTT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số tiền thu": "75,000", "Mã bill": "ORD000001", "Phiếu thu": "PAY000001", "Thời gian thu": "2025-01-01 06:09:58", "PTTT": "Tiền mặt"}
{"Số tiền thu": "119,000", "Mã bill": "ORD000002", "Phiếu thu": "PAY000002", "Thời gian thu": "2025-01-01 07:00:31", "PTTT": "Tiền mặt"}
{"Số tiền thu": "18,000", "Mã bill": "ORD000003", "Phiếu thu": "PAY000003", "Thời gian thu": "2025-01-01 07:26:25", "PTTT": "Tiền mặt"}
```

#### Table `BanHang_Thuoc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã HH, Hoạt chất, Kê đơn
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã HH": "SP0001", "Hoạt chất": "Paracetamol + Cafein", "Kê đơn": "False"}
{"Mã HH": "SP0002", "Hoạt chất": "Paracetamol", "Kê đơn": "False"}
{"Mã HH": "SP0003", "Hoạt chất": "Paracetamol", "Kê đơn": "False"}
```

#### Table `SoTay_ChiPhi.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (4):** Ghi chú, Ngày chi, Mục, So tien
  - *Date cols:* None
  - *Amount/Qty cols:* ['So tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ghi chú": null, "Ngày chi": "01/01/2025", "Mục": "thuê", "So tien": "25000k"}
{"Ghi chú": null, "Ngày chi": "05/01/2025", "Mục": "điện", "So tien": "3950k"}
{"Ghi chú": null, "Ngày chi": "05/01/2025", "Mục": "nước", "So tien": "578.000đ"}
```

#### Table `SoTay_NhapHang.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (11):** SL nhập, Mô tả, Product, Thành tiền, Lô, HSD, Ngày nhập, Nhà cung cấp, ĐVT nhập, Số phiếu, Giá nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"SL nhập": "2", "Mô tả": "nhập đầu kỳ", "Product": "Panadol Extra hộp 15 vỉ x 12 viên", "Thành tiền": "396k", "Lô": "E2501244", "HSD": "2025-05-16 00:00:00", "Ngày nhập": "01/01/2025", "Nhà cung cấp": "Cty Mai Tâm"}
{"SL nhập": "11", "Mô tả": "nhập đầu kỳ", "Product": "Hapacol 250 hộp 24 gói", "Thành tiền": "422.400đ", "Lô": "I2501674", "HSD": "2025-05-22 00:00:00", "Ngày nhập": "01/01/2025", "Nhà cung cấp": "Cty Mai Tâm"}
{"SL nhập": "3", "Mô tả": "nhập đầu kỳ", "Product": "Panadol 500mg hộp 10 vỉ x 12 viên", "Thành tiền": "288.000đ", "Lô": "Y2501592", "HSD": "2026-07-19 00:00:00", "Ngày nhập": "01/01/2025", "Nhà cung cấp": "Cty Mai Tâm"}
```

#### Table `ton_kho.csv`
- **Rows:** 80 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** ID SP, Đơn vị, Ton kho, Hàng hóa
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"ID SP": "SP0001", "Đơn vị": "viên", "Ton kho": "112", "Hàng hóa": "Panadol Extra hộp 15 vỉ x 12 viên"}
{"ID SP": "SP0002", "Đơn vị": "gói", "Ton kho": "4", "Hàng hóa": "Hapacol 250 hộp 24 gói"}
{"ID SP": "SP0003", "Đơn vị": "viên", "Ton kho": "279", "Hàng hóa": "Panadol 500mg hộp 10 vỉ x 12 viên"}
```

---

## Business `biz_125`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_125  Một file phẳng, mỗi dòng một bản ghi (một dòng hàng trong đơn).  ## File - `ban_hang.csv` (csv)  ## Cột trong `ban_hang.csv` - **dvt**: đơn vị tính - **Hàng bán**: tên hàng - **Khách hàng (tên)**: tên khách (Khách lẻ nếu không lưu) - **Số lượng lẻ**: số lượng đã đổi ra đơn vị cơ bản - **Amount**: thành tiền sau giảm - **Trạng thái xử lý**: trạng thái đơn - **SL bán**: số lượng - **Ngày bán**: ngày bán - **Số phiếu**: mã đơn - **Giá 1 đv**: đơn giá  ## Quy ước - Dữ liệu có đến
- **Files on disk (2):** README.md, ban_hang.csv

### Tables / Sheets Detail:
#### Table `ban_hang.csv`
- **Rows:** 79,052 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** dvt, Hàng bán, Khách hàng (tên), Số lượng lẻ, Amount, Trạng thái xử lý, SL bán, Ngày bán, Số phiếu, Giá 1 đv
  - *Date cols:* None
  - *Amount/Qty cols:* ['Amount']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"dvt": "đĩa", "Hàng bán": "Gỏi xoài tôm nướng", "Khách hàng (tên)": "Hứa Hiếu Phương", "Số lượng lẻ": "1", "Amount": "125000", "Trạng thái xử lý": "Đã hoàn thành", "SL bán": "1", "Ngày bán": "01/01/2025"}
{"dvt": "ly", "Hàng bán": "Trà đá", "Khách hàng (tên)": "Hứa Hiếu Phương", "Số lượng lẻ": "2", "Amount": "10000", "Trạng thái xử lý": "Đã hoàn thành", "SL bán": "2", "Ngày bán": "01/01/2025"}
{"dvt": "đĩa", "Hàng bán": "Sụn gà rang muối", "Khách hàng (tên)": "Hứa Hiếu Phương", "Số lượng lẻ": "1", "Amount": "89,000", "Trạng thái xử lý": "Đã hoàn thành", "SL bán": "1", "Ngày bán": "01/01/2025"}
```

---

## Business `biz_126`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_126  Sổ bán hàng chủ tiệm tự ghi trên Excel, một sheet: mỗi dòng một mặt hàng khách mua, không ghi mã đơn, không ghi tên khách.  ## File - `SoBanHang.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **Đơn vị tính**: đơn vị tính - **Số lượng bán**: số lượng - **Thành tiền (đ)**: thành tiền sau giảm - **Ten hang**: tên hàng - **SL lẻ**: số lượng đã đổi ra đơn vị cơ bản - **Trạng thái đơn**: trạng thái đơn - **Ngày tháng**: ngày bán - **Price**: đơn giá  ## Quy ước - Dữ liệu có đến hết 0
- **Files on disk (2):** README.md, SoBanHang.xlsx

### Tables / Sheets Detail:
#### Table `SoBanHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Đơn vị tính, Số lượng bán, Thành tiền (đ), Ten hang, SL lẻ, Trạng thái đơn, Ngày tháng, Price
  - *Date cols:* None
  - *Amount/Qty cols:* ['Price']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn vị tính": "đĩa", "Số lượng bán": "1", "Thành tiền (đ)": "99000", "Ten hang": "Tôm nướng mọi", "SL lẻ": "1", "Trạng thái đơn": "Đã giao", "Ngày tháng": "01/01/2025", "Price": "99000"}
{"Đơn vị tính": "phần", "Số lượng bán": "1", "Thành tiền (đ)": "79.000đ", "Ten hang": "Thịt ba rọi kho tộ", "SL lẻ": "1", "Trạng thái đơn": "Đã giao", "Ngày tháng": "01/01/2025", "Price": "79000"}
{"Đơn vị tính": "nồi", "Số lượng bán": "1", "Thành tiền (đ)": "189000", "Ten hang": "Lẩu gà lá é", "SL lẻ": "1", "Trạng thái đơn": "Đã giao", "Ngày tháng": "01/01/2025", "Price": "189,000"}
```

---

## Business `biz_127`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_127  Dữ liệu bán hàng của tiệm, gồm vài file nối với nhau qua mã.  ## File - `don_hang.csv` (csv) - `chi_tiet_don.csv` (csv) - `san_pham.csv` (csv) - `khach_hang.csv` (csv) - `thanh_toan.csv` (csv)  ## Cột trong `don_hang.csv` - **Còn nợ**: còn nợ - **Diễn giải**: cột trống, không có dữ liệu - **Tổng đơn**: tổng tiền đơn - **Loại bán**: kênh bán - **Ngày**: ngày bán - **Mã chứng từ**: mã đơn - **Customer ID**: mã khách (trống nếu khách lẻ) - **Khách trả**: đã thanh toán - **Trả bằn
- **Files on disk (6):** README.md, chi_tiet_don.csv, don_hang.csv, khach_hang.csv, san_pham.csv, thanh_toan.csv

### Tables / Sheets Detail:
#### Table `chi_tiet_don.csv`
- **Rows:** 131,192 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Mã đơn hàng, SoLuong, No., DVT, Amount, Số lượng lẻ, Mã mặt hàng, Đơn giá (đ)
  - *Date cols:* None
  - *Amount/Qty cols:* ['SoLuong', 'No.', 'Amount']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "SoLuong": "1", "No.": "1", "DVT": "phần", "Amount": "10.000đ", "Số lượng lẻ": "1", "Mã mặt hàng": "SP0011", "Đơn giá (đ)": "10000"}
{"Mã đơn hàng": "ORD000001", "SoLuong": "1", "No.": "2", "DVT": "nồi", "Amount": "189.000đ", "Số lượng lẻ": "1", "Mã mặt hàng": "SP0004", "Đơn giá (đ)": "189000"}
{"Mã đơn hàng": "ORD000001", "SoLuong": "1", "No.": "3", "DVT": "đĩa", "Amount": "69.000đ", "Số lượng lẻ": "1", "Mã mặt hàng": "SP0007", "Đơn giá (đ)": "69000"}
```

#### Table `don_hang.csv`
- **Rows:** 33,874 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Còn nợ, Diễn giải, Tổng đơn, Loại bán, Ngày, Mã chứng từ, Customer ID, Khách trả, Trả bằng, Tình trạng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Còn nợ": "0", "Diễn giải": "nan", "Tổng đơn": "457000", "Loại bán": "store", "Ngày": "2025-03-01", "Mã chứng từ": "ORD000001", "Customer ID": "KH0169", "Khách trả": "457000"}
{"Còn nợ": "0", "Diễn giải": "nan", "Tổng đơn": "347000", "Loại bán": "store", "Ngày": "2025-03-01", "Mã chứng từ": "ORD000002", "Customer ID": "nan", "Khách trả": "347000"}
{"Còn nợ": "0", "Diễn giải": "nan", "Tổng đơn": "1617000", "Loại bán": "store", "Ngày": "2025-03-01", "Mã chứng từ": "ORD000003", "Customer ID": "KH0167", "Khách trả": "1617000"}
```

#### Table `khach_hang.csv`
- **Rows:** 200 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (14):** CCCD, Tên công ty, Di động, Email, Sinh nhật, Người tạo, Tổng điểm, Loại hình khách, Mã KH, Khách hàng (tên), Điểm hiện tại, MST, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"CCCD": "nan", "Tên công ty": "nan", "Di động": "0912852391", "Email": "nan", "Sinh nhật": "28/04/1998", "Người tạo": "admin", "Tổng điểm": "0", "Loại hình khách": "Cá nhân"}
{"CCCD": "nan", "Tên công ty": "nan", "Di động": "0354919024", "Email": "nan", "Sinh nhật": "nan", "Người tạo": "admin", "Tổng điểm": "0", "Loại hình khách": "Cá nhân"}
{"CCCD": "nan", "Tên công ty": "nan", "Di động": "0323083991", "Email": "nan", "Sinh nhật": "nan", "Người tạo": "admin", "Tổng điểm": "0", "Loại hình khách": "Cá nhân"}
```

#### Table `san_pham.csv`
- **Rows:** 61 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Trọng lượng, Giá niêm yết, Mô tả chi tiết, Danh mục, Ghi chú, Mã sản phẩm bán, Tên SP, Mẫu ghi chú, Mã barcode, Loại hàng hóa, Tồn lớn nhất, Thương hiệu, Thuộc tính, Hình ảnh (url1,url2...), Đơn vị cơ bản...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Trọng lượng": "nan", "Giá niêm yết": "52500", "Mô tả chi tiết": "nan", "Danh mục": "rau", "Ghi chú": "nan", "Mã sản phẩm bán": "SP0001", "Tên SP": "Rau muống xào tỏi", "Mẫu ghi chú": "nan"}
{"Trọng lượng": "nan", "Giá niêm yết": "22000", "Mô tả chi tiết": "nan", "Danh mục": "bia", "Ghi chú": "nan", "Mã sản phẩm bán": "SP0002", "Tên SP": "Bia Tiger lon", "Mẫu ghi chú": "nan"}
{"Trọng lượng": "nan", "Giá niêm yết": "79000", "Mô tả chi tiết": "nan", "Danh mục": "chiên xào", "Ghi chú": "nan", "Mã sản phẩm bán": "SP0003", "Tên SP": "Cánh gà chiên nước mắm", "Mẫu ghi chú": "nan"}
```

#### Table `thanh_toan.csv`
- **Rows:** 33,473 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Số CT, Ngày thu, Mã GD, Giá trị, HTTT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số CT": "ORD000001", "Ngày thu": "2025-03-01 07:15:59", "Mã GD": "PAY000001", "Giá trị": "457000", "HTTT": "cash"}
{"Số CT": "ORD000002", "Ngày thu": "2025-03-01 07:22:30", "Mã GD": "PAY000002", "Giá trị": "347000", "HTTT": "cash"}
{"Số CT": "ORD000003", "Ngày thu": "2025-03-01 07:42:10", "Mã GD": "PAY000003", "Giá trị": "1617000", "HTTT": "cash"}
```

---

## Business `biz_128`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_128  File Excel xuất từ phần mềm bán hàng, mỗi danh sách một file (danh sách dài tách thành nhiều file, tên thêm đuôi _1, _2… hoặc đuôi năm _2025, _2026…), nối với nhau qua mã. Ngày dạng dd/mm/yyyy.  File `DanhSachHoaDon.xlsx` chia mỗi tháng một sheet, tên sheet ghi tháng và năm.  ## File - `DanhSachHoaDon.xlsx` (xlsx) - `DanhSachHoaDonChiTiet.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DanhSachKhachHang.xlsx` (xlsx) - `BaoCaoTonKho.xlsx` (xlsx) - `DanhSachNhapHang.xlsx` (xlsx)
- **Files on disk (9):** BaoCaoTonKho.xlsx, DanhSachChiTietNhapHang.xlsx, DanhSachHoaDon.xlsx, DanhSachHoaDonChiTiet.xlsx, DanhSachHoaDonPhongBan.xlsx, DanhSachKhachHang.xlsx, DanhSachNhapHang.xlsx, DanhSachSanPham.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BaoCaoTonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hàng, Tên hàng, ĐVT, Tồn cuối kỳ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tên hàng": "Rau muống xào tỏi", "ĐVT": "đĩa", "Tồn cuối kỳ": "204"}
{"Mã hàng": "SP0002", "Tên hàng": "Bia Tiger lon", "ĐVT": "lon", "Tồn cuối kỳ": "43"}
{"Mã hàng": "SP0003", "Tên hàng": "Cánh gà chiên nước mắm", "ĐVT": "đĩa", "Tồn cuối kỳ": "192"}
```

#### Table `DanhSachChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, STT, Mã hàng, ĐVT, Số lượng, Đơn giá
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "STT": "1", "Mã hàng": "SP0001", "ĐVT": "đĩa", "Số lượng": "223", "Đơn giá": "16,000"}
{"Mã nhập hàng": "PN00001", "STT": "2", "Mã hàng": "SP0002", "ĐVT": "thùng", "Số lượng": "10", "Đơn giá": "360,000"}
{"Mã nhập hàng": "PN00001", "STT": "3", "Mã hàng": "SP0003", "ĐVT": "đĩa", "Số lượng": "201", "Đơn giá": "33,000"}
```

#### Table `DanhSachHoaDon.xlsx :: 04.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Thời gian": "01/04/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "196,000", "Giảm giá": "0", "Khách đã trả": "196,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD000002", "Thời gian": "01/04/2025", "Mã KH": "KH0128", "Khách hàng": "Tăng Phương Hoa", "Tổng tiền hàng": "69,000", "Giảm giá": "0", "Khách đã trả": "69,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD000003", "Thời gian": "01/04/2025", "Mã KH": "KH0027", "Khách hàng": "Mai Sơn Hương", "Tổng tiền hàng": "160,000", "Giảm giá": "0", "Khách đã trả": "160,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 05.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD001538", "Thời gian": "01/05/2025", "Mã KH": "KH0073", "Khách hàng": "Trương Hạnh Ngọc", "Tổng tiền hàng": "238,000", "Giảm giá": "0", "Khách đã trả": "238,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD001539", "Thời gian": "01/05/2025", "Mã KH": "KH0085", "Khách hàng": "Hồ Nhung Thảo", "Tổng tiền hàng": "338,000", "Giảm giá": "10,000", "Khách đã trả": "328,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD001540", "Thời gian": "01/05/2025", "Mã KH": "KH0120", "Khách hàng": "Giang Nam Châu", "Tổng tiền hàng": "434,000", "Giảm giá": "10,000", "Khách đã trả": "424,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 06.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD003062", "Thời gian": "01/06/2025", "Mã KH": "KH0113", "Khách hàng": "Đoàn Đức Thu", "Tổng tiền hàng": "79,000", "Giảm giá": "0", "Khách đã trả": "79,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD003063", "Thời gian": "01/06/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "588,000", "Giảm giá": "10,000", "Khách đã trả": "578,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD003064", "Thời gian": "01/06/2025", "Mã KH": "KH0005", "Khách hàng": "Huỳnh Phương Dũng", "Tổng tiền hàng": "299,000", "Giảm giá": "0", "Khách đã trả": "299,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 07.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD004451", "Thời gian": "01/07/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "646,000", "Giảm giá": "10,000", "Khách đã trả": "636,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD004452", "Thời gian": "01/07/2025", "Mã KH": "KH0150", "Khách hàng": "Lâm Giang Tâm", "Tổng tiền hàng": "198,000", "Giảm giá": "0", "Khách đã trả": "198,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD004453", "Thời gian": "01/07/2025", "Mã KH": "KH0104", "Khách hàng": "Lương Loan Bảo", "Tổng tiền hàng": "822,000", "Giảm giá": "10,000", "Khách đã trả": "812,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 08.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD006026", "Thời gian": "01/08/2025", "Mã KH": "KH0111", "Khách hàng": "Quách Minh Minh", "Tổng tiền hàng": "717,000", "Giảm giá": "10,000", "Khách đã trả": "707,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD006027", "Thời gian": "01/08/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "350,000", "Giảm giá": "10,000", "Khách đã trả": "340,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD006028", "Thời gian": "01/08/2025", "Mã KH": "KH0028", "Khách hàng": "Vũ Hà Minh", "Tổng tiền hàng": "1,103,000", "Giảm giá": "10,000", "Khách đã trả": "1,093,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 09.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD007581", "Thời gian": "01/09/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "173,000", "Giảm giá": "0", "Khách đã trả": "173,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD007582", "Thời gian": "01/09/2025", "Mã KH": "KH0020", "Khách hàng": "Tống Phúc Bình", "Tổng tiền hàng": "425,000", "Giảm giá": "10,000", "Khách đã trả": "415,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD007583", "Thời gian": "01/09/2025", "Mã KH": "KH0171", "Khách hàng": "Chung Linh Hương", "Tổng tiền hàng": "559,000", "Giảm giá": "10,000", "Khách đã trả": "549,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 10.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD009120", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "380,000", "Giảm giá": "10,000", "Khách đã trả": "370,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD009121", "Thời gian": "01/10/2025", "Mã KH": "KH0168", "Khách hàng": "Bùi Thắng Phương", "Tổng tiền hàng": "22,000", "Giảm giá": "0", "Khách đã trả": "22,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD009122", "Thời gian": "01/10/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "292,000", "Giảm giá": "0", "Khách đã trả": "292,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 11.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD010716", "Thời gian": "01/11/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "84,000", "Giảm giá": "0", "Khách đã trả": "84,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD010717", "Thời gian": "01/11/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "104,000", "Giảm giá": "0", "Khách đã trả": "104,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD010718", "Thời gian": "01/11/2025", "Mã KH": "KH0021", "Khách hàng": "Hứa Quân Hoa", "Tổng tiền hàng": "446,000", "Giảm giá": "10,000", "Khách đã trả": "436,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 12.2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD012173", "Thời gian": "01/12/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "661,500", "Giảm giá": "10,000", "Khách đã trả": "651,500", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD012174", "Thời gian": "01/12/2025", "Mã KH": "KH0126", "Khách hàng": "Vương Trang Lan", "Tổng tiền hàng": "176,000", "Giảm giá": "0", "Khách đã trả": "176,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD012175", "Thời gian": "01/12/2025", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "89,000", "Giảm giá": "0", "Khách đã trả": "89,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 01.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD013746", "Thời gian": "01/01/2026", "Mã KH": "KH0065", "Khách hàng": "Bùi Ngân Quang", "Tổng tiền hàng": "317,000", "Giảm giá": "10,000", "Khách đã trả": "307,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD013747", "Thời gian": "01/01/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "606,000", "Giảm giá": "10,000", "Khách đã trả": "596,000", "Trạng thái": "xong"}
{"Mã hóa đơn": "ORD013748", "Thời gian": "01/01/2026", "Mã KH": "KH0094", "Khách hàng": "Quách Hoa Thảo", "Tổng tiền hàng": "616,000", "Giảm giá": "10,000", "Khách đã trả": "606,000", "Trạng thái": "xong"}
```

#### Table `DanhSachHoaDon.xlsx :: 02.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD015361", "Thời gian": "01/02/2026", "Mã KH": "KH0066", "Khách hàng": "Hứa Bình Sơn", "Tổng tiền hàng": "2,910,000", "Giảm giá": "10,000", "Khách đã trả": "2,900,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD015362", "Thời gian": "01/02/2026", "Mã KH": "KH0114", "Khách hàng": "Triệu Thanh Dương", "Tổng tiền hàng": "444,000", "Giảm giá": "10,000", "Khách đã trả": "434,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD015363", "Thời gian": "01/02/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "118,000", "Giảm giá": "0", "Khách đã trả": "118,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 03.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD016362", "Thời gian": "01/03/2026", "Mã KH": "KH0177", "Khách hàng": "Bùi Hương Dương", "Tổng tiền hàng": "226,000", "Giảm giá": "0", "Khách đã trả": "226,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD016363", "Thời gian": "01/03/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "222,000", "Giảm giá": "0", "Khách đã trả": "222,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD016364", "Thời gian": "01/03/2026", "Mã KH": "KH0068", "Khách hàng": "Hoàng Hùng Trung", "Tổng tiền hàng": "101,000", "Giảm giá": "0", "Khách đã trả": "101,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 04.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD017973", "Thời gian": "01/04/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "247,000", "Giảm giá": "0", "Khách đã trả": "247,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD017974", "Thời gian": "01/04/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,064,500", "Giảm giá": "10,000", "Khách đã trả": "1,054,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD017975", "Thời gian": "01/04/2026", "Mã KH": "KH0072", "Khách hàng": "Triệu Tâm Thảo", "Tổng tiền hàng": "493,000", "Giảm giá": "10,000", "Khách đã trả": "483,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 05.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD019575", "Thời gian": "01/05/2026", "Mã KH": "KH0159", "Khách hàng": "Phạm Sơn Ngân", "Tổng tiền hàng": "1,040,500", "Giảm giá": "10,000", "Khách đã trả": "1,030,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD019576", "Thời gian": "01/05/2026", "Mã KH": "KH0031", "Khách hàng": "Quách Bình Thắng", "Tổng tiền hàng": "318,500", "Giảm giá": "10,000", "Khách đã trả": "308,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD019577", "Thời gian": "01/05/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "702,000", "Giảm giá": "10,000", "Khách đã trả": "692,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 06.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD021176", "Thời gian": "01/06/2026", "Mã KH": "KH0014", "Khách hàng": "Hồ Chi Dương", "Tổng tiền hàng": "755,000", "Giảm giá": "10,000", "Khách đã trả": "745,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD021177", "Thời gian": "01/06/2026", "Mã KH": "KH0143", "Khách hàng": "Nghiêm Bình Hằng", "Tổng tiền hàng": "22,000", "Giảm giá": "0", "Khách đã trả": "22,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD021178", "Thời gian": "01/06/2026", "Mã KH": "KH0167", "Khách hàng": "Quách Hoàng Thắng", "Tổng tiền hàng": "373,000", "Giảm giá": "10,000", "Khách đã trả": "363,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 07.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD022768", "Thời gian": "01/07/2026", "Mã KH": "KH0120", "Khách hàng": "Giang Nam Châu", "Tổng tiền hàng": "920,700", "Giảm giá": "10,000", "Khách đã trả": "925,700", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD022769", "Thời gian": "01/07/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "288,000", "Giảm giá": "0", "Khách đã trả": "303,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD022770", "Thời gian": "01/07/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "517,000", "Giảm giá": "10,000", "Khách đã trả": "507,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 08.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD024452", "Thời gian": "01/08/2026", "Mã KH": "KH0151", "Khách hàng": "Diệp Hiếu Mai", "Tổng tiền hàng": "845,500", "Giảm giá": "10,000", "Khách đã trả": "835,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD024453", "Thời gian": "01/08/2026", "Mã KH": "KH0064", "Khách hàng": "Trương Thắng Hằng", "Tổng tiền hàng": "393,000", "Giảm giá": "10,000", "Khách đã trả": "383,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD024454", "Thời gian": "01/08/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "310,000", "Giảm giá": "10,000", "Khách đã trả": "300,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDon.xlsx :: 09.2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Mã hóa đơn, Thời gian, Mã KH, Khách hàng, Tổng tiền hàng, Giảm giá, Khách đã trả, Trạng thái, Thời gian tạo, Tổng sau giảm giá, Còn nợ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD026142", "Thời gian": "01/09/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "1,879,000", "Giảm giá": "10,000", "Khách đã trả": "1,869,000", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD026143", "Thời gian": "01/09/2026", "Mã KH": null, "Khách hàng": "Khách lẻ", "Tổng tiền hàng": "93,500", "Giảm giá": "0", "Khách đã trả": "93,500", "Trạng thái": "Thành công"}
{"Mã hóa đơn": "ORD026144", "Thời gian": "01/09/2026", "Mã KH": "KH0109", "Khách hàng": "Chung Loan Thảo", "Tổng tiền hàng": "418,000", "Giảm giá": "10,000", "Khách đã trả": "408,000", "Trạng thái": "Thành công"}
```

#### Table `DanhSachHoaDonChiTiet.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã hóa đơn, Mã hàng, Tên hàng, Số lượng, Đơn giá, Giảm giá, Thành tiền, Số lượng quy đổi, STT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0005", "Tên hàng": "Gỏi xoài khô cá sặc", "Số lượng": "1", "Đơn giá": "99,000", "Giảm giá": "0", "Thành tiền": "99,000", "Số lượng quy đổi": "1"}
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0029", "Tên hàng": "Mì xào hải sản", "Số lượng": "1", "Đơn giá": "79,000", "Giảm giá": "0", "Thành tiền": "79,000", "Số lượng quy đổi": "1"}
{"Mã hóa đơn": "ORD000001", "Mã hàng": "SP0030", "Tên hàng": "Bia Sài Gòn Lager chai", "Số lượng": "1", "Đơn giá": "18,000", "Giảm giá": "0", "Thành tiền": "18,000", "Số lượng quy đổi": "1"}
```

#### Table `DanhSachHoaDonPhongBan.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã hóa đơn, Phòng/Bàn, Khu vực, Số khách
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hóa đơn": "ORD000001", "Phòng/Bàn": "B11", "Khu vực": "sân", "Số khách": "3"}
{"Mã hóa đơn": "ORD000002", "Phòng/Bàn": "B05", "Khu vực": "trong nhà", "Số khách": "1"}
{"Mã hóa đơn": "ORD000003", "Phòng/Bàn": "B05", "Khu vực": "trong nhà", "Số khách": "5"}
```

#### Table `DanhSachKhachHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Sinh nhật, Người tạo, Mã khách hàng, Email, Tên khách hàng, Điện thoại, Nhóm khách hàng, Loại hình khách, Điểm hiện tại, CCCD, Ghi chú KH, Công ty, Địa chỉ, Trạng thái, Giới tính...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Sinh nhật": null, "Người tạo": "admin", "Mã khách hàng": "KH0001", "Email": null, "Tên khách hàng": "Kiều Long Đức", "Điện thoại": "0978608839", "Nhóm khách hàng": "lẻ", "Loại hình khách": "Cá nhân"}
{"Sinh nhật": "21/02/1987", "Người tạo": "admin", "Mã khách hàng": "KH0002", "Email": null, "Tên khách hàng": "Kiều Quân Hùng", "Điện thoại": "0908588993", "Nhóm khách hàng": "thân thiết", "Loại hình khách": "Cá nhân"}
{"Sinh nhật": null, "Người tạo": "admin", "Mã khách hàng": "KH0003", "Email": null, "Tên khách hàng": "Tạ Khánh Hoa", "Điện thoại": "0934635968", "Nhóm khách hàng": "thân thiết", "Loại hình khách": "Cá nhân"}
```

#### Table `DanhSachNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Mã nhập hàng, Thời gian, Mã NCC, Cần trả NCC, Trạng thái, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã nhập hàng": "PN00001", "Thời gian": "01/04/2025", "Mã NCC": "NCC003", "Cần trả NCC": "227,262,100", "Trạng thái": "Đã nhập hàng", "Ghi chú": "nhập đầu kỳ"}
{"Mã nhập hàng": "PN00002", "Thời gian": "11/04/2025", "Mã NCC": "NCC002", "Cần trả NCC": "2,880,000", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
{"Mã nhập hàng": "PN00003", "Thời gian": "13/04/2025", "Mã NCC": "NCC003", "Cần trả NCC": "878,400", "Trạng thái": "Đã nhập hàng", "Ghi chú": null}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (19):** Mã hàng, Tồn nhỏ nhất, Loại hàng hóa, Tồn lớn nhất, Tên hàng, Nhóm hàng(3 Cấp), Ghi chú, Giá bán, Thương hiệu, Mã HH Liên quan, Mẫu ghi chú, Mã barcode, Vị trí, Thuộc tính, Hình ảnh...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng": "SP0001", "Tồn nhỏ nhất": "0", "Loại hàng hóa": "Hàng hóa", "Tồn lớn nhất": "999999999", "Tên hàng": "Rau muống xào tỏi", "Nhóm hàng(3 Cấp)": "rau", "Ghi chú": null, "Giá bán": "52500"}
{"Mã hàng": "SP0002", "Tồn nhỏ nhất": "0", "Loại hàng hóa": "Hàng hóa", "Tồn lớn nhất": "999999999", "Tên hàng": "Bia Tiger lon", "Nhóm hàng(3 Cấp)": "bia", "Ghi chú": null, "Giá bán": "22000"}
{"Mã hàng": "SP0003", "Tồn nhỏ nhất": "0", "Loại hàng hóa": "Hàng hóa", "Tồn lớn nhất": "999999999", "Tên hàng": "Cánh gà chiên nước mắm", "Nhóm hàng(3 Cấp)": "chiên xào", "Ghi chú": null, "Giá bán": "83000"}
```

---

## Business `biz_129`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu biz_129  Dữ liệu bán hàng của tiệm, gồm vài file nối với nhau qua mã.  ## File - `don_hang.csv` (csv) - `chi_tiet_don.csv` (csv) - `san_pham.csv` (csv) - `khach_hang.csv` (csv) - `thanh_toan.csv` (csv)  ## Cột trong `don_hang.csv` - **Hình thức thanh toán**: hình thức thanh toán của đơn: cash tiền mặt, transfer chuyển khoản, ewallet ví điện tử, cod giao hàng thu tiền, debt ghi nợ - **Dư nợ**: còn nợ - **Thanh toán**: đã thanh toán - **Tình trạng đơn**: trạng thái đơn - **Số phiếu**: mã
- **Files on disk (6):** README.md, chi_tiet_don.csv, don_hang.csv, khach_hang.csv, san_pham.csv, thanh_toan.csv

### Tables / Sheets Detail:
#### Table `chi_tiet_don.csv`
- **Rows:** 145,479 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Tiền bán, TT dòng, S.L, Mã hàng bán, Quy ra ĐV lẻ, Số CT, Giảm giá, Giá 1 đv, ĐV tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền bán": "50.000đ", "TT dòng": "1", "S.L": "1", "Mã hàng bán": "SP0001", "Quy ra ĐV lẻ": "1", "Số CT": "ORD000001", "Giảm giá": "0", "Giá 1 đv": "50000"}
{"Tiền bán": "99.000đ", "TT dòng": "2", "S.L": "1", "Mã hàng bán": "SP0023", "Quy ra ĐV lẻ": "1", "Số CT": "ORD000001", "Giảm giá": "0", "Giá 1 đv": "99000"}
{"Tiền bán": "15.000đ", "TT dòng": "1", "S.L": "1", "Mã hàng bán": "SP0010", "Quy ra ĐV lẻ": "1", "Số CT": "ORD000002", "Giảm giá": "0", "Giá 1 đv": "15000"}
```

#### Table `don_hang.csv`
- **Rows:** 38,499 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Hình thức thanh toán, Dư nợ, Thanh toán, Tình trạng đơn, Số phiếu, Mã khách mua, Phải thu, Ngày bán
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hình thức thanh toán": "transfer", "Dư nợ": "0", "Thanh toán": "149000", "Tình trạng đơn": "completed", "Số phiếu": "ORD000001", "Mã khách mua": "KH0180", "Phải thu": "149000", "Ngày bán": "2025-01-01"}
{"Hình thức thanh toán": "cash", "Dư nợ": "0", "Thanh toán": "20000", "Tình trạng đơn": "completed", "Số phiếu": "ORD000002", "Mã khách mua": "nan", "Phải thu": "20000", "Ngày bán": "2025-01-01"}
{"Hình thức thanh toán": "cash", "Dư nợ": "0", "Thanh toán": "446000", "Tình trạng đơn": "completed", "Số phiếu": "ORD000003", "Mã khách mua": "KH0115", "Phải thu": "446000", "Ngày bán": "2025-01-01"}
```

#### Table `khach_hang.csv`
- **Rows:** 220 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (15):** Ghi chú KH, Ngày sinh, Điểm hiện tại, Nhóm, Tổng điểm, KH, Email, Mã số thuế, Người tạo, Công ty, Số điện thoại, Số CMND/CCCD, Đối tượng KH, Trạng thái, Mã khách lẻ/sỉ
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ghi chú KH": "nan", "Ngày sinh": "nan", "Điểm hiện tại": "0", "Nhóm": "lẻ", "Tổng điểm": "0", "KH": "Hứa Hoàng Bích", "Email": "nan", "Mã số thuế": "nan"}
{"Ghi chú KH": "nan", "Ngày sinh": "nan", "Điểm hiện tại": "0", "Nhóm": "lẻ", "Tổng điểm": "0", "KH": "Bùi Bảo Khánh", "Email": "nan", "Mã số thuế": "nan"}
{"Ghi chú KH": "nan", "Ngày sinh": "nan", "Điểm hiện tại": "0", "Nhóm": "thân thiết", "Tổng điểm": "0", "KH": "Huỳnh Quân Minh", "Email": "nan", "Mã số thuế": "nan"}
```

#### Table `san_pham.csv`
- **Rows:** 61 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Bảo hành, Giá hiện tại, Mã vạch EAN, Mã HH Liên quan, Đơn vị tính, Tên sản phẩm, Vị trí kệ, Nhom hang, Mô tả chi tiết, Ghi chú, Mẫu ghi chú, Được bán trực tiếp, Mã HH, Loại hàng hóa, Thuộc tính...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Bảo hành": "nan", "Giá hiện tại": "52500", "Mã vạch EAN": "8937586855798", "Mã HH Liên quan": "nan", "Đơn vị tính": "đĩa", "Tên sản phẩm": "Rau muống xào tỏi", "Vị trí kệ": "nan", "Nhom hang": "rau"}
{"Bảo hành": "nan", "Giá hiện tại": "23000", "Mã vạch EAN": "8938254717905", "Mã HH Liên quan": "nan", "Đơn vị tính": "lon", "Tên sản phẩm": "Bia Tiger lon", "Vị trí kệ": "nan", "Nhom hang": "bia"}
{"Bảo hành": "nan", "Giá hiện tại": "79000", "Mã vạch EAN": "8938553854431", "Mã HH Liên quan": "nan", "Đơn vị tính": "đĩa", "Tên sản phẩm": "Cánh gà chiên nước mắm", "Vị trí kệ": "nan", "Nhom hang": "chiên xào"}
```

#### Table `thanh_toan.csv`
- **Rows:** 38,072 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Mã GD, PTTT, Tiền, Mã giao dịch, Thời điểm
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã GD": "PAY000001", "PTTT": "transfer", "Tiền": "149000", "Mã giao dịch": "ORD000001", "Thời điểm": "2025-01-01 07:22:55"}
{"Mã GD": "PAY000002", "PTTT": "cash", "Tiền": "20000", "Mã giao dịch": "ORD000002", "Thời điểm": "2025-01-01 07:37:55"}
{"Mã GD": "PAY000003", "PTTT": "cash", "Tiền": "446000", "Mã giao dịch": "ORD000003", "Thời điểm": "2025-01-01 07:40:48"}
```

---

## Business `biz_130`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu biz_130  File Excel xuất từ phần mềm bán hàng. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng.  ## File - `So_chi_tiet_ban_hang_1.xlsx` (xlsx) - `So_chi_tiet_ban_hang_2.xlsx` (xlsx) - `Danh sách hàng hóa.xlsx` (xlsx)  ## Cột trong `So_chi_tiet_ban_hang_1.xlsx` - **Ngày**: ngày bán - **Mã đơn hàng**: mã đơn - **Tên hàng hóa**: tên hàng - **Đơn vị tính**: đơn vị tính - **Số lượng**: số lượng - **Đơn giá**: đơn giá - **Thành tiền**: thành tiền sau giảm - **
- **Files on disk (4):** Danh sách hàng hóa.xlsx, README.md, So_chi_tiet_ban_hang_1.xlsx, So_chi_tiet_ban_hang_2.xlsx

### Tables / Sheets Detail:
#### Table `Danh sách hàng hóa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (16):** Mã hàng hóa, Mô tả sản phẩm, Bảo hành, Được bán trực tiếp, Loại hàng hóa, Mã HH Liên quan, Mẫu ghi chú, Tên hàng hóa, Nhóm hàng hóa, Thương hiệu, Định mức tồn tối thiểu, Vị trí kệ, Đơn vị tính, Định mức tồn tối đa, Ghi chú...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã hàng hóa": "SP0001", "Mô tả sản phẩm": null, "Bảo hành": null, "Được bán trực tiếp": "1", "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mẫu ghi chú": null, "Tên hàng hóa": "Rau muống xào tỏi"}
{"Mã hàng hóa": "SP0002", "Mô tả sản phẩm": null, "Bảo hành": null, "Được bán trực tiếp": "1", "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mẫu ghi chú": null, "Tên hàng hóa": "Bia Tiger lon"}
{"Mã hàng hóa": "SP0003", "Mô tả sản phẩm": null, "Bảo hành": null, "Được bán trực tiếp": "1", "Loại hàng hóa": "Hàng hóa", "Mã HH Liên quan": null, "Mẫu ghi chú": null, "Tên hàng hóa": "Cánh gà chiên nước mắm"}
```

#### Table `So_chi_tiet_ban_hang_1.xlsx :: Sheet1`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Bia Sài Gòn Special lon", "Đơn vị tính": "lon", "Số lượng": "1", "Đơn giá": "19,000.0000", "Thành tiền": "19,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Mì xào hải sản", "Đơn vị tính": "đĩa", "Số lượng": "2 đĩa", "Đơn giá": "79,000.0000", "Thành tiền": "158,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "01/02/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Đậu hũ chiên giòn", "Đơn vị tính": "đĩa", "Số lượng": "1", "Đơn giá": "49,000.0000", "Thành tiền": "49,000.0000", "Trạng thái": "Đã hoàn thành"}
```

#### Table `So_chi_tiet_ban_hang_2.xlsx :: Sheet1`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "03/01/2026", "Mã đơn hàng": "ORD026603", "Tên hàng hóa": "Trà đá", "Đơn vị tính": "ly", "Số lượng": "1", "Đơn giá": "5,000.0000", "Thành tiền": "5,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "03/01/2026", "Mã đơn hàng": "ORD026603", "Tên hàng hóa": "Bia Tiger lon", "Đơn vị tính": "lon", "Số lượng": "1", "Đơn giá": "24,000.0000", "Thành tiền": "24,000.0000", "Trạng thái": "Đã hoàn thành"}
{"Ngày": "03/01/2026", "Mã đơn hàng": "ORD026603", "Tên hàng hóa": "Cơm chiên hải sản", "Đơn vị tính": "đĩa", "Số lượng": "1 đĩa", "Đơn giá": "79,000.0000", "Thành tiền": "79,000.0000", "Trạng thái": "Đã hoàn thành"}
```

---
