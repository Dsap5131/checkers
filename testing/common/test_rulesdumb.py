from collections import deque

from src.common.rulesdumb import RulesDumb
from src.player.localplayer import LocalPlayer
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.board import Board
from src.common.leap import Leap
from src.common.position import Position
from src.common.move import Move

def test_constructor() -> None:
    rules = RulesDumb()


def test_check_move() -> None:
    rules = RulesDumb()
    strategy = DumbStrategy()

    red_piece = GamePiece(Piece.RED, False)
    blank_piece = GamePiece(Piece.BLANK, False)
    player = LocalPlayer(Piece.RED, strategy)

    board_list = [[blank_piece, red_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size=2, column_size=2, board=board_list)
    leaps = deque([Leap(Position(0,1), Position(1,0))])
    move = Move(leaps)
    
    assert rules.check_move(move, board, player), \
        "RulesDumb.check_move(Move, Board, Player) failing."


def test_check_position() -> None:
    rules = RulesDumb()
    
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size=2, column_size=2, board=board_list)

    assert rules.check_position(Position(0,0), board), \
        "RulesDumb.check_position(Position, Board) not working."


def test_is_game_over() -> None:
    rules = RulesDumb()

    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size=2, column_size=2, board=board_list)

    assert not rules.is_game_over(board, num_players=2), \
        "RulesDumb.is_game_over(Board, num_players) not working correctly."


def test_kickable() -> None:
    rules = RulesDumb()

    assert rules.kickable(), \
        "RulesDumb.kickable() not working correctly."