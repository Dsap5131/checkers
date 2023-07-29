import socket

from src.common.piece import Piece
from src.remote.refereeproxy import RefereeProxy
from src.player.localplayer import LocalPlayer
from src.player.strategies.strategy import Strategy


class Client():
    '''
    Clients connect to a server and allow players to remotely play a game 
    of checkers

    @param: Piece
    '''

    def __init__(self, piece: Piece, strategy: Strategy) -> None:
        self.__piece = piece
        self.__strategy = strategy

    
    def play_game(self, hostname: str, port: int) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((hostname, port))
            local_player = LocalPlayer(self.__piece, self.__strategy)
            refereeproxy = RefereeProxy(client_socket, local_player)
            refereeproxy.listening()

