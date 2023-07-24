from collections import deque

from src.common.rulesstandard import RulesStandard
from src.common.move import Move
from src.common.board import Board
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.common.position import Position
from src.common.leap import Leap
from src.common.playerstate import PlayerState


def test_constructor() -> None:
    rules_standard = RulesStandard()


def test_check_move() -> None:
    rules_standard = RulesStandard()

    strategy = DumbStrategy()
    player = LocalPlayer(Piece.RED, strategy)
    player_black = LocalPlayer(Piece.BLACK, strategy)
    # Test an valid move where a piece is not jumped
    board_list_1 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_1 = Board(row_size=2, column_size=2, board=board_list_1)
    leaps_1 = deque([Leap(Position(0,1), 
                          Position(1,0),
                          promote_positions=[Position(1,0)])])
    move_1 = Move(leaps_1)
    
    assert rules_standard.check_move(move_1, board_1, player_black), \
        "RulesStandard.check_move(Move, Board, Player) failing clean move."
    
    # Test an valid move where a piece is jumped
    board_list_2 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)
    leaps_2 = deque([Leap(Position(2,0), 
                          Position(0,2), 
                          capture_positions=[Position(1,1)],
                          promote_positions=[Position(0,2)])])
    move_2 = Move(leaps_2)

    assert rules_standard.check_move(move_2, board_2, player), \
        "RulesStandard.check_move(Move, Board, Player) failing capture move."
    
    # Test an invalid move where you move horizontal 
    board_list_3 = [[GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_3 = Board(row_size=2, column_size=2, board=board_list_3)
    leaps_3 = deque([Leap(Position(0,1), 
                          Position(0,0),
                          promote_positions=[Position(0,0)])])
    move_3 = Move(leaps_3)

    assert rules_standard.check_move(move_3, board_3, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows horizontal moves."
    
    # Test an invalid move where you move vertical
    board_list_4 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_4 = Board(row_size=2, column_size=2, board=board_list_4)
    leaps_4 = deque([Leap(Position(1,1), 
                          Position(0,1),
                          promote_positions=[Position(0,1)])])
    move_4 = Move(leaps_4)

    assert rules_standard.check_move(move_4, board_4, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows vertical moves."
    
    # Test an invalid capture move over a players own piece
    board_list_5 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_5 = Board(row_size=3, column_size=3, board=board_list_5)
    leaps_5 = deque([Leap(Position(2,0), 
                          Position(0,2), 
                          capture_positions=[Position(1,1)],
                          promote_positions=[Position(0,2)])])
    move_5 = Move(leaps_5)

    assert rules_standard.check_move(move_5, board_5, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows \
        capturing a players own piece."
    
    # Test an invalid capture move over a blank gamepiece
    board_list_6 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_6 = Board(row_size=3, column_size=3, board=board_list_6)
    leaps_6 = deque([Leap(Position(2,0), 
                          Position(0,2),
                          promote_positions=[Position(0,2)])])
    move_6 = Move(leaps_6)

    assert rules_standard.check_move(move_6, board_6, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows capturing \
        a blank gamepiece."

    # Test invalid move that is off the top of the board.
    board_list_7 = [[GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_7 = Board(row_size=2, column_size=2, board=board_list_7)
    leaps_7 = deque([Leap(Position(0,1), Position(-1, 0))])
    move_7 = Move(leaps_7)

    assert rules_standard.check_move(move_7, board_7, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        top of the Board."

    # Test invalid move that is off the right of the board.
    board_list_8 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_8 = Board(row_size=2, column_size=2, board=board_list_8)
    leaps_8 = deque([Leap(Position(1,1), Position(0,2))])
    move_8 = Move(leaps_8)

    assert rules_standard.check_move(move_8, board_8, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        right side of the Board."
    
    # Test invalid move that is off the left of the board.
    board_list_9 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_9 = Board(row_size=2, column_size=2, board=board_list_9)
    leaps_9 = deque([Leap(Position(1,0), Position(0,-1))])
    move_9 = Move(leaps_9)

    assert rules_standard.check_move(move_9, board_9, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        left side of the Board."
    
    # Test invalid move that is off the bottom of the board.
    board_list_10 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)]]
    board_10 = Board(row_size=2, column_size=2, board=board_list_10)
    leaps_10 = deque([Leap(Position(1,0), Position(2,1))])
    move_10 = Move(leaps_10)

    assert rules_standard.check_move(move_10, board_10, player_black) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving off the \
        bottom of the Board."
    
    # Test invalid move of a different players piece.
    board_list_11 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_11 = Board(row_size=2, column_size=2, board=board_list_11)
    leaps_11 = deque([Leap(Position(0,1), 
                           Position(1,0),
                           promote_positions=[Position(1,0)])])
    move_11 = Move(leaps_11)

    assert rules_standard.check_move(move_11, board_11, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving other \
        Players GamePieces."
    
    # Test invalid move of a blank piece.
    board_list_12 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_12 = Board(row_size=2, column_size=2, board=board_list_12)
    leaps_12 = deque([Leap(Position(0,1), Position(1,0))])
    move_12 = Move(leaps_12)

    assert rules_standard.check_move(move_12, board_12, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving other \
        Blank GamePieces."
    
    # Test invalid move on top of another piece.
    board_list_13 = [[GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_13 = Board(row_size=2, column_size=2, board=board_list_13)
    leaps_13 = deque([Leap(Position(1,0), 
                           Position(0,1),
                           promote_positions=[Position(0,1)])])
    move_13 = Move(leaps_13)

    assert rules_standard.check_move(move_13, board_13, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving ontop of \
            other GamePieces."
    
    # Test invalid move where the player is moving from off the top of the
    # board.
    board_list_14 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_14 = Board(row_size=2, column_size=2, board=board_list_14)
    leaps_14 = deque([Leap(Position(-1,0), Position(0,1))])
    move_14 = Move(leaps_14)

    assert rules_standard.check_move(move_14, board_14, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from \
        above the top of the board."
    
    # Test invalid move starting from off the left of the board.
    board_list_15 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_15 = Board(row_size=2, column_size=2, board=board_list_15)
    leaps_15 = deque([Leap(Position(0,-1), Position(1,0))])
    move_15 = Move(leaps_15)

    assert rules_standard.check_move(move_15, board_15, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from \
        off the left of the board."
    
    # Test invalid move starting from off the right of the board.
    board_list_16 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_16 = Board(row_size=2, column_size=2, board=board_list_16)
    leaps_16 = deque([Leap(Position(0,2), Position(1,1))])
    move_16 = Move(leaps_16)
    
    assert rules_standard.check_move(move_16, board_16, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from off \
        the right side of the board."
    
    # Test invalid move starting from off the bottom of the board.
    board_list_17 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_17 = Board(row_size=2, column_size=2, board=board_list_17)
    leaps_17 = deque([Leap(Position(2,0), Position(1,1))])
    move_17 = Move(leaps_17)

    assert rules_standard.check_move(move_17, board_17, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving from off \
        the bottom of the board."
    

    # Test invalid move where red_piece moves down.
    board_list_18 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.RED)],
                   [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                    GamePiece(Piece.BLANK)],
                   [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                    GamePiece(Piece.BLANK)]]
    board_18 = Board(row_size=3, column_size=3, board=board_list_18)
    leaps_18 = deque([Leap(Position(0,2), Position(2,0), [Position(1,1)])])
    move_18 = Move(leaps_18)

    assert rules_standard.check_move(move_18, board_18, player) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows moving red \
        pieces backwards"
    
    # Test invalid move where black_piece moves up.
    board_list_19 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_19 = Board(row_size=3, column_size=3, board=board_list_19)
    leaps_19 = deque([Leap(Position(2,0), Position(0,2), [Position(1,1)])])
    move_19 = Move(leaps_19)
    assert rules_standard.check_move(move_19, board_19, player_black) == False,\
        "RulesStandard.check_move(Move, Board, Player) allowing moving black \
        piece backwards"

    # Test valid move where red king moves down.
    board_list_20 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.RED, True)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_20 = Board(row_size=3, column_size=3, board=board_list_20)
    move_20 = Move(deque([Leap(Position(0,2), Position(2,0), [Position(1,1)])]))
    assert rules_standard.check_move(move_20, board_20, player), \
        "RulesStandard.check_move(Move, Board, Player) failing red king moves."

    # Test valid move where black king moves up.
    board_list_21 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLACK, True), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_21 = Board(row_size=3, column_size=3, board=board_list_21)
    move_21 = Move(deque([Leap(Position(2,0), Position(0,2), [Position(1,1)])]))
    assert rules_standard.check_move(move_21, board_21, player_black), \
        "RulesStandard.check_move(Move, Board, Player) fails black king moves."
    

    # Test a invalid move with a capture leap without a capture position 
    player_red = LocalPlayer(Piece.RED, DumbStrategy())
    board_list_22 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_22 = Board(row_size=3, column_size=3, board=board_list_22)
    move_22 = Move(deque([Leap(Position(2,0), 
                               Position(0,2),
                               promote_positions=[Position(0,2)])]))
    assert rules_standard.check_move(move_22, board_22, player_red) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows bad \
        captures_positions."
    
    # Test a invalid move with a capture leap with a bad capture position
    board_list_23 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_23 = Board(row_size=3, column_size=3, board=board_list_23)
    move_23 = Move(deque([Leap(Position(2,0), 
                               Position(0,2), 
                               capture_positions=[Position(0,0)],
                               promote_positions=[Position(0,2)])]))
    assert rules_standard.check_move(move_23, board_23, player_red) == False,\
        "RulesStandard.check_move(Move, Board, Player) allows bad \
        capture_positions"

    # Test a invalid move with a capture leap with multiple bad capture 
    # positions
    board_list_24 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                      GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                      GamePiece(Piece.BLANK)]]
    board_24 = Board(row_size=3, column_size=3, board=board_list_24)
    leap_24 = Leap(Position(2,0), 
                   Position(0,2), 
                   capture_positions=[Position(1,1), Position(0,0)],
                   promote_positions=[Position(0,2)])
    move_24 = Move(deque([leap_24]))
    assert rules_standard.check_move(move_24, board_24, player_red) == False,\
        "RulesStandard.check_move(Move, Board, Player) allows bad \
        capture_positions"
    
    # Test a valid multi capture move
    board_list_25 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_25 = Board(row_size=5, column_size=5, board=board_list_25)
    leap_25_1 = Leap(Position(4,0), Position(2,2), [Position(3,1)])
    leap_25_2 = Leap(Position(2,2), 
                     Position(0,4), 
                     capture_positions=[Position(1,3)],
                     promote_positions=[Position(0,4)])
    move_25 = Move(deque([leap_25_1, leap_25_2]))
    assert rules_standard.check_move(move_25, board_25, player_red),\
        "RulesStandard.check_move(Move, Board, Player) failling good \
        multicaptures."
    
    # Test that move and board are left unmutated
    board_list_26 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_26 = Board(row_size=2, column_size=2, board=board_list_26)
    move_26 = Move(deque([Leap(Position(1,0), 
                               Position(0,1),
                               promote_positions=[Position(0,1)])]))
    rules_standard.check_move(move_26, board_26, player_red)
    expected_move_26 = Move(deque([Leap(Position(1,0),
                                        Position(0,1),
                                        promote_positions=[Position(0,1)])]))
    assert move_26 == expected_move_26, \
        "RulesStandard.check_move(Move, Board, Player) mutating move."
    expected_board_list_26 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                              [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    expected_board_26 = Board(row_size=2, 
                              column_size=2, 
                              board=expected_board_list_26)
    assert board_26 == expected_board_26, \
        "RulesStandard.check_move(Move, Board, Player) mutating board."
    

    # Test illegal move that promotes a piece not taking the leap
    board_list_27 = [[GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_27 = Board(row_size=2, column_size=2, board=board_list_27)
    leap_27 = Leap(Position(1,0), 
                   Position(0,1), 
                   promote_positions=[Position(0,0)])
    move_27 = Move(deque([leap_27]))
    assert rules_standard.check_move(move_27, board_27, player_red) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows invalid promote."

    # Test legal move that promotes a valid piece
    board_list_28 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_28 = Board(row_size=2, column_size=2, board=board_list_28)
    leap_28 = Leap(Position(1,0), 
                   Position(0,1),
                   promote_positions=[Position(0,1)])
    move_28 = Move(deque([leap_28]))
    assert rules_standard.check_move(move_28, board_28, player_red), \
        "RulesStandard.check_move(Move, Board, Player) failing valid promote."
    
    # Test illegal move where a piece should promote but doesn't
    board_list_29 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board_29 = Board(row_size=2, column_size=2, board=board_list_29)
    move_29 = Move(deque([Leap(Position(1,0), Position(0,1))]))
    assert rules_standard.check_move(move_29, board_29, player_red) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows not promoting"
    
    # Test illegal promote on a piece that is already a king
    board_list_30 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED, True), GamePiece(Piece.BLANK)]]
    board_30 = Board(row_size=2, column_size=2, board=board_list_30)
    leap_30 = Leap(Position(1,0), 
                   Position(0,1),
                   promote_positions=[Position(0,1)])
    move_30 = Move(deque([leap_30]))
    assert rules_standard.check_move(move_30, board_30, player_red) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows re-promoting"

    # Test illegal promote on the correct piece
    board_list_31 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                     [GamePiece(Piece.RED), GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_31 = Board(row_size=3, column_size=3, board=board_list_31)
    leap_31 = Leap(Position(2,0), 
                   Position(1,1),
                   promote_positions=[Position(1,1)])
    move_31 = Move(deque([leap_31]))
    assert rules_standard.check_move(move_31, board_31, player_red) == False, \
        "RulesStandard.check_move(Move, Board, Player) allows bad promotes."


def test_check_position():
    rules_standard = RulesStandard()
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
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
    row_size_1=3
    column_size_1=3
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    strategy = DumbStrategy()
    red_player = LocalPlayer(Piece.RED, strategy)
    black_player = LocalPlayer(Piece.BLACK, strategy)
    board_list_1=[[blank_piece, blank_piece, blank_piece],
                  [blank_piece, black_piece, blank_piece],
                  [red_piece, blank_piece, blank_piece]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)
    num_players_1 = 2

    assert rules.is_game_over(board_1, 
                              num_players_1, 
                              red_player,
                              50) == False, \
        "RulesStandard.is_game_over(Board, int, PlayerState, int) failling to \
            identify an active game."
    

    # Test a game over with only 1 player
    row_size_2=2
    column_size_2=2
    board_list_2=[[blank_piece, red_piece],
                  [black_piece, blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)
    num_players_2 = 1
    
    assert rules.is_game_over(board_2, num_players_2, red_player, 50), \
        "RulesStandard.is_game_over(Board, int, PlayerState, int) allowing a \
            game with 1 player."

    # Test a game over where there are one type of piece
    row_size_3=2
    column_size_3=2
    board_list_3=[[blank_piece, red_piece],
                  [blank_piece, blank_piece]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)
    num_players_3 = 2

    assert rules.is_game_over(board_3, num_players_3, red_player, 50), \
        "RulesStandard.is_game_over(Board, int, PlayerState, int) allowing a \
            game with only 1 type of piece left."
    

    # Test a gameover where there is no possible moves left
    row_size_4 = 2
    column_size_4=2
    board_list_4 = [[blank_piece, black_piece],
                    [red_piece, blank_piece]]
    board_4 = Board(row_size_4, column_size_4, board_list_4)
    num_players_4 = 2

    assert rules.is_game_over(board_4, num_players_4, black_player, 50), \
        "RulesStandard.is_game_over(Board, int, PlayerState, int) allowing a \
            game with no available moves left"

    # Test a gameover where it runs out of turns
    row_size_5 = 2
    column_size_5 = 2
    board_list_5 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_5 = Board(row_size_5, column_size_5, board_list_5)
    num_players_5 = 2

    assert rules.is_game_over(board_5, num_players_5, red_player, 201), \
        "RulesStandard.is_game_over(Board, int, PlayerState, int) not ending \
            after turn count."


def test_kickable() -> None:
    rules = RulesStandard()

    assert rules.kickable(), \
        "RulesStandard.kickable() not working as expected."
    

def test_valid_moves() -> None:
    rules = RulesStandard()
    player = LocalPlayer(Piece.RED, DumbStrategy())

    # Test valid moves 1
    board_list_1 = [[GamePiece(Piece.BLACK), 
                    GamePiece(Piece.BLANK), 
                    GamePiece(Piece.BLANK)],
                   [GamePiece(Piece.BLANK), 
                    GamePiece(Piece.RED), 
                    GamePiece(Piece.BLANK)],
                   [GamePiece(Piece.BLANK), 
                    GamePiece(Piece.BLANK), 
                    GamePiece(Piece.BLANK)]]
    board_1 = Board(row_size=3, column_size=3, board=board_list_1)
    leap_1_1 = Leap(Position(1,1), 
                    Position(0,2),
                    promote_positions=[Position(0,2)])
    move_1_1 = Move(deque([leap_1_1]))
    expected_moves_1 = [move_1_1]

    assert rules.valid_moves(board_1, player) == expected_moves_1, \
        "RulesStandard.valid_moves(Board, Player) not working as expected."

    # Test where there are no valid moves
    board_list_2 = [[GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.BLANK), 
                     GamePiece(Piece.RED), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)
    expected_moves_2 = []

    assert rules.valid_moves(board_2, player) == expected_moves_2, \
        "RulesStandard.valid_moves(Board, Player) not working as expected."


    # Test valid moves with captures and as a king piece
    board_list_3 = [[GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), 
                     GamePiece(Piece.RED, True)],
                    [GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_3 = Board(row_size=3, column_size=3, board=board_list_3)
    leap_3_1 = Leap(Position(0,2),
                    Position(2,0),
                    capture_positions=[Position(1,1)])
    move_3_1 = Move(deque([leap_3_1]))
    expected_moves_3 = [move_3_1]
    assert rules.valid_moves(board_3, player) == expected_moves_3, \
        "RulesStandard.valid_moves(Board, Player) not working as expected."
    
    # Test a double capture move
    board_list_4 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                     GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                     GamePiece(Piece.BLANK)]]
    board_4 = Board(row_size=5, column_size=5, board=board_list_4)
    leap_4_1 = Leap(Position(4,0),
                    Position(2,2),
                    capture_positions=[Position(3,1)])
    move_4_1 = Move(deque([leap_4_1]))
    leap_4_2 = Leap(Position(4,0),
                    Position(2,2),
                    capture_positions=[Position(3,1)])
    leap_4_3 = Leap(Position(2,2),
                    Position(0,4),
                    capture_positions=[Position(1,3)],
                    promote_positions=[Position(0,4)])
    move_4_2 = Move(deque([leap_4_2, leap_4_3]))

    expected_moves_4 = [move_4_1, move_4_2]

    assert rules.valid_moves(board_4, player) == expected_moves_4, \
        "RulesStandard.valid_moves(Board, Player) not working as expected."
    

def test_is_winner() -> None:
    rules = RulesStandard()

    # Test a valid winner
    board_list_1 = [[GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_1 = Board(row_size=2, column_size=2, board=board_list_1)
    playerstate_1 = PlayerState(Piece.RED)

    assert rules.is_winner(board_1, playerstate_1, 2), \
        "RulesStandard.is_winner(Board, PlayerState) not working correctly."
    
    # Test an invalid winner
    board_list_2 = [[GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_2 = Board(row_size=2, column_size=2, board=board_list_1)
    playerstate_2 = PlayerState(Piece.BLACK)

    assert rules.is_winner(board_2, playerstate_2, 2) == False, \
        "RulesStandard.is_winner(Board, PlayerState) not working correctly."
    
    # Test an invalid winner
    board_list_3 = [[GamePiece(Piece.BLACK), GamePiece(Piece.RED)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board_3 = Board(row_size=2, column_size=2, board=board_list_3)
    playerstate_3 = PlayerState(Piece.BLACK)

    assert rules.is_winner(board_3, playerstate_3, 2) == False, \
        "RulesStandard.is_winner(Board, PlayerState) not working correctly."
    
    # Test a valid winner because they are the only player
    board_list_4 = [[GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_4 = Board(row_size=2, column_size=2, board=board_list_4)
    playerstate_4 = PlayerState(Piece.RED)

    assert rules.is_winner(board_4, playerstate_4, 1), \
        "RulesStandard.is_winner(Board, PlayerState) not working correctly."


def test_starting_board() -> None:
    board_list = [[GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                  [GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLACK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.RED), 
                   GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                  [GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED), GamePiece(Piece.BLANK)]]
    board = Board(8,8,board_list)
    
    assert RulesStandard().starting_board() == board, \
        "RulesStandard.starting_board() not working correctly."