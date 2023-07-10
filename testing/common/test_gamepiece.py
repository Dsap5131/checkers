from src.common.gamepiece import GamePiece
from src.common.piece import Piece

def test_constructor() -> None:
    gamepiece = GamePiece(Piece.BLACK, False)


def test_get_piece() -> None:
    gamepiece = GamePiece(Piece.BLACK, False)

    assert gamepiece.get_piece() == Piece.BLACK, \
        "GamePiece.get_piece() not working correctly."
    

def test_is_king() -> None:
    gamepiece = GamePiece(Piece.BLACK, True)

    assert gamepiece.is_king(), \
        "GamePiece.is_king() not working correctly."
    

def test_make_king() -> None:
    gamepiece = GamePiece(Piece.RED, False)

    assert gamepiece.is_king() == False, \
        "GamePiece.make_king() setup failed."
    
    gamepiece.make_king()

    assert gamepiece.is_king(), \
        "GamePiece.make_king() not working correctly."
    

def test_eq() -> None:
    gamepiece_one = GamePiece(Piece.BLACK, False)
    gamepiece_two = GamePiece(Piece.BLACK, False)
    gamepiece_three = GamePiece(Piece.RED, False)
    gamepiece_four = GamePiece(Piece.BLACK, True)

    assert gamepiece_one == gamepiece_two, \
        "GamePiece == GamePiece not working"
    assert gamepiece_one != gamepiece_three, \
        "GamePiece == GamePiece not working"
    assert gamepiece_one != gamepiece_four, \
        "GamePiece == GamePiece not working"
    assert gamepiece_one != 4, \
        "GamePiece == GamePiece not working"