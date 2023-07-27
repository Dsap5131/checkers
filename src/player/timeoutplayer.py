import time

from src.common.piece import Piece
from src.common.player import Player
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.playerstate import PlayerState
from src.player.strategies.strategy import Strategy


class TimeoutPlayer(Player):
    '''
    TimeoutPlayer is a Player that infinitely loops on any method call.
    
    @param: piece: Piece
    @param: strategy: Strategy
    '''


    def __init__(self, piece: Piece, strategy: Strategy) -> None:
        self.__piece = piece
        self.__strategy = strategy


    def get_piece(self) -> Piece:
        while True:
            time.sleep(1)

    
    def get_move(self, playergamestate: PlayerGameState) -> Move:
        while True:
            time.sleep(1)


    def won(self, winner: bool) -> None:
        while True:
            time.sleep(1)

    
    def get_playerstate(self) -> PlayerState:
        while True:
            time.sleep(1)