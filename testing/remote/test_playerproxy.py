import time
import json
import socket

from collections import deque

from src.remote.playerproxy import PlayerProxy
from src.common.piece import Piece
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesdumb import RulesDumb
from src.common.playerstate import PlayerState 
from src.common.gamepiece import GamePiece
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.common.json_converter import JsonConverter

HOSTNAME = '127.0.0.1'
PORT = '12345'
PACKET_SIZE = 1024
ENCODING = "utf-8"

def test_constructor() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOSTNAME, PORT))
    server_socket.listen()

    time.sleep(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))

    payload, address = server_socket.accept()

    playerproxy = PlayerProxy(payload, Piece.RED)


def test_get_move() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOSTNAME, PORT))
    server_socket.listen()

    time.sleep(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))

    payload, address = server_socket.accept()

    playerproxy = PlayerProxy(payload, Piece.RED)

    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLACK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.RED)]]
    board = Board(row_size=2, column_size=2, board=board_list)

    playergamestate = PlayerGameState(board,
                                      RulesDumb(),
                                      [PlayerState(Piece.RED),
                                       PlayerState(Piece.BLACK)],
                                      1)

    jsonconverter = JsonConverter()
    
    expected = Move(deque([Leap(Position(1,1),
                                Position(0,0),
                                [],
                                [Position(0,0)])]))
    


    move = playerproxy.get_move(playergamestate)

    
    msg = json.loads(client_socket.recv(1000000).decode(ENCODING))
    pgs_json = jsonconverter.playergamestate_to_json(playergamestate)
    client_socket.sendall(
        (json.dumps(pgs_json, ensure_ascii=False) + '\n').encode("utf-8"))

    assert msg[0] == 'get_move', \
        "PlayerProxy.get_move(playergamestate) not working correctly."
    assert jsonconverter.json_to_playergamestate(msg[1]) == playergamestate, \
        "PlayerProxy.get_move(playergamestate) not working correctly."
    assert move == expected, \
        "PlayerProxy.get_move(playergamestate) not working correctly."
    

    playerproxy.get_move(playergamestate) == expected, \
        "PlayerProxy.get_piece() not working correctly."


def test_won() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOSTNAME, PORT))
    server_socket.listen()

    time.sleep(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))

    payload, address = server_socket.accept()

    playerproxy = PlayerProxy(payload, Piece.RED)

    playerproxy.won(True)
    msg = json.loads(client_socket.recv(1000000).decode(ENCODING))

    assert msg[0] == 'won', \
        "PlayerProxy.won(bool) not working correctly."
    assert msg[1] == True, \
        "PlayerProxy.won(bool) not working correctly."