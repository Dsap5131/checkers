from src.common.piece import Piece
from src.common.playerstate import PlayerState


def test_constructor() -> None:
    playerstate = PlayerState(Piece.BLACK)


def test_get_piece() -> None:
    playerstate = PlayerState(Piece.BLACK)

    assert playerstate.get_piece() == Piece.BLACK, \
        "PlayerState.get_piece() not working correctly."
    

def test_eq() -> None:
    playerstate_1 = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.BLACK)
    playerstate_3 = PlayerState(Piece.RED)

    assert playerstate_1 == playerstate_2, \
        "PlayerState == PlayerState not working correctly."
    assert playerstate_1 != playerstate_3, \
        "PlayerState == PlayerState not working correctly."
    assert playerstate_1 != 5, \
        "PlayerState == PlayerState not working correctly."