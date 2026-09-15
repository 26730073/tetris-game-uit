# 🧱 Tetris — Đồ án Kỹ năng nghề nghiệp, UIT

Game xếp gạch Tetris viết bằng **Python + Pygame**.
Đồ án môn Kỹ năng nghề nghiệp của nhóm 5 thành viên, Trường Đại học Công nghệ Thông tin — ĐHQG TP.HCM.

---

## 👥 Thành viên nhóm

| # | Họ và tên | MSSV | GitHub | Vai trò | Phụ trách | File |
|---|-----------|------|--------|---------|-----------|------|
| 1 | Hồ Văn Trọng | 26730077 | [@tronghv77](https://github.com/tronghv77) | Nhóm trưởng, Project Manager | Cấu trúc dữ liệu, ghép nối, duyệt code | `board.py`, `tetromino.py`, `game.py` |
| 2 | Trương Đình Nguyên | 26730052 | [@nguyen26730052](https://github.com/nguyen26730052) | Thành viên | Vẽ khối | `blocks.py` |
| 3 | Vũ Anh Tuấn | 26730080 | [@26730080](https://github.com/26730080) | Thành viên | Lập trình cho khối rơi xuống | `falling.py` |
| 4 | Phan Nguyễn Minh Thảo | 26730063 | [@26730063](https://github.com/26730063) | Thành viên | Chủ biên báo cáo giới thiệu và hướng dẫn chơi | Google Docs |
| 5 | Đặng Đức Tín | 26730073 | [@26730073](https://github.com/26730073) | Thành viên | Vẽ màn hình | `screen.py` |

Chi tiết từng việc: [docs/PHAN-CONG.md](docs/PHAN-CONG.md)

---

## 🛠️ Công cụ nhóm sử dụng

| Công cụ | Dùng để | Link |
|---------|---------|------|
| GitHub | Quản lý mã nguồn, giao việc qua Issues, duyệt code qua Pull Request | https://github.com/tronghv77/tetris-game-uit |
| Slack | Kênh thảo luận chính của nhóm | `#đồ-án-knnn-trọng-tín-tuấn-thảo-nguyên` |
| Google Docs | Cùng viết báo cáo | *(cập nhật khi tạo xong)* |

---

## 🚀 Cách chạy game

Yêu cầu: **Python 3.10 trở lên**.

```bash
git clone https://github.com/tronghv77/tetris-game-uit.git
cd tetris-game-uit

python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
python main.py
```

Giai đoạn hiện tại, chạy lên sẽ thấy cửa sổ có dòng chữ **"Khung du an da chay duoc!"** — nghĩa là máy đã cài đặt đúng.

### Điều khiển

| Phím | Tác dụng |
|------|----------|
| `←` `→` | Dịch khối sang trái, phải |
| `↑` | Xoay khối |
| `↓` (giữ) | Rơi nhanh |
| `Space` | Thả thẳng xuống đáy |
| `P` | Tạm dừng |
| `R` | Chơi lại sau khi thua |
| `Esc` | Thoát |

---

## 📁 Cấu trúc thư mục

```
tetris-game-uit/
├── main.py                 # File chạy game
├── src/tetris/
│   ├── config.py           # Hằng số dùng chung: kích thước, màu, tốc độ   (Trọng)
│   ├── tetromino.py        # CTDL: 7 loại khối và 4 trạng thái xoay        (Trọng)
│   ├── board.py            # CTDL: lưới bảng chơi, kiểm tra, xoá hàng      (Trọng)
│   ├── game.py             # Vòng lặp, nhận phím, ghép các phần lại        (Trọng)
│   ├── screen.py           # Vẽ màn hình: khung, lưới, điểm số             (Tín)
│   ├── blocks.py           # Vẽ khối: khối đang rơi, ô đã khoá, khối kế    (Nguyên)
│   └── falling.py          # Cho khối rơi xuống theo thời gian             (Tuấn)
├── tests/                  # Kiểm thử tự động
└── docs/                   # Tài liệu nhóm
```

### Cấu trúc dữ liệu cơ bản

**Khối** (`tetromino.py`) — mỗi loại khối lưu sẵn 4 trạng thái xoay, mỗi trạng thái là danh sách 4 toạ độ `(cột, hàng)`. Khối là **bất biến**: `piece.moved(1, 0)` và `piece.rotated()` trả về khối *mới*, khối cũ giữ nguyên. Nhờ vậy kiểm tra một nước đi rất gọn:

```python
thu = piece.moved(1, 0)
if board.is_valid(thu):
    piece = thu
```

**Bảng chơi** (`board.py`) — lưới 20 hàng × 10 cột, mỗi ô là `None` (trống) hoặc tên loại khối đang chiếm (để biết tô màu gì). Các thao tác chính: `is_valid(piece)`, `lock(piece)`, `clear_full_rows()`.

---

## 🧪 Kiểm thử

```bash
python -m pytest -v
```

---

## 🤝 Quy trình làm việc

Theo yêu cầu của môn học:

1. Nhóm trưởng đưa cấu trúc dữ liệu cơ bản lên Git ✅
2. Mỗi thành viên nhận một việc riêng
3. Các thành viên code song song, xong thì gửi lên Git bằng **Pull Request**
4. Nhóm trưởng duyệt code, thấy ổn thì merge

**Không ai push thẳng lên nhánh `main`.** Hướng dẫn chi tiết cho người mới dùng Git: [docs/HUONG-DAN-GIT.md](docs/HUONG-DAN-GIT.md)

---

## 📄 Giấy phép

[MIT License](LICENSE)
