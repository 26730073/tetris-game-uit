"""Cấu trúc dữ liệu cho một khối Tetris (tetromino).

Người phụ trách: Hồ Văn Trọng (26730077)

Cách biểu diễn
--------------
Mỗi loại khối được vẽ trong một hộp vuông cạnh ``n`` ô (``n`` = 4 với khối I,
2 với khối O, 3 với các khối còn lại). Hình dạng lưu dưới dạng danh sách toạ độ
``(cột, hàng)`` của các ô được tô, tính từ góc trên bên trái của hộp.

Toạ độ trên bảng chơi cũng theo quy ước ``(cột, hàng)``: cột tăng sang phải,
hàng tăng **xuống dưới**. Hàng 0 là hàng trên cùng.

Khối là bất biến
----------------
``Piece`` không bao giờ tự thay đổi. Muốn dịch hay xoay thì gọi ``moved()`` hoặc
``rotated()`` để lấy về một khối *mới*. Nhờ vậy việc kiểm tra rất gọn::

    thu = piece.moved(1, 0)
    if board.is_valid(thu):
        piece = thu          # hợp lệ thì mới nhận vị trí mới
"""

from __future__ import annotations

import random
from dataclasses import dataclass, replace

from . import config

Cell = tuple[int, int]

# Hình dạng gốc của 7 loại khối, ở trạng thái chưa xoay.
_BASE_SHAPES: dict[str, list[str]] = {
    "I": ["....",
          "####",
          "....",
          "...."],
    "O": ["##",
          "##"],
    "T": [".#.",
          "###",
          "..."],
    "S": [".##",
          "##.",
          "..."],
    "Z": ["##.",
          ".##",
          "..."],
    "J": ["#..",
          "###",
          "..."],
    "L": ["..#",
          "###",
          "..."],
}

KINDS: tuple[str, ...] = tuple(_BASE_SHAPES)


def _parse(rows: list[str]) -> list[Cell]:
    """Đổi hình vẽ bằng ký tự thành danh sách toạ độ các ô được tô."""
    return [(col, row)
            for row, line in enumerate(rows)
            for col, char in enumerate(line)
            if char == "#"]


def _rotate_clockwise(cells: list[Cell], size: int) -> list[Cell]:
    """Xoay 90 độ theo chiều kim đồng hồ bên trong hộp vuông cạnh ``size``.

    Ô ở ``(cột, hàng)`` sẽ tới ``(size - 1 - hàng, cột)``. Vì xoay trong hộp cố
    định chứ không xoay quanh một ô, khối không bị trôi dạt sau bốn lần xoay.
    """
    return sorted((size - 1 - row, col) for col, row in cells)


def _build_rotations() -> dict[str, list[list[Cell]]]:
    """Tính sẵn đủ 4 trạng thái xoay cho từng loại khối, chỉ làm một lần."""
    result = {}
    for kind, rows in _BASE_SHAPES.items():
        size = len(rows)
        states = [sorted(_parse(rows))]
        for _ in range(3):
            states.append(_rotate_clockwise(states[-1], size))
        result[kind] = states
    return result


# ROTATIONS["T"][1] là khối T sau khi xoay phải một lần.
ROTATIONS: dict[str, list[list[Cell]]] = _build_rotations()
BOX_SIZE: dict[str, int] = {kind: len(rows) for kind, rows in _BASE_SHAPES.items()}


@dataclass(frozen=True)
class Piece:
    """Một khối đang nằm trên bảng chơi.

    Attributes:
        kind: loại khối, một trong ``"I", "O", "T", "S", "Z", "J", "L"``.
        col: cột của góc trên bên trái hộp chứa khối.
        row: hàng của góc trên bên trái hộp chứa khối.
        rotation: trạng thái xoay, từ 0 tới 3.
    """

    kind: str
    col: int
    row: int
    rotation: int = 0

    def __post_init__(self) -> None:
        if self.kind not in ROTATIONS:
            raise ValueError(f"Không có loại khối {self.kind!r}")

    @classmethod
    def spawn(cls, kind: str) -> Piece:
        """Tạo khối mới ở giữa mép trên của bảng chơi."""
        return cls(kind, col=(config.COLS - BOX_SIZE[kind]) // 2, row=0)

    @property
    def color(self) -> tuple[int, int, int]:
        return config.PIECE_COLORS[self.kind]

    def cells(self) -> list[Cell]:
        """Toạ độ ``(cột, hàng)`` trên bảng chơi của 4 ô thuộc khối này."""
        return [(self.col + dc, self.row + dr)
                for dc, dr in ROTATIONS[self.kind][self.rotation]]

    def moved(self, dcol: int, drow: int) -> Piece:
        """Khối mới dịch đi ``dcol`` cột, ``drow`` hàng. Khối cũ giữ nguyên."""
        return replace(self, col=self.col + dcol, row=self.row + drow)

    def rotated(self, turns: int = 1) -> Piece:
        """Khối mới xoay ``turns`` lần, số dương là xoay theo chiều kim đồng hồ."""
        return replace(self, rotation=(self.rotation + turns) % 4)


def random_kind(rng: random.Random | None = None) -> str:
    """Chọn ngẫu nhiên một loại khối."""
    return (rng or random).choice(KINDS)
