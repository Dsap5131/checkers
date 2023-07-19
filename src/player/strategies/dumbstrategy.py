from collections import deque

from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.player.strategies.strategy import Strategy


class DumbStrategy(Strategy):
    '''
    DumbStrategy just does moves that leaps from top left position to 
    top left position.
    '''

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        return Move(deque([Leap(Position(0,0), Position(0,0))]))

    