from collections import deque

from src.common.rulesstandard import RulesStandard
from src.common.move import Move
from src.common.board import Board
from src.player.localplayer import LocalPlayer
from src.player.dumbstrategy import DumbStrategy
from src.common.gamepiece import GamePiece
from src.common.position import Position
from src.common.leap import Leap


def test_constructor() -> None:
    rules_standard = RulesStandard()


def test_check_move() -> None:
    rules_standard = RulesStandard()

    strategy = DumbStrategy()
    player = LocalPlayer(GamePiece.RED, strategy)

    # Test an valid move where a piece is not jumped
    board_list_1 = [[GamePiece.BLANK, GamePiece.RED],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board_1 = Board(row_size=2, column_size=2, board=board_list_1)
    leaps_1 = deque([Leap(Position(0,1), Position(1,0))])
    move_1 = Move(leaps_1)
    
    assert rules_standard.check_move(move_1, board_1, player), \
        "RulesStandard.check_move(Move, Board, Player) failing clean move."
    
    # Test an valid move where a piece is jumped
    board_list_2 = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLACK, GamePiece.BLANK],
                    [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)
    leaps_2 = deque([Leap(Position(0,2), Position(2,0))])
    move_2 = Move(leaps_2)

    assert rules_standard.check_move(move_2, board_2, player), \
        "RulesStandard.check_move(Move, Board, Player) failing capture move."
    
    # Test an invalid move where you move horizontal 
    board_list_3 = [[GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_3 = Board(row_size=2, column_size=2, board=board_list_3)
    leaps_3 = deque([Leap(Position(0,1), Position(0,0))])
    move_3 = Move(leaps_3)

    assert rules_standard.check_move(move_3, board_3, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows horizontal moves."
    
    # Test an invalid move where you move vertical
    board_list_4 = [[GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_4 = Board(row_size=2, column_size=2, board=board_list_4)
    leaps_4 = deque([Leap(Position(0,1), Position(1,1))])
    move_4 = Move(leaps_4)

    assert rules_standard.check_move(move_4, board_4, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows vertical moves."
    
    # Test an invalid capture move over a players own piece
    board_list_5 = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.RED, GamePiece.BLANK],
                    [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board_5 = Board(row_size=3, column_size=3, board=board_list_5)
    leaps_5 = deque([Leap(Position(0,2), Position(2,0))])
    move_5 = Move(leaps_5)

    assert rules_standard.check_move(move_5, board_5, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows \
        capturing a players own piece."
    
    # Test an invalid capture move over a blank gamepiece
    board_list_6 = [[GamePiece.BLANK, GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK],
                    [GamePiece.BLANK, GamePiece.BLANK, GamePiece.BLANK]]
    board_6 = Board(row_size=3, column_size=3, board=board_list_6)
    leaps_6 = deque([Leap(Position(0,2), Position(2,0))])
    move_6 = Move(leaps_6)

    assert rules_standard.check_move(move_6, board_6, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows capturing \
        a blank gamepiece."

    # Test invalid move that is off the top of the board.
    board_list_7 = [[GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_7 = Board(row_size=2, column_size=2, board=board_list_7)
    leaps_7 = deque([Leap(Position(0,1), Position(-1, 0))])
    move_7 = Move(leaps_7)

    assert rules_standard.check_move(move_7, board_7, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        top of the Board."

    # Test invalid move that is off the right of the board.
    board_list_8 = [[GamePiece.BLANK, GamePiece.RED],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_8 = Board(row_size=2, column_size=2, board=board_list_8)
    leaps_8 = deque([Leap(Position(0,1), Position(1,2))])
    move_8 = Move(leaps_8)

    assert rules_standard.check_move(move_8, board_8, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        right side of the Board."
    
    # Test invalid move that is off the left of the board.
    board_list_9 = [[GamePiece.BLANK, GamePiece.BLANK],
                    [GamePiece.RED, GamePiece.BLANK]]
    board_9 = Board(row_size=2, column_size=2, board=board_list_9)
    leaps_9 = deque([Leap(Position(1,0), Position(0,-1))])
    move_9 = Move(leaps_9)

    assert rules_standard.check_move(move_9, board_9, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        left side of the Board."
    
    # Test invalid move that is off the bottom of the board.
    board_list_10 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.RED, GamePiece.BLANK]]
    board_10 = Board(row_size=2, column_size=2, board=board_list_10)
    leaps_10 = deque([Leap(Position(1,0), Position(2,1))])
    move_10 = Move(leaps_10)

    assert rules_standard.check_move(move_10, board_10, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        bottom of the Board."
    
    # Test invalid move of a different players piece.
    board_list_11 = [[GamePiece.BLANK, GamePiece.BLACK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_11 = Board(row_size=2, column_size=2, board=board_list_11)
    leaps_11 = deque([Leap(Position(0,1), Position(1,0))])
    move_11 = Move(leaps_11)

    assert rules_standard.check_move(move_11, board_11, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving other \
        Players GamePieces."
    
    # Test invalid move of a blank piece.
    board_list_12 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_12 = Board(row_size=2, column_size=2, board=board_list_12)
    leaps_12 = deque([Leap(Position(0,1), Position(1,0))])
    move_12 = Move(leaps_12)

    assert rules_standard.check_move(move_12, board_12, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving other \
        Blank GamePieces."
    
    # Test invalid move on top of another piece.
    board_list_13 = [[GamePiece.BLANK, GamePiece.RED],
                     [GamePiece.RED, GamePiece.BLANK]]
    board_13 = Board(row_size=2, column_size=2, board=board_list_13)
    leaps_13 = deque([Leap(Position(0,1), Position(1,0))])
    move_13 = Move(leaps_13)

    assert rules_standard.check_move(move_13, board_13, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving ontop of \
            other GamePieces."
    
    # Test invalid move where the player is moving from off the top of the
    # board.
    board_list_14 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_14 = Board(row_size=2, column_size=2, board=board_list_14)
    leaps_14 = deque([Leap(Position(-1,0), Position(0,1))])
    move_14 = Move(leaps_14)

    assert rules_standard.check_move(move_14, board_14, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from \
        above the top of the board."
    
    # Test invalid move starting from off the left of the board.
    board_list_15 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_15 = Board(row_size=2, column_size=2, board=board_list_15)
    leaps_15 = deque([Leap(Position(0,-1), Position(1,0))])
    move_15 = Move(leaps_15)

    assert rules_standard.check_move(move_15, board_15, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from \
        off the left of the board."
    
    # Test invalid move starting from off the right of the board.
    board_list_16 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_16 = Board(row_size=2, column_size=2, board=board_list_16)
    leaps_16 = deque([Leap(Position(0,2), Position(1,1))])
    move_16 = Move(leaps_16)
    
    assert rules_standard.check_move(move_16, board_16, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from off \
        the right side of the board."
    
    # Test invalid move starting from off the bottom of the board.
    board_list_17 = [[GamePiece.BLANK, GamePiece.BLANK],
                     [GamePiece.BLANK, GamePiece.BLANK]]
    board_17 = Board(row_size=2, column_size=2, board=board_list_17)
    leaps_17 = deque([Leap(Position(2,0), Position(1,1))])
    move_17 = Move(leaps_17)

    assert rules_standard.check_move(move_17, board_17, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from off \
        the bottom of the board."


def test_check_position():
    rules_standard = RulesStandard()
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size=2, column_size=2, board=board_list)

    # Test a valid position
    position_1 = Position(0,1)
    assert rules_standard.check_position(position_1, board), \
        "RulesStandard.check_position(Position, Board) missing valid \
        positions."

    # Test a position off the top of the board
    position_2 = Position(-1,1)
    assert rules_standard.check_position(position_2, board) == False, \
        "RulesStandard.check_position(Position, Board) allows moving from \
        off the top of the board."
    
    # Test a position off the right of the board
    position_3 = Position(0,2)
    assert rules_standard.check_position(position_3, board) == False, \
        "RulesStandard.check_position(Position, Board) allows moving from \
        off the right of the board."
    
    # Test a position off the bottom of the board
    position_4 = Position(2,1)
    assert rules_standard.check_position(position_4, board) == False, \
        "RulesStandard.check_position(Position, Board) allows moving from \
        off the bottom of the board."
        

    # Test a position off the left of the board
    position_5 = Position(0,-1)
    assert rules_standard.check_position(position_5, board) == False, \
        "RulesStandard.check_position(Position, Board) allows moving from \
        off the left of the board."
    

def test_is_game_over() -> None:
    rules = RulesStandard()

    # Test a non-game over state
    row_size_1=2
    column_size_1=2
    board_list_1=[[GamePiece.BLANK, GamePiece.RED],
                  [GamePiece.BLACK, GamePiece.BLANK]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)
    num_players_1 = 2

    assert rules.is_game_over(board_1, num_players_1) == False, \
        "RulesStandard.is_game_over(Board, int) failling to identify an active \
        game."
    

    # Test a game over with only 1 player
    row_size_2=2
    column_size_2=2
    board_list_2=[[GamePiece.BLANK, GamePiece.RED],
                  [GamePiece.BLACK, GamePiece.BLANK]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)
    num_players_2 = 1
    
    assert rules.is_game_over(board_2, num_players_2), \
        "RulesStandard.is_game_over(Board, int) allowing a game with 1 player."

    # Test a game over where there are one type of piece
    row_size_3=2
    column_size_3=2
    board_list_3=[[GamePiece.BLANK, GamePiece.RED],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)
    num_players_3 = 2

    assert rules.is_game_over(board_3, num_players_3), \
        "RulesStandard.is_game_over(Board, int) allowing a game with only 1 \
        type of piece left."


