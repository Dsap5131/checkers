from collections import deque

from src.player.basicstrategy import BasicStrategy
from src.common.playergamestate import PlayerGameState
from src.common.piece import Piece
from src.common.gamepiece import GamePiece
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.player.localplayer import LocalPlayer


def test_constructor() -> None:
    strategy = BasicStrategy()


def test_make_move() -> None:
    strategy = BasicStrategy()

    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    row_size=3
    column_size=3
    board_list=[[blank_piece, blank_piece, black_piece],
                [blank_piece, red_piece, blank_piece],
                [blank_piece, blank_piece, red_piece]]
    board = Board(row_size, column_size, board_list)

    rules = RulesStandard()
    player = LocalPlayer(Piece.RED, strategy)
    playergamestate = PlayerGameState(board, rules, player)
    expected_move = Move(deque([Leap(Position(1,1), Position(0,0))]))
    actual_move = strategy.make_move(playergamestate)

    assert actual_move == expected_move, \
        "BasicStrategy.make_move() not working correctly."
    

