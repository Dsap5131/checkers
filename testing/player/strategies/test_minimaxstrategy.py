from collections import deque

from src.player.strategies.minimaxstrategy import MiniMaxStrategy
from src.common.playergamestate import PlayerGameState
from src.player.localplayer import LocalPlayer
from src.common.piece import Piece
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.rulesstandard import RulesStandard
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.common.playerstate import PlayerState


def test_constructor():
    strategy = MiniMaxStrategy()


def test_make_move():
    strategy = MiniMaxStrategy()
    playerstate_1_1 = PlayerState(Piece.RED)
    playerstate_1_2 = PlayerState(Piece.BLACK)
    players_1 = [playerstate_1_1, playerstate_1_2]
    rules = RulesStandard()

    # Test scenario 1: 1 move to end the game
    board_list_1 = [[GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.BLACK, False),
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.RED, False)]]
    board_1= Board(row_size=3, column_size=3, board=board_list_1)
    playergamestate_1 = PlayerGameState(board_1, rules, players_1, 0)
    expected_move_1 = Move(deque([Leap(Position(2,2), 
                                       Position(0,0),
                                       capture_positions=[Position(1,1)],
                                       promote_positions=[Position(0,0)])]))
    

    assert strategy.make_move(playergamestate_1) == expected_move_1, \
        "MiniMaxStrategy.make_move(PlayerGameState) not working correctly."

    # Test scenario 2
    board_list_2 = [[GamePiece(Piece.BLACK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.RED, False)]]
    board_2 = Board(row_size=4, column_size=4, board=board_list_2)
    playerstate_2_1 = PlayerState(Piece.RED)
    playerstate_2_2 = PlayerState(Piece.BLACK)
    players_2 = [playerstate_2_1, playerstate_2_2]
    playergamestate_2 = PlayerGameState(board_2, rules, players_2, 0)
    expected_move = Move(deque([Leap(Position(3,3), Position(2,2))]))
    assert strategy.make_move(playergamestate_2) == expected_move, \
        "MiniMaxStrategy.make_move(PlayerGameState) not working correctly."
