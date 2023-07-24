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
from src.common.playerstate import PlayerState


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
                     current_player: Player,
                     turns: int) -> bool:
        '''
        Check to see if the game is over. A game is over if there is only 1
        players, 1 type of piece on the board, or no available moves left
        for the current player.

        @param: board: Board
        @param: num_players: int: Number of players in the game
        @param: current_player: Player: current player in the game
        @param: turns: int: current turn of the game

        @returns: bool: True if the game is over.
        '''

        return (num_players <= 1 or 
                board.unique_piece_count() <= 1 or
                self.__check_no_moves(board, current_player) or
                turns > 200)
    

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
                current_position = Position(r,c)
                piece = board.get_gamepiece(current_position).get_piece()

                if piece == player.get_piece():
                    valid_moves += self.__get_extended_valid_moves(
                        self.__get_possible_leaps(current_position),
                        current_position,
                        board,
                        player)
        return valid_moves

    def __get_extended_valid_moves(self,
                                   leaps: List[Leap],
                                   current_position: Position,
                                   board: Board,
                                   player: Player) -> List[Move]:
        """
        Gets all possible moves given based on the possible leaps and
        the piece at the current_position.

        @params: end_positions: List[Position]
        @params: capture_positions: List[Position]
        @params: current_position: Position
        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        """

        valid_moves = []
        for leap in leaps:
            move = Move(deque([leap]))
            if self.check_move(move, board, player):
                valid_moves.append(move)

                new_board = Board.from_board(board)
                new_board.move_piece(move)
                move.reset()
                end_position = leap.get_end_position()
                new_leaps = self.__get_possible_leaps(end_position, True)
                extended_moves = self.__get_extended_valid_moves(
                    new_leaps,
                    end_position,
                    new_board,
                    player)
                for extended_move in extended_moves:
                        leaps = [Leap(current_position,
                                      end_position,
                                      leap.get_capture_positions(),
                                      leap.get_promote_positions())]
                        while extended_move.leaps_remaining()>0:
                            leaps.append(extended_move.get_next_leap())
                        valid_moves.append(Move(deque(leaps)))
        return valid_moves
    

    def __get_possible_leaps(self, 
                             position: Position,
                             only_captures: bool = False):
        '''
        This will return a list of all next leaps a piece can take valid or 
        invalid.

        @params: position: Position
        @params: captures: bool: True if you want only capture leaps

        @returns: List[Leap]
        '''

        start_row = position.get_row()
        start_column = position.get_column()
        leaps = []
        possible_captures = [(-2,-2),(-2,+2),(+2,-2),(+2,+2)]
        possible_singles = [(-1,-1),(-1,+1),(+1,-1),(+1,+1)]
        # Possible capture leaps
        for (end_updates, capture_updates) in \
                zip(possible_captures, possible_singles):
            end_position = Position(start_row+end_updates[0],
                                    start_column+end_updates[1])
            for promote_positions in [[], [end_position]]:
                capture_positions = [Position(start_row+capture_updates[0],
                                              start_column+capture_updates[1])]
                leaps.append(Leap(position,
                                end_position,
                                capture_positions,
                                promote_positions))
        # Possible single leaps
        if not only_captures:
            for end_updates in possible_singles:
                end_position = Position(start_row+end_updates[0],
                                        start_column+end_updates[1])
                for promote_positions in [[], [end_position]]:
                    leaps.append(Leap(position,
                                    end_position,
                                    [],
                                    promote_positions))
        return leaps
    

    def is_winner(self, 
                  board: Board, 
                  playerstate: PlayerState,
                  num_players: int) -> bool:
        '''
        Return if the player is a winner based on the given board
        
        @params: board: Board
        @params: playerstate: PlayerState
        
        @returns: List[Move]
        '''

        if num_players == 1:
            return True
        elif board.unique_piece_count() != 1:
            return False
        
        for r in range(board.get_row_size()):
            for c in range(board.get_column_size()):
                piece = board.get_gamepiece(Position(r,c)).get_piece()
                if piece == playerstate.get_piece():
                    return True
                elif piece != Piece.BLANK:
                    return False
                

    def starting_board(self) -> Board:
        '''
        Return the starting Board for a game using these rules.

        @returns: Board
        '''

        column_size = 8
        board_list = []
        # Black Player Starting Area
        for r in range(3):
            row = []
            for c in range(8):
                if (r+c)%2 == 0:
                    row.append(GamePiece(Piece.BLACK))
                else:
                    row.append(GamePiece(Piece.BLANK))
            board_list.append(row)
        # Neutral Area
        board_list.append([GamePiece(Piece.BLANK) for _ in range(column_size)])
        board_list.append([GamePiece(Piece.BLANK) for _ in range(column_size)])
        # Red Player Area
        for r in range(3):
            row = []
            for c in range(8):
                if (r+c)%2 == 0:
                    row.append(GamePiece(Piece.RED))
                else:
                    row.append(GamePiece(Piece.BLANK))
            board_list.append(row)
        return Board(row_size=8, column_size=column_size, board=board_list)
        




