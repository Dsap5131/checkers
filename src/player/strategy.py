from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.rules import Rules

class Strategy():
    '''
    Interface for a strategy.
    '''

    def make_move(self, playergamestate: PlayerGameState, rules: Rules) -> Move:
        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")

    