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
from src.common.playerstate import PlayerState

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
    

def test_valid_moves() -> None:
    rules = RulesDumb()

    board_list = [[GamePiece(Piece.BLANK, False), 
                   GamePiece(Piece.BLANK, False), 
                   GamePiece(Piece.BLANK, False)],
                  [GamePiece(Piece.BLANK, False), 
                   GamePiece(Piece.RED, False), 
                   GamePiece(Piece.BLANK, False)],
                  [GamePiece(Piece.BLANK, False), 
                   GamePiece(Piece.BLANK, False), 
                   GamePiece(Piece.BLANK, False)]]
    board = Board(row_size=3, column_size=3, board=board_list)
    player = LocalPlayer(Piece.RED, DumbStrategy())

    expected_moves = []
    
    assert rules.valid_moves(board, player) == expected_moves, \
        "RulesDumb.valid_moves(Board, Player) not working as expected."


def test_is_winner() -> None:
    rules = RulesDumb()

    board_list_1 = [[GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_1 = Board(row_size=1, column_size=1, board=board_list_1)
    playerstate_1 = PlayerState(Piece.RED)

    assert rules.is_winner(board_1, playerstate_1) == False, \
        "RulesDumb.is_winner(Board, PlayerState) not working correctly."
    
