from src.common.board import Board
from src.common.rules import Rules
from src.common.piece import Piece

class PlayerGameState():
    '''
    Represents the knowledge a player has about the game.

    @param: board: Board
    @param: rules: Rules
    @param: current_piece: Piece
    '''

    def __init__(self, board: Board, rules: Rules, current_piece: Piece)-> None:
        self.__board = board
        self.__rules = rules
        self.__current_piece = current_piece

    
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
    

    def get_piece(self) -> Piece:
        '''
        Get the piece of the current players piece.
        '''

        return self.__current_piece