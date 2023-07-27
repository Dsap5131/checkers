from multiprocessing import Process

from src.player.timeoutplayer import TimeoutPlayer
from src.common.piece import Piece
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.playergamestate import PlayerGameState
from src.common.rulesdumb import RulesDumb
from src.common.playerstate import PlayerState
from src.common.gamepiece import GamePiece
from src.common.board import Board


def test_constructor() -> None:
    timeoutplayer = TimeoutPlayer(Piece.RED, DumbStrategy())


def test_get_piece() -> None:
    timeoutplayer = TimeoutPlayer(Piece.RED, DumbStrategy())

    timeoutplayer_process = Process(target=timeoutplayer.get_piece)
    timeoutplayer_process.start()
    timeoutplayer_process.join(timeout=5)
    timeoutplayer_process.terminate()

    assert timeoutplayer_process.exitcode is None, \
        "timeoutplayer.get_piece() not working"


def test_get_move() -> None:
    timeoutplayer = TimeoutPlayer(Piece.RED, DumbStrategy())

    board_list = [[GamePiece(Piece.BLANK)]]
    board = Board(row_size=1, column_size=1, board=board_list)
    playergamestate = PlayerGameState(board,
                                      RulesDumb(),
                                      [PlayerState(Piece.RED)],
                                      1)

    timeoutplayer_process = Process(target=timeoutplayer.get_move, 
                                args=(playergamestate,))
    timeoutplayer_process.start()
    timeoutplayer_process.join(timeout=5)
    timeoutplayer_process.terminate()

    assert timeoutplayer_process.exitcode is None, \
        "timeoutplayer.get_move(playergamestate) not working"


def test_won() -> None:
    timeoutplayer = TimeoutPlayer(Piece.RED, DumbStrategy())

    timeoutplayer_process = Process(target=timeoutplayer.won,
                                args=(False,))
    timeoutplayer_process.start()
    timeoutplayer_process.join(timeout=5)
    timeoutplayer_process.terminate()

    assert timeoutplayer_process.exitcode is None, \
        "timeoutplayer.won(bool) not working"


def get_playerstate() -> None:
    timeoutplayer = TimeoutPlayer(Piece.RED, DumbStrategy())
    
    timeoutplayer_process = Process(target=timeoutplayer.get_playerstate)
    timeoutplayer_process.start()
    timeoutplayer_process.join(timeout=5)
    timeoutplayer_process.terminate()

    assert timeoutplayer_process.exitcode is None, \
        "timeoutplayer.get_playerstate() not working."