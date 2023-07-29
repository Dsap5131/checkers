import json
import socket

from multiprocessing import Process, Pipe

from src.common.piece import Piece
from src.referee.referee import Referee
from src.common.rulesstandard import RulesStandard
from src.common.json_converter import JsonConverter
from src.player.onlineplayer import OnlinePlayer
from src.remote.playerproxy import PlayerProxy


class Server():
    '''
    Server is the object to boot up a server of checkers to play games.
    
    @params: port: int: Port number for server to read TCP connections.
    '''

    PACKET_SIZE = 1024
    ENCODING = "utf-8"

    def __init__(self, port: int) -> None:
        self.__port = port
        self.__connection_pairs = []
        self.__hostname = '127.0.0.1'
        self.__converter = JsonConverter()
        

    def run_game(self) -> None:
        '''
        Runs a full game of checkers. 

        Opens a server on the port of the computer running this.
        Waits an listens for players to connect.
        After players connection run a game of checkers.
        '''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.__hostname, self.__port))
            self.__search_for_connections(server_socket)
            players = self.__make_players()
            referee = Referee()
            referee.start_game(RulesStandard(), players)


    def __make_players(self) -> list[OnlinePlayer]:
        players = []
        for (connection, piece) in self.__connection_pairs:
            playerproxy = PlayerProxy(connection)
            player = OnlinePlayer(piece, playerproxy)
            players.append(player)
        return players


    def __search_for_connections(self, server_socket) -> None:
        '''
        @param: server_socket: socket.socket
        '''

        num_players = 2
        while len(self.__connection_pairs) < num_players:
            server_socket.listen()
            connection, _ = server_socket.accept()
            validation, piece = self.__validate_connection(connection)
            if validation:
                self.__connection_pairs.append((connection, piece))
            else:
                connection.close()


    def __validate_connection(self, connection) -> tuple[bool, Piece]:
        '''
        A connection is valid if it sends a piece.

        @param: connection: Connection

        @return: tuple[bool, Piece]: If bool is True the connection is valid
                                     and there is a piece. If bool is false
                                     the connection is not valid and there
                                     is no piece.
        '''
        pipe_recv, pipe_send = Pipe()
        valid_connection_process = Process(target=self.__timeout_connection,
                                           args=[connection, pipe_send])
        valid_connection_process.start()
        valid_connection_process.join(timeout=2)
        valid_connection_process.terminate()

        if valid_connection_process.exitcode == 0:
            validate, piece = pipe_recv.recv()
            return validate, piece
        else:
            return False, None 

    def __timeout_connection(self, connection, pipe_connection) -> None:
        connection.send((json.dumps(['get_piece'])).encode(self.ENCODING))
        msg = connection.recv(self.PACKET_SIZE).decode(self.ENCODING)
        json_obj = json.loads(msg)
        piece = self.__converter.json_to_piece(json_obj)
        if isinstance(piece, Piece):
            pipe_connection.send((True, piece))
        else:
            pipe_connection.send((False, None))


