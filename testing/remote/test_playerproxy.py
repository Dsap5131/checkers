import time
import json
import socket

from multiprocessing import Process, Pipe
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
PACKET_SIZE = 1024
PORT = 12_347
ENCODING = "utf-8"

def mock_playerproxy_get_move(playerproxy, pgs, pipe):
    pipe.send(playerproxy.get_move(pgs))


def test_constructor() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)


def test_get_move() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)

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
        
        conn1, conn2 = Pipe()
        server_process = \
            Process(target=mock_playerproxy_get_move, args=(playerproxy,
                                                playergamestate,
                                                conn2))
        server_process.start()

        msg = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))
        move_json = jsonconverter.move_to_json(expected)
        client_socket.sendall(
            (json.dumps(move_json, ensure_ascii=False) + '\n').encode(ENCODING))
        
        server_process.join(timeout=5)
        server_process.terminate()

        move = conn1.recv()


        assert msg[0] == 'get_move', \
            "PlayerProxy.get_move(playergamestate) not working correctly."
        assert jsonconverter.json_to_playergamestate(msg[1]) ==playergamestate,\
            "PlayerProxy.get_move(playergamestate) not working correctly."
        assert move == expected, \
            "PlayerProxy.get_move(playergamestate) not working correctly."
    

def test_won() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)

        server_process = \
            Process(target=playerproxy.won, args=(True,))
        server_process.start()

        msg = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))

        server_process.join(timeout=5)
        server_process.terminate()

        assert msg[0] == 'won', \
            "PlayerProxy.won(bool) not working correctly."
        assert msg[1] == True, \
            "PlayerProxy.won(bool) not working correctly."