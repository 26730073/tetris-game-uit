"""Điểm khởi chạy game Tetris.

Chạy game bằng lệnh:  python main.py
"""

import sys
from pathlib import Path

# Cho phép import package `tetris` nằm trong thư mục src/
sys.path.insert(0, str(Path(__file__).parent / "src"))

from tetris.game import Game


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
