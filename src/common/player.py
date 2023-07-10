from src.common.piece import Piece
from src.common.move import Move

class Player():
    ''' 
    Interface that represents the knowledge the game knows about a player
    '''


    def get_gamepiece(self) -> Piece:
        '''
        Get the piece of the player.

        @returns: Piece
        '''
        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def get_move(self, gamestate: 'PlayerGameState') -> Move:
        '''
        Get the next move of a player.

        @param: gamestate: PlayerGameState

        @returns: Move
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def won(self, winner: bool) -> None:
        '''
        Tell the player whether they won the game or not

        @param: winner: True if the player won the game 
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")