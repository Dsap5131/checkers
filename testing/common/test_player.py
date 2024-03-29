import pytest

from src.common.player import Player
from src.common.gamepiece import Piece
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.playerstate import PlayerState


def test_get_piece() -> None:
    player_one = Player()
    player_two = Player()
    with pytest.raises(NotImplementedError):
        player_one.get_piece()
    with pytest.raises(NotImplementedError):
        player_two.get_piece()


def test_get_move() -> None:
    player = Player()

    row_size=2
    column_size=2
    board_list = [[Piece.BLANK, Piece.BLANK],
                  [Piece.BLANK, Piece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players, 0)

    with pytest.raises(NotImplementedError):
        player.get_move(playergamestate)


def test_won() -> None:
    player = Player()

    with pytest.raises(NotImplementedError):
        player.won(False)


def test_get_playerstate() -> None:
    player = Player()

    with pytest.raises(NotImplementedError):
        player.get_playerstate()