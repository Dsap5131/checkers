from src.common.gamepiece import GamePiece
from src.player.strategy import Strategy
from src.common.player import Player
from src.common.playergamestate import PlayerGameState
from src.common.move import Move

class LocalPlayer(Player):
    '''
    LocalPlayer is a player that is run on the gameserver. These are likely
    to be AI setup by the server and players used for testing. The server has
    greater control over these players.
    
    @param: gamepiece: GamePiece
    @param: startegy: Strategy
    '''

    def __init__(self, gamepiece: GamePiece, strategy: Strategy) -> None:
        self.__gamepiece = gamepiece
        self.__strategy = strategy
        self.__is_winner = False

    
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
    

    def won(self, winner: bool) -> None:
        '''
        Tell the player whether they won the game or not

        @param: winner: True if the player won the game 
        '''

        self.__is_winner = winner


    def get_is_winner(self) -> bool:
        '''
        Checks to see if this player won the game.
        
        This function is primarily used for testing

        @returns: bool
        '''

        return self.__is_winner