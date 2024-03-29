from collections import deque

from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.common.position import Position
from src.common.move import Move
from src.common.leap import Leap


def test_constructor() -> None:
    row_size = 3
    column_size = 3
    blank_piece = GamePiece(Piece.BLANK, False)
    board_setup = [[blank_piece, blank_piece, blank_piece],
                   [blank_piece, blank_piece, blank_piece],
                   [blank_piece, blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_setup)


def test_get_row_size() -> None:
    row_size = 2
    column_size = 3
    blank_piece = GamePiece(Piece.BLANK, False)
    board_setup = [[blank_piece, blank_piece, blank_piece],
                   [blank_piece, blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_setup)
    assert board.get_row_size() == 2, "Board.get_row_size() not working."

    row_size_2 = 4
    column_size_2 = 1
    board_setup_2 = [[blank_piece],
                     [blank_piece],
                     [blank_piece],
                     [blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_setup_2)
    assert board_2.get_row_size() == 4, "Board.get_row_size() not working."


def test_get_column_size() -> None:
    row_size = 2
    column_size = 3
    blank_piece = GamePiece(Piece.BLANK, False)
    board_setup = [[blank_piece, blank_piece, blank_piece],
                   [blank_piece, blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_setup)
    assert board.get_column_size() == 3, "Board.get_column_size() not working."

    row_size_2 = 4
    column_size_2 = 1
    board_setup_2 = [[blank_piece],
                     [blank_piece],
                     [blank_piece],
                     [blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_setup_2)
    assert board_2.get_column_size() == 1, "Board.get_column_size() not working."


def test_get_gamepiece() -> None:
    row_size = 2
    column_size = 3
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    board_setup = [[blank_piece, blank_piece, blank_piece],
                   [blank_piece, red_piece, blank_piece]]
    board = Board(row_size, column_size, board_setup)
    
    assert board.get_gamepiece(Position(0,0)) == GamePiece(Piece.BLANK, False), \
        "Board.get_gamepiece(position) not working."
    
    assert board.get_gamepiece(Position(1,1)) == GamePiece(Piece.RED, False), \
        "Board.get_piece(position) not working."
    

def test_move_piece() -> None:
    # Test single leap 
    row_size = 2
    column_size = 3
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    board_setup = [[blank_piece, blank_piece, blank_piece],
                   [blank_piece, red_piece, blank_piece]]
    board = Board(row_size, column_size, board_setup)

    assert board.get_gamepiece(Position(1,1)) == GamePiece(Piece.RED, False), \
        "Board.get_gamepiece(position) failed and ruins integration testing."
    
    assert board.get_gamepiece(Position(0,1)) == GamePiece(Piece.BLANK, False), \
        "Board.get_gamepiece(position) failed and ruins integration testing."
    

    move = Move(deque([Leap(Position(1,1), Position(0,1))]))
    board.move_piece(move)

    assert board.get_gamepiece(Position(0,1)) == GamePiece(Piece.RED, False), \
        "Board.move_piece(move) not working."
    
    # Test capture move
    board_list_2 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)

    assert board_2.get_gamepiece(Position(2,2)) == GamePiece(Piece.RED), \
        "Board.get_gamepiece(Position) failed and ruins integration testing."
    assert board_2.get_gamepiece(Position(1,1)) == GamePiece(Piece.BLACK), \
        "Board.get_gamepiece(Position) failed and ruins integration testing."
    move = Move(deque([Leap(Position(2,2), Position(0,0), [Position(1,1)])]))
    board_2.move_piece(move)
    assert board_2.get_gamepiece(Position(2,2)) == GamePiece(Piece.BLANK), \
        "Board.move_piece(Move) not working correctly."
    assert board_2.get_gamepiece(Position(1,1)) == GamePiece(Piece.BLANK), \
        "Board.move_piece(Move) not working correctly."
    assert board_2.get_gamepiece(Position(0,0)) == GamePiece(Piece.RED), \
        "Board.move_piece(Move) not working correctly."
    
    # Test promoting piece
    board_list_3 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLACK), GamePiece(Piece.RED)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_3 = Board(row_size=3, column_size=2, board=board_list_3)

    assert board_3.get_gamepiece(Position(1,0)).is_king() == False, \
        "Board.move_piece(Move) setup failed."
    assert board_3.get_gamepiece(Position(1,1)).is_king() == False, \
        "Board.move_piece(Move) setup failed."
    assert board_3.get_gamepiece(Position(2,0)).is_king() == False, \
        "Board.move_piece(Move) setup failed."
    board_3.move_piece(Move(deque([Leap(Position(1,0), 
                                        Position(2,1),
                                        promote_positions=[Position(2,1)])])))
    board_3.move_piece(Move(deque([Leap(Position(1,1),
                                        Position(0,0),
                                        promote_positions=[Position(0,0)])])))
    board_3.move_piece(Move(deque([Leap(Position(2,0),
                                        Position(1,1))])))
    assert board_3.get_gamepiece(Position(2,1)).is_king(), \
        "Board.move_piece(Move) failed to promote."
    assert board_3.get_gamepiece(Position(0,0)).is_king(), \
        "Board.move_piece(Move) failed to promote."
    assert board_3.get_gamepiece(Position(1,1)).is_king() == False, \
        "Board.move_piece(Move) promoted when it shouldn't."
    
    

def test_copy_constructor() -> None:
    row_size = 2
    column_size = 2
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    board_setup = [[blank_piece, red_piece],
                   [blank_piece, blank_piece]]
    board_one = Board(row_size, column_size, board_setup)
    board_two = Board.from_board(board_one)

    assert board_one.get_gamepiece(Position(0,0)) == GamePiece(Piece.BLANK, False),\
        "Board.from_board(Board) setup failed."
    
    assert board_two.get_gamepiece(Position(0,0)) == GamePiece(Piece.BLANK, False), \
        "Board.from_board(Board) setup failed."
    
    move = Move(deque([Leap(Position(0,1), 
                            Position(0,0),
                            promote_positions=[Position(0,0)])]))
    board_two.move_piece(move)

    assert board_one.get_gamepiece(Position(0,0)) == GamePiece(Piece.BLANK, False), \
        "Board.from_board(Board) failed."
    
    assert board_two.get_gamepiece(Position(0,0)) == GamePiece(Piece.RED, True), \
        "Board.from_board(Board) failed."
    

def test_unique_piece_count() -> None:
    # Test with only blank pieces
    row_size_1=2
    column_size_1=2
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    board_list_1=[[blank_piece, blank_piece],
                [blank_piece, blank_piece]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)

    assert board_1.unique_piece_count() == 0, \
        "Board.unique_piece_count() failing with only blank pieces."

    # Test with 1 type of piece
    row_size_2=2
    column_size_2=2
    board_list_2=[[blank_piece, red_piece],
                  [red_piece, blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)

    assert board_2.unique_piece_count() == 1, \
        "Board.unique_piece_count() failing with only 1 type of piece."

    # Test with 2 types of pieces
    row_size_3=2
    column_size_3=2
    board_list_3=[[blank_piece, red_piece],
                  [blank_piece, black_piece]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)

    assert board_3.unique_piece_count() == 2, \
        "Board.unique_piece_count() failing with 2 types of pieces."
    
    # Test with a non-king and king piece of the same type of piece
    row_size_4=2
    column_size_4=2
    black_king_piece = GamePiece(Piece.BLACK, True)
    board_list_4=[[black_king_piece, black_piece],
                  [blank_piece, blank_piece]]
    board_4 = Board(row_size_4, column_size_4, board_list_4)

    assert board_4.unique_piece_count() == 1, \
        "Board.unique_piece_count() failing with 2 types of pieces."
    

def test_eq() -> None:
    row_size_1 = 2
    column_size_1 = 2
    board_list_1 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)

    row_size_2 = 2
    column_size_2 = 2
    board_list_2 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)

    row_size_3 = 3
    column_size_3 = 2
    board_list_3 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)
    
    row_size_4 = 2
    column_size_4 = 3
    board_list_4 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_4 = Board(row_size_4, column_size_4, board_list_4)

    row_size_5 = 2
    column_size_5 = 2
    board_list_5 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_5 = Board(row_size_5, column_size_5, board_list_5)

    assert board_1 == board_2, "Board == Board not working correctly."
    assert board_1 != board_3, "Board == Board not working correctly."
    assert board_1 != board_4, "Board == Board not working correctly."
    assert board_1 != board_5, "Board == Board not working correctly."
    assert board_1 != 5, "Board == Board not working correctly."


def test__str() -> None:
    board_list = [[GamePiece(Piece.RED), GamePiece(Piece.BLACK, True), 
                   GamePiece(Piece.RED, True)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK),
                   GamePiece(Piece.BLACK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK),
                   GamePiece(Piece.BLANK)]]
    board = Board(row_size=3, column_size=3, board=board_list)

    expected = " O_ | XK | OK \n" + \
               "--------------\n" + \
               "  _ |  _ | X_ \n" + \
               "--------------\n" + \
               "  _ |  _ |  _ \n"
    assert str(board) == expected, "Board.__str__ not working."
    



