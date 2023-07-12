from src.player.localplayer import LocalPlayer
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.dumbstrategy import DumbStrategy
from src.common.board import Board
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.rulesstandard import RulesStandard


def test_constructor() -> None:
    strategy = DumbStrategy()
    localplayer = LocalPlayer(Piece.BLACK, strategy)    


def test_get_piece() -> None:
    strategy = DumbStrategy()
    localplayer = LocalPlayer(Piece.BLACK, strategy)

    assert localplayer.get_piece() == Piece.BLACK, \
        'LocalPlayer.get_gamepiece() not working properly.'


def test_get_move() -> None:
    strategy = DumbStrategy()
    localplayer = LocalPlayer(Piece.BLACK, strategy)

    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    assert isinstance(localplayer.get_move(playergamestate), Move)


def test_won() -> None:
    player = LocalPlayer(Piece.BLACK, DumbStrategy())
    player.won(True)


def test_get_is_winner() -> None:
    player = LocalPlayer(Piece.BLACK, DumbStrategy())

    assert player.get_is_winner() == False, \
        "Player.get_is_winner() setup failed."
    
    player.won(True)

    assert player.get_is_winner(), \
        "Player.get_is_winner() not working correctly."

