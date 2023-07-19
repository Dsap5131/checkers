from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.rules import Rules

class Strategy():
    '''
    Interface for a strategy.
    '''

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Make a move based on the given playergamestate.

        Given playergamestate should never be in a gameover state. Thus a valid
        move should exist.

        @param: playergamestate: PlayerGameState

        @returns: Move
        '''
        
        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")

    