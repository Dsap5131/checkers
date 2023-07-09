from collections import deque

from src.player.dumbstrategy import DumbStrategy
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position


def test_constructor() -> None:
    strategy = DumbStrategy()


def test_make_move() -> None:
    strategy = DumbStrategy()

    row_size=2
    column_size=2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    expected_move = Move(deque([Leap(Position(0,0), Position(0,0))]))

    assert strategy.make_move(playergamestate) == expected_move, \
        "DumbStrategy.make_move(Board, Rules) not working as expected."