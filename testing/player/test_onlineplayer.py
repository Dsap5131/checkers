import json
import socket

from collections import deque
from multiprocessing import Process, Pipe

from src.player.onlineplayer import OnlinePlayer
from src.remote.playerproxy import PlayerProxy
from src.common.piece import Piece 
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.rulesdumb import RulesDumb
from src.common.playerstate import PlayerState
from src.common.move import Move
from src.common.position import Position
from src.common.leap import Leap
from src.common.json_converter import JsonConverter


HOSTNAME = '127.0.0.1'
PACKET_SIZE = 1024
PORT = 12_348
ENCODING = "utf-8"


def test_constructor() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)
        online_player = OnlinePlayer(Piece.RED, playerproxy)


def test_get_piece() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)
        online_player = OnlinePlayer(Piece.RED, playerproxy)

        assert online_player.get_piece() == Piece.RED, \
            "OnlinePlayer.get_piece() not working correctly."


def test_get_move() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)
        online_player = OnlinePlayer(Piece.RED, playerproxy)

        board_list = [[GamePiece(Piece.BLANK)]]
        board = Board(row_size=1, column_size=1, board=board_list)
        playergamestate = PlayerGameState(board,
                                          RulesDumb(),
                                          [PlayerState(Piece.RED)],
                                          1)
        
        expected_move = Move(deque([Leap(Position(0,0), Position(0,0))]))

        jsonconverter = JsonConverter()
        conn1, conn2 = Pipe()
        process = Process(target=mock_onlineplayer_get_move,
                          args=(conn2, online_player, playergamestate))
        process.start()

        msg = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))
        move_json = jsonconverter.move_to_json(expected_move)
        client_socket.sendall(
            (json.dumps(move_json, ensure_ascii=False) + '\n').encode(ENCODING))

        process.join(timeout=5)
        process.terminate()
        actual_move = conn1.recv()

        assert msg[0] == 'get_move', \
            "OnlinePlayer.get_move(PlayerGameState) not working."
        assert msg[1]==jsonconverter.playergamestate_to_json(playergamestate), \
            "OnlinePlayer.get_move(PlayerGameState) not working."
        assert actual_move == expected_move, \
            "OnlinePlayer.get_move(PlayerGameState) not working."
        

def mock_onlineplayer_get_move(conn, 
                               onlineplayer: OnlinePlayer, 
                               playergamestate: PlayerGameState) -> None:
    conn.send(onlineplayer.get_move(playergamestate))


def test_won() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)
        online_player = OnlinePlayer(Piece.RED, playerproxy)

        online_player.won(True)
        msg = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))

        assert msg[0] == 'won', \
            "OnlinePlayer.won(bool) not working."
        assert msg[1] == True, \
            "OnlinePlayer.won(bool) not working."


def test_get_playerstate() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTNAME, PORT))

        payload, address = server_socket.accept()

        playerproxy = PlayerProxy(payload)
        online_player = OnlinePlayer(Piece.RED, playerproxy)

        assert online_player.get_playerstate() == PlayerState(Piece.RED), \
            "OnlinePlayer.get_playerstate() not working."