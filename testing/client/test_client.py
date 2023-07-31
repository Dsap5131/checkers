import json
import socket

from time import sleep
from multiprocessing import Process, Pipe

from src.client.client import Client
from src.common.piece import Piece
from src.common.json_converter import JsonConverter
from src.player.strategies.dumbstrategy import DumbStrategy
from src.client.displays.dumbdisplay import DumbDisplay


HOSTNAME = '127.0.0.1'
PACKET_SIZE = 1024
PORT = 12_346
ENCODING = "utf-8"


def test_constructor() -> None:
    client_1 = Client(DumbDisplay(HOSTNAME, PORT))


def mock_client() -> None:
    client_1 = Client(DumbDisplay(HOSTNAME, PORT))
    client_1.play_game()


def mock_server_connection(pipe_conn) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOSTNAME, PORT))
        server_socket.listen()
        conn, address = server_socket.accept()

        json_converter = JsonConverter()

        piece_json = json_converter.piece_to_json(Piece.RED)

        conn.send((json.dumps(["set_piece", piece_json])).encode(ENCODING))

        json_obj = json.loads(conn.recv(PACKET_SIZE).decode(ENCODING))
        pipe_conn.send(json_obj)


def test_play_game() -> None:
    # Test searching for a game
    pipe_conn1, pipe_conn2 = Pipe()

    client_process = Process(target=mock_client)
    server_process = Process(target=mock_server_connection,
                             args=[pipe_conn2])
    
    server_process.start()
    sleep(2)
    client_process.start()
    client_process.join(timeout=10)
    server_process.join(timeout=10)
    client_process.terminate()
    server_process.terminate()

    assert server_process.exitcode == 0, \
        'Client.play_game() not working correctly.'
    assert client_process.exitcode == 0, \
        'Client.play_game() not working correctly.'
    assert pipe_conn1.recv(), \
        'Client.play_game() not working correctly.'


    

