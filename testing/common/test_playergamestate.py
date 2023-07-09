from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece

def test_constructor() -> None:
    row_size = 2 
    column_size = 2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()

    playergamestate = PlayerGameState(board, rules)


def test_get_board() -> None:
    row_size = 2 
    column_size = 2
    board_list_1 = [[GamePiece.BLANK, GamePiece.BLANK],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_1 = Board(row_size, column_size, board_list_1)

    board_list_2 = [[GamePiece.RED, GamePiece.BLACK],
                    [GamePiece.BLANK, GamePiece.BLANK]]
    board_2 = Board(row_size, column_size, board_list_2)

    rules = RulesStandard()

    playergamestate_1 = PlayerGameState(board_1, rules)
    playergamestate_2 = PlayerGameState(board_2, rules)

    assert playergamestate_1.get_board() == board_1, \
        "PlayerGameState.get_board() not working."
    assert playergamestate_2.get_board() == board_2, \
        "PlayerGameState.get_board() not working."


def test_get_rules() -> None:
    row_size=2
    column_size=2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    assert playergamestate.get_rules() == rules, \
        "PlayerGameState.get_rules() not working."
