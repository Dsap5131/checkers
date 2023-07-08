from collections import deque

from src.common.rules import Rules
from src.common.move import Move
from src.common.board import Board
from src.common.player import Player
from src.common.position import Position
from src.common.gamepiece import GamePiece
from src.common.leap import Leap


class RulesStandard(Rules):
    '''
    Standard Set of Checkers rules.
    '''

    def check_move(self, move: Move, board: Board, player: Player) -> bool:
        '''
        A move is valid if a player is moving their own piece 1 space diagonally
        to a blank space. A move is allowed to jump diagonally over an 
        opponents piece, capturing their piece.

        @param: move: Move: move being made.
        @param: board: Board: board the move is made on.
        @param: player: Player: player making the move.

        @returns: bool: True if it is valid and False if not.
        '''
        
        valid_move = True
        while move.leaps_remaining() > 0:
            leap = move.get_next_leap()
            valid_move = valid_move and self.__check_leap(leap, board, player)
            if not valid_move:
                break
            board.move_piece(Move(deque([leap])))
        return valid_move


    def __check_leap(self, leap: Leap, board: Board, player: Player) -> bool:
        '''
        Check to see if a given leap is valid for the player on the board.

        @param: leap: Leap
        @param: board: Board
        @param: player: Player

        @returns: bool: True if it is valid and False if not.
        '''

        start_position = leap.get_start_position()
        end_position = leap.get_end_position()

        # Check to see if the leap is on the board
        if not (self.check_position(start_position, board) and 
                self.check_position(end_position, board)):
            return False
        
        # Check to see if the leap is using the correct players piece
        if (player.get_gamepiece() != board.get_piece(start_position)):
            return False
        
        # Check to see if the leap is a valid 1 space move
        one_leap = ((abs(end_position.get_row()
                        - start_position.get_row()) == 1) and
                    (abs(end_position.get_column()
                        - start_position.get_column()) == 1) and
                    board.get_piece(end_position) == GamePiece.BLANK)

        # Check to see if the leap is a valid capture
        if not ((abs(end_position.get_row()
                    - start_position.get_row()) == 2) and
                (abs(end_position.get_column()
                    - start_position.get_column()) == 2)):
            capture = False
        elif not one_leap:
            middle_position_row = int((end_position.get_row()-start_position.get_row())/2) + start_position.get_row()

            middle_position_column = int((end_position.get_column()-start_position.get_column())/2) + start_position.get_column()
            middle_position = Position(middle_position_row, middle_position_column)

            capture = (board.get_piece(end_position) == GamePiece.BLANK and
                       (board.get_piece(middle_position) != player.get_gamepiece() 
                        and board.get_piece(middle_position) != GamePiece.BLANK))
            
        if (one_leap or capture):
            return True
        else:
            return False


    def check_position(self, position: Position, board: Board) -> bool:
        '''
        Check to see if the given Position is on the Board.

        @param: position: Position
        @param: board: Board

        @returns: bool: True if it is on the board and False if not.
        '''

        return ((position.get_row() < board.get_row_size()) and
                (position.get_row() >= 0) and
                (position.get_column() < board.get_column_size()) and
                (position.get_column() >= 0))

