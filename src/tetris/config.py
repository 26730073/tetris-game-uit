"""Các hằng số cấu hình dùng chung cho cả nhóm.

Người phụ trách: Hồ Văn Trọng (26730077)

Mọi con số dùng ở nhiều file đều đặt tên ở đây. Muốn đổi kích thước bảng,
tốc độ rơi hay màu của khối thì sửa một chỗ này, cả game đổi theo.
"""

# --- Bảng chơi -------------------------------------------------------------
COLS = 10               # Số cột, theo chuẩn Tetris
ROWS = 20               # Số hàng nhìn thấy được
CELL_SIZE = 30          # Kích thước một ô vuông (pixel)

# --- Bố cục cửa sổ ---------------------------------------------------------
MARGIN = 20             # Khoảng trống quanh bảng chơi (pixel)
SIDE_PANEL_WIDTH = 180  # Cột bên phải: điểm, cấp độ, khối kế tiếp

BOARD_LEFT = MARGIN
BOARD_TOP = MARGIN
BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

SIDE_PANEL_LEFT = BOARD_LEFT + BOARD_WIDTH + MARGIN

WINDOW_WIDTH = SIDE_PANEL_LEFT + SIDE_PANEL_WIDTH + MARGIN
WINDOW_HEIGHT = BOARD_TOP + BOARD_HEIGHT + MARGIN
WINDOW_TITLE = "Tetris - Nhom KNNN - UIT"

FPS = 60

# --- Tốc độ rơi ------------------------------------------------------------
FALL_INTERVAL = 0.8     # Số giây để khối rơi xuống một hàng, ở cấp độ đầu
SOFT_DROP_INTERVAL = 0.05  # Khi giữ phím xuống

# --- Màu sắc (R, G, B) -----------------------------------------------------
COLOR_BACKGROUND = (16, 18, 28)
COLOR_BOARD = (24, 27, 40)
COLOR_GRID = (36, 40, 58)
COLOR_BORDER = (92, 100, 132)
COLOR_TEXT = (232, 236, 244)
COLOR_TEXT_DIM = (136, 144, 166)

# Màu của 7 loại khối, theo quy ước màu phổ biến của Tetris hiện đại
PIECE_COLORS = {
    "I": (0, 200, 230),     # xanh lơ
    "O": (240, 200, 0),     # vàng
    "T": (160, 70, 200),    # tím
    "S": (70, 190, 90),     # xanh lá
    "Z": (220, 60, 60),     # đỏ
    "J": (50, 100, 220),    # xanh dương
    "L": (240, 140, 30),    # cam
}

# --- Điểm số ---------------------------------------------------------------
# Điểm thưởng khi xoá cùng lúc 1, 2, 3, 4 hàng
LINE_SCORES = {1: 100, 2: 300, 3: 500, 4: 800}
