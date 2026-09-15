"""Cấu trúc dữ liệu cho bảng chơi Tetris.

Người phụ trách: Hồ Văn Trọng (26730077)

Bảng chơi là một lưới ``ROWS`` hàng × ``COLS`` cột. Mỗi ô lưu một trong hai giá
trị:

- ``None`` — ô trống
- một chuỗi như ``"T"`` — ô đã bị một khối loại T chiếm, dùng để biết tô màu gì

Truy cập theo thứ tự **hàng trước, cột sau**: ``grid[hàng][cột]``. Đây là chỗ
dễ nhầm nhất, vì ở mọi nơi khác trong code toạ độ lại viết ``(cột, hàng)``.
Để khỏi nhầm, các bạn nên dùng hàm ``get()`` thay vì chọc thẳng vào ``grid``.
"""

from __future__ import annotations

from . import config
from .tetromino import Cell, Piece


class Board:
    """Lưới các ô đã bị khối chiếm."""

    def __init__(self, cols: int = config.COLS, rows: int = config.ROWS) -> None:
        self.cols = cols
        self.rows = rows
        self.grid: list[list[str | None]] = [
            [None] * cols for _ in range(rows)
        ]

    # --- Đọc ô ---------------------------------------------------------------

    def inside(self, col: int, row: int) -> bool:
        """Ô ``(col, row)`` có nằm trong bảng không."""
        return 0 <= col < self.cols and 0 <= row < self.rows

    def get(self, col: int, row: int) -> str | None:
        """Loại khối đang chiếm ô ``(col, row)``, hoặc ``None`` nếu ô trống."""
        return self.grid[row][col]

    def is_free(self, col: int, row: int) -> bool:
        """Ô nằm trong bảng và đang trống."""
        return self.inside(col, row) and self.grid[row][col] is None

    def filled_cells(self) -> list[tuple[Cell, str]]:
        """Danh sách ``((cột, hàng), loại_khối)`` của mọi ô đã bị chiếm.

        Dùng cho phần vẽ: duyệt danh sách này rồi tô màu từng ô.
        """
        return [((col, row), kind)
                for row, line in enumerate(self.grid)
                for col, kind in enumerate(line)
                if kind is not None]

    # --- Kiểm tra và ghi khối ------------------------------------------------

    def is_valid(self, piece: Piece) -> bool:
        """Khối có đặt được ở vị trí hiện tại không.

        Hợp lệ khi cả 4 ô của khối đều nằm trong bảng và không đè lên ô nào đã
        bị chiếm. Đây là hàm quan trọng nhất của bảng: dịch trái phải, xoay, rơi
        xuống đều hỏi hàm này trước khi cho khối đi.
        """
        return all(self.is_free(col, row) for col, row in piece.cells())

    def lock(self, piece: Piece) -> None:
        """Ghi khối vào bảng khi nó đã chạm đáy, không di chuyển được nữa.

        Raises:
            ValueError: nếu khối đang ở vị trí không hợp lệ. Gặp lỗi này nghĩa là
                code gọi ``lock`` đã quên kiểm tra ``is_valid`` trước.
        """
        if not self.is_valid(piece):
            raise ValueError(f"Không thể khoá khối ở vị trí không hợp lệ: {piece}")
        for col, row in piece.cells():
            self.grid[row][col] = piece.kind

    def full_rows(self) -> list[int]:
        """Chỉ số các hàng đã được lấp đầy, từ trên xuống."""
        return [row for row, line in enumerate(self.grid)
                if all(kind is not None for kind in line)]

    def clear_full_rows(self) -> int:
        """Xoá mọi hàng đầy, đẩy các hàng phía trên rơi xuống.

        Returns:
            Số hàng vừa xoá, từ 0 tới 4. Dùng để cộng điểm.
        """
        remaining = [line for line in self.grid
                     if any(kind is None for kind in line)]
        cleared = self.rows - len(remaining)
        empty_rows = [[None] * self.cols for _ in range(cleared)]
        self.grid = empty_rows + remaining
        return cleared
