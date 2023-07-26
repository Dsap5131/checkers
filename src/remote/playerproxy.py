import json
import socket

from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.json_converter import JsonConverter

class PlayerProxy():
    '''
    PlayerProxy is a way for the game to communicate to a player.
    PlayerProxy is a proxy for the communication to a player.

    @param: payload: Connection
    '''

    PACKET_SIZE = 1024
    ENCODING = "utf-8"

    def __init__(self, payload: socket.socket) -> None:
        self.__payload = payload
        self.__converter = JsonConverter()


    def get_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Send a request through the payload for a move using JSON formats 
        sending the playergamestate.

        @param: playergamestate: PlayerGameState

        @return: Move
        '''

        json_obj = ['get_move', 
                    self.__converter.playergamestate_to_json(playergamestate)]
        self.__send(json_obj)
        return self.__converter.json_to_move(self.__receive())
    

    def won(self, winner: bool) -> None:
        '''
        Send an update through payload telling the user if they won or not.

        @param: winner: bool
        '''

        json_obj = ['won', winner]
        self.__send(json_obj)


    def __send(self, json_object) -> None:
        '''
        Send JSON through payload using PACKET_SIZE and ENCODING.

        @param: json_object
        '''

        self.__payload.send((json.dumps(json_object)).encode(self.ENCODING))


    def __receive(self):
        '''
        Check for message through payload

        @return: JSON object
        '''    

        msg = self.__payload.recv(self.PACKET_SIZE).decode(self.ENCODING)
        json_obj = json.loads(msg)
        if json_obj != 'void':
            return json_obj

        
    

    


