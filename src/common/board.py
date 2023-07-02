from typing import List

from src.common.gamepiece import GamePiece
from src.common.position import Position
from src.common.move import Move

class Board():
    '''
    Board represents the board of a checkers board. 


    @param: row_size: int: The number of rows the board has
    @param: column_size: int: The number of columns the board has
    @param: board: List[List[GamePiece]]: The board.
    '''

    def __init__(self, 
                 row_size: int, 
                 column_size: int, 
                 board: List[List[GamePiece]]) -> None:
        self.__row_size = row_size
        self.__column_size = column_size
        self.__board = board

    
    def get_row_size(self) -> int:
        '''
        Get the number of rows of the board.

        @returns: int
        '''

        return self.__row_size
    

    def get_column_size(self) -> int:
        '''
        Get the number of columns of the board.

        @returns: int
        '''
        return self.__column_size
    

    def get_piece(self, position: Position) -> GamePiece:
        '''
        Get GamePiece at a given Position

        @param: position: Position
        
        @returns: GamePiece
        '''

        return self.__board[position.get_row()][position.get_column()]
    
    def move_piece(self, move: Move) -> None:
        '''
        Move a GamePiece 

        @param: move: Move
        '''

        current_position = move.get_current_position()
        new_position = move.get_new_position()
        gamepiece = self.get_piece(current_position)
        
        self.__board[current_position.get_row()][current_position.get_column()] = GamePiece.BLANK
        self.__board[new_position.get_row()][new_position.get_column()] = gamepiece


