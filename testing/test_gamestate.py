from src.common.gamestate import GameState
from src.common.player import Player
from src.common.gamepiece import GamePiece
from src.common.move import Move
from src.common.position import Position
from src.common.board import Board

def test_constructor() -> None:
    gamepiece1 = GamePiece.BLACK
    player1 = Player(gamepiece1)
    players = [player1]

    row_size = 2
    column_size = 2
    board_list = [[GamePiece.BLANK, GamePiece.BLANK],
             [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    gamestate = GameState(board, players)


def test_get_piece() -> None:
    gamepiece1 = GamePiece.BLACK
    player1 = Player(gamepiece1)
    players = [player1]

    row_size = 2
    column_size = 2
    board_list = [[GamePiece.RED, GamePiece.BLANK],
             [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    gamestate = GameState(board, players)

    assert gamestate.get_piece(Position(0,0)) == GamePiece.RED, \
        "GameState.getPiece(Position) not working."


def test_make_move() -> None:
    gamepiece1 = GamePiece.BLACK
    player1 = Player(gamepiece1)
    players = [player1]

    row_size = 2
    column_size = 2
    board_list = [[GamePiece.RED, GamePiece.BLANK],
             [GamePiece.BLANK, GamePiece.BLANK]]
    board = Board(row_size, column_size, board_list)
    gamestate = GameState(board, players)

    assert gamestate.get_piece(Position(0,0)) == GamePiece.RED, \
        "GameState.make_move(Move) test setup failed."
    assert gamestate.get_piece(Position(1,1)) == GamePiece.BLANK, \
        "GameState.make_move(Move) test setup failed."

    move = Move(Position(0,0), Position(1,1))
    gamestate.make_move(move)

    assert gamestate.get_piece(Position(1,1)) == GamePiece.RED, \
        "GameState.make_move(Move) not working."
    