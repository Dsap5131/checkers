from collections import deque

from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.position import Position
from src.common.move import Move
from src.common.leap import Leap


def test_constructor() -> None:
    row_size = 3
    column_size = 3
    board_setup = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_setup)


def test_get_row_size() -> None:
    row_size = 2
    column_size = 3
    board_setup = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_setup)
    assert board.get_row_size() == 2, "Board.get_row_size() not working."

    row_size_2 = 4
    column_size_2 = 1
    board_setup_2 = [[GamePiece.BLANK],
                     [GamePiece.BLANK],
                     [GamePiece.BLANK],
                     [GamePiece.BLANK]]
    board_2 = Board(row_size_2, column_size_2, board_setup_2)
    assert board_2.get_row_size() == 4, "Board.get_row_size() not working."


def test_get_column_size() -> None:
    row_size = 2
    column_size = 3
    board_setup = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_setup)
    assert board.get_column_size() == 3, "Board.get_column_size() not working."

    row_size_2 = 4
    column_size_2 = 1
    board_setup_2 = [[GamePiece.BLANK],
                     [GamePiece.BLANK],
                     [GamePiece.BLANK],
                     [GamePiece.BLANK]]
    board_2 = Board(row_size_2, column_size_2, board_setup_2)
    assert board_2.get_column_size() == 1, "Board.get_column_size() not working."


def test_get_piece() -> None:
    row_size = 2
    column_size = 3
    board_setup = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.RED, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_setup)
    
    assert board.get_piece(Position(0,0)) == GamePiece.BLANK, \
        "Board.get_piece(position) not working."
    
    assert board.get_piece(Position(1,1)) == GamePiece.RED, \
        "Board.get_piece(position) not working."
    

def test_move_piece() -> None:
    row_size = 2
    column_size = 3
    board_setup = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                   [GamePiece.BLANK, GamePiece.RED, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_setup)

    assert board.get_piece(Position(1,1)) == GamePiece.RED, \
        "Board.get_piece(position) failed and ruins integration testing."
    
    assert board.get_piece(Position(0,1)) == GamePiece.BLANK, \
        "Board.get_piece(position) failed and ruins integration testing."
    

    move = Move(deque([Leap(Position(1,1), Position(0,1))]))
    board.move_piece(move)

    assert board.get_piece(Position(0,1)) == GamePiece.RED, \
        "Board.move_piece(move) not working."
    

def test_copy_constructor() -> None:
    row_size = 2
    column_size = 2
    board_setup = [[GamePiece.BLANK, GamePiece.RED],
                   [GamePiece.BLANK, GamePiece.BLANK]]
    board_one = Board(row_size, column_size, board_setup)
    board_two = Board.from_board(board_one)

    assert board_one.get_piece(Position(0,0)) == GamePiece.BLANK, \
        "Board.from_board(Board) setup failed."
    
    assert board_two.get_piece(Position(0,0)) == GamePiece.BLANK, \
        "Board.from_board(Board) setup failed."
    
    move = Move(deque([Leap(Position(0,1), Position(0,0))]))
    board_two.move_piece(move)

    assert board_one.get_piece(Position(0,0)) == GamePiece.BLANK, \
        "Board.from_board(Board) failed."
    
    assert board_two.get_piece(Position(0,0)) == GamePiece.RED, \
        "Board.from_board(Board) failed."
    



