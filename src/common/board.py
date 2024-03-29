from __future__ import annotations
from typing import List

from src.common.gamepiece import GamePiece
from src.common.piece import Piece
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

    
    @classmethod
    def from_board(self, board: Board) -> Board:
        '''
        Copy Constructor

        @param: board: Board: Board to create a copy of.
        '''

        copied_row_size = board.get_row_size()
        copied_column_size = board.get_column_size()

        copied_board_list = []
        for r in range(copied_row_size):
            copied_row = []
            for c in range(copied_column_size):
                gamepiece = board.get_gamepiece(Position(r,c))
                new_gamepiece = GamePiece(gamepiece.get_piece(), 
                                          gamepiece.is_king())
                copied_row.append(new_gamepiece)
            copied_board_list.append(copied_row)


        return Board(row_size=copied_row_size,
                     column_size=copied_column_size,
                     board=copied_board_list)

    
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
    

    def get_gamepiece(self, position: Position) -> GamePiece:
        '''
        Get GamePiece at a given Position

        @param: position: Position
        
        @returns: GamePiece
        '''

        return self.__board[position.get_row()][position.get_column()]
    
    def move_piece(self, move: Move) -> None:
        '''
        Move a GamePiece, remove captured piece, promote selected pieces.

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
        gamepiece = self.get_gamepiece(start_position)

        self.__board[start_position.get_row()][start_position.get_column()] \
            = GamePiece(Piece.BLANK, False)
        self.__board[end_position.get_row()][end_position.get_column()] \
            = gamepiece
        
        capture_positions = leap.get_capture_positions()
        for capture_position in capture_positions:
            capture_row = capture_position.get_row()
            capture_column = capture_position.get_column()
            self.__board[capture_row][capture_column] = GamePiece(Piece.BLANK)

        promote_positions = leap.get_promote_positions()
        for promote_position in promote_positions:
            promote_row = promote_position.get_row()
            promote_column = promote_position.get_column()
            gamepiece = self.get_gamepiece(promote_position)
            gamepiece.make_king()
            self.__board[promote_row][promote_column] = gamepiece


    def unique_piece_count(self) -> int:
        '''
        Return the number of unique pieces on the board.
        Does not include blank pieces.

        @returns: int
        '''

        unique_piece_count = 0
        seen = []
        for r in range(self.get_row_size()):
            for c in range(self.get_column_size()):
                current_piece = self.get_gamepiece(Position(r,c))
                if (current_piece.get_piece() != Piece.BLANK
                        and not current_piece.get_piece() in seen):
                    unique_piece_count += 1
                    seen.append(current_piece.get_piece())
        return unique_piece_count


    def __eq__(self, obj) -> bool:
        """
        Boards are equal if all of their contents are equal.

        @returns: bool
        """

        if not isinstance(obj, Board):
            return False
        
        if (obj.get_row_size() == self.get_row_size() and
                obj.get_column_size() == self.get_column_size()):
            for r in range(self.get_row_size()):
                for c in range(self.get_column_size()):
                    if (self.get_gamepiece(Position(r,c)) != \
                            obj.get_gamepiece(Position(r,c))):
                        return False
            return True
        return False


    def __str__(self) -> str:
        """
        Override __str__ of Board

        @returns Board
        """

        output = ""
        for r in range(self.get_row_size()):
            row_output = ""
            divider_output = ""
            for c in range(self.get_column_size()):
                piece = self.get_gamepiece(Position(r,c))
                row_output += f" {str(piece)} "
                divider_output += "----"
                if c != self.get_column_size() - 1:
                    row_output += "|"
                    divider_output += "-"
            row_output += "\n"
            divider_output += "\n"
            output += row_output
            if r != self.get_row_size() - 1:
                output += divider_output
        return output

                    


