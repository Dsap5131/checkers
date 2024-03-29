from collections import deque
from multiprocessing import Process

from src.player.timeoutplayer import TimeoutPlayer
from src.common.rulesstandard import RulesStandard
from src.common.rulesdumb import RulesDumb
from src.common.gamestate import GameState
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy

def test_constructor() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list=[[blank_piece, blank_piece],
                [blank_piece, blank_piece]]
    board=Board(row_size,column_size,board_list)
    rules = RulesStandard()
    strategy = DumbStrategy()
    red_piece = GamePiece(Piece.RED, False)
    player_one = LocalPlayer(Piece.RED, strategy)
    players = deque([player_one])
    gamestate = GameState(board, rules, players, 0)


def test_is_game_over() -> None:
    rules = RulesStandard()
    strategy = DumbStrategy()
    red_piece = GamePiece(Piece.RED, False)
    red_player = LocalPlayer(Piece.RED, strategy)
    black_piece = GamePiece(Piece.BLACK, False)
    black_player = LocalPlayer(Piece.BLACK, strategy)
    
    # Game with 1 player
    row_size_1=2
    column_size_1=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list_1=[[blank_piece, blank_piece],
                  [red_piece, black_piece]]
    board_1 = Board(row_size_1, column_size_1, board_list_1)
    players_1 = deque([red_player])
    gamestate_1 = GameState(board_1, rules, players_1, 0)

    assert gamestate_1.is_game_over(), \
        "GameState.is_game_over() failing with 1 player."

    # Non-gameover state
    row_size_2=3
    column_size_2=3
    board_list_2=[[blank_piece, blank_piece, blank_piece],
                  [blank_piece, blank_piece, black_piece],
                  [blank_piece, red_piece, blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)
    players_2 = deque([red_player, black_player])
    gamestate_2 = GameState(board_2, rules, players_2, 0)

    assert gamestate_2.is_game_over() == False, \
        "GameState.is_game_over() failing with active games."

    # 2 players with 1 type of piece on board.
    row_size_3=2
    column_size_3=2
    board_list_3=[[blank_piece, black_piece],
                  [black_piece, blank_piece]]
    board_3 = Board(row_size_3, column_size_3, board_list_3)
    players_3 = deque([red_player, black_player])
    gamestate_3 = GameState(board_3, rules, players_3, 0)

    assert gamestate_3.is_game_over(), \
        "GameState.is_game_over() failing with 1 type of piece."

    # Gameover based on turns
    row_size_2=3
    column_size_2=3
    board_list_2=[[blank_piece, blank_piece, blank_piece],
                  [blank_piece, blank_piece, black_piece],
                  [blank_piece, red_piece, blank_piece]]
    board_2 = Board(row_size_2, column_size_2, board_list_2)
    players_2 = deque([red_player, black_player])
    gamestate_2 = GameState(board_2, rules, players_2, 201)

    assert gamestate_2.is_game_over(), \
        "GameState.is_game_over() failing with high turn counts."


def test_take_turn() -> None:

    #Basic Take Turn and make sure nothing errors
    rules = RulesDumb()
    strategy = DumbStrategy()
    red_piece = GamePiece(Piece.RED, False)
    red_player = LocalPlayer(Piece.RED, strategy)
    black_piece = GamePiece(Piece.BLACK, False)
    black_player = LocalPlayer(Piece.BLACK, strategy)
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list=[[blank_piece, blank_piece],
                  [red_piece, black_piece]]
    board = Board(row_size, column_size, board_list)
    players = deque([black_player, red_player])
    gamestate = GameState(board, rules, players, 0)

    gamestate.take_turn()
    gamestate.take_turn()

    #Take Turn where a player times out 
    board_list_2 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                    [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board_2 = Board(row_size=2, column_size=2, board=board_list_2)
    player_2_1 = TimeoutPlayer(Piece.RED, DumbStrategy())
    players_2 = deque([player_2_1,
                       LocalPlayer(Piece.BLACK, DumbStrategy())])
    gamestate_2 = GameState(board_2, RulesDumb(), players_2, 0)

    gs2_process = Process(target=gamestate_2.take_turn)
    gs2_process.start()
    gs2_process.join(timeout=45)
    gs2_process.terminate()
    
    assert gs2_process.exitcode != 0, 'GameState.take_turn() not working.'

def test_end_game() -> None:
    board = Board(1, 1, [[GamePiece(Piece.RED)]])
    player_1 = LocalPlayer(Piece.RED, DumbStrategy())
    player_2 = LocalPlayer(Piece.BLACK, DumbStrategy())

    gamestate = GameState(board, RulesStandard(), deque([player_1, player_2]),0)

    assert player_1.get_is_winner()==False,"GameState.end_game() setup failed."
    assert player_2.get_is_winner()==False,"GameState.end_game() setup failed."
    
    gamestate.end_game()

    assert player_1.get_is_winner(), "GameState.end_game() failed."
    assert player_2.get_is_winner() == False, "GameState.end_game() failed."
    
