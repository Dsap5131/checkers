from collections import deque
from typing import List

from src.common.rules import Rules
from src.common.move import Move
from src.common.board import Board
from src.common.player import Player
from src.common.position import Position
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
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

        Red pieces can only move up on the board unless it is a king.
        Black pieces can only move down on the board unless it is a king.

        A piece may only promote itself when it gets to the end of the board.
        It may only promote on the opponents side. It may only promote itself 
        and not others.

        @param: move: Move: move being made.
        @param: board: Board: board the move is made on.
        @param: player: Player: player making the move.

        @returns: bool: True if it is valid and False if not.
        '''

        private_board = Board.from_board(board)

        while move.leaps_remaining() > 0:
            leap = move.get_next_leap()
            if not self.__check_leap(leap, private_board, player):
                move.reset()
                return False
            private_board.move_piece(Move(deque([leap])))
        move.reset()
        return True


    def __check_leap(self, leap: Leap, board: Board, player: Player) -> bool:
        '''
        Check to see if a given leap is valid for the player on the board.

        A red piece can only leap upwards on the board unless it is a king.
        A black piece can only leap downwards on the board unless it isi a king.

        @param: leap: Leap
        @param: board: Board
        @param: player: Player

        A piece may only promote itself when it gets to the end of the board.
        It may only promote on the opponents side. It may only promote itself 
        and not others.

        @returns: bool: True if it is valid and False if not.
        '''

        start_position = leap.get_start_position()
        end_position = leap.get_end_position()

        onboard = (self.check_position(start_position, board) and 
                   self.check_position(end_position, board))  
        if not onboard:
            return False
        
        players_piece = (player.get_piece()==
                         board.get_gamepiece(start_position).get_piece())
        if not players_piece:
            return False

        direction = self.__check_leap_direction(
            leap, 
            board.get_gamepiece(start_position))  
        one_leap = self.__check_single_leap(leap, board)
        capture = self.__check_capture_leap(leap, board)
        proper_promote = self.__check_promotion(leap,
                                                board)

        return direction and (one_leap or capture) and proper_promote
    

    def __check_promotion(self, leap: Leap, board: Board) -> bool:
        '''
        Check to see if a piece is properly being promoted.
        A piece may only promote itself when it gets to the end of the board.
        It may only promote on the opponents side. It may only promote itself 
        and not others.

        Assumes leap is on the board and valid.
        
        @param: leap: Leap
        @param: board: Board

        @returns: bool: True if the promote is valid
        '''

        promote_positions = leap.get_promote_positions()
        
        if len(promote_positions) == 1:
            end_position = leap.get_end_position()
            end_row = end_position.get_row()

            gamepiece = board.get_gamepiece(leap.get_start_position())
            piece = gamepiece.get_piece()
            is_king = gamepiece.is_king()

            valid_red_promote = piece == Piece.RED and end_row == 0
            valid_black_promote = (piece == Piece.BLACK and 
                                   end_row == board.get_row_size()-1)
            valid_promote = (promote_positions[0] == end_position and 
                             not is_king)

            return (valid_red_promote or valid_black_promote) and valid_promote
    
        if len(promote_positions) == 0:
            end_row = leap.get_end_position().get_row()
            piece = board.get_gamepiece(leap.get_start_position()).get_piece()

            return ((piece == Piece.RED and end_row != 0)
                    or (piece == Piece.BLACK and
                        end_row != board.get_row_size()-1))
    
        return False


    def __check_leap_direction(self, leap: Leap, gamepiece: GamePiece) -> bool:
        '''
        Checks to see if the direction of a leap is valid.

        Red pieces can only leap up on the board unless they are a king.
        Black pieces can only leap down on the board unless they are a king.

        @param: leap: Leap
        @param: gamepiece: GamePiece

        @returns: bool
        '''

        end_row = leap.get_end_position().get_row()
        start_row = leap.get_start_position().get_row()
        direction_row = end_row-start_row

        red_direction = direction_row<=-1 and gamepiece.get_piece()==Piece.RED
        black_direction = (direction_row>=1 and 
                          gamepiece.get_piece()==Piece.BLACK)

        return (gamepiece.is_king() or 
                red_direction or
                black_direction)
        


    def __check_capture_leap(self, leap: Leap, board: Board) \
        -> bool:
        '''
        Checks to see if a leap moves a piece 2 spaces diagonally capturing
        an opponents piece.

        Assumes the leap is on the board.

        @param: leap: Leap
        @param: board: Board

        @returns: bool: True if the leap is a capture leap.
        '''

        start_position = leap.get_start_position()
        end_position = leap.get_end_position()
        start_row = start_position.get_row()
        end_row = end_position.get_row()
        start_column = start_position.get_column()
        end_column = end_position.get_column()

        two_space_leap = ((abs(end_row - start_row) == 2) and
                          (abs(end_column - start_column) == 2))
        
        if two_space_leap:
            middle_row = int((end_row-start_row)/2) + start_row
            middle_column= int((end_column-start_column)/2) + start_column
            middle_position = Position(middle_row, middle_column)

            to_blank = board.get_gamepiece(end_position).get_piece() \
                        == Piece.BLANK
            over_opponent = board.get_gamepiece(middle_position) \
                                != board.get_gamepiece(start_position)
            not_over_blank = board.get_gamepiece(middle_position).get_piece() \
                                 != Piece.BLANK
            correct_captures = leap.get_capture_positions() == \
                                [middle_position]
        
            return (to_blank and 
                    over_opponent and 
                    not_over_blank and 
                    correct_captures)
    
        return False
        

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
        to_blank_space = board.get_gamepiece(end_position).get_piece() \
                            == Piece.BLANK
        no_captures = leap.get_capture_positions() == []
        
        return within_rows and within_cols and to_blank_space and no_captures


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
    

    def is_game_over(self, board: Board, 
                     num_players: int, 
                     current_player: Player) -> bool:
        '''
        Check to see if the game is over. A game is over if there is only 1
        players, 1 type of piece on the board, or no available moves left
        for the current player.

        @param: board: Board
        @param: num_players: int: Number of players in the game
        @param: current_player: Player: 

        @returns: bool: True if the game is over.
        '''

        return (num_players <= 1 or 
                board.unique_piece_count() <= 1 or
                self.__check_no_moves(board, current_player))
    

    def __check_no_moves(self, board: Board, current_player: Player) -> bool:
        '''
        Checks to see if the current player has any moves left on the board.

        @returns: True if they have a valid move.
        '''
        
        current_piece = current_player.get_piece()

        for r in range(board.get_row_size()):
            for c in range(board.get_column_size()):
                piece = board.get_gamepiece(Position(r,c)).get_piece()
                if piece == current_piece:
                    has_moves = self.__check_moves_from_position(
                        board, Position(r,c), current_player)
                    if has_moves:
                        return False
                    
        return True


    def __check_moves_from_position(self, 
                                    board: Board, 
                                    position: Position, 
                                    player: Player) -> bool:
        '''
        Checks to see if the piece at position has any possible moves.

        @params: board: Board
        @params: position: Position
        @params: player: Player

        @returns: True if they have a valid move.
        '''

        start_row = position.get_row()
        start_column = position.get_column()
        end_positions = [Position(start_row-2, start_column-2),
                         Position(start_row-2, start_column+2),
                         Position(start_row+2, start_column-2),
                         Position(start_row+2, start_column+2),
                         Position(start_row-1, start_column-1),
                         Position(start_row-1, start_column+1),
                         Position(start_row+1, start_column-1),
                         Position(start_row+1, start_column+1)]
        capture_positions = [[Position(start_row-1, start_column-1)],
                             [Position(start_row-1, start_column+1)],
                             [Position(start_row+1, start_column-1)],
                             [Position(start_row+1, start_column+1)],
                             [],
                             [],
                             [],
                             []]
        for (end_position, capture_position) in zip(end_positions, 
                                                    capture_positions):
            for promote_position in [[], [end_position]]:
                leap = Leap(position, 
                            end_position, 
                            capture_position,
                            promote_position)
                if self.__check_leap(leap, board, player):
                    return True
        return False
    

    def kickable(self) -> bool:
        '''
        Check to see if players are kicked from the game for invalid
        inputs.

        @returns: bool: True if they are kicked.
        '''

        return True
    

    def valid_moves(self, board: Board, player: Player) -> List[Move]:
        '''
        Return all valid moves the given player can make on the given
        board.

        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        '''

        valid_moves = []
        for r in range(board.get_row_size()):
            for c in range(board.get_column_size()):
                piece = board.get_gamepiece(Position(r,c)).get_piece()

                if piece == player.get_piece():
                    valid_moves += self.__get_valid_moves(Position(r,c), 
                                                          board,
                                                          player)
        return valid_moves


    def __get_valid_moves(self, 
                          position: Position, 
                          board: Board, 
                          player: Player) -> List[Move]:
        """
        Returns the valid moves of the piece at position on board.
        
        @params: position: Position
        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        """

        start_row = position.get_row()
        start_column = position.get_column()

        end_positions = [Position(start_row-2, start_column-2),
                         Position(start_row-2, start_column+2),
                         Position(start_row+2, start_column-2),
                         Position(start_row+2, start_column+2),
                         Position(start_row-1, start_column-1),
                         Position(start_row-1, start_column+1),
                         Position(start_row+1, start_column-1),
                         Position(start_row+1, start_column+1)]
        
        valid_moves = []
        for end_position in end_positions:
            leaps = [Leap(position, end_position)]
            move = Move(deque(leaps))
            valid_move = self.check_move(move, board, player)
            move.reset()
            if valid_move:
                valid_moves.append(move)
            
                new_board = Board.from_board(board)
                new_board.move_piece(move)
                move.reset()
                extended_moves = self.__get_valid_capture_moves(end_position, 
                                                                new_board, 
                                                                player)
                

                for extended_move in extended_moves:
                    new_leaps = [Leap(position, end_position)]
                    while extended_move.leaps_remaining() > 0:
                        new_leaps.append(extended_move.get_next_leap())
                    new_move = Move[deque(leaps)]
                    valid_moves.append(new_move)
        return valid_moves
    

    def __get_valid_capture_moves(self, 
                          position: Position, 
                          board: Board, 
                          player: Player) -> List[Move]:
        """
        Returns the valid moves of the piece at position on board.
        
        @params: position: Position
        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        """

        start_row = position.get_row()
        start_column = position.get_column()

        end_positions = [Position(start_row-2, start_column-2),
                         Position(start_row-2, start_column+2),
                         Position(start_row+2, start_column-2),
                         Position(start_row+2, start_column+2)]
        
        valid_moves = []
        for end_position in end_positions:
            leaps = [Leap(position, end_position)]
            move = Move(deque(leaps))
            valid_move = self.check_move(move, board, player)
            move.reset()
            if valid_move:
                valid_moves.append(move)
            
                new_board = Board.from_board(board)
                new_board.move_piece(move)
                move.reset()
                extended_moves = self.__get_valid_capture_moves(end_position, 
                                                                new_board, 
                                                                player)
                

                for extended_move in extended_moves:
                    new_leaps = [Leap(position, end_position)]
                    while extended_move.leaps_remaining() > 0:
                        new_leaps.append(extended_move.get_next_leap())
                    new_move = Move[deque(leaps)]
                    valid_moves.append(new_move)
        return valid_moves

