# Phân công công việc

> Bản đề xuất ban đầu. Ai muốn đổi việc thì trao đổi trong kênh Slack của nhóm.

Mỗi người làm trên **file riêng**, nên năm người code song song mà gần như không bao
giờ đụng vào cùng một dòng — Git gộp code tự động được.

---

## Hồ Văn Trọng — Nhóm trưởng, Project Manager

**Code:** `tetromino.py`, `board.py`, `game.py`, `config.py`

- [x] Đưa cấu trúc dữ liệu cơ bản lên Git: khối, bảng chơi, kèm 25 bài kiểm thử
- [x] Vòng lặp game: nhận phím, dịch, xoay, khoá khối, xoá hàng, tính điểm, cấp độ
- [ ] Duyệt Pull Request của các bạn, thấy ổn thì merge
- [ ] Tắt dòng chữ tạm `SHOW_SETUP_MESSAGE` khi phần vẽ đã xong

**Báo cáo:**
- [ ] Hợp đồng nhóm, gom chữ ký đủ 5 người
- [ ] Mục "Các link công cụ nhóm đã dùng"

---

## Đặng Đức Tín — Vẽ màn hình

**File:** `src/tetris/screen.py`

- [ ] `draw_board_frame` — nền bảng chơi, đường lưới, viền
- [ ] `draw_side_panel` — điểm, cấp độ, số hàng đã xoá
- [ ] `draw_paused` — lớp phủ khi tạm dừng
- [ ] `draw_game_over` — lớp phủ khi thua

**Coi như xong khi:** chạy game thấy bảng 10×20 có lưới, cột bên phải hiện điểm và
cấp độ, bấm `P` thấy chữ tạm dừng.

---

## Trương Đình Nguyên — Vẽ khối

**File:** `src/tetris/blocks.py`

- [ ] `draw_cell` — vẽ một ô vuông có hiệu ứng nổi khối
- [ ] `draw_piece` — vẽ khối đang rơi
- [ ] `draw_locked_cells` — vẽ các ô đã khoá trên bảng
- [ ] `draw_next_piece` — vẽ khối kế tiếp ở cột bên phải

**Coi như xong khi:** chạy game thấy khối đúng màu, bấm `←` `→` `↑` thấy khối dịch
và xoay đúng.

Hàm `cell_rect(col, row)` đổi toạ độ ô sang pixel đã viết sẵn, dùng luôn.

---

## Vũ Anh Tuấn — Cho khối rơi xuống

**File:** `src/tetris/falling.py`

- [ ] `FallController.update` — cộng thời gian, đủ nhịp thì cho khối rơi một hàng,
      chạm đáy thì báo `landed=True`
- [ ] `FallController.hard_drop` — thả thẳng xuống đáy khi bấm `Space`
- [ ] Viết kiểm thử cho hai hàm trên trong `tests/test_falling.py`

**Coi như xong khi:** khối tự rơi đều, chạm đáy thì khoá lại và khối mới xuất hiện,
giữ `↓` thì rơi nhanh, bấm `Space` thì rơi thẳng xuống đáy.

Phần này không cần vẽ gì, nên kiểm thử tự động được hoàn toàn mà không cần mở cửa
sổ game.

---

## Phan Nguyễn Minh Thảo — Chủ biên báo cáo giới thiệu Tetris

**Nơi làm:** Google Docs của nhóm

Theo yêu cầu của thầy, dựa trên các phiên bản Tetris phổ biến, **chưa cần lập trình**:

- [ ] Tetris là gì — nguồn gốc, vì sao nổi tiếng
- [ ] Các chức năng chính của game
- [ ] Cách chơi dành cho người dùng cuối: điều khiển, cách tính điểm, khi nào thua
- [ ] Trình bày hấp dẫn, dễ hiểu, có hình minh hoạ
- [ ] Độ dài 2–10 trang

**Coi như xong khi:** một người chưa từng chơi Tetris đọc xong biết cách chơi.

Các bạn còn lại gửi cho Thảo ảnh chụp phần mình làm để minh hoạ khi game chạy được.

---

## Việc chung của cả nhóm

- [ ] Ký hợp đồng nhóm (scan chữ ký tay hoặc chữ ký điện tử)
- [ ] Mỗi người clone repo và chạy được `python main.py`
