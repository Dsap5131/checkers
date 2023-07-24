from collections import deque

from src.referee.referee import Referee
from src.player.strategies.minimaxstrategy import MiniMaxStrategy
from src.common.piece import Piece
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.board import Board
from src.common.gamestate import GameState
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy


def test_constructor() -> None:
    referee = Referee()


def test_start_game() -> None:
    player_1_1 = LocalPlayer(Piece.RED, DumbStrategy())
    player_1_2 = LocalPlayer(Piece.BLACK, MiniMaxStrategy())
    rules_1 = RulesStandard()

    referee_1 = Referee()
    referee_1.start_game(rules_1, [player_1_1, player_1_2])

    assert player_1_1.get_is_winner() == False, \
        "Referee.start_game(Rules, Player) not working correctly."
    assert player_1_2.get_is_winner(), \
        "Referee.start_game(Rules, Player) not working correctly."


def test_continue_game() -> None:
    # Test scenario 1: 1 move to end the game
    strategy_1 = MiniMaxStrategy()
    player_1_1 = LocalPlayer(Piece.RED, strategy_1)
    player_1_2 = LocalPlayer(Piece.BLACK, strategy_1)
    players_1 = deque([player_1_1, player_1_2])
    rules = RulesStandard()

    
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
    gamestate_1 = GameState(board_1,rules,players_1)

    referee_1 = Referee()
    referee_1.continue_game(gamestate_1)

    assert player_1_1.get_is_winner(), \
        "Referee.continue_game(GameState) not working correctly."
    assert player_1_2.get_is_winner() == False, \
        "Referee.continue_game(GameState) not working correctly."
    
    
    # Test scenario 2: player gives an illegal move and is kicked. Other player
    # wins
    player_2_1 = LocalPlayer(Piece.BLACK, DumbStrategy())
    player_2_2 = LocalPlayer(Piece.RED, MiniMaxStrategy())
    players_2 = deque([player_2_1, player_2_2])
    rules_2 = RulesStandard()
    board_list_2 = [[GamePiece(Piece.BLACK, False), 
                     GamePiece(Piece.BLANK, False), 
                     GamePiece(Piece.BLACK, False)],
                    [GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.BLANK, False)],
                    [GamePiece(Piece.RED, False),
                     GamePiece(Piece.BLANK, False),
                     GamePiece(Piece.RED, False)]]
    board_2= Board(row_size=3, column_size=3, board=board_list_2)
    gamestate_2 = GameState(board_2, rules_2, players_2)
    referee_2 = Referee()
    
    referee_2.continue_game(gamestate_2)

    assert player_2_2.get_is_winner(), \
        "Referee.continue_game(GameState) not working correctly."
    assert player_2_1.get_is_winner() == False, \
        "Referee.continue_game(GameState) not working correctly."
        