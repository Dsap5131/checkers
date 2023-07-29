import time
import json
import socket
from multiprocessing import Process, Pipe

from src.server.server import Server
from src.remote.refereeproxy import RefereeProxy
from src.common.piece import Piece
from src.player.localplayer import LocalPlayer
from src.player.strategies.minimaxstrategy import MiniMaxStrategy
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.json_converter import JsonConverter


HOSTNAME = '127.0.0.1'
PACKET_SIZE = 1024
PORT = 12_345
ENCODING = "utf-8"

def test_constructor() -> None:
    server = Server(PORT)


def mock_client_player(conn, strategy) -> bool:
    json_converter = JsonConverter()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
        client_socket.connect((HOSTNAME, PORT))
        json_obj = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))
        
        if json_obj[0] == 'set_piece':
            piece = json_converter.json_to_piece(json_obj[1])
            client_socket.sendall(
                (json.dumps(True, 
                            ensure_ascii=False) + '\n').encode(ENCODING))
            local_player = LocalPlayer(piece, strategy)
            referee_proxy = RefereeProxy(client_socket, local_player)
            referee_proxy.listening()

            conn.send(local_player.get_is_winner())  
            

def test_run_game() -> None:
    json_converter = JsonConverter()

    # Test 1: Check that a server will keep listening when players aren't
    # connecting
    server = Server(PORT)
    server_process = Process(target=server.run_game)
    server_process.start()
    server_process.join(timeout=10)
    server_process.terminate()

    assert server_process.exitcode == None, \
        'Server.run_game() not working correctly.'
    
    # Test 2: Check that a server will validate a client connection
    server = Server(PORT)
    server_process = Process(target=server.run_game)
    server_process.start()

    time.sleep(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOSTNAME, PORT))
    json_obj = json.loads(client_socket.recv(PACKET_SIZE).decode(ENCODING))

    if json_obj[0] == ['set_piece']:
        piece = json_converter.json_to_piece(json_obj[1])
        msg = json.dumps(True, ensure_ascii=False) + '\n'
        client_socket.sendall(msg.encode(ENCODING))
    client_socket.close()
    server_process.join(timeout=10)
    server_process.terminate()
    

    assert json_obj[0] == 'set_piece', \
        'server.run_game() not working.'
    assert json_converter.json_to_piece(json_obj[1]) == Piece.RED, \
        'server.run_game() not working.'

    
    # Test 3: Check that 2 players can connect and play a full game
    server = Server(PORT)

    p1_conn1, p1_conn2 = Pipe()
    player_1_process = Process(target=mock_client_player, 
                               args=(p1_conn2, DumbStrategy()))

    p2_conn1, p2_conn2 = Pipe()
    player_2_process = Process(target=mock_client_player, 
                               args=(p2_conn2, MiniMaxStrategy()))


    server_process = Process(target=server.run_game)
    server_process.start()
    time.sleep(2)
    player_1_process.start()
    time.sleep(4)
    player_2_process.start()

    server_process.join(timeout=20)
    player_1_process.join(timeout=20)
    player_2_process.join(timeout=20)
    server_process.terminate()
    player_1_process.terminate()
    player_2_process.terminate()
    

    assert server_process.exitcode == 0, \
        'server.run_game() not working correctly.'
    assert player_1_process.exitcode == 0, \
        'server.run_game() not working correctly.'
    assert player_2_process.exitcode == 0, \
        'server.run_game() not working correctly.'
    assert p1_conn1.recv() == False, \
        'server.run_game() not working correctly.'
    assert p2_conn1.recv(), \
        'server.run_game() not working correctly.'