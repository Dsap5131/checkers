from src.common.rulesstandard import RulesStandard
from src.common.gamestate import GameState
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.player.localplayer import LocalPlayer
from src.player.dumbstrategy import DumbStrategy

def test_constructor() -> None:
    row_size=2
    column_size=2
    board_list=[[GamePiece.BLANK, GamePiece.BLANK],
                [GamePiece.BLANK, GamePiece.BLANK]]
    board=Board(row_size,column_size,board_list)
    rules = RulesStandard()
    strategy = DumbStrategy()
    player_one = LocalPlayer(GamePiece.RED, strategy)
    players = [player_one]
    gamestate = GameState(board, rules, players)


def test_is_game_over() -> None:
    rules = RulesStandard()
    strategy = DumbStrategy()
    red_player = LocalPlayer(GamePiece.RED, strategy)
    black_player = LocalPlayer(GamePiece.BLACK, strategy)
    
    # Game with 1 player
    row_size_1=2
    column_size_1=2
    board_list_1=[[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.RED, GamePiece.BLACK]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)
    players_1 = [red_player]
    gamestate_1 = GameState(board_1, rules, players_1)

    assert gamestate_1.is_game_over(), \
        "GameState.is_game_over() failing with 1 player."

    # Non-gameover state
    row_size_2=2
    column_size_2=2
    board_list_2=[[GamePiece.BLANK, GamePiece.BLACK],
                  [GamePiece.RED, GamePiece.BLANK]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)
    players_2 = [red_player, black_player]
    gamestate_2 = GameState(board_2, rules, players_2)

    assert gamestate_2.is_game_over() == False, \
        "GameState.is_game_over() failing with active games."

    # 2 players with 1 type of piece on board.
    row_size_3=2
    column_size_3=2
    board_list_3=[[GamePiece.BLANK, GamePiece.BLACK],
                  [GamePiece.BLACK, GamePiece.BLANK]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)
    players_3 = [red_player, black_player]
    gamestate_3 = GameState(board_3, rules, players_3)

    assert gamestate_3.is_game_over(), \
        "GameState.is_game_over() failing with 1 type of piece."


def test_take_turn() -> None:
    ...