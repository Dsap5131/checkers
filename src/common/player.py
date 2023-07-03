from src.common.gamepiece import GamePiece

class Player():
    '''
    This represents the knowledge about a player that is required for a 
    game of checkers.
    
    @param gamepiece: GamePiece: game piece that represents this player.
    '''

    def __init__(self, gamepiece: GamePiece) -> None:
        self.__gamepiece = gamepiece

    
    def get_gamepiece(self) -> GamePiece:
        '''
        Get the GamePiece of the player.
        '''

        return self.__gamepiece