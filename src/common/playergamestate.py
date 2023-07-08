from src.common.board import Board
from src.common.rules import Rules

class PlayerGameState():
    '''
    Represents the knowledge a player has about the game.

    @param: board: Board
    @param: rules: Rules
    '''

    def __init__(self, board: Board, rules: Rules) -> None:
        self.__board = board
        self.__rules = rules

    
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