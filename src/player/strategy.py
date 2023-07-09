from src.common.playergamestate import PlayerGameState
from src.common.move import Move

class Strategy():
    '''
    Interface for a strategy.
    '''

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")

    