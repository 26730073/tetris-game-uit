"""Kiểm thử cấu trúc dữ liệu khối Tetris.

Chạy:  python -m pytest -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest  # noqa: E402

from tetris import config  # noqa: E402
from tetris.tetromino import BOX_SIZE, KINDS, ROTATIONS, Piece, random_kind  # noqa: E402


def test_co_du_7_loai_khoi():
    assert sorted(KINDS) == ["I", "J", "L", "O", "S", "T", "Z"]


def test_moi_khoi_luon_co_4_o_o_moi_trang_thai_xoay():
    for kind in KINDS:
        for state in ROTATIONS[kind]:
            assert len(state) == 4, f"khoi {kind} co {len(state)} o"
            assert len(set(state)) == 4, f"khoi {kind} bi trung o"


def test_moi_o_nam_trong_hop_chua():
    for kind in KINDS:
        n = BOX_SIZE[kind]
        for state in ROTATIONS[kind]:
            for col, row in state:
                assert 0 <= col < n and 0 <= row < n


def test_xoay_4_lan_thi_ve_hinh_ban_dau():
    for kind in KINDS:
        assert ROTATIONS[kind][0] == sorted(ROTATIONS[kind][0])
        p = Piece(kind, 3, 3)
        assert p.rotated(4).cells() == p.cells()


def test_khoi_o_xoay_kieu_gi_cung_giong_nhau():
    trang_thai = ROTATIONS["O"]
    assert all(s == trang_thai[0] for s in trang_thai)


def test_khoi_i_xoay_1_lan_thanh_hang_doc():
    cols = {c for c, _ in ROTATIONS["I"][1]}
    rows = {r for _, r in ROTATIONS["I"][1]}
    assert len(cols) == 1 and len(rows) == 4


def test_khoi_t_xoay_phai_dung_hinh():
    # T chua xoay:  .#.     xoay phai:  .#.
    #               ###                 .##
    #               ...                 .#.
    assert ROTATIONS["T"][0] == sorted([(1, 0), (0, 1), (1, 1), (2, 1)])
    assert ROTATIONS["T"][1] == sorted([(1, 0), (1, 1), (2, 1), (1, 2)])


def test_dich_chuyen_tao_khoi_moi_khong_sua_khoi_cu():
    p = Piece("T", 3, 0)
    q = p.moved(1, 2)
    assert (p.col, p.row) == (3, 0)
    assert (q.col, q.row) == (4, 2)


def test_cells_cong_dung_vi_tri_cua_khoi():
    p = Piece("O", 4, 10)
    assert sorted(p.cells()) == [(4, 10), (4, 11), (5, 10), (5, 11)]


def test_khoi_moi_sinh_ra_nam_giua_mep_tren():
    for kind in KINDS:
        p = Piece.spawn(kind)
        cols = [c for c, _ in p.cells()]
        assert min(cols) >= 0 and max(cols) < config.COLS
        assert p.row == 0


def test_loai_khoi_sai_thi_bao_loi():
    with pytest.raises(ValueError):
        Piece("X", 0, 0)


def test_random_kind_luon_tra_ve_loai_hop_le():
    for _ in range(200):
        assert random_kind() in KINDS


def test_moi_loai_khoi_deu_co_mau():
    for kind in KINDS:
        assert Piece(kind, 0, 0).color == config.PIECE_COLORS[kind]
