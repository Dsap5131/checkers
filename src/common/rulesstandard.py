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

        onboard = (self.check_position(start_position, board) and 
                   self.check_position(end_position, board))  
        if not onboard:
            return False
        
        players_piece = player.get_gamepiece()==board.get_piece(start_position)  
        one_leap = self.__check_single_leap(leap, board)
        capture = self.__check_capture_leap(leap, board)
            
        return players_piece and (one_leap or capture)
        

    def __check_capture_leap(self, leap: Leap, board: Board) \
        -> bool:
        '''
        Checks to see if a leap moves a piece 2 spaces diagonally capturing
        an opponents piece.

        @param: leap: Leap
        @param: board: Board

        @returns: bool: True if the leap is a capture leap.
        '''

        start_position = leap.get_start_position()
        end_position = leap.get_end_position()

        two_space_leap = ((abs(end_position.get_row()
                              - start_position.get_row()) == 2) and
                          (abs(end_position.get_column()
                              - start_position.get_column()) == 2))
        
        if not two_space_leap:
            capture = False
        else:
            start_row = start_position.get_row()
            end_row = end_position.get_row()
            start_column = start_position.get_column()
            end_column = end_position.get_column()

            middle_row = int((end_row-start_row)/2) + start_row
            middle_column= int((end_column-start_column)/2) + start_column
            middle_position = Position(middle_row, middle_column)

            to_blank = board.get_piece(end_position) == GamePiece.BLANK
            over_opponent = board.get_piece(middle_position) \
                            != board.get_piece(start_position)
            not_over_blank = board.get_piece(middle_position) != GamePiece.BLANK
        
            capture = to_blank and over_opponent and not_over_blank
    
        return capture
        

    def __check_single_leap(self, leap: Leap, board: Board) -> bool:
        '''
        Checks to see if a leap moves a piece 1 space diagonally
        onto a blank space

        @param: leap: Leap
        @param: board: Board

        @returns: bool: True if the leap is a 1 space diagonal leap.
        '''
        
        start_position = leap.get_start_position()
        end_position = leap.get_end_position()

        within_rows = (abs(end_position.get_row()-start_position.get_row())==1)
        within_cols = (abs(end_position.get_column()
                           -start_position.get_column())==1)
        to_blank_space = board.get_piece(end_position) == GamePiece.BLANK
        
        return within_rows and within_cols and to_blank_space


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

