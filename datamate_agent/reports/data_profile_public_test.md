# Data Profile Report: `public_test`
Total Businesses: 14

## Business `dev_001`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu dev_001  File Excel xuất từ phần mềm bán hàng. Sổ chi tiết bán hàng: mỗi dòng một dòng hàng, thông tin đơn lặp lại ở mọi dòng.  ## File - `So_chi_tiet_ban_hang.xlsx` (xlsx) - `Danh sách hàng hóa.xlsx` (xlsx)  ## Cột trong `So_chi_tiet_ban_hang.xlsx` - **Ngày**: ngày bán - **Mã đơn hàng**: mã đơn - **Tên hàng hóa**: tên hàng - **Đơn vị tính**: đơn vị tính - **Số lượng**: số lượng - **Đơn giá**: đơn giá - **Thành tiền**: thành tiền sau giảm - **Trạng thái**: trạng thái đơn - **Số lượng q
- **Files on disk (3):** Danh sách hàng hóa.xlsx, README.md, So_chi_tiet_ban_hang.xlsx

### Tables / Sheets Detail:
#### Table `Danh sách hàng hóa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (19):** Vị trí, Mã hàng hóa, Định mức tồn tối đa, Được bán trực tiếp, Ghi chú, Thuộc tính, Tên hàng hóa, Mã barcode, Mô tả sản phẩm, Mã HH Liên quan, Bảo hành, Nhóm hàng hóa, Đơn vị tính, Trọng lượng, Định mức tồn tối thiểu...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Vị trí": null, "Mã hàng hóa": "SP0001", "Định mức tồn tối đa": "999999999", "Được bán trực tiếp": "1", "Ghi chú": null, "Thuộc tính": null, "Tên hàng hóa": "Coca Cola 330ml", "Mã barcode": "8936254610875"}
{"Vị trí": null, "Mã hàng hóa": "SP0002", "Định mức tồn tối đa": "999999999", "Được bán trực tiếp": "1", "Ghi chú": null, "Thuộc tính": null, "Tên hàng hóa": "Pepsi 330ml", "Mã barcode": "8935497051209"}
{"Vị trí": null, "Mã hàng hóa": "SP0003", "Định mức tồn tối đa": "999999999", "Được bán trực tiếp": "1", "Ghi chú": null, "Thuộc tính": null, "Tên hàng hóa": "Sting dâu 330ml", "Mã barcode": "8938829398904"}
```

#### Table `So_chi_tiet_ban_hang.xlsx :: Sheet1`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (10):** Ngày, Mã đơn hàng, Tên hàng hóa, Đơn vị tính, Số lượng, Đơn giá, Thành tiền, Trạng thái, Số lượng quy đổi, Khách hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/01/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Kẹo cao su Doublemint", "Đơn vị tính": "vỉ", "Số lượng": "3", "Đơn giá": "8,000.0000", "Thành tiền": "24,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/01/2025", "Mã đơn hàng": "ORD000001", "Tên hàng hóa": "Red Bull 250ml", "Đơn vị tính": "lon", "Số lượng": "1 lon", "Đơn giá": "12,000.0000", "Thành tiền": "12,000.0000", "Trạng thái": "đã xong"}
{"Ngày": "01/01/2025", "Mã đơn hàng": "ORD000002", "Tên hàng hóa": "Mì Hảo Hảo tôm chua cay", "Đơn vị tính": "gói", "Số lượng": "1 gói", "Đơn giá": "4,500.0000", "Thành tiền": "4,500.0000", "Trạng thái": "đã xong"}
```

---

