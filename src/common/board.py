from typing import List

from src.common.gamepiece import GamePiece
from src.common.position import Position
from src.common.move import Move
from src.common.leap import Leap

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

        while move.leaps_remaining() > 0:
            self.__leap_piece(move.get_next_leap())


    def __leap_piece(self, leap: Leap) -> None:
        '''
        Perform a leap with a piece
        
        @param: leap: Leap
        '''

        start_position = leap.get_start_position()
        end_position = leap.get_end_position()
        gamepiece = self.get_piece(start_position)

        self.__board[start_position.get_row()][start_position.get_column()] \
            = GamePiece.BLANK
        self.__board[end_position.get_row()][end_position.get_column()] \
            = gamepiece


