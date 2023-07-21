from collections import deque
from typing import Tuple

from src.player.strategies.strategy import Strategy
from src.common.move import Move
from src.common.playergamestate import PlayerGameState
from src.common.position import Position
from src.common.board import Board
from src.common.rules import Rules
from src.common.leap import Leap
from src.common.player import Player
from src.common.piece import Piece

class BasicStrategy(Strategy):
    '''
    Basic Strategy is a simple strategy in checkers. It is made to be played
    against the standard ruleset

    The strategy works by
     
    1) Selecting the top-left most piece with a valid move. 
        Prioritizing row over column.
    2) Check for captures prioritizing capturing towards the top left.
        Prioritizing row over column
    3) Check for leaps prioritizing leaping towards the top left. 
        Prioritizing row over column
    '''

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Make a move based on the given playergamestate.

        Given playergamestate should never be in a gameover state. Thus a valid
        move should exist.

        @param: playergamestate: PlayerGameState

        @returns: Move
        '''
        board = playergamestate.get_board()
        player = playergamestate.get_current_player()
        piece = player.get_piece()

        for r in range(board.get_row_size()):
            for c in range(board.get_column_size()):
                current_piece = board.get_gamepiece(Position(r,c))
                if current_piece.get_piece() == piece:
                    valid, move = \
                        self.__check_for_move(board, 
                                              Position(r,c), 
                                              playergamestate.get_rules(),
                                              player)
                    if valid:
                        return move
        return Move(deque([Leap(Position(0,0), Position(0,0))]))
                    
    
    def __check_for_move(self, 
                         board: Board, 
                         position: Position,
                         rules: Rules,
                         player: Player) -> Tuple[bool, Move]:
        """
        Checks for valid moves from a given position in the form 
        this strategy follows. Will return a tuple with a bool 
        where it is True if there is a valid move. If bool is True
        then there will be a Move returned as the second object of 
        the tuple. Otherwise the second object will be none.

        @param: board: Board
        @param: position: Position
        @param: rules: Rules
        @param: player: Player

        @returns: Tuple[bool, Move]
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
        capture_positions = [[Position(start_row-1, start_column-1)],
                             [Position(start_row-1, start_column+1)],
                             [Position(start_row+1, start_column-1)],
                             [Position(start_row+1, start_column+1)],
                             [],
                             [],
                             [],
                             []]
        
        for (end_position, capture_position_list) in zip(end_positions,
                                                         capture_positions):
            
            gamepiece = board.get_gamepiece(position)
            piece = gamepiece.get_piece()
            is_king = gamepiece.is_king()

            promote_positions = []
            valid_red_promote = (end_position.get_row() == 0 
                                 and piece == Piece.RED)
            valid_black_promote = (end_position.get_row() \
                                        == board.get_row_size()-1
                                   and piece == Piece.BLACK)
            valid_promote = not is_king
            if (valid_red_promote or valid_black_promote) and valid_promote:
                promote_positions.append(end_position)
                
            move = Move(deque([Leap(position, 
                                    end_position,
                                    capture_position_list,
                                    promote_positions)]))
            valid_move = rules.check_move(move, board, player) 
            move.reset()
            if valid_move:
                return True, move
            
        return False, None
            
        