import pytest

from src.player.strategy import Strategy
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece

def test_constructor() -> None: 
    strategy = Strategy()


def test_make_move() -> None:
    strategy = Strategy()

    row_size=2
    column_size=2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    with pytest.raises(NotImplementedError):
        strategy.make_move(playergamestate)