## Business `dev_002`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu dev_002  File Excel xuất từ phần mềm bán hàng. File đơn hàng mỗi dòng một sản phẩm, thông tin đơn lặp lại ở mọi dòng của đơn; file này không có mã sản phẩm, nối với các danh sách sản phẩm qua tên sản phẩm. Ngày dạng dd/mm/yyyy.  Dữ liệu bán hàng xuất theo tháng, mỗi tháng một file (tách theo tháng, không theo năm): từ `BanHang_T1_2025.xlsx` đến `BanHang_T5_2026.xlsx` (17 file), các tháng cùng cột; mỗi file có sheet `DonHang_ChiTiet`.  ## File - `BanHang_T<tháng>_<năm>.xlsx` (xlsx) - `D
- **Files on disk (19):** BanHang_T10_2025.xlsx, BanHang_T11_2025.xlsx, BanHang_T12_2025.xlsx, BanHang_T1_2025.xlsx, BanHang_T1_2026.xlsx, BanHang_T2_2025.xlsx, BanHang_T2_2026.xlsx, BanHang_T3_2025.xlsx, BanHang_T3_2026.xlsx, BanHang_T4_2025.xlsx, BanHang_T4_2026.xlsx, BanHang_T5_2025.xlsx, BanHang_T5_2026.xlsx, BanHang_T6_2025.xlsx, BanHang_T7_2025.xlsx, BanHang_T8_2025.xlsx, BanHang_T9_2025.xlsx, DanhSachQuyDoi.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BanHang_T10_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD029551", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "25,000", "Tổng tiền": "25000"}
{"Mã đơn hàng": "ORD029552", "Ngày đặt hàng": "2025-10-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Trần Phương Hương", "Tên sản phẩm": "Bánh tiramisu", "Số lượng sản phẩm": "2", "Giá sản phẩm": "45,000", "Tổng tiền": "90000"}
{"Mã đơn hàng": "ORD029553", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đỗ Hằng Phúc", "Tên sản phẩm": "Cà phê sữa (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "29,000", "Tổng tiền": "29k"}
```

#### Table `BanHang_T11_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD032853", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Trà chanh (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "31,000", "Tổng tiền": "31000"}
{"Mã đơn hàng": "ORD032854", "Ngày đặt hàng": "2025-11-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Cà phê sữa (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "35000", "Tổng tiền": "35000"}
{"Mã đơn hàng": "ORD032855", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Doãn Loan Duy", "Tên sản phẩm": "Cà phê sữa (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "29,000", "Tổng tiền": "29k"}
```

#### Table `BanHang_T12_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD035975", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lưu Đức Huy", "Tên sản phẩm": "Trà chanh (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "31,000", "Tổng tiền": "31000"}
{"Mã đơn hàng": "ORD035976", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Giang Phong Quân", "Tên sản phẩm": "Trà chanh (L)", "Số lượng sản phẩm": "3", "Giá sản phẩm": "31000", "Tổng tiền": "93000"}
{"Mã đơn hàng": "ORD035976", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Giang Phong Quân", "Tên sản phẩm": "Trà sữa trân châu (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "50500", "Tổng tiền": "50500"}
```

#### Table `BanHang_T1_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Trà chanh (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "25000", "Tổng tiền": "25000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Topping Pudding trứng", "Số lượng sản phẩm": "1", "Giá sản phẩm": "10,000", "Tổng tiền": "10.000đ"}
{"Mã đơn hàng": "ORD000003", "Ngày đặt hàng": "2025-01-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Nước ép dưa hấu (M)", "Số lượng sản phẩm": "3 ly", "Giá sản phẩm": "35,000", "Tổng tiền": "105k"}
```

#### Table `BanHang_T1_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD039184", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Đá xay cookie (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "55000", "Tổng tiền": "55k"}
{"Mã đơn hàng": "ORD039184", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "25,000", "Tổng tiền": "25.000đ"}
{"Mã đơn hàng": "ORD039185", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Châu Hùng", "Tên sản phẩm": "Trà vải (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "39000", "Tổng tiền": "39000"}
```

#### Table `BanHang_T2_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD003070", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Latte (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "51,000", "Tổng tiền": "51.000đ"}
{"Mã đơn hàng": "ORD003071", "Ngày đặt hàng": "2025-02-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lý Linh Quang", "Tên sản phẩm": "Cà phê sữa (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "35,000", "Tổng tiền": "35000"}
{"Mã đơn hàng": "ORD003071", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Lý Linh Quang", "Tên sản phẩm": "Sinh tố bơ (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "51000", "Tổng tiền": "51k"}
```

#### Table `BanHang_T2_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD042372", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hoàng Mai Lan", "Tên sản phẩm": "Trà sữa trân châu (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "42,000", "Tổng tiền": "42.000đ"}
{"Mã đơn hàng": "ORD042372", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hoàng Mai Lan", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "2 ly", "Giá sản phẩm": "25000", "Tổng tiền": "50k"}
{"Mã đơn hàng": "ORD042372", "Ngày đặt hàng": "2026-02-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Hoàng Mai Lan", "Tên sản phẩm": "Trà sữa ô long (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "45000", "Tổng tiền": "45000"}
```

#### Table `BanHang_T3_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD005948", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Châu Hùng", "Tên sản phẩm": "Latte (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "45000", "Tổng tiền": "45k"}
{"Mã đơn hàng": "ORD005949", "Ngày đặt hàng": "2025-03-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Trà sữa trân châu (L)", "Số lượng sản phẩm": "2", "Giá sản phẩm": "50,500", "Tổng tiền": "101.000đ"}
{"Mã đơn hàng": "ORD005950", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Quách Khánh Phương", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "25000", "Tổng tiền": "25000"}
```

#### Table `BanHang_T3_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD044646", "Ngày đặt hàng": "2026-03-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Bạc xỉu (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "38000", "Tổng tiền": "38.000đ"}
{"Mã đơn hàng": "ORD044647", "Ngày đặt hàng": "2026-03-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Phạm Châu Thu", "Tên sản phẩm": "Sinh tố bơ (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "53500", "Tổng tiền": "53.500đ"}
{"Mã đơn hàng": "ORD044647", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Phạm Châu Thu", "Tên sản phẩm": "Trà sữa trân châu (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "42,000", "Tổng tiền": "42.000đ"}
```

#### Table `BanHang_T4_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD009498", "Ngày đặt hàng": "2025-04-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Hằng An", "Tên sản phẩm": "Trà đào cam sả (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "39000", "Tổng tiền": "39000"}
{"Mã đơn hàng": "ORD009498", "Ngày đặt hàng": "2025-04-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Hằng An", "Tên sản phẩm": "Nước ép cam (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "45000", "Tổng tiền": "45k"}
{"Mã đơn hàng": "ORD009499", "Ngày đặt hàng": "2025-04-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Dương Hương Cường", "Tên sản phẩm": "Trà sữa trân châu (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "42000", "Tổng tiền": "42000"}
```

#### Table `BanHang_T4_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD047772", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Cà phê sữa (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "29000", "Tổng tiền": "29.000đ"}
{"Mã đơn hàng": "ORD047772", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Trà đào cam sả (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "39,000", "Tổng tiền": "39000"}
{"Mã đơn hàng": "ORD047773", "Ngày đặt hàng": "2026-04-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đàm Thanh Bình", "Tên sản phẩm": "Cold brew (L)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "51,000", "Tổng tiền": "51000"}
```

#### Table `BanHang_T5_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD012874", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Trang Dương", "Tên sản phẩm": "Bánh tiramisu", "Số lượng sản phẩm": "1 cái", "Giá sản phẩm": "45,000", "Tổng tiền": "45.000đ"}
{"Mã đơn hàng": "ORD012874", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Trang Dương", "Tên sản phẩm": "Cà phê muối (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "37,000", "Tổng tiền": "37k"}
{"Mã đơn hàng": "ORD012875", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Vũ Bích Phong", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "2 ly", "Giá sản phẩm": "25,000", "Tổng tiền": "50k"}
```

#### Table `BanHang_T5_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD050741", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Topping Thạch cà phê", "Số lượng sản phẩm": "1 phần", "Giá sản phẩm": "7,000", "Tổng tiền": "7000"}
{"Mã đơn hàng": "ORD050741", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Bánh croissant", "Số lượng sản phẩm": "1", "Giá sản phẩm": "35000", "Tổng tiền": "35k"}
{"Mã đơn hàng": "ORD050742", "Ngày đặt hàng": "2026-05-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Từ Tâm Hương", "Tên sản phẩm": "Trà đào cam sả (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "39000", "Tổng tiền": "39000"}
```

#### Table `BanHang_T6_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD016411", "Ngày đặt hàng": "2025-06-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Cà phê đen (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "31,000", "Tổng tiền": "31.000đ"}
{"Mã đơn hàng": "ORD016412", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Cà phê sữa (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "35,000", "Tổng tiền": "35000"}
{"Mã đơn hàng": "ORD016412", "Ngày đặt hàng": "2025-06-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Trà đào cam sả (L)", "Số lượng sản phẩm": "2 ly", "Giá sản phẩm": "45,000", "Tổng tiền": "90.000đ"}
```

#### Table `BanHang_T7_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD019682", "Ngày đặt hàng": "2025-07-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "1", "Giá sản phẩm": "25000", "Tổng tiền": "25k"}
{"Mã đơn hàng": "ORD019683", "Ngày đặt hàng": "2025-07-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Hồng trà sữa (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "45,000", "Tổng tiền": "45000"}
{"Mã đơn hàng": "ORD019684", "Ngày đặt hàng": "2025-07-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "kl", "Tên sản phẩm": "Cold  brew (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "51000", "Tổng tiền": "51k"}
```

#### Table `BanHang_T8_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD022979", "Ngày đặt hàng": "2025-08-01 00:00:00", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Hồng trà sữa (L)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "45000", "Tổng tiền": "45.000đ"}
{"Mã đơn hàng": "ORD022979", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Bạc Xỉu (m)", "Số lượng sản phẩm": "2 ly", "Giá sản phẩm": "32000", "Tổng tiền": "64000"}
{"Mã đơn hàng": "ORD022980", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Cà phê đen (M)", "Số lượng sản phẩm": "1 ly", "Giá sản phẩm": "25,000", "Tổng tiền": "25k"}
```

#### Table `BanHang_T9_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD026390", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đỗ Chi Hằng", "Tên sản phẩm": "Topping Kem cheese", "Số lượng sản phẩm": "1", "Giá sản phẩm": "12000", "Tổng tiền": "12.000đ"}
{"Mã đơn hàng": "ORD026390", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Đỗ Chi Hằng", "Tên sản phẩm": "Cappuccino (L)", "Số lượng sản phẩm": "2", "Giá sản phẩm": "51,000", "Tổng tiền": "102000"}
{"Mã đơn hàng": "ORD026391", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "Đã hoàn thành", "Tên khách hàng": "Tạ Tâm Hạnh", "Tên sản phẩm": "Cà phê sữa (M)", "Số lượng sản phẩm": "2 ly", "Giá sản phẩm": "29000", "Tổng tiền": "58k"}
```

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

---

## Business `dev_003`
- **Structure Archetype:** Multi-file Partitioned / Monthly Log (2 time-sliced files)
- **README (truncated 500 chars):** # Dữ liệu dev_003  Chủ tiệm gửi dữ liệu từ bốn nguồn: file Excel xuất từ phần mềm bán hàng (tên file bắt đầu BanHang_), sổ chủ tiệm tự ghi trên Excel (SoTay_), file tồn kho CSV, và báo cáo tiền mặt theo ca. Các file nối với nhau qua mã hoá đơn, mã hàng; sổ tay không có mã hàng, nối qua tên hàng. Tên cột mỗi file đặt theo cách của tiệm.  Hóa đơn và chi tiết hóa đơn gộp chung sheet `BanHang`: mỗi dòng là một dòng hàng, thông tin hóa đơn lặp lại trên mọi dòng của cùng hóa đơn. Cột **SĐT** lấy theo
- **Files on disk (8):** BanHang_PhieuThu.xlsx, BanHang_TongHop_2025.xlsx, BanHang_TongHop_2026.xlsx, BaoCaoCa.xlsx, README.md, SoTay_ChiPhi.xlsx, SoTay_NhapHang.xlsx, ton_kho.csv

### Tables / Sheets Detail:
#### Table `BanHang_PhieuThu.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** PTTT, Mã thanh toán, Ngày TT, Ma don, Tiền thu
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"PTTT": "Ví điện tử", "Mã thanh toán": "PAY000001", "Ngày TT": "2025-03-01 06:02:07", "Ma don": "ORD000001", "Tiền thu": "84,000"}
{"PTTT": "Tiền mặt", "Mã thanh toán": "PAY000002", "Ngày TT": "2025-03-01 06:05:28", "Ma don": " ORD000002", "Tiền thu": "90,000"}
{"PTTT": "Tiền mặt", "Mã thanh toán": "PAY000003", "Ngày TT": "2025-03-01 06:08:43", "Ma don": "ORD000003", "Tiền thu": "100,000"}
```

#### Table `BanHang_TongHop_2025.xlsx :: BanHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (26):** Đơn số, Phí ship, Công nợ, Tiền hàng trước giảm, Nguồn, Tiền giảm, Tổng thanh toán, Mã NV bán, Da tra, Ngày HĐ, Trạng thái giao, Giờ tạo đơn, Khách hàng (tên), Mã khách, Hình thức thanh toán...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn số": "ORD000001", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "84,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "84,000", "Mã NV bán": "NV002"}
{"Đơn số": "ORD000001", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "84,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "84,000", "Mã NV bán": "NV002"}
{"Đơn số": "ORD000002", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "90,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "90,000", "Mã NV bán": "NV002"}
```

#### Table `BanHang_TongHop_2025.xlsx :: BanHang_HangHoa`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Thuộc tính, Trọng lượng, Nhóm hàng, Giá lẻ, Mã H.hóa, Được bán trực tiếp, Giá vốn hiện tại, Hình ảnh (url1,url2...), DVT, Bảo hành, Mô tả sản phẩm, Loại hàng hóa, Tồn lớn nhất, Định mức tồn tối thiểu, Vị trí kệ...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Thuộc tính": null, "Trọng lượng": null, "Nhóm hàng": "cà phê", "Giá lẻ": "25000", "Mã H.hóa": "SP0001", "Được bán trực tiếp": "1", "Giá vốn hiện tại": "6902", "Hình ảnh (url1,url2...)": null}
{"Thuộc tính": null, "Trọng lượng": null, "Nhóm hàng": "cà phê", "Giá lẻ": "31000", "Mã H.hóa": "SP0002", "Được bán trực tiếp": "1", "Giá vốn hiện tại": "9112", "Hình ảnh (url1,url2...)": null}
{"Thuộc tính": null, "Trọng lượng": null, "Nhóm hàng": "cà phê", "Giá lẻ": "30500", "Mã H.hóa": "SP0003", "Được bán trực tiếp": "1", "Giá vốn hiện tại": "8905", "Hình ảnh (url1,url2...)": null}
```

#### Table `BanHang_TongHop_2025.xlsx :: BanHang_KhachHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Người tạo, Email, SĐT, Địa chỉ, Khách hàng mua, Đối tượng KH, Ghi chú, Mã KH mua, MST, Kiểu khách, Tổng điểm, CCCD, Điểm hiện tại, Sinh nhật, Trạng thái...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Người tạo": "admin", "Email": null, "SĐT": "974532329", "Địa chỉ": "366 Hồng Bàng", "Khách hàng mua": "Diệp Hạnh Hương - 0974 532 329", "Đối tượng KH": "Cá nhân", "Ghi chú": null, "Mã KH mua": "KH0001"}
{"Người tạo": "admin", "Email": null, "SĐT": "0352233328", "Địa chỉ": "470 Tỉnh Lộ 10", "Khách hàng mua": "Mai Giang Hiếu", "Đối tượng KH": "Cá nhân", "Ghi chú": null, "Mã KH mua": "KH0002"}
{"Người tạo": "admin", "Email": null, "SĐT": "0902768534", "Địa chỉ": "413 Nguyễn Tất Thành", "Khách hàng mua": "Đàm Mai Duy (0902768534)", "Đối tượng KH": "Cá nhân", "Ghi chú": null, "Mã KH mua": "KH0003"}
```

#### Table `BanHang_TongHop_2025.xlsx :: BanHang_DonViQuyDoi`
- **Rows:** 2 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Giá bán theo đơn vị quy đổi, Mã vạch, Bằng, Quy cách
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá bán theo đơn vị quy đổi": "210000", "Mã vạch": "SP0049", "Bằng": "6", "Quy cách": "hộp"}
{"Giá bán theo đơn vị quy đổi": "282000", "Mã vạch": "SP0050", "Bằng": "6", "Quy cách": "hộp"}
```

#### Table `BanHang_TongHop_2025.xlsx :: BanHang_LichSuGia`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Giá cũ, Item, Mã H.hóa, Ngày áp dụng, Giá mới
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá cũ": null, "Item": "Cà phê đen (M)", "Mã H.hóa": "SP0001", "Ngày áp dụng": "2025-03-01 00:00:00", "Giá mới": "25000"}
{"Giá cũ": null, "Item": "Cà phê đen (L)", "Mã H.hóa": "SP0002", "Ngày áp dụng": "2025-03-01 00:00:00", "Giá mới": "31000"}
{"Giá cũ": null, "Item": "Cà phê sữa (M)", "Mã H.hóa": "SP0003", "Ngày áp dụng": "2025-03-01 00:00:00", "Giá mới": "29000"}
```

#### Table `BanHang_TongHop_2026.xlsx :: BanHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (26):** Đơn số, Phí ship, Công nợ, Tiền hàng trước giảm, Nguồn, Tiền giảm, Tổng thanh toán, Mã NV bán, Da tra, Ngày HĐ, Trạng thái giao, Giờ tạo đơn, Khách hàng (tên), Mã khách, Hình thức thanh toán...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn số": "ORD034403", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "37,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "37,000", "Mã NV bán": "NV003"}
{"Đơn số": "ORD034404", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "35,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "35,000", "Mã NV bán": "NV003"}
{"Đơn số": "ORD034405", "Phí ship": "0", "Công nợ": "0", "Tiền hàng trước giảm": "121,000", "Nguồn": "store", "Tiền giảm": "0", "Tổng thanh toán": "121,000", "Mã NV bán": "NV003"}
```

#### Table `BaoCaoCa.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Ca, Mã NV, Tiền mặt thu, Tiền mặt hoàn khách, Tiền mặt ròng của ca
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "2025-03-01 00:00:00", "Ca": "sáng", "Mã NV": "NV002", "Tiền mặt thu": "2403000", "Tiền mặt hoàn khách": "0", "Tiền mặt ròng của ca": "2403000"}
{"Ngày": "2025-03-01 00:00:00", "Ca": "chiều", "Mã NV": "NV003", "Tiền mặt thu": "1719000", "Tiền mặt hoàn khách": "0", "Tiền mặt ròng của ca": "1719000"}
{"Ngày": "2025-03-02 00:00:00", "Ca": "sáng", "Mã NV": "NV003", "Tiền mặt thu": "2548000", "Tiền mặt hoàn khách": "0", "Tiền mặt ròng của ca": "2548000"}
```

#### Table `SoTay_ChiPhi.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (4):** Ngày mua, Lưu ý, Tiền chi, Nhóm
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày mua": "45717", "Lưu ý": null, "Tiền chi": "50000k", "Nhóm": "thuê"}
{"Ngày mua": "05/03/2025", "Lưu ý": null, "Tiền chi": "11,067tr", "Nhóm": "điện"}
{"Ngày mua": "45721", "Lưu ý": null, "Tiền chi": "1,976tr", "Nhóm": "nước"}
```

#### Table `SoTay_NhapHang.xlsx :: Sheet1`
- **Rows:** 12 | **Header Row Index:** 2 | **Subtotal Keywords Detected:** No
- **Columns (9):** Số phiếu, Product, Nhà cung cấp, Thành tiền, Lưu ý, Giá nhập, SL nhập, ĐVT nhập, Ngày nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số phiếu": "PN00001", "Product": "Cà phê đen (M)", "Nhà cung cấp": "Cty Đàm Phương", "Thành tiền": "1386k", "Lưu ý": "nhập đầu kỳ", "Giá nhập": "7.000đ", "SL nhập": "198", "ĐVT nhập": "ly"}
{"Số phiếu": "PN00001", "Product": "Cà phê đen (L)", "Nhà cung cấp": "Cty Đàm Phương", "Thành tiền": "900.900đ", "Lưu ý": "nhập đầu kỳ", "Giá nhập": "9.100đ", "SL nhập": "99", "ĐVT nhập": "ly"}
{"Số phiếu": "PN00001", "Product": "Cà phê sữa (M)", "Nhà cung cấp": "Cty Đàm Phương", "Thành tiền": "2.148.900đ", "Lưu ý": "nhập đầu kỳ", "Giá nhập": "8.700đ", "SL nhập": "247", "ĐVT nhập": "ly"}
```

#### Table `ton_kho.csv`
- **Rows:** 50 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Ton kho, ma_sp, ten_hang, ĐVT
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* ['ma_sp']
- **Sample 3 rows:**
```json
{"Ton kho": "176", "ma_sp": "SP0001", "ten_hang": "Cà phê đen (M)", "ĐVT": "ly"}
{"Ton kho": "66", "ma_sp": "SP0002", "ten_hang": "Cà phê đen (L)", "ĐVT": "ly"}
{"Ton kho": "160", "ma_sp": "SP0003", "ten_hang": "Cà phê sữa (M)", "ĐVT": "ly"}
```

---

## Business `dev_004`
- **Structure Archetype:** Multi-table Relational (24 tables)
- **README (truncated 500 chars):** # Dữ liệu dev_004  Sổ bán hàng ghi tay chuyển sang Excel, mỗi tháng một sheet.  ## File - `SoBanHang.xlsx` (xlsx) - `DanhMuc.xlsx` (xlsx) - `TonKho.xlsx` (xlsx) - `SoGiaoHang.xlsx` (xlsx) - `SoHanNo.xlsx` (xlsx) - `SoNhapHang.xlsx` (xlsx) - `BangGia.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **Khách hàng (tên)**: tên khách (Khách lẻ nếu không lưu) - **Giờ**: giờ đặt đơn (dòng trả hàng: lúc trả) - **Thời gian**: ngày bán - **Ma don**: mã đơn - **SL bán**: số lượng - **dvt**: đơn vị tính - **Hà
- **Files on disk (8):** BangGia.xlsx, DanhMuc.xlsx, README.md, SoBanHang.xlsx, SoGiaoHang.xlsx, SoHanNo.xlsx, SoNhapHang.xlsx, TonKho.xlsx

### Tables / Sheets Detail:
#### Table `BangGia.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Giá cũ, Ngày áp dụng, Giá mới, Diễn giải
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá cũ": null, "Ngày áp dụng": "1 thg 1 2025", "Giá mới": "105k", "Diễn giải": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Giá cũ": "105.000đ", "Ngày áp dụng": "23/07/2025", "Giá mới": "110.000đ", "Diễn giải": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Giá cũ": null, "Ngày áp dụng": "01/01/2025", "Giá mới": "100k", "Diễn giải": "Xi măng INSEE Power-S bao 50kg"}
```

#### Table `DanhMuc.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Hàng, Hệ số, ĐV gốc, Loại ĐV
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Xi măng Hà Tiên PCB40 bao 50kg", "Hệ số": "20", "ĐV gốc": "bao", "Loại ĐV": "tấn"}
{"Hàng": "Xi măng INSEE Power-S bao 50kg", "Hệ số": "20", "ĐV gốc": "bao", "Loại ĐV": "tấn"}
{"Hàng": "Cát xây tô", "Hệ số": "4", "ĐV gốc": "m3", "Loại ĐV": "xe 4m3"}
```

#### Table `SoBanHang.xlsx :: T01-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "lẻ", "col_1": "2025-01-01 06:09:24", "col_2": "1/1", "col_3": "ORD000001", "Hàng": "2 cái", "col_5": "cái", "col_6": "Bóng LED bulb Rạng Đông A60 9W", "Tiền": "Đã hoàn thành"}
{"Đơn": null, "col_1": "2025-01-01 06:09:24", "col_2": null, "col_3": null, "Hàng": "5 viên", "col_5": "viên", "col_6": "Gạch thẻ đặc 4x8x18", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T02-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "kl", "col_1": "2025-02-01 06:38:06", "col_2": "1 thg 2 2025", "col_3": "ORD000821", "Hàng": "3 m", "col_5": "m", "col_6": "Lưới B40 mạ kẽm khổ 1.5m", "Tiền": "Hoàn thành"}
{"Đơn": null, "col_1": "2025-02-01 06:38:06", "col_2": null, "col_3": null, "Hàng": "3", "col_5": "bình", "col_6": "Nước khoáng Lavie 19L", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T03-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "lẻ", "col_1": "2025-03-01 06:16:49", "col_2": "1 thg 3 2025", "col_3": "ORD001541", "Hàng": "1", "col_5": "thùng", "col_6": "Sơn Maxilite trong nhà 18L", "Tiền": "đã xong"}
{"Đơn": "kl", "col_1": "2025-03-01 06:42:52", "col_2": "1/3", "col_3": "ORD001542", "Hàng": "10 cây", "col_5": "cây", "col_6": "Thép hộp 40x80 dày 1.4mm cây 6m", "Tiền": "Đã hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T04-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "lẻ", "col_1": "2025-04-01 06:04:59", "col_2": "01/04/2025", "col_3": "ORD002461", "Hàng": "1", "col_5": "bình", "col_6": "Nước tinh khiết Vihawa 20L", "Tiền": "Đã hoàn thành"}
{"Đơn": "Giang Bảo Thảo", "col_1": "2025-04-01 06:28:46", "col_2": "01/04/2025", "col_3": "ORD002462", "Hàng": "2", "col_5": "m3", "col_6": "Cát bê tông", "Tiền": "đã xong"}
```

#### Table `SoBanHang.xlsx :: T05-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Tăng Châu Loan", "col_1": "2025-05-01 06:20:53", "col_2": "1 thg 5 2025", "col_3": "ORD003358", "Hàng": "10", "col_5": "bao", "col_6": "Xi măng Hà Tiên PCB40 bao 50kg", "Tiền": "Đã hoàn thành"}
{"Đơn": "Khách lẻ", "col_1": "2025-05-01 07:06:06", "col_2": "45778", "col_3": "ORD003359", "Hàng": "2", "col_5": "bình", "col_6": "Nước kiềm Ion Life 19L", "Tiền": "Hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T06-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Hà Quang Dương", "col_1": "2025-06-01 12:44:45", "col_2": "1/6", "col_3": "ORD004182", "Hàng": "-1", "col_5": "bình", "col_6": "Nước tinh khiết Vihawa 20L", "Tiền": "hàng trả về"}
{"Đơn": "Khách lẻ", "col_1": "2025-06-01 06:30:25", "col_2": "1 thg 6 2025", "col_3": "ORD004281", "Hàng": "1", "col_5": "cây", "col_6": "Thep Pomina D10 cay 11.7m", "Tiền": "Đã hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T07-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Hà Hoa Huy", "col_1": "2025-07-01 06:06:10", "col_2": "01/07/2025", "col_3": "ORD005110", "Hàng": "10", "col_5": "bao", "col_6": "Xi măng Hà Tiên PCB40 bao 50kg", "Tiền": "Hoàn thành"}
{"Đơn": null, "col_1": "2025-07-01 06:06:10", "col_2": null, "col_3": null, "Hàng": "1", "col_5": "cuộn", "col_6": "Dây điện Cadivi CV 2.5 cuộn 100m", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T08-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Vương Ngọc Huy", "col_1": "2025-08-01 06:14:41", "col_2": "1/8", "col_3": "ORD006015", "Hàng": "1 m3", "col_5": "m3", "col_6": "Cát san lấp", "Tiền": "đã xong"}
{"Đơn": "Cao Mai Hùng", "col_1": "2025-08-01 07:00:06", "col_2": "45870", "col_3": "ORD006016", "Hàng": "5", "col_5": "viên", "col_6": "Ngói Đồng Nai 22 viên/m2", "Tiền": "Hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T09-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Khách lẻ", "col_1": "2025-09-01 06:21:23", "col_2": "1/9", "col_3": "ORD006916", "Hàng": "1", "col_5": "gói", "col_6": "Keo chà ron Weber 1kg", "Tiền": "đã xong"}
{"Đơn": null, "col_1": "2025-09-01 06:21:23", "col_2": null, "col_3": null, "Hàng": "1", "col_5": "bình", "col_6": "Nước khoáng Lavie 19L", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T10-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Nguyễn Hồng Huy", "col_1": "2025-10-01 06:38:56", "col_2": "01/10/2025", "col_3": "ORD007767", "Hàng": "1 cây", "col_5": "cây", "col_6": "Thép hộp 40x80 dày 1.4mm cây 6m", "Tiền": "Đã hoàn thành"}
{"Đơn": null, "col_1": "2025-10-01 06:38:56", "col_2": null, "col_3": null, "Hàng": "1 bao", "col_5": "bao", "col_6": "Xi măng Hà Tiên PCB40 bao 50kg", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T11-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Triệu Hồng Duy", "col_1": "2025-11-01 06:08:50", "col_2": "1/11", "col_3": "ORD008628", "Hàng": "2", "col_5": "thùng", "col_6": "Gạch ốp tường Viglacera 30x60 thùng 8 vi", "Tiền": "Đã hoàn thành"}
{"Đơn": "Trần Loan Chi", "col_1": "2025-11-01 06:27:36", "col_2": "45962", "col_3": "ORD008629", "Hàng": "1", "col_5": "cây", "col_6": "Ống luồn dây điện Sino SP D20 cây 2.92m", "Tiền": "Hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T12-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Tống Hải Quang", "col_1": "2025-12-01 06:56:22", "col_2": "01/12/2025", "col_3": "ORD009454", "Hàng": "1 thùng", "col_5": "thùng", "col_6": "Gạch ốp tường Viglacera 30x60 thùng 8 vi", "Tiền": "Huỷ đơn"}
{"Đơn": null, "col_1": "2025-12-01 06:56:22", "col_2": null, "col_3": null, "Hàng": "2", "col_5": "thùng", "col_6": "Gạch lát nền Prime 60x60 thùng 4 viên", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T01-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Đặng Thanh Hạnh", "col_1": "2026-01-01 06:22:08", "col_2": "46023", "col_3": "ORD010387", "Hàng": "5 bao", "col_5": "bao", "col_6": "Xi măng INSEE Power-S bao 50kg", "Tiền": "đã xong"}
{"Đơn": "Triệu Minh Khánh", "col_1": "2026-01-01 07:14:42", "col_2": "01/01/2026", "col_3": "ORD010388", "Hàng": "1 thùng", "col_5": "thùng", "col_6": "Chống thấm Kova CT-11A tường 20kg", "Tiền": "Đã hoàn thành"}
```

#### Table `SoBanHang.xlsx :: T02-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Chung Hồng Dương", "col_1": "2026-02-01 07:41:45", "col_2": "1 thg 2 2026", "col_3": "ORD011232", "Hàng": "1", "col_5": "cuộn 10m", "col_6": "Lưới B40 mạ kẽm khổ 1.5m", "Tiền": "đã xong"}
{"Đơn": null, "col_1": "2026-02-01 07:41:45", "col_2": null, "col_3": null, "Hàng": "1", "col_5": "viên", "col_6": "Gạch thẻ đặc 4x8x18", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T03-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Kiều Hùng Quân", "col_1": "2026-03-01 07:02:34", "col_2": "01/03/2026", "col_3": "ORD011788", "Hàng": "1", "col_5": "m", "col_6": "Lưới B40 mạ kẽm khổ 1.5m", "Tiền": "Hoàn thành"}
{"Đơn": null, "col_1": "2026-03-01 07:02:34", "col_2": null, "col_3": null, "Hàng": "1", "col_5": "m2", "col_6": "Bạt xanh cam khổ 4m", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T04-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "khách lẻ", "col_1": "2026-04-01 06:20:28", "col_2": "1 thg 4 2026", "col_3": "ORD012627", "Hàng": "5", "col_5": "bao", "col_6": "Xi măng INSEE Power-S bao 50kg", "Tiền": "Đã hoàn thành"}
{"Đơn": "Từ Thanh Long", "col_1": "2026-04-01 06:25:52", "col_2": "1 thg 4 2026", "col_3": "ORD012628", "Hàng": "2 bình", "col_5": "bình", "col_6": "Gas Petrolimex 12kg", "Tiền": "đã xong"}
```

#### Table `SoBanHang.xlsx :: T05-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Hoàng Cường Giang", "col_1": "2026-05-01 07:34:59", "col_2": "46143", "col_3": "ORD013534", "Hàng": "3", "col_5": "m3", "col_6": "Đá mi bụi", "Tiền": "Hoàn thành"}
{"Đơn": null, "col_1": "2026-05-01 07:34:59", "col_2": null, "col_3": null, "Hàng": "3 viên", "col_5": "viên", "col_6": "Gạch ống 8x8x18 Tuynel", "Tiền": null}
```

#### Table `SoBanHang.xlsx :: T06-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** Yes
- **Columns (11):** Đơn, col_1, col_2, col_3, Hàng, col_5, col_6, Tiền, col_8, col_9, col_10
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Đơn": "Khách hàng (tên)", "col_1": "Giờ", "col_2": "Thời gian", "col_3": "Ma don", "Hàng": "SL bán", "col_5": "dvt", "col_6": "Hàng bán", "Tiền": "Trạng thái xử lý"}
{"Đơn": "Bạch Hoa Cường", "col_1": "2026-06-01 06:07:46", "col_2": "46174", "col_3": "ORD014383", "Hàng": "3", "col_5": "viên", "col_6": "Gạch ống 8x8x18 Tuynel", "Tiền": "đã xong"}
{"Đơn": null, "col_1": "2026-06-01 06:07:46", "col_2": null, "col_3": null, "Hàng": "1 bao", "col_5": "bao", "col_6": "Xi măng Hà Tiên PCB40 bao 50kg", "Tiền": null}
```

#### Table `SoGiaoHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Số lượng giao, Biển số xe, Lượt giao, Số đơn, Thời gian giao, Hàng hóa, Lái xe, ĐV gốc
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Số lượng giao": "2", "Biển số xe": "51D-479.21", "Lượt giao": "1", "Số đơn": "ORD000001", "Thời gian giao": "2025-01-02 00:00:00", "Hàng hóa": "Bóng LED bulb Rạng Đông A60 9W", "Lái xe": "Huỳnh Đạt", "ĐV gốc": "cái"}
{"Số lượng giao": "5", "Biển số xe": "51D-479.21", "Lượt giao": "1", "Số đơn": "ORD000001", "Thời gian giao": "2025-01-02 00:00:00", "Hàng hóa": "Gạch thẻ đặc 4x8x18", "Lái xe": "Huỳnh Đạt", "ĐV gốc": "viên"}
{"Số lượng giao": "1", "Biển số xe": "51D-479.21", "Lượt giao": "1", "Số đơn": "ORD000001", "Thời gian giao": "2025-01-02 00:00:00", "Hàng hóa": "Sơn Maxilite trong nhà 18L", "Lái xe": "Huỳnh Đạt", "ĐV gốc": "thùng"}
```

#### Table `SoHanNo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Mã đơn hàng, Kỳ hạn, Ngày phải trả
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000002", "Kỳ hạn": "30", "Ngày phải trả": "2025-01-31 00:00:00"}
{"Mã đơn hàng": "ORD000013", "Kỳ hạn": "60", "Ngày phải trả": "2025-03-02 00:00:00"}
{"Mã đơn hàng": "ORD000033", "Kỳ hạn": "30", "Ngày phải trả": "2025-02-01 00:00:00"}
```

#### Table `SoNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Product, ĐVT, Số phiếu, Ghi chú, Nhà cung cấp, Thành tiền, Giá nhập, Ngày nhập, SL nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Product": "Xi măng Hà Tiên PCB40 bao 50kg", "ĐVT": "tấn", "Số phiếu": "PN00001", "Ghi chú": "nhập đầu kỳ", "Nhà cung cấp": "Cty Triệu Hương", "Thành tiền": "18400k", "Giá nhập": "1840k", "Ngày nhập": "1 thg 1 2025"}
{"Product": "Xi măng INSEE Power-S bao 50kg", "ĐVT": "tấn", "Số phiếu": "PN00001", "Ghi chú": "nhập đầu kỳ", "Nhà cung cấp": "Cty Triệu Hương", "Thành tiền": "12tr460", "Giá nhập": "1tr780", "Ngày nhập": "1 thg 1 2025"}
{"Product": "Cát xây tô", "ĐVT": "xe 4m3", "Số phiếu": "PN00001", "Ghi chú": "nhập đầu kỳ", "Nhà cung cấp": "Cty Triệu Hương", "Thành tiền": "36tr936", "Giá nhập": "972k", "Ngày nhập": "1 thg 1 2025"}
```

#### Table `TonKho.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Tồn cuối, ĐV gốc, Tên sản phẩm
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tồn cuối": "56", "ĐV gốc": "bao", "Tên sản phẩm": "Xi măng Hà Tiên PCB40 bao 50kg"}
{"Tồn cuối": "136", "ĐV gốc": "bao", "Tên sản phẩm": "Xi măng INSEE Power-S bao 50kg"}
{"Tồn cuối": "135", "ĐV gốc": "m3", "Tên sản phẩm": "Cát xây tô"}
```

---

## Business `dev_005`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu dev_005  File Excel xuất từ phần mềm bán hàng. File đơn hàng mỗi dòng một sản phẩm.  Dữ liệu bán hàng xuất theo tháng, mỗi tháng một file (tách theo tháng, không theo năm): từ `BanHang_Thang01_2025.xlsx` đến `BanHang_Thang05_2026.xlsx` (17 file), các tháng cùng cột; mỗi file có sheet `DonHang_ChiTiet`.  ## File - `BanHang_Thang<tháng>_<năm>.xlsx` (xlsx) - `DanhSachQuyDoi.xlsx` (xlsx) - `DanhSachSanPham.xlsx` (xlsx) - `DonNhapHang.xlsx` (xlsx) - `DonNhapHang_ChiTiet.xlsx` (xlsx) - `DonH
- **Files on disk (24):** BanHang_Thang01_2025.xlsx, BanHang_Thang01_2026.xlsx, BanHang_Thang02_2025.xlsx, BanHang_Thang02_2026.xlsx, BanHang_Thang03_2025.xlsx, BanHang_Thang03_2026.xlsx, BanHang_Thang04_2025.xlsx, BanHang_Thang04_2026.xlsx, BanHang_Thang05_2025.xlsx, BanHang_Thang05_2026.xlsx, BanHang_Thang06_2025.xlsx, BanHang_Thang07_2025.xlsx, BanHang_Thang08_2025.xlsx, BanHang_Thang09_2025.xlsx, BanHang_Thang10_2025.xlsx, BanHang_Thang11_2025.xlsx, BanHang_Thang12_2025.xlsx, DanhSachQuyDoi.xlsx, DanhSachSanPham.xlsx, DanhSachThuoc.xlsx, DonHang_Lo.xlsx, DonNhapHang.xlsx, DonNhapHang_ChiTiet.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BanHang_Thang01_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Acyclovir Stella kem 5% tuýp 5g", "Số lượng sản phẩm": "1 tuýp", "Giá sản phẩm": "17,000", "Tổng tiền": "17000"}
{"Mã đơn hàng": "ORD000002", "Ngày đặt hàng": "01/01/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Salonpas cao dán hộp 24 gói x 10 miếng", "Số lượng sản phẩm": "1", "Giá sản phẩm": "14500", "Tổng tiền": "14500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Nature's Bounty Vitamin E 400 IU chai 30", "Số lượng sản phẩm": "2", "Giá sản phẩm": "165,000", "Tổng tiền": "330000"}
```

#### Table `BanHang_Thang01_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD029498", "Ngày đặt hàng": "01/01/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Đinh Thảo Hương", "Tên sản phẩm": "Băng cá nhân Urgo Transparent hộp 100 mi", "Số lượng sản phẩm": "1", "Giá sản phẩm": "80,000", "Tổng tiền": "80,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Siro ho Bổ phế Nam Hà Chỉ Khái Lộ chai 1", "Số lượng sản phẩm": "1", "Giá sản phẩm": "55000", "Tổng tiền": "55,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Otrivin 0,1% xịt mũi chai 10ml", "Số lượng sản phẩm": "2 chai", "Giá sản phẩm": "58,000", "Tổng tiền": "116000"}
```

#### Table `BanHang_Thang02_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD002634", "Ngày đặt hàng": "01/02/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Diệp Hoa Tâm", "Tên sản phẩm": "Fugacar 500mg hộp 1 viên", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "22,000", "Tổng tiền": "22,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Phosphalugel hộp 26 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "122200", "Tổng tiền": "122200"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Magne-B6 Corbière hộp 5 vỉ x 10 viên", "Số lượng sản phẩm": "10 viên", "Giá sản phẩm": "2100", "Tổng tiền": "21,000"}
```

#### Table `BanHang_Thang02_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD032127", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Nurofen for Children hỗn dịch chai 60ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "60,000", "Tổng tiền": "60,000"}
{"Mã đơn hàng": "ORD032128", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Cao Hằng Thắng", "Tên sản phẩm": "Otrivin 0,1% xịt mũi chai 10ml", "Số lượng sản phẩm": "3", "Giá sản phẩm": "58000", "Tổng tiền": "174,000"}
{"Mã đơn hàng": "ORD032129", "Ngày đặt hàng": "01/02/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Giang Hiếu Tâm", "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "10", "Giá sản phẩm": "5300", "Tổng tiền": "53000"}
```

#### Table `BanHang_Thang03_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD004944", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Enterogermina 2 tỷ/5ml hộp 20 ống", "Số lượng sản phẩm": "1", "Giá sản phẩm": "194000", "Tổng tiền": "194,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "106000", "Tổng tiền": "106000"}
{"Mã đơn hàng": "ORD004945", "Ngày đặt hàng": "01/03/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Đinh Loan Tâm", "Tên sản phẩm": "Berberin 100mg Mekophar chai 100 viên", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "800", "Tổng tiền": "800"}
```

#### Table `BanHang_Thang03_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD034446", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Trương Châu Hùng", "Tên sản phẩm": "Smecta hộp 30 gói", "Số lượng sản phẩm": "6", "Giá sản phẩm": "5100", "Tổng tiền": "30600"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Kudos Vitamin C 1000mg viên sủi tuýp 20 ", "Số lượng sản phẩm": "2", "Giá sản phẩm": "132500", "Tổng tiền": "265000"}
{"Mã đơn hàng": "ORD034447", "Ngày đặt hàng": "01/03/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Trần Phúc Dũng", "Tên sản phẩm": "Lorastad 10mg Stella hộp 10 vỉ x 10 viên", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "800", "Tổng tiền": "800"}
```

#### Table `BanHang_Thang04_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD007344", "Ngày đặt hàng": "01/04/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "lẻ", "Tên sản phẩm": "Smecta hộp 30 gói", "Số lượng sản phẩm": "6 gói", "Giá sản phẩm": "5,100", "Tổng tiền": "30,600"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Salonpas cao dán hộp 24 gói x 10 miếng", "Số lượng sản phẩm": "2", "Giá sản phẩm": "14,500", "Tổng tiền": "29000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Kẹo ngậm Bổ phế Nam Hà Candy hộp 10 vỉ x", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "2600", "Tổng tiền": "2600"}
```

#### Table `BanHang_Thang04_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD036968", "Ngày đặt hàng": "01/04/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Ngô Hoàng Khoa", "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Số lượng sản phẩm": "1 vỉ", "Giá sản phẩm": "18,000", "Tổng tiền": "17000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Khẩu trang y tế 4 lớp Khánh An hộp 50 cá", "Số lượng sản phẩm": "1 cái", "Giá sản phẩm": "800", "Tổng tiền": "800"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Amoxicillin 500mg Domesco hộp 10 vỉ x 10", "Số lượng sản phẩm": "1 vỉ", "Giá sản phẩm": "10,000", "Tổng tiền": "10,000"}
```

#### Table `BanHang_Thang05_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD009723", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Đoàn Huy Hải", "Tên sản phẩm": "Efferalgan 500mg viên sủi hộp 4 vỉ x 4 v", "Số lượng sản phẩm": "4", "Giá sản phẩm": "3400", "Tổng tiền": "13600"}
{"Mã đơn hàng": "ORD009724", "Ngày đặt hàng": "01/05/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Đỗ Thảo Huy", "Tên sản phẩm": "Salonpas cao dán hộp 24 gói x 10 miếng", "Số lượng sản phẩm": "1 gói", "Giá sản phẩm": "14,500", "Tổng tiền": "14,500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Cefuroxim 500mg Vidipha hộp 10 vỉ x 10 v", "Số lượng sản phẩm": "10", "Giá sản phẩm": "3,400", "Tổng tiền": "34,000"}
```

#### Table `BanHang_Thang05_2026.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD039461", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Berberin 100mg Mekophar chai 100 viên", "Số lượng sản phẩm": "6 viên", "Giá sản phẩm": "800", "Tổng tiền": "4,800"}
{"Mã đơn hàng": "ORD039462", "Ngày đặt hàng": "01/05/2026", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Hồ Mai Dương", "Tên sản phẩm": "Augmentin 625mg hộp 2 vỉ x 7 viên", "Số lượng sản phẩm": "2 viên", "Giá sản phẩm": "13900", "Tổng tiền": "27800"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Yumangel hộp 20 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "5300", "Tổng tiền": "5,300"}
```

#### Table `BanHang_Thang06_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD012292", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Ông Bích Cường", "Tên sản phẩm": "Siro Tiffy chai 30ml", "Số lượng sản phẩm": "2 chai", "Giá sản phẩm": "16000", "Tổng tiền": "32,000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Clorpheniramin 4mg DHG hộp 10 vỉ x 20 vi", "Số lượng sản phẩm": "1 vỉ", "Giá sản phẩm": "2,000", "Tổng tiền": "2,000"}
{"Mã đơn hàng": "ORD012293", "Ngày đặt hàng": "01/06/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Bio-acimin Gold men vi sinh hộp 30 gói", "Số lượng sản phẩm": "1", "Giá sản phẩm": "159000", "Tổng tiền": "159,000"}
```

#### Table `BanHang_Thang07_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD014739", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "kl", "Tên sản phẩm": "Povidine 10% chai 90ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "18000", "Tổng tiền": "18,000"}
{"Mã đơn hàng": "ORD014740", "Ngày đặt hàng": "01/07/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Siro ho Bổ phế Nam Hà Chỉ Khái Lộ chai 1", "Số lượng sản phẩm": "2", "Giá sản phẩm": "55000", "Tổng tiền": "110000"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Số lượng sản phẩm": "2 viên", "Giá sản phẩm": "1400", "Tổng tiền": "2800"}
```

#### Table `BanHang_Thang08_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD017279", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Efticol 0,9% lốc 10 lọ x 10ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "2,700", "Tổng tiền": "2,700"}
{"Mã đơn hàng": "ORD017280", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "UPSA-C 1g viên sủi tuýp 10 viên", "Số lượng sản phẩm": "2 viên", "Giá sản phẩm": "3,900", "Tổng tiền": "7,800"}
{"Mã đơn hàng": "ORD017281", "Ngày đặt hàng": "01/08/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Clorpheniramin 4mg DHG hộp 10 vỉ x 20 vi", "Số lượng sản phẩm": "1", "Giá sản phẩm": "2000", "Tổng tiền": "2000"}
```

#### Table `BanHang_Thang09_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD019719", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Lương Long Tâm", "Tên sản phẩm": "Phosphalugel hộp 26 gói", "Số lượng sản phẩm": "3 gói", "Giá sản phẩm": "4900", "Tổng tiền": "14,700"}
{"Mã đơn hàng": "ORD019720", "Ngày đặt hàng": "01/09/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "khách lẻ", "Tên sản phẩm": "Prednisolon 5mg Boston chai 500 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "500", "Tổng tiền": "500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Eugica hộp 10 vỉ x 10 viên nang", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "700", "Tổng tiền": "700"}
```

#### Table `BanHang_Thang10_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD022058", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Ngô Anh Bích", "Tên sản phẩm": "Povidine 10% chai 90ml", "Số lượng sản phẩm": "2", "Giá sản phẩm": "18000", "Tổng tiền": "36000"}
{"Mã đơn hàng": "ORD022059", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Khách lẻ", "Tên sản phẩm": "Prospan siro ho chai 100ml", "Số lượng sản phẩm": "1 chai", "Giá sản phẩm": "93,000", "Tổng tiền": "93000"}
{"Mã đơn hàng": "ORD022060", "Ngày đặt hàng": "01/10/2025", "Trạng thái đơn hàng": "ok", "Tên khách hàng": "Tô Ngọc Thu", "Tên sản phẩm": "Savi Losartan 50mg hộp 3 vỉ x 10 viên", "Số lượng sản phẩm": "1 hộp", "Giá sản phẩm": "45000", "Tổng tiền": "45000"}
```

#### Table `BanHang_Thang11_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD024571", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Lâm Châu Đạt", "Tên sản phẩm": "Loperamid 2mg Domesco hộp 5 vỉ x 10 viên", "Số lượng sản phẩm": "1 viên", "Giá sản phẩm": "500", "Tổng tiền": "500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Alaxan hộp 25 vỉ x 4 viên", "Số lượng sản phẩm": "4 viên", "Giá sản phẩm": "1,300", "Tổng tiền": "5,200"}
{"Mã đơn hàng": "ORD024572", "Ngày đặt hàng": "01/11/2025", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Doãn Thu Thu", "Tên sản phẩm": "Efticol 0,9% lốc 10 lọ x 10ml", "Số lượng sản phẩm": "1", "Giá sản phẩm": "27,000", "Tổng tiền": "27,000"}
```

#### Table `BanHang_Thang12_2025.xlsx :: DonHang_ChiTiet`
- **Rows:** 11 | **Header Row Index:** 3 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã đơn hàng, Ngày đặt hàng, Trạng thái đơn hàng, Tên khách hàng, Tên sản phẩm, Số lượng sản phẩm, Giá sản phẩm, Tổng tiền, Đơn vị tính
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD026970", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Quách Hoa Trang", "Tên sản phẩm": "Khẩu trang y tế 4 lớp Khánh An hộp 50 cá", "Số lượng sản phẩm": "2", "Giá sản phẩm": "800", "Tổng tiền": "1600"}
{"Mã đơn hàng": "ORD026971", "Ngày đặt hàng": "01/12/2025", "Trạng thái đơn hàng": "Đã giao", "Tên khách hàng": "Cao Đạt Châu", "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "1,500", "Tổng tiền": "1,500"}
{"Mã đơn hàng": null, "Ngày đặt hàng": null, "Trạng thái đơn hàng": null, "Tên khách hàng": null, "Tên sản phẩm": "Panadol 500mg hộp 10 vỉ x 12 viên", "Số lượng sản phẩm": "1", "Giá sản phẩm": "1000", "Tổng tiền": "1000"}
```

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
{"Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "15 vỉ", "Đơn vị cơ bản": "viên"}
{"Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Đơn vị quy đổi": "hộp", "Tỉ lệ quy đổi": "24", "Đơn vị cơ bản": "gói"}
```

#### Table `DanhSachSanPham.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** Định mức tồn tối thiểu, Mã SKU, Được bán trực tiếp, Ghi chú, Mẫu ghi chú, Bảo hành, Tên sản phẩm, Mã HH Liên quan, Mô tả chi tiết, Thương hiệu, Tồn lớn nhất, Đơn vị, Thuộc tính, Mã vạch EAN, Loại sản phẩm...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Định mức tồn tối thiểu": "0", "Mã SKU": "SP0001", "Được bán trực tiếp": "1", "Ghi chú": null, "Mẫu ghi chú": null, "Bảo hành": null, "Tên sản phẩm": "Panadol Extra hộp 15 vỉ x 12 viên", "Mã HH Liên quan": null}
{"Định mức tồn tối thiểu": "0", "Mã SKU": "SP0002", "Được bán trực tiếp": "1", "Ghi chú": null, "Mẫu ghi chú": null, "Bảo hành": null, "Tên sản phẩm": "Hapacol 250 hộp 24 gói", "Mã HH Liên quan": null}
{"Định mức tồn tối thiểu": "0", "Mã SKU": "SP0003", "Được bán trực tiếp": "1", "Ghi chú": null, "Mẫu ghi chú": null, "Bảo hành": null, "Tên sản phẩm": "Panadol 500mg hộp 10 vỉ x 12 viên", "Mã HH Liên quan": null}
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

#### Table `DonHang_Lo.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Mã đơn hàng, Mã lô, Số lượng, Số lượng trả
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã đơn hàng": "ORD000001", "Mã lô": "N2501227", "Số lượng": "1", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000002", "Mã lô": "O2501732", "Số lượng": "1", "Số lượng trả": "0"}
{"Mã đơn hàng": "ORD000002", "Mã lô": "H2501163", "Số lượng": "2", "Số lượng trả": "0"}
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
{"Mã đơn nhập": "PN00001", "Ngày nhập": "01/01/2025", "Mã nhà cung cấp": "NCC002"}
{"Mã đơn nhập": "PN00002", "Ngày nhập": "04/01/2025", "Mã nhà cung cấp": "NCC004"}
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
{"Mã đơn nhập": "PN00138", "Mã SKU": "SP0001", "Mã lô": "A2505755", "Hạn sử dụng": "14/01/2028", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00108", "Mã SKU": "SP0001", "Mã lô": "B2504662", "Hạn sử dụng": "04/05/2027", "Số lượng nhập": "360"}
{"Mã đơn nhập": "PN00196", "Mã SKU": "SP0001", "Mã lô": "B2507196", "Hạn sử dụng": "08/11/2025", "Số lượng nhập": "360"}
```

---

## Business `dev_006`
- **Structure Archetype:** SQLite Database (17 tables in pos.sqlite)
- **README (truncated 500 chars):** # Dữ liệu dev_006  File máy POS xuất ra.  ## File - `pos.sqlite` (sqlite)  ## Bảng `chi_nhanh`, `nhan_vien`, `khach_hang`, `nha_cung_cap`, `san_pham`, `don_vi_sp`, `phieu_nhap`, `chi_tiet_nhap`, `don_hang`, `chi_tiet_don`, `thanh_toan`, `tra_hang`, `the_kho`, `lich_su_gia`, `lo_hang`, `chi_tiet_don_lo`, `thong_tin_thuoc`  Mã đơn nối `don_hang` với `chi_tiet_don`. Ngày giờ dạng text.  ## Quy ước - Dữ liệu có đến hết 08/08/2026. - **Dòng hàng**: `chi_tiet_don.TriGia` là thành tiền của dòng (đã trừ
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
{"IDCuaHang": "dev_006", "MaChiNhanh": "CN1", "TenGoi": "Nhà thuốc Khánh", "DiaChiLienHe": "334 Quang Trung", "NgayKhaiTruong": "2023-06-28"}
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
{"IDCuaHang": "dev_006", "MaNhanVien": "NV001", "TenGoi": "Võ Trung Hoa", "MaChiNhanh": "CN1", "ChucVu": "owner", "NgayNhanViec": "2023-06-08", "NgayThoiViec": null}
{"IDCuaHang": "dev_006", "MaNhanVien": "NV002", "TenGoi": "Từ Hùng Hằng", "MaChiNhanh": "CN1", "ChucVu": "cashier", "NgayNhanViec": "2024-09-22", "NgayThoiViec": null}
{"IDCuaHang": "dev_006", "MaNhanVien": "NV003", "TenGoi": "Đinh Đạt Đức", "MaChiNhanh": "CN1", "ChucVu": "sales", "NgayNhanViec": "2024-04-03", "NgayThoiViec": null}
```

#### Table `pos.sqlite :: khach_hang`
- **Rows:** 320 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (18):** IDCuaHang, MaKhachHang, TenGoi, trang_thai_kh, tong_diem, diem_hien_tai, loai_hinh_kh, cccd, SoDienThoai, email, ghi_chu_kh, NamNu, LoaiKhachHang, cong_ty, TaoLuc...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* ['trang_thai_kh']
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaKhachHang": "KH0001", "TenGoi": "Đoàn Huy Khoa", "trang_thai_kh": "Đang hoạt động", "tong_diem": "0", "diem_hien_tai": "0", "loai_hinh_kh": "Cá nhân", "cccd": null}
{"IDCuaHang": "dev_006", "MaKhachHang": "KH0002", "TenGoi": "Dương Đạt Lan", "trang_thai_kh": "Đang hoạt động", "tong_diem": "0", "diem_hien_tai": "0", "loai_hinh_kh": "Cá nhân", "cccd": null}
{"IDCuaHang": "dev_006", "MaKhachHang": "KH0003", "TenGoi": "Phùng Mai Khoa", "trang_thai_kh": "Đang hoạt động", "tong_diem": "0", "diem_hien_tai": "0", "loai_hinh_kh": "Cá nhân", "cccd": null}
```

#### Table `pos.sqlite :: nha_cung_cap`
- **Rows:** 5 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** email, IDCuaHang, nhom_ncc, MaNhaCungCap, ma_so_thue, nguoi_tao, trang_thai_ncc, TenGoi, SoDienThoai, DiaChiLienHe
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* ['trang_thai_ncc']
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"email": null, "IDCuaHang": "dev_006", "nhom_ncc": null, "MaNhaCungCap": "NCC001", "ma_so_thue": null, "nguoi_tao": "admin", "trang_thai_ncc": "Đang hoạt động", "TenGoi": "Cty Giang Thanh"}
{"email": null, "IDCuaHang": "dev_006", "nhom_ncc": null, "MaNhaCungCap": "NCC002", "ma_so_thue": null, "nguoi_tao": "admin", "trang_thai_ncc": "Đang hoạt động", "TenGoi": "Cty Diệp Đức"}
{"email": null, "IDCuaHang": "dev_006", "nhom_ncc": null, "MaNhaCungCap": "NCC003", "ma_so_thue": null, "nguoi_tao": "admin", "trang_thai_ncc": "Đang hoạt động", "TenGoi": "Cty Trương Hoa"}
```

#### Table `pos.sqlite :: san_pham`
- **Rows:** 80 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (25):** mo_ta, ghi_chu_hh, IDCuaHang, MaHangHoa, ma_hh_lien_quan, thuoc_tinh, ban_truc_tiep, mau_ghi_chu, vi_tri, trong_luong, ton_nho_nhat, TenGoi, ma_vach_ean, DanhMuc, DonViCoSo...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"mo_ta": null, "ghi_chu_hh": null, "IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "ma_hh_lien_quan": null, "thuoc_tinh": null, "ban_truc_tiep": "1", "mau_ghi_chu": null}
{"mo_ta": null, "ghi_chu_hh": null, "IDCuaHang": "dev_006", "MaHangHoa": "SP0002", "ma_hh_lien_quan": null, "thuoc_tinh": null, "ban_truc_tiep": "1", "mau_ghi_chu": null}
{"mo_ta": null, "ghi_chu_hh": null, "IDCuaHang": "dev_006", "MaHangHoa": "SP0003", "ma_hh_lien_quan": null, "thuoc_tinh": null, "ban_truc_tiep": "1", "mau_ghi_chu": null}
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
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "DonViTinh": "hộp", "HeSoQuyDoi": "180", "GiaDonVi": "270000"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "DonViTinh": "vỉ", "HeSoQuyDoi": "12", "GiaDonVi": "18000"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0002", "DonViTinh": "hộp", "HeSoQuyDoi": "24", "GiaDonVi": "50400"}
```

#### Table `pos.sqlite :: phieu_nhap`
- **Rows:** 494 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** IDCuaHang, MaPhieuNhap, MaNhaCungCap, MaChiNhanh, NgayNhapKho, TinhTrang, TongGiaTriNhap, DienGiai
  - *Date cols:* ['NgayNhapKho']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00001", "MaNhaCungCap": "NCC003", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-04-01", "TinhTrang": "received", "TongGiaTriNhap": "185863400", "DienGiai": "nhập đầu kỳ"}
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00002", "MaNhaCungCap": "NCC003", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-04-02", "TinhTrang": "received", "TongGiaTriNhap": "200000", "DienGiai": null}
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00003", "MaNhaCungCap": "NCC005", "MaChiNhanh": "CN1", "NgayNhapKho": "2025-04-04", "TinhTrang": "received", "TongGiaTriNhap": "415000", "DienGiai": null}
```

#### Table `pos.sqlite :: chi_tiet_nhap`
- **Rows:** 3,234 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** IDCuaHang, MaPhieuNhap, SoThuTu, MaHangHoa, DonViTinh, SL, DonGiaNhap, MaLo, HanSuDung
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00001", "SoThuTu": "1", "MaHangHoa": "SP0001", "DonViTinh": "hộp", "SL": "2", "DonGiaNhap": "198000", "MaLo": "D2504828"}
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00001", "SoThuTu": "2", "MaHangHoa": "SP0002", "DonViTinh": "hộp", "SL": "9", "DonGiaNhap": "38400", "MaLo": "G2504735"}
{"IDCuaHang": "dev_006", "MaPhieuNhap": "PN00001", "SoThuTu": "3", "MaHangHoa": "SP0003", "DonViTinh": "hộp", "SL": "2", "DonGiaNhap": "96000", "MaLo": "M2504926"}
```

#### Table `pos.sqlite :: don_hang`
- **Rows:** 37,833 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (22):** IDCuaHang, MaHoaDon, MaChiNhanh, MaKhachHang, MaNhanVien, MaCaLam, KenhBanHang, ThoiGianLap, NgayLap, TinhTrang, TongTienHang, ChietKhau, PhiVanChuyen, ThueGTGT, TongThanhToan...
  - *Date cols:* ['NgayLap']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000001", "MaChiNhanh": "CN1", "MaKhachHang": null, "MaNhanVien": "NV002", "MaCaLam": "CA202504011", "KenhBanHang": "store", "ThoiGianLap": "2025-04-01 06:00:39"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000002", "MaChiNhanh": "CN1", "MaKhachHang": "KH0210", "MaNhanVien": "NV002", "MaCaLam": "CA202504011", "KenhBanHang": "store", "ThoiGianLap": "2025-04-01 06:19:45"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000003", "MaChiNhanh": "CN1", "MaKhachHang": null, "MaNhanVien": "NV002", "MaCaLam": "CA202504011", "KenhBanHang": "store", "ThoiGianLap": "2025-04-01 07:25:46"}
```

#### Table `pos.sqlite :: chi_tiet_don`
- **Rows:** 72,411 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** IDCuaHang, MaHoaDon, SoThuTu, MaHangHoa, DonViTinh, SL, SLQuyDoi, GiaDonVi, ChietKhau, TriGia, GiaVonLucBan
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000001", "SoThuTu": "1", "MaHangHoa": "SP0074", "DonViTinh": "viên", "SL": "6", "SLQuyDoi": "6", "GiaDonVi": "2600"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000002", "SoThuTu": "1", "MaHangHoa": "SP0013", "DonViTinh": "hộp", "SL": "1", "SLQuyDoi": "16", "GiaDonVi": "51200"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000003", "SoThuTu": "1", "MaHangHoa": "SP0001", "DonViTinh": "viên", "SL": "1", "SLQuyDoi": "1", "GiaDonVi": "1400"}
```

#### Table `pos.sqlite :: thanh_toan`
- **Rows:** 37,939 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaPhieuThu, MaHoaDon, NgayGioThu, SoTienThu, PhuongThuc, DienGiai
  - *Date cols:* ['NgayGioThu']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaPhieuThu": "PAY000001", "MaHoaDon": "ORD000002", "NgayGioThu": "2025-04-01 06:19:45", "SoTienThu": "51.200đ", "PhuongThuc": "cash", "DienGiai": null}
{"IDCuaHang": "dev_006", "MaPhieuThu": "PAY000002", "MaHoaDon": "ORD000003", "NgayGioThu": "2025-04-01 07:25:46", "SoTienThu": "1.400đ", "PhuongThuc": "transfer", "DienGiai": null}
{"IDCuaHang": "dev_006", "MaPhieuThu": "PAY000003", "MaHoaDon": "ORD000004", "NgayGioThu": "2025-04-01 07:28:36", "SoTienThu": "41.400đ", "PhuongThuc": "transfer", "DienGiai": null}
```

#### Table `pos.sqlite :: tra_hang`
- **Rows:** 352 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaPhieuTra, MaHoaDon, NgayGioTra, NguyenNhan, TienHoanTra, CachHoanTien
  - *Date cols:* ['NgayGioTra']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaPhieuTra": "TH00001", "MaHoaDon": "ORD000158", "NgayGioTra": "2025-04-03 20:12:33", "NguyenNhan": "mua nhầm", "TienHoanTra": "14800", "CachHoanTien": "cash"}
{"IDCuaHang": "dev_006", "MaPhieuTra": "TH00002", "MaHoaDon": "ORD000085", "NgayGioTra": "2025-04-04 19:27:27", "NguyenNhan": null, "TienHoanTra": "1600", "CachHoanTien": "cash"}
{"IDCuaHang": "dev_006", "MaPhieuTra": "TH00003", "MaHoaDon": "ORD000140", "NgayGioTra": "2025-04-06 18:18:15", "NguyenNhan": null, "TienHoanTra": "1400", "CachHoanTien": "cash"}
```

#### Table `pos.sqlite :: the_kho`
- **Rows:** 73,901 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** IDCuaHang, MaGiaoDichKho, MaHangHoa, MaChiNhanh, NgayGioPhatSinh, LoaiGiaoDich, SLQuyDoi, KieuChungTu, MaChungTu, TonCuoi
  - *Date cols:* ['NgayGioPhatSinh']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaGiaoDichKho": "MV0000001", "MaHangHoa": "SP0001", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-04-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "360", "KieuChungTu": "purchase"}
{"IDCuaHang": "dev_006", "MaGiaoDichKho": "MV0000002", "MaHangHoa": "SP0002", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-04-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "216", "KieuChungTu": "purchase"}
{"IDCuaHang": "dev_006", "MaGiaoDichKho": "MV0000003", "MaHangHoa": "SP0003", "MaChiNhanh": "CN1", "NgayGioPhatSinh": "2025-04-01 06:00:00", "LoaiGiaoDich": "in_purchase", "SLQuyDoi": "240", "KieuChungTu": "purchase"}
```

#### Table `pos.sqlite :: lich_su_gia`
- **Rows:** 120 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** IDCuaHang, MaHangHoa, NgayApDung, GiaBanLe
  - *Date cols:* ['NgayApDung']
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "NgayApDung": "2025-04-01", "GiaBanLe": "1400"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "NgayApDung": "2026-03-26", "GiaBanLe": "1500"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0002", "NgayApDung": "2025-04-01", "GiaBanLe": "2000"}
```

#### Table `pos.sqlite :: lo_hang`
- **Rows:** 3,234 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** IDCuaHang, MaHangHoa, MaLo, MaPhieuNhap, HanSuDung, SLNhapQuyDoi, DonGiaNhap
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "MaLo": "B2504172", "MaPhieuNhap": "PN00019", "HanSuDung": "2027-06-30", "SLNhapQuyDoi": "360", "DonGiaNhap": "1000"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "MaLo": "B2505387", "MaPhieuNhap": "PN00051", "HanSuDung": "2025-10-09", "SLNhapQuyDoi": "360", "DonGiaNhap": "1100"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "MaLo": "B2506788", "MaPhieuNhap": "PN00064", "HanSuDung": "2027-07-15", "SLNhapQuyDoi": "360", "DonGiaNhap": "1100"}
```

#### Table `pos.sqlite :: chi_tiet_don_lo`
- **Rows:** 72,710 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (6):** IDCuaHang, MaHoaDon, SoThuTu, MaLo, SLQuyDoi, SLTraQuyDoi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000002", "SoThuTu": "1", "MaLo": "U2504390", "SLQuyDoi": "16", "SLTraQuyDoi": "0"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000003", "SoThuTu": "1", "MaLo": "D2504828", "SLQuyDoi": "1", "SLTraQuyDoi": "0"}
{"IDCuaHang": "dev_006", "MaHoaDon": "ORD000004", "SoThuTu": "1", "MaLo": "D2504828", "SLQuyDoi": "2", "SLTraQuyDoi": "0"}
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
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0001", "ThanhPhanChinh": "Paracetamol + Cafein", "BanTheoDon": "0"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0002", "ThanhPhanChinh": "Paracetamol", "BanTheoDon": "0"}
{"IDCuaHang": "dev_006", "MaHangHoa": "SP0003", "ThanhPhanChinh": "Paracetamol", "BanTheoDon": "0"}
```

---

## Business `dev_007`
- **Structure Archetype:** Multi-table Relational (3 tables)
- **README (truncated 500 chars):** # Dữ liệu dev_007  File xuất từ phần mềm bán hàng, 3 danh sách: chi tiết hoá đơn (mỗi dòng một mặt hàng trong đơn; thông tin đơn, khách lặp lại ở mọi dòng của đơn), danh mục hàng kèm tồn kho, chi tiết nhập hàng (thông tin phiếu nhập lặp lại ở mọi dòng của phiếu). Các file nối với nhau qua mã hàng.  ## File - `chi_tiet_hoa_don.csv` (csv) - `danh_muc_hang.csv` (csv) - `chi_tiet_nhap_hang.csv` (csv)  ## Cột trong `chi_tiet_hoa_don.csv` - **Bàn**: bàn - **Thành tiền**: thành tiền sau giảm - **Nhóm k
- **Files on disk (4):** README.md, chi_tiet_hoa_don.csv, chi_tiet_nhap_hang.csv, danh_muc_hang.csv

### Tables / Sheets Detail:
#### Table `chi_tiet_hoa_don.csv`
- **Rows:** 121,067 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (30):** Bàn, Thành tiền, Nhóm khách hàng, Mặt hàng, Khu vực, Nguồn, Nội dung, Giờ bán, Giới tính, No., Ngày giao dịch, Tiến độ, Trạng thái HĐĐT, Mã vạch, Khách trả...
  - *Date cols:* None
  - *Amount/Qty cols:* ['No.']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Bàn": "Bàn 05", "Thành tiền": "79k", "Nhóm khách hàng": "nan", "Mặt hàng": "Cơm chiên hải sản", "Khu vực": "trong nhà", "Nguồn": "store", "Nội dung": "nan", "Giờ bán": "2025-02-01 08:54:32"}
{"Bàn": "Bàn 05", "Thành tiền": "50k", "Nhóm khách hàng": "nan", "Mặt hàng": "Rau  muống xào tỏi", "Khu vực": "trong nhà", "Nguồn": "store", "Nội dung": "nan", "Giờ bán": "2025-02-01 08:54:32"}
{"Bàn": "B01", "Thành tiền": "158k", "Nhóm khách hàng": "nan", "Mặt hàng": "Cánh gà chiên nước mắm", "Khu vực": "trong nhà", "Nguồn": "store", "Nội dung": "nan", "Giờ bán": "2025-02-01 09:27:53"}
```

#### Table `chi_tiet_nhap_hang.csv`
- **Rows:** 1,731 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (13):** Mã NCC, Tổng tiền phiếu, SL nhập, Hàng hóa, STT, ĐVT nhập, Mã hàng bán, Giá nhập, Note, Ngày nhập, Thành tiền, Mã phiếu nhập, Trạng thái phiếu
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã NCC": "NCC001", "Tổng tiền phiếu": "248870400", "SL nhập": "240", "Hàng hóa": "Rau muống xào tỏi", "STT": "1", "ĐVT nhập": "đĩa", "Mã hàng bán": "SP0001", "Giá nhập": "17000"}
{"Mã NCC": "NCC001", "Tổng tiền phiếu": "248870400", "SL nhập": "10", "Hàng hóa": "Bia Tiger lon", "STT": "2", "ĐVT nhập": "thùng", "Mã hàng bán": "SP0002", "Giá nhập": "384000"}
{"Mã NCC": "NCC001", "Tổng tiền phiếu": "248870400", "SL nhập": "216", "Hàng hóa": "Cánh gà chiên nước mắm", "STT": "3", "ĐVT nhập": "đĩa", "Mã hàng bán": "SP0003", "Giá nhập": "33000"}
```

#### Table `danh_muc_hang.csv`
- **Rows:** 61 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Tra cứu thông tin bổ sung, Đang kinh doanh, ĐVT, Giá vốn, Hàng bán, Nhóm, Giá, Tồn cuối, Mã SKU
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tra cứu thông tin bổ sung": "#VALUE!", "Đang kinh doanh": "True", "ĐVT": "đĩa", "Giá vốn": "15,044", "Hàng bán": "Rau muống xào tỏi", "Nhóm": "rau", "Giá": "50,000", "Tồn cuối": "85"}
{"Tra cứu thông tin bổ sung": "nan", "Đang kinh doanh": "True", "ĐVT": "lon", "Giá vốn": "16,004", "Hàng bán": "Bia Tiger lon", "Nhóm": "bia", "Giá": "22,000", "Tồn cuối": "150"}
{"Tra cứu thông tin bổ sung": "nan", "Đang kinh doanh": "True", "ĐVT": "đĩa", "Giá vốn": "31,051", "Hàng bán": "Cánh gà chiên nước mắm", "Nhóm": "chiên xào", "Giá": "79,000", "Tồn cuối": "23"}
```

---

## Business `dev_008`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu dev_008  File xuất từ phần mềm bán hàng, 3 danh sách: chi tiết hoá đơn (mỗi dòng một mặt hàng trong đơn; thông tin đơn, khách lặp lại ở mọi dòng của đơn), danh mục hàng kèm tồn kho, chi tiết nhập hàng (thông tin phiếu nhập lặp lại ở mọi dòng của phiếu). Các file nối với nhau qua mã hàng.  ## File - `ChiTietHoaDon_1.xlsx` (xlsx) - `ChiTietHoaDon_2.xlsx` (xlsx) - `DanhMucHang.xlsx` (xlsx) - `ChiTietNhapHang.xlsx` (xlsx)  ## Cột trong `ChiTietHoaDon_1.xlsx` - **Bill**: mã đơn - **Trạng th
- **Files on disk (5):** ChiTietHoaDon_1.xlsx, ChiTietHoaDon_2.xlsx, ChiTietNhapHang.xlsx, DanhMucHang.xlsx, README.md

### Tables / Sheets Detail:
#### Table `ChiTietHoaDon_1.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (32):** Bill, Trạng thái HĐĐT, Mã người mua, Bàn, Đơn vị (tính), Phi ship, Thành tiền, Giảm (đ), Giờ bán, Tổng tiền hàng, Addr, Giới tính, Giảm giá HĐ, Nhóm hàng, Khách...
  - *Date cols:* None
  - *Amount/Qty cols:* ['Tong tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Bill": "ORD000001", "Trạng thái HĐĐT": null, "Mã người mua": "KH0022", "Bàn": null, "Đơn vị (tính)": "đĩa", "Phi ship": "15000", "Thành tiền": "198000", "Giảm (đ)": "0"}
{"Bill": "ORD000001", "Trạng thái HĐĐT": null, "Mã người mua": "KH0022", "Bàn": null, "Đơn vị (tính)": "lon", "Phi ship": "15000", "Thành tiền": "44000", "Giảm (đ)": "0"}
{"Bill": "ORD000001", "Trạng thái HĐĐT": null, "Mã người mua": "KH0022", "Bàn": null, "Đơn vị (tính)": "đĩa", "Phi ship": "15000", "Thành tiền": "290000", "Giảm (đ)": "0"}
```

#### Table `ChiTietHoaDon_2.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (32):** Bill, Trạng thái HĐĐT, Mã người mua, Bàn, Đơn vị (tính), Phi ship, Thành tiền, Giảm (đ), Giờ bán, Tổng tiền hàng, Addr, Giới tính, Giảm giá HĐ, Nhóm hàng, Khách...
  - *Date cols:* None
  - *Amount/Qty cols:* ['Tong tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Bill": "ORD026196", "Trạng thái HĐĐT": null, "Mã người mua": "KH0139", "Bàn": "Bàn 16", "Đơn vị (tính)": "tô", "Phi ship": "0", "Thành tiền": "109000", "Giảm (đ)": "0"}
{"Bill": "ORD026196", "Trạng thái HĐĐT": null, "Mã người mua": "KH0139", "Bàn": "Bàn 16", "Đơn vị (tính)": "chai", "Phi ship": "0", "Thành tiền": "19000", "Giảm (đ)": "0"}
{"Bill": "ORD026196", "Trạng thái HĐĐT": null, "Mã người mua": "KH0139", "Bàn": "Bàn 16", "Đơn vị (tính)": "đĩa", "Phi ship": "0", "Thành tiền": "93500", "Giảm (đ)": "0"}
```

#### Table `ChiTietNhapHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (13):** Giá nhập, Mã NCC, Trạng thái phiếu, Ngày nhập, STT, Mã phiếu nhập, Tổng tiền phiếu, Lưu ý, Tên mặt hàng, Mã vạch, Thành tiền, SL nhập, ĐVT nhập
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Giá nhập": "16.000đ", "Mã NCC": "NCC004", "Trạng thái phiếu": "Đã nhập hàng", "Ngày nhập": "01/01/2025", "STT": "1", "Mã phiếu nhập": "PN00001", "Tổng tiền phiếu": "294.770.300đ", "Lưu ý": "nhập đầu kỳ"}
{"Giá nhập": "360.000đ", "Mã NCC": "NCC004", "Trạng thái phiếu": "Đã nhập hàng", "Ngày nhập": "01/01/2025", "STT": "2", "Mã phiếu nhập": "PN00001", "Tổng tiền phiếu": "294,7703tr", "Lưu ý": "nhập đầu kỳ"}
{"Giá nhập": "31.000đ", "Mã NCC": "NCC004", "Trạng thái phiếu": "Đã nhập hàng", "Ngày nhập": "01/01/2025", "STT": "3", "Mã phiếu nhập": "PN00001", "Tổng tiền phiếu": "294.770.300đ", "Lưu ý": "nhập đầu kỳ"}
```

#### Table `DanhMucHang.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Hàng, Đang kinh doanh, Mã sản phẩm bán, DVT, Tồn thực, Loại hàng, Giá vốn, Giá hiện tại
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Hàng": "Rau muống xào tỏi", "Đang kinh doanh": "True", "Mã sản phẩm bán": "SP0001", "DVT": "đĩa", "Tồn thực": "279", "Loại hàng": "rau", "Giá vốn": "16 076", "Giá hiện tại": "50 000"}
{"Hàng": "Bia Tiger lon", "Đang kinh doanh": "True", "Mã sản phẩm bán": "SP0002", "DVT": "lon", "Tồn thực": "199", "Loại hàng": "bia", "Giá vốn": "16 000", "Giá hiện tại": "22 000"}
{"Hàng": "Cánh gà chiên nước mắm", "Đang kinh doanh": "True", "Mã sản phẩm bán": "SP0003", "DVT": "đĩa", "Tồn thực": "85", "Loại hàng": "chiên xào", "Giá vốn": "30 921", "Giá hiện tại": "83 000"}
```

---

## Business `dev_009`
- **Structure Archetype:** Single Flat Sales Log / Multi-sheet Register
- **README (truncated 500 chars):** # Dữ liệu dev_009  Danh sách hoá đơn, một file CSV: mỗi dòng một đơn hàng (hoá đơn), không có chi tiết mặt hàng trong đơn.  ## File - `danh_sach_hoa_don.csv` (csv)  ## Cột trong `danh_sach_hoa_don.csv` - **Ngày tháng**: ngày bán - **Trạng thái đơn**: trạng thái đơn - **TongTien**: số khách phải trả cho cả đơn (đã tính giảm giá của đơn và phí giao) - **Mã hóa đơn**: mã đơn - **Nợ**: số khách còn nợ của đơn (đơn huỷ: 0) - **Đã thu**: đã thanh toán - **Đối tác**: tên khách (Khách lẻ nếu không lưu)
- **Files on disk (2):** README.md, danh_sach_hoa_don.csv

### Tables / Sheets Detail:
#### Table `danh_sach_hoa_don.csv`
- **Rows:** 23,338 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày tháng, Trạng thái đơn, TongTien, Mã hóa đơn, Nợ, Đã thu, Đối tác, Giá trị hàng
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày tháng": "2025-01-01 00:00:00", "Trạng thái đơn": "Xong", "TongTien": "32000", "Mã hóa đơn": "ORD000001", "Nợ": "0", "Đã thu": "32,000", "Đối tác": "Lý Anh Lan", "Giá trị hàng": "32,000"}
{"Ngày tháng": "01/01/2025", "Trạng thái đơn": "Xong", "TongTien": "878000", "Mã hóa đơn": "ORD000002", "Nợ": "0", "Đã thu": "878000", "Đối tác": "Phan Ngân Bảo", "Giá trị hàng": "888,000"}
{"Ngày tháng": "01/01/2025", "Trạng thái đơn": "Xong", "TongTien": "375000", "Mã hóa đơn": "ORD000003", "Nợ": "0", "Đã thu": "375000", "Đối tác": "Hoàng Huy Quang", "Giá trị hàng": "385000"}
```

---

## Business `dev_010`
- **Structure Archetype:** Header-Detail Relational (Orders + OrderDetails)
- **README (truncated 500 chars):** # Dữ liệu dev_010  Dữ liệu bán hàng của tiệm, gồm vài file nối với nhau qua mã.  ## File - `don_hang.csv` (csv) - `chi_tiet_don.csv` (csv) - `san_pham.csv` (csv) - `khach_hang.csv` (csv) - `thanh_toan.csv` (csv)  ## Cột trong `don_hang.csv` - **Kênh đặt**: kênh bán - **Thành tiền**: tổng tiền đơn - **Số CT**: mã đơn - **Con no**: còn nợ - **Date**: ngày bán - **Phương thức TT**: hình thức thanh toán của đơn: cash tiền mặt, transfer chuyển khoản, ewallet ví điện tử, cod giao hàng thu tiền, debt g
- **Files on disk (6):** README.md, chi_tiet_don.csv, don_hang.csv, khach_hang.csv, san_pham.csv, thanh_toan.csv

### Tables / Sheets Detail:
#### Table `chi_tiet_don.csv`
- **Rows:** 45,251 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Mã bill, Cộng, CK, SoLuong, Mã H.hóa, SL quy đổi, No., Đơn giá (đ), dvt
  - *Date cols:* None
  - *Amount/Qty cols:* ['SoLuong', 'No.']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mã bill": "ORD000001", "Cộng": "375000", "CK": "0", "SoLuong": "1", "Mã H.hóa": "SP0005", "SL quy đổi": "1", "No.": "1", "Đơn giá (đ)": "375000"}
{"Mã bill": "ORD000001", "Cộng": "65000", "CK": "0", "SoLuong": "1", "Mã H.hóa": "SP0012", "SL quy đổi": "1", "No.": "2", "Đơn giá (đ)": "65000"}
{"Mã bill": "ORD000001", "Cộng": "139000", "CK": "0", "SoLuong": "1 chai", "Mã H.hóa": "SP0014", "SL quy đổi": "1", "No.": "3", "Đơn giá (đ)": "139000"}
```

#### Table `don_hang.csv`
- **Rows:** 25,702 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (11):** Kênh đặt, Thành tiền, Số CT, Con no, Date, Phương thức TT, Tiền giảm, Phí vận chuyển, Khách trả, Mã thẻ, Xử lý
  - *Date cols:* ['Date']
  - *Amount/Qty cols:* ['Con no']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Kênh đặt": "store", "Thành tiền": "569.000đ", "Số CT": "ORD000001", "Con no": "0đ", "Date": "2025-05-01", "Phương thức TT": "ewallet", "Tiền giảm": "10000", "Phí vận chuyển": "0"}
{"Kênh đặt": "store", "Thành tiền": "112.000đ", "Số CT": "ORD000002", "Con no": "0", "Date": "2025-05-01", "Phương thức TT": "cash", "Tiền giảm": "0", "Phí vận chuyển": "0"}
{"Kênh đặt": "store", "Thành tiền": "123.000đ", "Số CT": "ORD000003", "Con no": "0", "Date": "2025-05-01", "Phương thức TT": "cash", "Tiền giảm": "0", "Phí vận chuyển": "0"}
```

#### Table `khach_hang.csv`
- **Rows:** 260 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (13):** Người tạo, Ghi chú KH, Khách lẻ/sỉ, Loại khách, Mã số thuế, Loại hình khách, Mã khách, Email, Tổng điểm, Trạng thái, Số CMND/CCCD, Phone, Công ty
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Người tạo": "admin", "Ghi chú KH": "nan", "Khách lẻ/sỉ": "Lý Nhung Dương", "Loại khách": "thân thiết", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân", "Mã khách": "KH0001", "Email": "nan"}
{"Người tạo": "admin", "Ghi chú KH": "nan", "Khách lẻ/sỉ": "Vương Hương Hằng", "Loại khách": "thân thiết", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân", "Mã khách": "KH0002", "Email": "nan"}
{"Người tạo": "admin", "Ghi chú KH": "nan", "Khách lẻ/sỉ": "Hoàng Hùng Trang (0930872831)", "Loại khách": "lẻ", "Mã số thuế": "nan", "Loại hình khách": "Cá nhân", "Mã khách": "KH0003", "Email": "nan"}
```

#### Table `san_pham.csv`
- **Rows:** 60 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (17):** Mô tả chi tiết, Mẫu ghi chú, Loại hàng hóa, Thương hiệu, Đơn vị tính, Ghi chú, Bảo hành, Nhóm hàng, Mã vạch EAN, Hình ảnh (url1,url2...), ten_hang, Thuộc tính, Trọng lượng, Giá bán, Mã vạch...
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Mô tả chi tiết": "nan", "Mẫu ghi chú": "nan", "Loại hàng hóa": "Hàng hóa", "Thương hiệu": "nan", "Đơn vị tính": "lon", "Ghi chú": "nan", "Bảo hành": "nan", "Nhóm hàng": "sữa bột"}
{"Mô tả chi tiết": "nan", "Mẫu ghi chú": "nan", "Loại hàng hóa": "Hàng hóa", "Thương hiệu": "nan", "Đơn vị tính": "lon", "Ghi chú": "nan", "Bảo hành": "nan", "Nhóm hàng": "sữa bột"}
{"Mô tả chi tiết": "nan", "Mẫu ghi chú": "nan", "Loại hàng hóa": "Hàng hóa", "Thương hiệu": "nan", "Đơn vị tính": "lon", "Ghi chú": "nan", "Bảo hành": "nan", "Nhóm hàng": "sữa bột"}
```

#### Table `thanh_toan.csv`
- **Rows:** 26,246 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Loại TT, Ngay thu, So tien, Mã đơn, Mã TT
  - *Date cols:* ['Ngay thu']
  - *Amount/Qty cols:* ['So tien']
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Loại TT": "ewallet", "Ngay thu": "2025-05-01 06:48:23", "So tien": "569000", "Mã đơn": "ORD000001", "Mã TT": "PAY000001"}
{"Loại TT": "cash", "Ngay thu": "2025-05-01 07:23:09", "So tien": "112000", "Mã đơn": "ORD000002", "Mã TT": "PAY000002"}
{"Loại TT": "cash", "Ngay thu": "2025-05-01 07:31:13", "So tien": "123000", "Mã đơn": "ORD000003", "Mã TT": "PAY000003"}
```

---

## Business `dev_011`
- **Structure Archetype:** Multi-table Relational (2 tables)
- **README (truncated 500 chars):** # Dữ liệu dev_011  Sổ bán hàng của cửa hàng điện thoại, chủ tiệm tự ghi trên Excel: sheet `Ghi tắt` (cách ghi tắt tên hàng và loại hàng) và sheet `Sổ bán hàng` cả kỳ, mỗi dòng một mặt hàng của một đơn.  ## File - `SoBanHang.xlsx` (xlsx)  ## Cột trong `SoBanHang.xlsx` - **Ngày**: ngày bán - **STT**: số thứ tự đơn (hoá đơn) trong sổ - **Khách**: tên khách (khách không lưu: khách lẻ) - **Hàng**: hàng bán, có thể ghi tắt (tra ở sheet Ghi tắt) - **IMEI**: IMEI của máy bán (máy mới, máy cũ), dòng 2 má
- **Files on disk (2):** README.md, SoBanHang.xlsx

### Tables / Sheets Detail:
#### Table `SoBanHang.xlsx :: Ghi tắt`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Ghi tắt, Tên hàng, Loại
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ghi tắt": "Cáp C", "Tên hàng": "Cáp Type-C 1m", "Loại": "phụ kiện"}
{"Ghi tắt": "Cáp C-L", "Tên hàng": "Cáp Type-C sang Lightning 1m", "Loại": "phụ kiện"}
{"Ghi tắt": "Sạc 20W", "Tên hàng": "Củ sạc nhanh 20W Type-C", "Loại": "phụ kiện"}
```

#### Table `SoBanHang.xlsx :: Sổ bán hàng`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Thu máy cũ, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "2025-06-01 00:00:00", "STT": "1", "Khách": "Khách lẻ", "Hàng": "Sạc 25W SS", "IMEI": null, "SL": "2", "Giá": "290000", "Thành tiền": "580000"}
{"Ngày": "2025-06-01 00:00:00", "STT": null, "Khách": null, "Hàng": "Cáp C-L", "IMEI": null, "SL": "1", "Giá": "150000", "Thành tiền": "150000"}
{"Ngày": "2025-06-01 00:00:00", "STT": "2", "Khách": "kl", "Hàng": "Pin sạc dự phòng 10000mAh", "IMEI": null, "SL": "2", "Giá": "390000", "Thành tiền": "780000"}
```

---

## Business `dev_012`
- **Structure Archetype:** Multi-table Relational (15 tables)
- **README (truncated 500 chars):** # Dữ liệu dev_012  Sổ sửa xe chủ tiệm tự ghi trên Excel, mỗi tháng một sheet: mỗi dòng một lượt xe vào sửa (một phiếu), không ghi mã phiếu, không ghi tên khách. Ô Làm gì ghi mọi việc của phiếu. Tiền là tổng cả phiếu, không ghi tiền từng việc. File DanhSachTho.xlsx ghi họ tên, phần trăm hoa hồng các thợ; sổ ghi thợ theo tên gọi. Phiếu ghi chú bảo hành, Tiền 0: xe quay lại bảo hành việc của một phiếu trước, tiệm không thu tiền.  ## File - `SoSuaXe.xlsx` (xlsx) - `DanhSachTho.xlsx` (xlsx)  ## Cột t
- **Files on disk (3):** DanhSachTho.xlsx, README.md, SoSuaXe.xlsx

### Tables / Sheets Detail:
#### Table `DanhSachTho.xlsx :: Sheet1`
- **Rows:** 4 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Họ tên, Ngày vào làm, Hoa hồng (%)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Họ tên": "Hà Loan Đạt", "Ngày vào làm": "2023-05-29 00:00:00", "Hoa hồng (%)": "32"}
{"Họ tên": "Lương Chi Đức", "Ngày vào làm": "2024-09-19 00:00:00", "Hoa hồng (%)": "25"}
{"Họ tên": "Đoàn Bảo Phúc", "Ngày vào làm": "2024-08-04 00:00:00", "Hoa hồng (%)": "28"}
```

#### Table `SoSuaXe.xlsx :: T7-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2025", "Xe": "future 59B6-219.16", "Làm gì": "vệ sinh nồi", "Thợ": "A.Đức", "Tiền": "120000", "Ghi chú": null}
{"Ngày": "1 thg 7 2025", "Xe": "wave alpha 50K2-994.07", "Làm gì": "bdtq + vs nồi", "Thợ": "Đức", "Tiền": "270.000đ", "Ghi chú": null}
{"Ngày": "01/07/2025", "Xe": "Vario 50F1-334.29", "Làm gì": "bộ nhông xích + thay nước mát", "Thợ": "a Đức", "Tiền": "440000", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T8-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45870", "Xe": "grande 51L3-168.55", "Làm gì": "thay bugi + bdtq + nhớt hãng", "Thợ": "a Đạt", "Tiền": "310.000đ", "Ghi chú": "xe để lại qua đêm"}
{"Ngày": "45870", "Xe": "airblade 50F5-227.38", "Làm gì": "dây cu roa + nhớt láp + nhớt Honda", "Thợ": "A.Đạt", "Tiền": "405.000đ", "Ghi chú": null}
{"Ngày": "1 thg 8 2025", "Xe": "Future 61N3-574.63", "Làm gì": "Shell 1L + thay nhớt Motul", "Thợ": "Đạt", "Tiền": "415000", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T9-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2025", "Xe": "sirius 51M2-125.32", "Làm gì": "thay nhớt + vá xe", "Thợ": "a An", "Tiền": "120.000đ", "Ghi chú": null}
{"Ngày": "1 thg 9 2025", "Xe": "vision 72L7-223.37", "Làm gì": "vá ruột + bố trước + bố sau", "Thợ": "A.An", "Tiền": "175.000đ", "Ghi chú": null}
{"Ngày": "1 thg 9 2025", "Xe": "Exciter 60T2-479.52", "Làm gì": "vs nồi + thay vỏ", "Thợ": "a An", "Tiền": "456000", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T10-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/10/2025", "Xe": "LEAD 61H7-440.84", "Làm gì": "nhớt Honda, thay nhớt Castrol", "Thợ": "Đức", "Tiền": "215.000đ", "Ghi chú": null}
{"Ngày": "45931", "Xe": "Alpha 54T8-428.71", "Làm gì": "thay vỏ + bdtq", "Thợ": "Đức", "Tiền": "486.000đ", "Ghi chú": null}
{"Ngày": "01/10/2025", "Xe": "AB 54P3-820.93", "Làm gì": "thay bugi, bố sau", "Thợ": "Đức", "Tiền": "135.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T11-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "1 thg 11 2025", "Xe": "AB 51U2-574.02", "Làm gì": "bố thắng trước, vá xe", "Thợ": "Đạt", "Tiền": "105.000đ", "Ghi chú": null}
{"Ngày": "45962", "Xe": "Alpha 61N1-806.33", "Làm gì": "đèn pha, vá ruột", "Thợ": "a Đạt", "Tiền": "80000", "Ghi chú": "xe để lại qua đêm"}
{"Ngày": "45962", "Xe": "Vision 110 59N7-633.33", "Làm gì": "bình + vá xe", "Thợ": "Đạt", "Tiền": "475000", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T12-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/12/2025", "Xe": "Wave RSX 59N7-534.01", "Làm gì": "bố thắng trước", "Thợ": "a Phúc", "Tiền": "80.000đ", "Ghi chú": "xe để lại qua đêm"}
{"Ngày": "1 thg 12 2025", "Xe": "exciter 51X2-652.38", "Làm gì": "bdtq", "Thợ": "Phúc", "Tiền": "150000", "Ghi chú": null}
{"Ngày": "01/12/2025", "Xe": "Alpha 50S2-338.65", "Làm gì": "nhớt, Motul", "Thợ": "A.Phúc", "Tiền": "230.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T1-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46023", "Xe": "Wave α 51S3-559.01", "Làm gì": "thay vỏ", "Thợ": "A.Đức", "Tiền": "336.000đ", "Ghi chú": null}
{"Ngày": "46023", "Xe": "LEAD 54G6-426.07", "Làm gì": "rửa kim phun, vá", "Thợ": "A.Đức", "Tiền": "176.000đ", "Ghi chú": null}
{"Ngày": "01/01/2026", "Xe": "RSX 72C8-233.86", "Làm gì": "BD + sửa điện + nhớt", "Thợ": "Đức", "Tiền": "490.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T2-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "1 thg 2 2026", "Xe": "sirius 61B2-515.41", "Làm gì": "nhớt", "Thợ": "A.Đạt", "Tiền": "95000", "Ghi chú": null}
{"Ngày": "1 thg 2 2026", "Xe": "Sirius 59N3-928.90", "Làm gì": "làm điện", "Thợ": "A.Đạt", "Tiền": "80000", "Ghi chú": null}
{"Ngày": "1 thg 2 2026", "Xe": "Wave RSX 51L1-358.05", "Làm gì": "nhớt hãng", "Thợ": "Đạt", "Tiền": "95.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T3-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "1 thg 3 2026", "Xe": "Sirius FI 60S4-802.46", "Làm gì": "bảo dưỡng, bu gi", "Thợ": "Đạt", "Tiền": "295.500đ", "Ghi chú": null}
{"Ngày": "01/03/2026", "Xe": "wave alpha 59C9-434.79", "Làm gì": "nhớt", "Thợ": "Đạt", "Tiền": "95.000đ", "Ghi chú": null}
{"Ngày": "01/03/2026", "Xe": "sirius 72X6-109.34", "Làm gì": "vỏ xe + bảo dưỡng + bố trước + thay lọc ", "Thợ": "A.Đạt", "Tiền": "676.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T4-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/04/2026", "Xe": "LEAD 59G4-721.13", "Làm gì": "curoa", "Thợ": "a An", "Tiền": "280.000đ", "Ghi chú": null}
{"Ngày": "1 thg 4 2026", "Xe": "Wave α 50G1-441.69", "Làm gì": "nhớt Castrol Power1, thay nhớt, nhớt Mot", "Thợ": "An", "Tiền": "350.000đ", "Ghi chú": null}
{"Ngày": "01/04/2026", "Xe": "vision 54V8-379.04", "Làm gì": "BD + nước làm mát + nhớt Castrol Power1 ", "Thợ": "An", "Tiền": "410.500đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T5-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/05/2026", "Xe": "Air Blade 50C5-913.97", "Làm gì": "đèn pha", "Thợ": "A.Đức", "Tiền": "58000", "Ghi chú": null}
{"Ngày": "01/05/2026", "Xe": "Wave Alpha 50F5-847.70", "Làm gì": "láp, vệ sinh nồi", "Thợ": "A.Đức", "Tiền": "156.000đ", "Ghi chú": null}
{"Ngày": "1 thg 5 2026", "Xe": "wave alpha 54B3-967.91", "Làm gì": "ruột xe", "Thợ": "Đức", "Tiền": "84.000đ", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T6-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46174", "Xe": "janus 59C2-382.22", "Làm gì": "làm nồi", "Thợ": "a Đạt", "Tiền": "126000", "Ghi chú": null}
{"Ngày": "01/06/2026", "Xe": "lead 50V8-550.07", "Làm gì": "vá, má phanh trước, rửa", "Thợ": "Đạt", "Tiền": "136000", "Ghi chú": null}
{"Ngày": "46174", "Xe": "Future 125 59L9-714.43", "Làm gì": "vs nồi", "Thợ": "a Đạt", "Tiền": "126000", "Ghi chú": null}
```

#### Table `SoSuaXe.xlsx :: T7-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2026", "Xe": "Vision 59X5-435.74", "Làm gì": "láp", "Thợ": "a Phúc", "Tiền": "30.000đ", "Ghi chú": null}
{"Ngày": "01/07/2026", "Xe": "grande 61H2-326.44", "Làm gì": "bảo dưỡng + nhớt Castrol", "Thợ": "A.Phúc", "Tiền": "285.500đ", "Ghi chú": null}
{"Ngày": "46204", "Xe": "Ex 59X6-248.83", "Làm gì": "thay bóng đèn, BD, vá xe", "Thợ": "A.Phúc", "Tiền": "249500", "Ghi chú": "kiểm tra lại tuần sau"}
```

#### Table `SoSuaXe.xlsx :: T8-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (6):** Ngày, Xe, Làm gì, Thợ, Tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "1 thg 8 2026", "Xe": "Vision 110 72B9-225.05", "Làm gì": "làm nồi, rửa, má phanh sau", "Thợ": "Đức", "Tiền": "226.000đ", "Ghi chú": null}
{"Ngày": "01/08/2026", "Xe": "Lead 61F2-542.23", "Làm gì": "bu gi", "Thợ": "Đức", "Tiền": "65000", "Ghi chú": null}
{"Ngày": "46235", "Xe": "future 59P6-377.22", "Làm gì": "bdtq", "Thợ": "Đức", "Tiền": "165.500đ", "Ghi chú": null}
```

---

## Business `dev_013`
- **Structure Archetype:** Multi-file Partitioned / Monthly Log (2 time-sliced files)
- **README (truncated 500 chars):** # Dữ liệu dev_013  Sổ sách Excel của tiệm mẹ và bé. `BanHang_<năm>.xlsx`: sổ bán hàng, mỗi tháng một sheet, header gộp 2 dòng (nhóm Hàng hoá, Tiền ở dòng trên). Mỗi dòng một mặt hàng khách mua; một hoá đơn nhiều dòng cùng số HĐ. Ngay sau các dòng hàng của một hoá đơn có thể có dòng không phải hàng, chỉ ghi HĐ, tên và TT: "Voucher" (tiền giảm của hoá đơn từ các chương trình ở sheet KhuyenMai, TT ghi số âm), "Dùng <n> điểm" (khách dùng n điểm thành viên, mỗi điểm trừ 100đ, TT ghi số âm), "Phí ship
- **Files on disk (4):** BanHang_2025.xlsx, BanHang_2026.xlsx, QuanLy.xlsx, README.md

### Tables / Sheets Detail:
#### Table `BanHang_2025.xlsx :: T05-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "305.000đ", "col_1": "305.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Tã quần Bobby size XXL 44 miếng", "Hoá đơn": "ORD000001", "col_6": "1 thg 5 2025", "col_7": "Đặng Thanh Thắng"}
{"Tiền": "190.000đ", "col_1": "190.000đ", "Hàng hoá": "1", "col_3": "cái", "col_4": "Nhiệt kế điện tử Microlife MT200", "Hoá đơn": "ORD000001", "col_6": "1 thg 5 2025", "col_7": "Đặng Thanh Thắng"}
```

#### Table `BanHang_2025.xlsx :: T06-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "95.000đ", "col_1": "95.000đ", "Hàng hoá": "1", "col_3": "chai", "col_4": "Tắm gội toàn thân D-nee Pure 380ml", "Hoá đơn": "ORD000842", "col_6": "1/6", "col_7": "Lâm Phong An"}
{"Tiền": null, "col_1": "25.000đ", "Hàng hoá": null, "col_3": null, "col_4": "Phí ship", "Hoá đơn": "ORD000842", "col_6": null, "col_7": null}
```

#### Table `BanHang_2025.xlsx :: T07-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "145.000đ", "col_1": "145.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Miếng lót sơ sinh Bobby Newborn 1 108 mi", "Hoá đơn": "ORD001662", "col_6": "45839", "col_7": "Khách lẻ"}
{"Tiền": "260.000đ", "col_1": "260.000đ", "Hàng hoá": "1", "col_3": "chai", "col_4": "Sữa dưỡng ẩm Cetaphil Baby 400ml", "Hoá đơn": "ORD001662", "col_6": "1/7", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2025.xlsx :: T08-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "380.000đ", "col_1": "380.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Tã quần Moony size L 44 miếng", "Hoá đơn": "ORD002534", "col_6": "45870", "col_7": "Châu Thu Tâm"}
{"Tiền": "560.000đ", "col_1": "1,12tr", "Hàng hoá": "2", "col_3": "lon", "col_4": "Sữa Enfamil A+ NeuroPro số 1 830g", "Hoá đơn": "ORD002534", "col_6": "45870", "col_7": "Châu Thu Tâm"}
```

#### Table `BanHang_2025.xlsx :: T09-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "380.000đ", "col_1": "760.000đ", "Hàng hoá": "2", "col_3": "bịch", "col_4": "Tã quần Moony size L 44 miếng", "Hoá đơn": "ORD003382", "col_6": "1 thg 9 2025", "col_7": "Khách lẻ"}
{"Tiền": "340.000đ", "col_1": "340.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Tã quần Huggies Dry size L 68 miếng", "Hoá đơn": "ORD003382", "col_6": "1 thg 9 2025", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2025.xlsx :: T10-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "145.000đ", "col_1": "145.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Miếng lót sơ sinh Bobby Newborn 1 108 mi", "Hoá đơn": "ORD004151", "col_6": "1 thg 10 2025", "col_7": "Doãn Dũng Sơn"}
{"Tiền": "335.000đ", "col_1": "335.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Tã dán Merries size M 64 miếng", "Hoá đơn": "ORD004151", "col_6": "01/10/2025", "col_7": "Doãn Dũng Sơn"}
```

#### Table `BanHang_2025.xlsx :: T11-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "425.000đ", "col_1": "425.000đ", "Hàng hoá": "1", "col_3": "cái", "col_4": "Bình sữa Comotomo 250ml", "Hoá đơn": "ORD005036", "col_6": "1/11", "col_7": "Khách lẻ"}
{"Tiền": "505.000đ", "col_1": "505.000đ", "Hàng hoá": "1", "col_3": "lon", "col_4": "Sữa Enfagrow A+ NeuroPro số 3 830g", "Hoá đơn": "ORD005036", "col_6": "45962", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2025.xlsx :: T12-2025`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "435.000đ", "col_1": "435.000đ", "Hàng hoá": "1", "col_3": "lon", "col_4": "Sữa Abbott Grow Gold 3+ 900g", "Hoá đơn": "ORD005848", "col_6": "1 thg 12 2025", "col_7": "Khách lẻ"}
{"Tiền": "395.000đ", "col_1": "790.000đ", "Hàng hoá": "2", "col_3": "lon", "col_4": "Sữa Nan Optipro Plus 3 900g", "Hoá đơn": "ORD005848", "col_6": "01/12/2025", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2026.xlsx :: T01-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "150.000đ", "col_1": "150.000đ", "Hàng hoá": "1", "col_3": "hộp", "col_4": "Nước muối sinh lý Fysoline hồng hộp 40 ố", "Hoá đơn": "ORD006691", "col_6": "1/1", "col_7": "Khách lẻ"}
{"Tiền": "107.000đ", "col_1": "107.000đ", "Hàng hoá": "1", "col_3": "hộp", "col_4": "Bánh ăn dặm Gerber Puffs 42g", "Hoá đơn": "ORD006692", "col_6": "01/01/2026", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2026.xlsx :: T02-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "340.000đ", "col_1": "340.000đ", "Hàng hoá": "1", "col_3": "bịch", "col_4": "Tã quần Huggies Dry size L 68 miếng", "Hoá đơn": "ORD007525", "col_6": "46054", "col_7": "Tô Ngọc Bích"}
{"Tiền": null, "col_1": "-10.000đ", "Hàng hoá": null, "col_3": null, "col_4": "Voucher", "Hoá đơn": "ORD007525", "col_6": null, "col_7": null}
```

#### Table `BanHang_2026.xlsx :: T03-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "435.000đ", "col_1": "435.000đ", "Hàng hoá": "1", "col_3": "lon", "col_4": "Sữa Abbott Grow Gold 3+ 900g", "Hoá đơn": "ORD008453", "col_6": "01/03/2026", "col_7": "Hà Hà Hằng"}
{"Tiền": null, "col_1": "-10.000đ", "Hàng hoá": null, "col_3": null, "col_4": "Voucher", "Hoá đơn": "ORD008453", "col_6": null, "col_7": null}
```

#### Table `BanHang_2026.xlsx :: T04-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "165.500đ", "col_1": "331.000đ", "Hàng hoá": "2", "col_3": "chai", "col_4": "Dầu tràm Huế Kim Vui 100ml", "Hoá đơn": "ORD009313", "col_6": "46113", "col_7": "Hồ Hằng Thắng"}
{"Tiền": "395.000đ", "col_1": "790.000đ", "Hàng hoá": "2", "col_3": "lon", "col_4": "Sữa Nan Optipro Plus 3 900g", "Hoá đơn": "ORD009313", "col_6": "01/04/2026", "col_7": "Hồ Hằng Thắng"}
```

#### Table `BanHang_2026.xlsx :: T05-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "279.000đ", "col_1": "279.000đ", "Hàng hoá": "1", "col_3": "cái", "col_4": "Bình tập uống Richell TLI 200ml", "Hoá đơn": "ORD010120", "col_6": "01/05/2026", "col_7": "Khách lẻ"}
{"Tiền": "40.000đ", "col_1": "80.000đ", "Hàng hoá": "2", "col_3": "gói", "col_4": "Khăn sữa cotton 2 lớp gói 10 cái", "Hoá đơn": "ORD010120", "col_6": "1/5", "col_7": "Khách lẻ"}
```

#### Table `BanHang_2026.xlsx :: T06-2026`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (10):** Tiền, col_1, Hàng hoá, col_3, col_4, Hoá đơn, col_6, col_7, col_8, col_9
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tiền": "ĐG", "col_1": "TT", "Hàng hoá": "SL", "col_3": "ĐVT", "col_4": "Tên hàng", "Hoá đơn": "HĐ", "col_6": "Ngày", "col_7": "Khách"}
{"Tiền": "524.000đ", "col_1": "1.048.000đ", "Hàng hoá": "2", "col_3": "lon", "col_4": "Sữa Similac IQ số 3 900g", "Hoá đơn": "ORD011025", "col_6": "1/6", "col_7": "Khách lẻ"}
{"Tiền": "40.000đ", "col_1": "40.000đ", "Hàng hoá": "1", "col_3": "gói", "col_4": "Khăn sữa cotton 2 lớp gói 10 cái", "Hoá đơn": "ORD011025", "col_6": "01/06/2026", "col_7": "Khách lẻ"}
```

#### Table `QuanLy.xlsx :: DanhMuc`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Tên hàng, Tên gọi khác, Nhóm, Hãng, Số / Size, ĐVT, Quy đổi
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên hàng": "Sữa Similac 5G số 1 900g", "Tên gọi khác": "similac 1, similac số 1", "Nhóm": "sữa bột", "Hãng": "Similac", "Số / Size": "Số 1", "ĐVT": "lon", "Quy đổi": null}
{"Tên hàng": "Sữa Similac 5G số 2 900g", "Tên gọi khác": "similac 2, similac số 2", "Nhóm": "sữa bột", "Hãng": "Similac", "Số / Size": "Số 2", "ĐVT": "lon", "Quy đổi": null}
{"Tên hàng": "Sữa Similac IQ số 3 900g", "Tên gọi khác": "similac 3, similac IQ 3", "Nhóm": "sữa bột", "Hãng": "Similac", "Số / Size": "Số 3", "ĐVT": "lon", "Quy đổi": null}
```

#### Table `QuanLy.xlsx :: KhachHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (5):** Tên KH, SĐT, Tên bé, Ngày đăng ký, Điểm hiện có
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Tên KH": "Châu Thu Tâm", "SĐT": "0980590313", "Tên bé": "Xoài", "Ngày đăng ký": "2024-07-14 00:00:00", "Điểm hiện có": "35"}
{"Tên KH": "Lê Quang Đạt", "SĐT": "0977421922", "Tên bé": "Sữa", "Ngày đăng ký": "2025-05-22 00:00:00", "Điểm hiện có": "232"}
{"Tên KH": "Chung Phương Nhung", "SĐT": "0919096077", "Tên bé": "Bon", "Ngày đăng ký": "2026-06-20 00:00:00", "Điểm hiện có": "0"}
```

#### Table `QuanLy.xlsx :: NhapHang`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (9):** Ngày, Số phiếu, Nhà cung cấp, Hàng, SL, ĐVT, Đơn giá, Thành tiền, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45778", "Số phiếu": "PN00001", "Nhà cung cấp": "Cty Phạm Giang", "Hàng": "Sữa Similac 5G số 1 900g", "SL": "29", "ĐVT": "lon", "Đơn giá": "484k", "Thành tiền": "14036k"}
{"Ngày": "45778", "Số phiếu": "PN00001", "Nhà cung cấp": "Cty Phạm Giang", "Hàng": "Sữa Similac 5G số 2 900g", "SL": "24", "ĐVT": "lon", "Đơn giá": "482k", "Thành tiền": "11568k"}
{"Ngày": "45778", "Số phiếu": "PN00001", "Nhà cung cấp": "Cty Phạm Giang", "Hàng": "Sữa Similac IQ số 3 900g", "SL": "19", "ĐVT": "lon", "Đơn giá": "460k", "Thành tiền": "8740k"}
```

#### Table `QuanLy.xlsx :: KhuyenMai`
- **Rows:** 10 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (4):** Chương trình, Hàng áp dụng, Từ ngày, Đến ngày
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Chương trình": "Giảm 10k cho đơn từ 300k", "Hàng áp dụng": "Tất cả", "Từ ngày": "2025-05-01 00:00:00", "Đến ngày": "2026-06-30 00:00:00"}
{"Chương trình": "Giảm 30k mỗi bịch Miếng lót sơ sinh Bobb", "Hàng áp dụng": "Miếng lót sơ sinh Bobby Newborn 1 108 mi", "Từ ngày": "2025-05-21 00:00:00", "Đến ngày": "2025-06-01 00:00:00"}
{"Chương trình": "Giảm 10k mỗi bịch Tã quần Huggies Dry si", "Hàng áp dụng": "Tã quần Huggies Dry size XL 62 miếng", "Từ ngày": "2025-07-07 00:00:00", "Đến ngày": "2025-07-22 00:00:00"}
```

---

## Business `dev_014`
- **Structure Archetype:** Multi-table Relational (20 tables)
- **README (truncated 500 chars):** # Dữ liệu dev_014  Cửa hàng điện thoại gửi các sổ tự ghi trên Excel (mục File): sổ bán hàng (sheet `Ghi tắt` và mỗi tháng một sheet) và các sổ phụ: sổ thu máy cũ một file; sổ nợ, sổ góp, sổ bảo hành chung một file, mỗi sổ một sheet. Các sổ nối với nhau qua số thứ tự đơn trong sổ bán, IMEI và tên, số điện thoại của khách.  ## File - `SoBanHang.xlsx` (xlsx) - `ThuMayCu.xlsx` (xlsx) - `SoNo.xlsx` (xlsx)  ## Quy ước - Dữ liệu có đến hết 30/09/2026. - **Đơn**: các dòng cùng **STT** là một đơn; khách,
- **Files on disk (4):** README.md, SoBanHang.xlsx, SoNo.xlsx, ThuMayCu.xlsx

### Tables / Sheets Detail:
#### Table `SoBanHang.xlsx :: Ghi tắt`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (3):** Ghi tắt, Tên hàng, Loại
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ghi tắt": "Cáp C", "Tên hàng": "Cáp Type-C 1m", "Loại": "phụ kiện"}
{"Ghi tắt": "Cáp C-L", "Tên hàng": "Cáp Type-C sang Lightning 1m", "Loại": "phụ kiện"}
{"Ghi tắt": "Sạc 20W", "Tên hàng": "Củ sạc nhanh 20W Type-C", "Loại": "phụ kiện"}
```

#### Table `SoBanHang.xlsx :: T7-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45839", "STT": "1", "Khách": "Triệu Linh An 0327988481", "Hàng": "IP16 128 đen", "IMEI": "358841973775088", "SL": "1", "Giá": "19tr990", "Thành tiền": "19.990.000đ"}
{"Ngày": "45839", "STT": "1", "Khách": "Triệu Linh An - 0327 988 481", "Hàng": "Ốp lưng silicon iPhone", "IMEI": null, "SL": "1", "Giá": "120k", "Thành tiền": "120000"}
{"Ngày": "45839", "STT": "2", "Khách": "Bùi Khoa Hoàng 0701076413", "Hàng": "Ốp trong", "IMEI": null, "SL": "1", "Giá": "80.000đ", "Thành tiền": "80000"}
```

#### Table `SoBanHang.xlsx :: T8-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45870", "STT": "378", "Khách": "Trần Hương Mai (0908995064)", "Hàng": "Miếng dán lưng PPF", "IMEI": null, "SL": "1", "Giá": "70000", "Thành tiền": "70000"}
{"Ngày": "01/08/2025", "STT": "378", "Khách": "Trần Hương Mai 0908995064", "Hàng": "Sạc 20W", "IMEI": null, "SL": "2", "Giá": "250k", "Thành tiền": "500000"}
{"Ngày": "01/08/2025", "STT": "379", "Khách": "Kiều Hoa Hồng (0919703447)", "Hàng": "Ốp lưng silicon iPhone", "IMEI": null, "SL": "1", "Giá": "120000", "Thành tiền": "120000"}
```

#### Table `SoBanHang.xlsx :: T9-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/09/2025", "STT": "814", "Khách": "lẻ", "Hàng": "Thẻ nhớ microSD 64GB", "IMEI": null, "SL": "1", "Giá": "160000", "Thành tiền": "160000"}
{"Ngày": "01/09/2025", "STT": "815", "Khách": "Tống Bích Hoa (0906849000)", "Hàng": "IP13 128 trắng", "IMEI": "357704596492997", "SL": "1", "Giá": "11.990.000đ", "Thành tiền": "11990000"}
{"Ngày": "01/09/2025", "STT": "815", "Khách": "Tống Bích Hoa - 0906 849 000", "Hàng": "Kính cường lực chống nhìn trộm", "IMEI": null, "SL": "1", "Giá": "180k", "Thành tiền": "180.000đ"}
```

#### Table `SoBanHang.xlsx :: T10-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/10/2025", "STT": "1208", "Khách": "Phùng Lan Trung (0989358811)", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "100000", "Thành tiền": "100000"}
{"Ngày": "01/10/2025", "STT": "1208", "Khách": "Phùng Lan Trung - 0989 358 811", "Hàng": "ỐP SILICON IP", "IMEI": null, "SL": "1", "Giá": "120.000đ", "Thành tiền": "120.000đ"}
{"Ngày": "45931", "STT": "1209", "Khách": "Đàm Minh Ngân 0328612829", "Hàng": "Sạc 20W", "IMEI": null, "SL": "1", "Giá": "250000", "Thành tiền": "250.000đ"}
```

#### Table `SoBanHang.xlsx :: T11-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45962", "STT": "1606", "Khách": "kl", "Hàng": "Kính cường lực 9D", "IMEI": null, "SL": "2", "Giá": "100.000đ", "Thành tiền": "200000"}
{"Ngày": "45962", "STT": "1607", "Khách": "kl", "Hàng": "Cáp C", "IMEI": null, "SL": "1", "Giá": "90k", "Thành tiền": "90.000đ"}
{"Ngày": "01/11/2025", "STT": "1608", "Khách": "Khách lẻ", "Hàng": "Dây đeo điện thoại", "IMEI": null, "SL": "1", "Giá": "40000", "Thành tiền": "40000"}
```

#### Table `SoBanHang.xlsx :: T12-2025`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/12/2025", "STT": "2043", "Khách": "Dương Sơn Anh (0325258544)", "Hàng": "IP16PM 256 đen", "IMEI": "352269387291755 / 352276232122457", "SL": "2", "Giá": "30tr990", "Thành tiền": "61tr980"}
{"Ngày": "45992", "STT": "2044", "Khách": "Huỳnh Ngọc Quang (0796035871)", "Hàng": "IPXSM 64 cũ", "IMEI": "357831936960100", "SL": "1", "Giá": "3tr900", "Thành tiền": "3tr900"}
{"Ngày": "01/12/2025", "STT": "2044", "Khách": "Huỳnh Ngọc Quang (0796035871)", "Hàng": "Sạc 25W SS", "IMEI": null, "SL": "1", "Giá": "290.000đ", "Thành tiền": "290.000đ"}
```

#### Table `SoBanHang.xlsx :: T1-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/01/2026", "STT": "2462", "Khách": "lẻ", "Hàng": "Dán PPF", "IMEI": null, "SL": "1", "Giá": "70k", "Thành tiền": "70.000đ"}
{"Ngày": "46023", "STT": "2463", "Khách": "khách lẻ", "Hàng": "Pin DP 20k", "IMEI": null, "SL": "1", "Giá": "590000", "Thành tiền": "590.000đ"}
{"Ngày": "46023", "STT": "2463", "Khách": "khách lẻ", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "100.000đ", "Thành tiền": "100.000đ"}
```

#### Table `SoBanHang.xlsx :: T2-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/02/2026", "STT": "2899", "Khách": "kl", "Hàng": "Dây đeo", "IMEI": null, "SL": "1", "Giá": "40.000đ", "Thành tiền": "40000"}
{"Ngày": "01/02/2026", "STT": "2900", "Khách": "lẻ", "Hàng": "Dán PPF", "IMEI": null, "SL": "1", "Giá": "70000", "Thành tiền": "70.000đ"}
{"Ngày": "01/02/2026", "STT": "2901", "Khách": "Trần Hương Mai 0908995064", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "100.000đ", "Thành tiền": "100.000đ"}
```

#### Table `SoBanHang.xlsx :: T3-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46082", "STT": "3415", "Khách": "Khách lẻ", "Hàng": "Cáp Type-C sang Lightning 1m", "IMEI": null, "SL": "2", "Giá": "157.500đ", "Thành tiền": "315000"}
{"Ngày": "01/03/2026", "STT": "3416", "Khách": "Tạ An Đức (0989713791)", "Hàng": "IP15 128 xanh", "IMEI": "357194060663630", "SL": "1", "Giá": "16.490.000đ", "Thành tiền": "16490000"}
{"Ngày": "01/03/2026", "STT": "3416", "Khách": "Tạ An Đức (0989713791)", "Hàng": "ỐP SILICON IP", "IMEI": null, "SL": "2", "Giá": "120k", "Thành tiền": "240000"}
```

#### Table `SoBanHang.xlsx :: T4-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46113", "STT": "3816", "Khách": "Trịnh Thắng Hoa - 0323 725 649", "Hàng": "Sạc MagSafe", "IMEI": null, "SL": "1", "Giá": "550.000đ", "Thành tiền": "550.000đ"}
{"Ngày": "01/04/2026", "STT": "3817", "Khách": "Khách lẻ", "Hàng": "Tai nghe dây", "IMEI": null, "SL": "1", "Giá": "90.000đ", "Thành tiền": "90.000đ"}
{"Ngày": "46113", "STT": "3818", "Khách": "Đoàn Phúc Hiếu 0917760104", "Hàng": "Sạc 20W", "IMEI": null, "SL": "1", "Giá": "250000", "Thành tiền": "250000"}
```

#### Table `SoBanHang.xlsx :: T5-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46143", "STT": "4209", "Khách": "Nguyễn Thắng Châu - 0938 835 539", "Hàng": "IP12 64 CŨ", "IMEI": "358117143254530", "SL": "1", "Giá": "6300000", "Thành tiền": "6.300.000đ"}
{"Ngày": "01/05/2026", "STT": "4210", "Khách": "Diệp Hải Phương - 0322 942 195", "Hàng": "Ốp chống sốc SS", "IMEI": null, "SL": "1", "Giá": "150.000đ", "Thành tiền": "150k"}
{"Ngày": "46143", "STT": "4210", "Khách": "Diệp Hải Phương (0322942195)", "Hàng": "Mi14T 256 xám", "IMEI": "359946479709587", "SL": "1", "Giá": "12.990.000đ", "Thành tiền": "12,99tr"}
```

#### Table `SoBanHang.xlsx :: T6-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/06/2026", "STT": "4653", "Khách": "kl", "Hàng": "CL chống nhìn trộm", "IMEI": null, "SL": "1", "Giá": "180k", "Thành tiền": "180000"}
{"Ngày": "46174", "STT": "4654", "Khách": "Lương Khánh Nam (0791683655)", "Hàng": "Ốp lưng silicon iPhone", "IMEI": null, "SL": "1", "Giá": "120.000đ", "Thành tiền": "120000"}
{"Ngày": "46174", "STT": "4655", "Khách": "La Sơn Hoa - 0359 697 991", "Hàng": "Pin DP 10k", "IMEI": null, "SL": "1", "Giá": "390k", "Thành tiền": "390.000đ"}
```

#### Table `SoBanHang.xlsx :: T7-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/07/2026", "STT": "5053", "Khách": "Hà Linh Nhung 0797032377", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "105.000đ", "Thành tiền": "105000"}
{"Ngày": "01/07/2026", "STT": "5054", "Khách": "Khách lẻ", "Hàng": "Sạc MagSafe", "IMEI": null, "SL": "2", "Giá": "550.000đ", "Thành tiền": "1,1tr"}
{"Ngày": "01/07/2026", "STT": "5055", "Khách": "Khách lẻ", "Hàng": "Cáp C", "IMEI": null, "SL": "1", "Giá": "90.000đ", "Thành tiền": "90.000đ"}
```

#### Table `SoBanHang.xlsx :: T8-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "01/08/2026", "STT": "5505", "Khách": "Cao Đạt Hải - 0352 309 029", "Hàng": "Cáp C", "IMEI": null, "SL": "1", "Giá": "90.000đ", "Thành tiền": "90000"}
{"Ngày": "46235", "STT": "5505", "Khách": "Cao Đạt Hải - 0352 309 029", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "105000", "Thành tiền": "105000"}
{"Ngày": "01/08/2026", "STT": "5505", "Khách": "Cao Đạt Hải 0352309029", "Hàng": "Ốp  lưng chống sốc Samsung", "IMEI": null, "SL": "1", "Giá": "150.000đ", "Thành tiền": "150.000đ"}
```

#### Table `SoBanHang.xlsx :: T9-2026`
- **Rows:** 13 | **Header Row Index:** 1 | **Subtotal Keywords Detected:** No
- **Columns (11):** Ngày, STT, Khách, Hàng, IMEI, SL, Giá, Thành tiền, Bớt, Khách trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "46266", "STT": "5914", "Khách": "Trịnh Hải Ngọc (0354728959)", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "105000", "Thành tiền": "105000"}
{"Ngày": "01/09/2026", "STT": "5915", "Khách": "Bùi Đạt Tâm - 0905 123 498", "Hàng": "Cáp C", "IMEI": null, "SL": "1", "Giá": "90.000đ", "Thành tiền": "90000"}
{"Ngày": "46266", "STT": "5916", "Khách": "Doãn Đạt Hằng - 0911 803 238", "Hàng": "CL 9D", "IMEI": null, "SL": "1", "Giá": "105.000đ", "Thành tiền": "105000"}
```

#### Table `SoNo.xlsx :: Sổ nợ`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (7):** Ngày, Khách, SĐT, Nợ, Đã trả, Ngày trả, Ghi chú
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "02/07/2025", "Khách": "Quách Cường Lan", "SĐT": "0909377857", "Nợ": "270k", "Đã trả": "270k", "Ngày trả": "30/07/2025", "Ghi chú": "STT 26"}
{"Ngày": "45841", "Khách": "Giang Quân An", "SĐT": "0359938682", "Nợ": "240.000đ", "Đã trả": "80k", "Ngày trả": "17/07/2025", "Ghi chú": "STT 34"}
{"Ngày": null, "Khách": null, "SĐT": null, "Nợ": null, "Đã trả": "80k", "Ngày trả": "45863", "Ghi chú": "STT 34"}
```

#### Table `SoNo.xlsx :: Trả góp`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (12):** Ngày, STT, Khách, SĐT, Máy, Giá, Trả trước, Số kỳ, Góp/tháng, Hạn góp (ngày), Ngày góp, Đã góp
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45841", "STT": "33", "Khách": "Đinh Mai Hoa", "SĐT": "0988028309", "Máy": "iPhone 16 128GB Đen", "Giá": "19.980.000đ", "Trả trước": "4,38tr", "Số kỳ": "6"}
{"Ngày": null, "STT": "33", "Khách": null, "SĐT": null, "Máy": null, "Giá": null, "Trả trước": null, "Số kỳ": null}
{"Ngày": null, "STT": "33", "Khách": null, "SĐT": null, "Máy": null, "Giá": null, "Trả trước": null, "Số kỳ": null}
```

#### Table `SoNo.xlsx :: Bảo hành`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày nhận, Khách, SĐT, Máy, IMEI, Ngày mua, Lỗi, Xử lý
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày nhận": "45860", "Khách": "Phan Trung Hoàng", "SĐT": "0703695348", "Máy": "Xiaomi Redmi Note 14", "IMEI": "353862268796170", "Ngày mua": "03/07/2025", "Lỗi": "màn hình sọc", "Xử lý": "thay linh kiện"}
{"Ngày nhận": "11/08/2025", "Khách": "Thân Bình Hiếu", "SĐT": "0324923706", "Máy": "iPhone 15", "IMEI": "356354004843729", "Ngày mua": "03/08/2025", "Lỗi": "màn hình sọc", "Xử lý": "đổi máy khác"}
{"Ngày nhận": "45882", "Khách": "Hoàng Hùng Hoàng", "SĐT": "0327519549", "Máy": "iPhone 15", "IMEI": "358208076832937", "Ngày mua": "06/08/2025", "Lỗi": "pin tụt nhanh", "Xử lý": "sửa tại tiệm"}
```

#### Table `ThuMayCu.xlsx :: Sheet1`
- **Rows:** 14 | **Header Row Index:** 0 | **Subtotal Keywords Detected:** No
- **Columns (8):** Ngày, Khách, SĐT, Máy thu, Tình trạng, IMEI, Giá thu, Trừ vào (STT sổ bán)
  - *Date cols:* None
  - *Amount/Qty cols:* None
  - *Status cols:* None
  - *ID/Code cols:* None
- **Sample 3 rows:**
```json
{"Ngày": "45841", "Khách": "Trần Phương Hồng", "SĐT": "0973495724", "Máy thu": "Samsung Galaxy A32", "Tình trạng": "trầy nhẹ", "IMEI": "354987866187974", "Giá thu": "1.200.000đ", "Trừ vào (STT sổ bán)": "30"}
{"Ngày": "04/07/2025", "Khách": "Triệu Linh An", "SĐT": "0327988481", "Máy thu": "Samsung Galaxy S21", "Tình trạng": "bể kính lưng", "IMEI": "357656628792010", "Giá thu": "3000k", "Trừ vào (STT sổ bán)": "53"}
{"Ngày": "05/07/2025", "Khách": "Bùi Châu Ngọc", "SĐT": "0791558407", "Máy thu": "iPhone 11 64GB", "Tình trạng": "đẹp 99%", "IMEI": "359403787348310", "Giá thu": "3.000.000đ", "Trừ vào (STT sổ bán)": "63"}
```

---
