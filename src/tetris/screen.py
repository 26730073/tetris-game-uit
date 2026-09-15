"""Vẽ màn hình: nền, khung bảng chơi, lưới, cột thông tin bên phải.

Người phụ trách: Đặng Đức Tín (26730073)

Các hàm dưới đây hiện chưa vẽ gì — gọi vào vẫn chạy, chỉ là màn hình trống.
Nhờ vậy cả nhóm chạy được game ngay từ đầu, và Tín vẽ tới đâu thấy tới đó.
Thay từng chỗ ``TODO(Tín)`` bằng code thật.

Toạ độ pixel của bảng chơi lấy từ ``config``: ``BOARD_LEFT``, ``BOARD_TOP``,
``BOARD_WIDTH``, ``BOARD_HEIGHT``, ``CELL_SIZE``. Đừng viết số cứng.
"""

from __future__ import annotations

import pygame

from . import config


def draw_text(
    surface: pygame.Surface,
    text: str,
    size: int,
    pos: tuple[int, int],
    color: tuple[int, int, int] = config.COLOR_TEXT,
    center: bool = False,
) -> None:
    """Vẽ một dòng chữ. Hàm tiện ích này đã viết sẵn, dùng luôn được."""
    font = pygame.font.Font(None, size)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=pos) if center else rendered.get_rect(topleft=pos)
    surface.blit(rendered, rect)


def draw_background(surface: pygame.Surface) -> None:
    """Tô nền toàn cửa sổ. Đã viết sẵn."""
    surface.fill(config.COLOR_BACKGROUND)


def draw_board_frame(surface: pygame.Surface) -> None:
    """Vẽ nền bảng chơi, các đường lưới và viền quanh bảng.

    Gợi ý:
        - ``pygame.Rect(config.BOARD_LEFT, config.BOARD_TOP,
          config.BOARD_WIDTH, config.BOARD_HEIGHT)`` là vùng bảng chơi
        - tô vùng đó bằng ``COLOR_BOARD``
        - kẻ ``COLS - 1`` đường dọc và ``ROWS - 1`` đường ngang màu ``COLOR_GRID``
        - vẽ viền ngoài màu ``COLOR_BORDER``
    """
    # TODO(Tín)


def draw_side_panel(
    surface: pygame.Surface,
    score: int,
    level: int,
    lines: int,
) -> None:
    """Vẽ cột thông tin bên phải: điểm, cấp độ, số hàng đã xoá.

    Vị trí bắt đầu: ``config.SIDE_PANEL_LEFT``, rộng ``SIDE_PANEL_WIDTH``.
    Chừa một khoảng phía trên để Nguyên vẽ khối kế tiếp vào (hàm
    ``blocks.draw_next_piece``).
    """
    # TODO(Tín)


def draw_game_over(surface: pygame.Surface, score: int) -> None:
    """Lớp phủ khi thua: chữ GAME OVER, điểm, hướng dẫn phím chơi lại."""
    # TODO(Tín)


def draw_paused(surface: pygame.Surface) -> None:
    """Lớp phủ khi tạm dừng."""
    # TODO(Tín)
