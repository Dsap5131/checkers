from collections import deque

from src.player.strategies.basicstrategy import BasicStrategy
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

    # Test basic red move
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    row_size=3
    column_size=3
    board_list_1=[[blank_piece, blank_piece, black_piece],
                [blank_piece, red_piece, blank_piece],
                [blank_piece, blank_piece, red_piece]]
    board_1 = Board(row_size, column_size, board_list_1)

    rules = RulesStandard()
    player_red = LocalPlayer(Piece.RED, strategy)
    playergamestate_2 = PlayerGameState(board_1, rules, player_red)
    expected_move = Move(deque([Leap(Position(1,1), Position(0,0))]))
    actual_move = strategy.make_move(playergamestate_2)

    assert actual_move == expected_move, \
        "BasicStrategy.make_move() not working correctly."
    
    # Test basic black move
    player_black = LocalPlayer(Piece.BLACK, strategy)
    board_list_2 = [[blank_piece, blank_piece, blank_piece],
                    [blank_piece, black_piece, blank_piece],
                    [blank_piece, blank_piece, blank_piece]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)
    playergamestate_2 = PlayerGameState(board_2, rules, player_black)
    actual_move = strategy.make_move(playergamestate_2)
    expected_move = Move(deque([Leap(Position(1,1), Position(2,0))]))
    assert actual_move == expected_move, \
        "BasicStrategy.make_move() not working correctly."
    
    # Test prioritzed capture over regular leap
    board_list_3 = [[blank_piece, blank_piece, blank_piece, blank_piece],
                    [blank_piece, black_piece, blank_piece, blank_piece],
                    [blank_piece, blank_piece, red_piece, blank_piece],
                    [blank_piece, blank_piece, blank_piece, blank_piece]]
    board_3 = Board(row_size=4, column_size=4, board=board_list_3)
    playergamestate_3 = PlayerGameState(board_3, rules, player_black)
    actual_move_3 = strategy.make_move(playergamestate_3)
    expected_leap_3 = Leap(Position(1,1), Position(3,3), [Position(2,2)])
    expected_move_3 = Move(deque([expected_leap_3]))
    assert actual_move_3 == expected_move_3, \
        "BasicStrategy.make_move() not working correctly."
    


    


    


    

