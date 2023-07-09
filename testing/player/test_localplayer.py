from src.player.localplayer import LocalPlayer
from src.common.gamepiece import GamePiece
from src.player.dumbstrategy import DumbStrategy
from src.common.board import Board
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.rulesstandard import RulesStandard


def test_constructor() -> None:
    gamepiece = GamePiece.BLACK
    strategy = DumbStrategy()
    localplayer = LocalPlayer(gamepiece, strategy)    


def test_get_gamepiece() -> None:
    gamepiece = GamePiece.BLACK
    strategy = DumbStrategy()
    localplayer = LocalPlayer(gamepiece, strategy)

    assert localplayer.get_gamepiece() == GamePiece.BLACK, \
        'LocalPlayer.get_gamepiece() not working properly.'


def test_get_move() -> None:
    gamepiece = GamePiece.BLACK
    strategy = DumbStrategy()
    localplayer = LocalPlayer(gamepiece, strategy)

    row_size=2
    column_size=2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
                  [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playergamestate = PlayerGameState(board, rules)

    assert isinstance(localplayer.get_move(playergamestate), Move)

