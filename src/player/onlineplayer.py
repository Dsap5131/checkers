from src.common.player import Player
from src.common.piece import Piece
from src.remote.playerproxy import PlayerProxy
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.playerstate import PlayerState

class OnlinePlayer(Player):
    '''
    OnlinePlayer represents a Player that usings proxies to allow
    remote connections to the game.

    @param: Piece
    @param: PlayerProxy
    '''

    
    def __init__(self, piece: Piece, playerproxy: PlayerProxy) -> None:
        self.__piece = piece
        self.__playerproxy = playerproxy

    
    def get_piece(self) -> None:
        return self.__piece
    

    def get_move(self, playergamestate: PlayerGameState) -> Move:
        return self.__playerproxy.get_move(playergamestate)
    

    def won(self, winner: bool) -> None:
        self.__playerproxy.won(winner)


    def get_playerstate(self) -> PlayerState:
        return PlayerState(self.__piece)
