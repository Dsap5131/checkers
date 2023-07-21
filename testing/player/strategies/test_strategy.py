import pytest

from src.player.strategies.strategy import Strategy
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.common.playerstate import PlayerState

def test_constructor() -> None: 
    strategy = Strategy()


def test_make_move() -> None:
    strategy = Strategy()

    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    playergamestate = PlayerGameState(board, rules, [playerstate])

    with pytest.raises(NotImplementedError):
        strategy.make_move(playergamestate)
