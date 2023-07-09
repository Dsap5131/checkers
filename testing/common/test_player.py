import pytest

from src.common.player import Player
from src.common.gamepiece import GamePiece
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard

def test_constructor() -> None:
    player_one = Player(GamePiece.RED)


def test_get_gamepiece() -> None:
    player_one = Player(GamePiece.RED)
    assert player_one.get_gamepiece() == GamePiece.RED, \
        "Player.get_gamepiece() not working."

    player_two = Player(GamePiece.BLACK)
    assert player_two.get_gamepiece() == GamePiece.BLACK, \
        "Player.get_gamepiece() not working."


def test_get_move() -> None:
    player = Player(GamePiece.RED)

    row_size=2
    column_size=2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    with pytest.raises(NotImplementedError):
        player.get_move(playergamestate)
    