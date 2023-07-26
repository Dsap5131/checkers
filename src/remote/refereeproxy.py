import json
import socket

from src.player.localplayer import LocalPlayer
from src.common.json_converter import JsonConverter
from src.common.playergamestate import PlayerGameState

class RefereeProxy():
    '''
    RefereeProxy represents a way for a player to remotely communicate
    to the game.

    @param: payload: socket.socket
    @param: player: LocalPlayer
    '''

    PACKET_SIZE = 1024
    ENCODING = "utf-8"

    def __init__(self, payload: socket.socket, player: LocalPlayer) -> None:
        self.__payload = payload
        self.__player = player
        self.__converter = JsonConverter()


    def listening(self) -> None:
        '''
        Start the referee proxy to listen for requests from the referee.    
        '''
        while True:
            try:
                msg=self.__payload.recv(self.PACKET_SIZE).decode(self.ENCODING)
                self.__parse_function_call(json.loads(msg))
            except:
                return False
            

    def __parse_function_call(self, json_obj: list) -> None:
        '''
        Parse the json_obj based on Referee-Player communication documentation

        @param: json_obj: list
        '''

        function = json_obj[0]
        if function == 'get_piece':
            self.__get_piece()
        elif function == 'get_move':
            self.__get_move(
                self.__converter.json_to_playergamestate(json_obj[1]))
        elif function == 'won':
            self.__won(json_obj[1])


    def __get_piece(self) -> None:
        piece = self.__player.get_piece()
        self.__send(self.__converter.piece_to_json(piece))

    
    def __get_move(self, playergamestate: PlayerGameState) -> None:
        move = self.__player.get_move(playergamestate)
        self.__send(self.__converter.move_to_json(move))


    def __won(self, winner: bool) -> None:
        self.__player.won(winner)

    
    def __send(self, json_obj) -> None:
        msg = json.dumps(json_obj, ensure_ascii=False) + '\n'
        self.__payload.sendall(msg.encode(self.ENCODING))