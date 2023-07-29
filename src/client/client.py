import json
import socket

from src.common.piece import Piece
from src.remote.refereeproxy import RefereeProxy
from src.player.localplayer import LocalPlayer
from src.player.strategies.strategy import Strategy
from src.common.json_converter import JsonConverter


class Client():
    '''
    Clients connect to a server and allow players to remotely play a game 
    of checkers

    @param: strategy: Strategy
    '''

    PACKET_SIZE = 1024
    ENCODING = "utf-8"

    def __init__(self, strategy: Strategy) -> None:
        self.__strategy = strategy
        self.__converter = JsonConverter()

    
    def play_game(self, hostname: str, port: int) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((hostname, port))
            piece = self.__receive_piece(client_socket)
            local_player = LocalPlayer(piece, self.__strategy)
            refereeproxy = RefereeProxy(client_socket, local_player)
            refereeproxy.listening()

    
    def __receive_piece(self, client_socket: socket.socket) -> None:
        '''
        Receive piece from server via the starting game communication guide
        
        @param: client_socket: socket.socket
        '''

        json_obj = json.loads(
            client_socket.recv(self.PACKET_SIZE).decode(self.ENCODING))
        
        if json_obj[0] == 'set_piece':
            client_socket.sendall(
                (json.dumps(True, 
                            ensure_ascii=False) + '\n').encode(self.ENCODING))
            return self.__converter.json_to_piece(json_obj[1])
        
        

        

