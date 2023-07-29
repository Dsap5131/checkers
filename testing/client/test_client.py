import json
import socket

from time import sleep
from multiprocessing import Process, Pipe

from src.client.client import Client
from src.common.piece import Piece
from src.common.json_converter import JsonConverter
from src.player.strategies.dumbstrategy import DumbStrategy


HOSTNAME = '127.0.0.1'
PACKET_SIZE = 1024
PORT = 12_346
ENCODING = "utf-8"


def test_constructor() -> None:
    client_1 = Client(Piece.RED, DumbStrategy())


def mock_client() -> None:
    client_1 = Client(Piece.RED, DumbStrategy())
    client_1.play_game(HOSTNAME, PORT)


def mock_server_connection(pipe_conn) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()
        conn, address = server_socket.accept()

        conn.send((json.dumps(["get_piece"])).encode(ENCODING))

        json_obj = json.loads(conn.recv(PACKET_SIZE).decode(ENCODING))
        pipe_conn.send(json_obj)


def test_play_game() -> None:
    json_converter = JsonConverter()

    # Test searching for a game
    pipe_conn1, pipe_conn2 = Pipe()

    client_process = Process(target=mock_client)
    sleep(2)
    server_process = Process(target=mock_server_connection,
                             args=[pipe_conn2])
    
    server_process.start()
    client_process.start()
    client_process.join(timeout=10)
    server_process.join(timeout=10)
    client_process.terminate()
    server_process.terminate()

    assert client_process.exitcode == 0, \
        'Client.play_game() not working correctly.'
    assert server_process.exitcode == 0, \
        'Client.play_game() not working correctly.'
    json_obj = pipe_conn1.recv()
    assert json_converter.json_to_piece(json_obj) == Piece.RED, \
        'Client.play_game() not working correctly.'


    

