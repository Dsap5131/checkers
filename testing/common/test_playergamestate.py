from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.localplayer import LocalPlayer
from src.player.dumbstrategy import DumbStrategy

def test_constructor() -> None:
    row_size = 2 
    column_size = 2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    strategy = DumbStrategy()
    player = LocalPlayer(Piece.BLACK, strategy)
    playergamestate = PlayerGameState(board, rules, player)


def test_get_board() -> None:
    row_size = 2 
    column_size = 2
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    board_list_1 = [[blank_piece, blank_piece],
                    [blank_piece, blank_piece]]
    board_1 = Board(row_size, column_size, board_list_1)

    board_list_2 = [[red_piece, black_piece],
                    [blank_piece, blank_piece]]
    board_2 = Board(row_size, column_size, board_list_2)

    rules = RulesStandard()
    strategy = DumbStrategy()
    player = LocalPlayer(Piece.BLACK, strategy)
    playergamestate_1 = PlayerGameState(board_1, rules, player)
    playergamestate_2 = PlayerGameState(board_2, rules, player)

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
    strategy = DumbStrategy()
    player = LocalPlayer(Piece.BLACK, strategy)
    playergamestate = PlayerGameState(board, rules, player)

    assert playergamestate.get_rules() == rules, \
        "PlayerGameState.get_rules() not working."
    

def test_get_player() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    strategy = DumbStrategy()
    player = LocalPlayer(Piece.BLACK, strategy)
    playergamestate = PlayerGameState(board, rules, player)

    assert playergamestate.get_player() == player, \
        "PlayerGameState.get_piece() not working."
