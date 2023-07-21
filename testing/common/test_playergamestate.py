from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.playerstate import PlayerState

def test_constructor() -> None:
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size=2, column_size=2, board=board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players)


def test_get_board() -> None:
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    board_list_1 = [[blank_piece, blank_piece],
                    [blank_piece, blank_piece]]
    board_1 = Board(row_size=2, column_size=2, board=board_list_1)

    board_list_2 = [[red_piece, black_piece],
                    [blank_piece, blank_piece]]
    board_2 = Board(row_size=2, column_size=2, board=board_list_2)

    rules = RulesStandard()
    playerstate_1 = PlayerState(Piece.BLACK)
    players = [playerstate_1]

    playergamestate_1 = PlayerGameState(board_1, rules, players)
    playergamestate_2 = PlayerGameState(board_2, rules, players)

    assert playergamestate_1.get_board() == board_1, \
        "PlayerGameState.get_board() not working."
    assert playergamestate_2.get_board() == board_2, \
        "PlayerGameState.get_board() not working."


def test_get_rules() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players)

    assert playergamestate.get_rules() == rules, \
        "PlayerGameState.get_rules() not working."
    

def test_get_current_player() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players)

    assert playergamestate.get_current_player() == playerstate, \
        "PlayerGameState.get_piece() not working."
    

def test_set_next_player() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate_1  = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.BLACK)
    players = [playerstate_1, playerstate_2]
    playergamestate = PlayerGameState(board, rules, players)

    assert playergamestate.get_current_player() == playerstate_1, \
        "PlayerGameState.next_player() setup failed."
    playergamestate.set_next_player()
    assert playergamestate.get_current_player() == playerstate_2, \
        "PlayerGameState.next_player() not working."

def test_get_num_players() -> None:
    row_size=2
    column_size=2
    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate_1 = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.RED)
    players = [playerstate_1, playerstate_2]
    playergamestate = PlayerGameState(board, rules, players)

    assert playergamestate.get_num_players() == 2, \
        "PlayerGameState.get_num_players() not working."