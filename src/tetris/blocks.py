"""Vẽ khối: khối đang rơi, các ô đã khoá trên bảng, khối kế tiếp.

Người phụ trách: Trương Đình Nguyên (26730052)

Các hàm dưới đây hiện chưa vẽ gì — gọi vào vẫn chạy, chỉ là chưa thấy khối.
Thay từng chỗ ``TODO(Nguyên)`` bằng code thật, chạy ``python main.py`` là thấy
kết quả ngay.

Dữ liệu đầu vào đã có sẵn, không cần tự tính:
    - ``piece.cells()``  — 4 toạ độ ``(cột, hàng)`` của khối trên bảng
    - ``piece.color``    — màu của khối
    - ``board.filled_cells()`` — mọi ô đã khoá, kèm loại khối
    - ``config.PIECE_COLORS[loại]`` — màu theo loại khối
"""

from __future__ import annotations

import pygame

from . import config
from .board import Board
from .tetromino import ROTATIONS, Piece


def cell_rect(col: int, row: int) -> pygame.Rect:
    """Hình chữ nhật pixel của ô ``(col, row)`` trên bảng. Đã viết sẵn.

    Đây là chỗ đổi từ toạ độ ô lưới sang toạ độ pixel — mọi hàm vẽ khối nên
    dùng hàm này thay vì tự nhân ``CELL_SIZE``.
    """
    return pygame.Rect(
        config.BOARD_LEFT + col * config.CELL_SIZE,
        config.BOARD_TOP + row * config.CELL_SIZE,
        config.CELL_SIZE,
        config.CELL_SIZE,
    )


def draw_cell(
    surface: pygame.Surface,
    rect: pygame.Rect,
    color: tuple[int, int, int],
) -> None:
    """Vẽ một ô vuông của khối vào vị trí ``rect``.

    Gợi ý: tô màu chính, rồi thêm viền sáng ở cạnh trên và trái, viền tối ở cạnh
    dưới và phải để ô trông nổi khối như Tetris thật.
    """
    # TODO(Nguyên)


def draw_piece(surface: pygame.Surface, piece: Piece) -> None:
    """Vẽ khối đang rơi: gọi ``draw_cell`` cho từng ô trong ``piece.cells()``."""
    # TODO(Nguyên)


def draw_locked_cells(surface: pygame.Surface, board: Board) -> None:
    """Vẽ mọi ô đã khoá trên bảng, lấy từ ``board.filled_cells()``."""
    # TODO(Nguyên)


def draw_next_piece(
    surface: pygame.Surface,
    kind: str,
    left: int,
    top: int,
) -> None:
    """Vẽ khối kế tiếp trong khung xem trước ở cột bên phải.

    Hình dạng lấy từ ``ROTATIONS[kind][0]`` — danh sách toạ độ ô trong hộp chứa.
    ``left``, ``top`` là góc trên bên trái chỗ được phép vẽ, tính bằng pixel.
    """
    # TODO(Nguyên)
    _ = ROTATIONS  # dùng tới khi cài đặt
