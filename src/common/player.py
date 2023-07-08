from src.common.gamepiece import GamePiece
from src.common.move import Move

class Player():
    ''' 
    Abstract class that represents the knowledge the game knows about a player
    
    @param: gamepiece: GamePiece: gamepiece of a player.
    '''

    def __init__(self, gamepiece: GamePiece) -> None:
        self.__gamepiece = gamepiece

    
    def get_gamepiece(self) -> GamePiece:
        '''
        Get the gamepiece of the player.

        @returns GamePiece
        '''
        return self.__gamepiece
    

    def get_move(self) -> Move:
        '''
        Get the next move of a player.

        @returns Move
        '''

        raise NotImplemented('MUST OVERRIDE THIS CLASS')