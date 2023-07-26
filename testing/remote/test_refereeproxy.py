import socket
import json
import time

from collections import deque

from multiprocessing import Process, Pipe
from src.remote.refereeproxy import RefereeProxy
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.piece import Piece
from src.common.json_converter import JsonConverter
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.playerstate import PlayerState
from src.common.rulesdumb import RulesDumb
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position

HOSTNAME = '127.0.0.1'
PORT = 12345
PACKET_SIZE = 1024
ENCODING = "utf-8"

def mock_referee_won(payload, conn) -> None:
    localplayer = LocalPlayer(Piece.RED, DumbStrategy())
    refereeproxy = RefereeProxy(payload, localplayer)  
    refereeproxy.listening()
    conn.send(localplayer.get_is_winner())


def test_constructor() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOSTNAME, PORT))
    server_socket.listen()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))

    payload, address = server_socket.accept()

    referee = RefereeProxy(client_socket, 
                           LocalPlayer(Piece.RED, DumbStrategy()))

    payload.close()
    client_socket.close()
    server_socket.close()


def test_listening() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOSTNAME, PORT))
    server_socket.listen()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))

    payload, address = server_socket.accept()
    json_converter = JsonConverter()
    player = LocalPlayer(Piece.RED, DumbStrategy())
    referee = RefereeProxy(client_socket, player)
    
    referee_process = Process(target=referee.listening)
    referee_process.start()

    # Test where you are get_piece    
    payload.send((json.dumps(["get_piece"])).encode(ENCODING))
    msg_1 = payload.recv(PACKET_SIZE).decode(ENCODING)
    piece = json_converter.json_to_piece(json.loads(msg_1))

    referee_process.join(timeout=2)
    referee_process.terminate()

    assert piece == Piece.RED, \
        "Referee.listening() not working"
    
    # Test where you are get_move
    referee_process = Process(target=referee.listening)
    referee_process.start()

    board_list = [[GamePiece(Piece.BLANK)]]
    board = Board(row_size=1, column_size=1, board=board_list)
    playergamestate = PlayerGameState(board,
                                      RulesDumb(),
                                      [PlayerState(Piece.RED)],
                                      1)

    msg_2 = 'get_move'
    json_obj_2 = json_converter.playergamestate_to_json(playergamestate)
    payload.send((json.dumps([msg_2, json_obj_2])).encode(ENCODING))
    response_2 = payload.recv(PACKET_SIZE).decode(ENCODING)
    move = json_converter.json_to_move(json.loads(response_2))

    referee_process.join(timeout=2)
    referee_process.terminate()

    assert move == Move(deque([Leap(Position(0,0), Position(0,0), [], [])])), \
        "Referee.listening() not working."
    
    # Test where you are won
    conn1, conn2 = Pipe()
    referee_process = Process(target=mock_referee_won, args=(client_socket,conn2))
    referee_process.start()
    payload.send((json.dumps(['won', True])).encode(ENCODING))
    payload.close()
    client_socket.close()
    server_socket.close()
    
    referee_process.join(timeout=2)
    referee_process.terminate()

    expected = conn1.recv()

    assert True == expected, \
        "Referee.listening() not working."
    