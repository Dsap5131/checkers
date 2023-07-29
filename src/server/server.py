import json
import socket

from collections import deque
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
        self.__rules = RulesStandard()
        self.__available_pieces = deque([Piece.RED, Piece.BLACK])
        self.__num_players = len(self.__available_pieces)
        

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
            referee.start_game(self.__rules, players)
            self.__close_connections()

        
    def __close_connections(self) -> None:
        for connection, piece in self.__connection_pairs:
            connection.close()


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

        while len(self.__connection_pairs) < self.__num_players:
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

        piece = self.__available_pieces.popleft()
        pipe_recv, pipe_send = Pipe()
        valid_connection_process = Process(target=self.__timeout_connection,
                                           args=[connection, pipe_send, piece])
        valid_connection_process.start()
        valid_connection_process.join(timeout=2)
        valid_connection_process.terminate()

        if valid_connection_process.exitcode == 0:
            validate, piece = pipe_recv.recv()
            return validate, piece
        else:
            self.__available_pieces.appendleft(piece)
            return False, None 

    def __timeout_connection(self, connection, pipe_connection, piece) -> None:
        piece_json = self.__converter.piece_to_json(piece)
        connection.send(
            (json.dumps(['set_piece', piece_json])).encode(self.ENCODING))
        msg = connection.recv(self.PACKET_SIZE).decode(self.ENCODING)
        json_obj = json.loads(msg)
        if json_obj == True:
            pipe_connection.send((True, piece))
        else:
            self.__available_pieces.appendleft(piece)
            pipe_connection.send((False, None))
            


