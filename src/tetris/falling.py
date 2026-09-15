"""Cho khối rơi xuống theo thời gian.

Người phụ trách: Vũ Anh Tuấn (26730080)

``FallController`` giữ nhịp rơi. Mỗi khung hình, ``game.py`` gọi ``update()``
và truyền vào số giây vừa trôi qua. Đủ một nhịp thì khối rơi xuống một hàng.
Rơi tiếp không được nữa nghĩa là khối đã **chạm đáy** — lúc đó ``game.py`` sẽ
khoá khối vào bảng và sinh khối mới.

Hiện các hàm dưới đây chưa làm gì nên khối đứng yên trên đầu bảng. Thay từng
chỗ ``TODO(Tuấn)`` bằng code thật.
"""

from __future__ import annotations

from dataclasses import dataclass

from . import config
from .board import Board
from .tetromino import Piece


@dataclass
class FallResult:
    """Kết quả sau một lần cập nhật.

    Attributes:
        piece: vị trí mới của khối (có thể giữ nguyên nếu chưa đủ nhịp).
        landed: ``True`` nếu khối đã chạm đáy, không rơi thêm được nữa.
    """

    piece: Piece
    landed: bool = False


class FallController:
    """Bộ đếm nhịp rơi của khối."""

    def __init__(self, interval: float = config.FALL_INTERVAL) -> None:
        self.interval = interval   # số giây rơi một hàng
        self.timer = 0.0           # thời gian tích luỹ từ lần rơi trước
        self.soft_drop = False     # True khi người chơi đang giữ phím xuống

    def update(self, dt: float, board: Board, piece: Piece) -> FallResult:
        """Cộng thời gian, đủ nhịp thì cho khối rơi một hàng.

        Args:
            dt: số giây trôi qua kể từ khung hình trước.
            board: bảng chơi, để hỏi ``board.is_valid()``.
            piece: khối đang rơi.

        Gợi ý:
            1. Cộng ``dt`` vào ``self.timer``.
            2. Nhịp hiện tại là ``SOFT_DROP_INTERVAL`` nếu ``self.soft_drop``,
               ngược lại là ``self.interval``.
            3. Nếu ``self.timer`` chưa đủ một nhịp → trả về khối giữ nguyên.
            4. Đủ nhịp: trừ bớt một nhịp khỏi ``self.timer``, thử
               ``piece.moved(0, 1)``. Hợp lệ thì trả về khối mới. Không hợp lệ
               thì trả về khối cũ kèm ``landed=True``.
        """
        # TODO(Tuấn)
        return FallResult(piece)

    def hard_drop(self, board: Board, piece: Piece) -> Piece:
        """Thả rơi thẳng xuống đáy ngay lập tức (phím Space).

        Gợi ý: lặp ``piece.moved(0, 1)`` chừng nào còn hợp lệ, trả về vị trí
        cuối cùng còn hợp lệ.
        """
        # TODO(Tuấn)
        return piece

    def reset(self) -> None:
        """Đặt lại bộ đếm khi có khối mới."""
        self.timer = 0.0
