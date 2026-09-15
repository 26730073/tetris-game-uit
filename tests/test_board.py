"""Kiểm thử cấu trúc dữ liệu bảng chơi.

Chạy:  python -m pytest -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest  # noqa: E402

from tetris import config  # noqa: E402
from tetris.board import Board  # noqa: E402
from tetris.tetromino import Piece  # noqa: E402


def test_bang_moi_trong_hoan_toan():
    b = Board()
    assert len(b.grid) == config.ROWS
    assert all(len(line) == config.COLS for line in b.grid)
    assert b.filled_cells() == []


def test_inside_dung_bien():
    b = Board()
    assert b.inside(0, 0)
    assert b.inside(config.COLS - 1, config.ROWS - 1)
    assert not b.inside(-1, 0)
    assert not b.inside(config.COLS, 0)
    assert not b.inside(0, config.ROWS)


def test_khoi_moi_sinh_ra_hop_le():
    b = Board()
    assert b.is_valid(Piece.spawn("T"))


def test_khoi_ra_ngoai_tuong_thi_khong_hop_le():
    b = Board()
    assert not b.is_valid(Piece("O", -1, 0))
    assert not b.is_valid(Piece("O", config.COLS - 1, 0))
    assert not b.is_valid(Piece("O", 0, config.ROWS - 1))


def test_khoa_khoi_ghi_dung_4_o():
    b = Board()
    p = Piece("O", 0, config.ROWS - 2)
    b.lock(p)
    assert sorted(cell for cell, _ in b.filled_cells()) == sorted(p.cells())
    assert b.get(0, config.ROWS - 1) == "O"


def test_khoi_de_len_o_da_chiem_thi_khong_hop_le():
    b = Board()
    b.lock(Piece("O", 0, config.ROWS - 2))
    assert not b.is_valid(Piece("O", 1, config.ROWS - 2))
    assert b.is_valid(Piece("O", 2, config.ROWS - 2))


def test_khoa_khoi_o_vi_tri_sai_thi_bao_loi():
    b = Board()
    with pytest.raises(ValueError):
        b.lock(Piece("O", -1, 0))


def _lap_day_hang(b: Board, row: int, tru_cot: int | None = None) -> None:
    for col in range(b.cols):
        if col != tru_cot:
            b.grid[row][col] = "I"


def test_xoa_1_hang_day():
    b = Board()
    _lap_day_hang(b, config.ROWS - 1)
    assert b.full_rows() == [config.ROWS - 1]
    assert b.clear_full_rows() == 1
    assert b.filled_cells() == []


def test_hang_chua_day_thi_khong_xoa():
    b = Board()
    _lap_day_hang(b, config.ROWS - 1, tru_cot=4)
    assert b.clear_full_rows() == 0
    assert len(b.filled_cells()) == config.COLS - 1


def test_xoa_hang_thi_cac_hang_tren_roi_xuong():
    b = Board()
    _lap_day_hang(b, config.ROWS - 1)
    b.grid[config.ROWS - 2][3] = "T"  # mot o nam ngay tren hang day

    b.clear_full_rows()

    assert b.get(3, config.ROWS - 1) == "T"
    assert b.get(3, config.ROWS - 2) is None
    assert len(b.grid) == config.ROWS


def test_xoa_4_hang_cung_luc_tetris():
    b = Board()
    for row in range(config.ROWS - 4, config.ROWS):
        _lap_day_hang(b, row)
    assert b.clear_full_rows() == 4
    assert b.filled_cells() == []


def test_xoa_hai_hang_khong_lien_nhau():
    b = Board()
    _lap_day_hang(b, config.ROWS - 1)
    _lap_day_hang(b, config.ROWS - 2, tru_cot=0)
    _lap_day_hang(b, config.ROWS - 3)

    assert b.clear_full_rows() == 2

    # Hang chua day (thieu cot 0) roi xuong day bang
    assert b.get(0, config.ROWS - 1) is None
    assert b.get(1, config.ROWS - 1) == "I"
