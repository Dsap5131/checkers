from src.common.gamepiece import Piece
from src.player.strategies.strategy import Strategy
from src.common.player import Player
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.playerstate import PlayerState

class LocalPlayer(Player):
    '''
    LocalPlayer is a player that is run on the gameserver. These are likely
    to be AI setup by the server and players used for testing. The server has
    greater control over these players.
    
    @param: piece: Piece
    @param: startegy: Strategy
    '''

    def __init__(self, piece: Piece, strategy: Strategy) -> None:
        self.__piece = piece
        self.__strategy = strategy
        self.__is_winner = False

    
    def get_piece(self) -> Piece:
        '''
        Get the piece of the player.

        @returns: Piece
        '''

        return self.__piece
    

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
    

    def get_playerstate(self) -> PlayerState:
        '''
        Get PlayerState of this players public information

        @returns: PlayerState
        '''

        return PlayerState(self.get_piece())