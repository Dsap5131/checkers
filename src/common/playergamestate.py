from src.common.board import Board
from src.common.rules import Rules
from src.common.player import Player

class PlayerGameState():
    '''
    Represents the knowledge a player has about the game.

    @param: board: Board
    @param: rules: Rules
    @param: current_player: Player
    @param: num_players: int
    '''

    def __init__(self, 
                 board: Board, 
                 rules: Rules, 
                 current_player: Player,
                 num_players: int) -> None:
        self.__board = board
        self.__rules = rules
        self.__current_player = current_player
        self.__num_players = num_players

    
    def get_board(self) -> Board:
        '''
        Get the board of the gamestate
        '''

        return self.__board
    

    def get_rules(self) -> Rules:
        '''
        Get the rules of the game
        '''

        return self.__rules
    

    def get_player(self) -> Player:
        '''
        Get the current player
        '''

        return self.__current_player
    
    def get_num_players(self) -> int:
        '''
        Get the number of players in the game
        '''

        return self.__num_players