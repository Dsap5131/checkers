from src.common.gamepiece import GamePiece
from src.player.strategy import Strategy
from src.common.player import Player
from src.common.playergamestate import PlayerGameState
from src.common.move import Move

class LocalPlayer(Player):
    '''
    LocalPlayer is a player that is run on the gameserver. 
    
    @param: gamepiece: GamePiece
    @param: startegy: Strategy
    '''

    def __init__(self, gamepiece: GamePiece, strategy: Strategy) -> None:
        self.__gamepiece = gamepiece
        self.__strategy = strategy

    
    def get_gamepiece(self) -> GamePiece:
        '''
        Get the gamepiece of the player.

        @returns: GamePiece
        '''

        return self.__gamepiece
    

    def get_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Get the next move of the player.
        
        @returns: Move
        '''

        return self.__strategy.make_move(playergamestate)