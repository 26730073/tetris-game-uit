"""Vòng lặp game: nhận phím, điều phối rơi, khoá khối, xoá hàng, tính điểm.

Người phụ trách: Hồ Văn Trọng (26730077)

File này là chỗ ghép phần việc của cả nhóm lại:

    board.py, tetromino.py  — cấu trúc dữ liệu        (Trọng)
    screen.py               — vẽ màn hình             (Tín)
    blocks.py               — vẽ khối                 (Nguyên)
    falling.py              — cho khối rơi xuống      (Tuấn)

Phần của mỗi bạn chưa xong thì game vẫn chạy, chỉ là thiếu phần đó.
"""

from __future__ import annotations

from enum import Enum, auto

import pygame

from . import blocks, config, falling, screen
from .board import Board
from .tetromino import Piece, random_kind

# Hiện dòng chữ báo khung dự án đã chạy được. Tắt đi khi Tín và Nguyên vẽ xong.
SHOW_SETUP_MESSAGE = True


class GameState(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


class Game:
    """Điều phối toàn bộ game."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(config.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.new_game()

    # --- Ván chơi --------------------------------------------------------------

    def new_game(self) -> None:
        """Dọn sạch bảng và bắt đầu ván mới."""
        self.board = Board()
        self.fall = falling.FallController()
        self.score = 0
        self.lines = 0
        self.level = 1
        self.next_kind = random_kind()
        self.piece = self.take_next_piece()
        self.state = GameState.PLAYING

    def take_next_piece(self) -> Piece:
        """Lấy khối kế tiếp ra bảng, và chọn sẵn một khối kế tiếp mới."""
        piece = Piece.spawn(self.next_kind)
        self.next_kind = random_kind()
        return piece

    def lock_piece(self) -> None:
        """Khoá khối vào bảng, xoá hàng đầy, cộng điểm, sinh khối mới."""
        self.board.lock(self.piece)

        cleared = self.board.clear_full_rows()
        if cleared:
            self.lines += cleared
            self.score += config.LINE_SCORES[cleared] * self.level
            self.level = 1 + self.lines // 10
            # Mỗi cấp độ rơi nhanh hơn 15%, nhưng không nhanh hơn 0.1 giây/hàng.
            self.fall.interval = max(
                0.1, config.FALL_INTERVAL * 0.85 ** (self.level - 1)
            )

        self.piece = self.take_next_piece()
        self.fall.reset()

        # Khối mới vừa sinh ra đã bị đè thì bảng đã đầy tới đỉnh.
        if not self.board.is_valid(self.piece):
            self.state = GameState.GAME_OVER

    # --- Điều khiển khối -------------------------------------------------------

    def try_move(self, dcol: int) -> None:
        """Dịch khối sang trái (-1) hoặc phải (+1) nếu còn chỗ."""
        moved = self.piece.moved(dcol, 0)
        if self.board.is_valid(moved):
            self.piece = moved

    def try_rotate(self) -> None:
        """Xoay khối. Kẹt sát tường thì thử đẩy sang một ô rồi mới xoay.

        Không có bước đẩy này, khối I nằm sát tường sẽ không bao giờ xoay được,
        người chơi rất khó chịu.
        """
        rotated = self.piece.rotated()
        for dcol in (0, -1, 1, -2, 2):
            candidate = rotated.moved(dcol, 0)
            if self.board.is_valid(candidate):
                self.piece = candidate
                return

    def hard_drop(self) -> None:
        self.piece = self.fall.hard_drop(self.board, self.piece)
        self.lock_piece()

    # --- Nhận phím -------------------------------------------------------------

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                self.fall.soft_drop = False

    def handle_keydown(self, key: int) -> None:
        if key == pygame.K_ESCAPE:
            self.running = False
            return

        if self.state is GameState.GAME_OVER:
            if key == pygame.K_r:
                self.new_game()
            return

        if key == pygame.K_p:
            self.state = (GameState.PLAYING if self.state is GameState.PAUSED
                          else GameState.PAUSED)
            return

        if self.state is not GameState.PLAYING:
            return

        if key == pygame.K_LEFT:
            self.try_move(-1)
        elif key == pygame.K_RIGHT:
            self.try_move(1)
        elif key == pygame.K_UP:
            self.try_rotate()
        elif key == pygame.K_DOWN:
            self.fall.soft_drop = True
        elif key == pygame.K_SPACE:
            self.hard_drop()

    # --- Cập nhật và vẽ ------------------------------------------------------

    def update(self, dt: float) -> None:
        if self.state is not GameState.PLAYING:
            return
        result = self.fall.update(dt, self.board, self.piece)
        self.piece = result.piece
        if result.landed:
            self.lock_piece()

    def draw(self) -> None:
        screen.draw_background(self.screen)
        screen.draw_board_frame(self.screen)
        blocks.draw_locked_cells(self.screen, self.board)
        blocks.draw_piece(self.screen, self.piece)
        screen.draw_side_panel(self.screen, self.score, self.level, self.lines)
        blocks.draw_next_piece(
            self.screen, self.next_kind,
            config.SIDE_PANEL_LEFT, config.BOARD_TOP + 40,
        )

        if self.state is GameState.PAUSED:
            screen.draw_paused(self.screen)
        elif self.state is GameState.GAME_OVER:
            screen.draw_game_over(self.screen, self.score)

        if SHOW_SETUP_MESSAGE:
            self.draw_setup_message()

        pygame.display.flip()

    def draw_setup_message(self) -> None:
        """Màn hình tạm để kiểm tra máy đã cài đặt đúng. Xoá khi vẽ xong."""
        cx = config.WINDOW_WIDTH // 2
        cy = config.WINDOW_HEIGHT // 2
        screen.draw_text(self.screen, "TETRIS - NHOM KNNN", 44,
                         (cx, cy - 40), center=True)
        screen.draw_text(self.screen, "Khung du an da chay duoc!", 26,
                         (cx, cy), config.COLOR_TEXT_DIM, center=True)
        screen.draw_text(self.screen, f"Khoi hien tai: {self.piece.kind}   "
                         f"Khoi ke tiep: {self.next_kind}", 22,
                         (cx, cy + 34), config.COLOR_TEXT_DIM, center=True)
        screen.draw_text(self.screen, "Nhan ESC de thoat", 20,
                         (cx, cy + 64), config.COLOR_TEXT_DIM, center=True)

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
