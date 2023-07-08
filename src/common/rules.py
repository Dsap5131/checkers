from src.common.move import Move
from src.common.board import Board
from src.common.player import Player

class Rules():
    '''
    Rules is an abstract class / interface that represents the template all
    Rules MUST follow. This class is not to directly used.
    '''

    def check_move(move: Move, board: Board, player: Player) \
        -> tuple[bool, str]:
        '''
        Check move checks a move based on a given move, board, and player 
        making the move.

        @param: move: Move: move being made.
        @param: board: Board: board the move is made on.
        @param: player: Player: player making the move.

        @returns: bool: True if it is valid and False if not.
        @returns: str: String that describes why a move was invalid. Will be an
                       empty string if the move is valid.
        '''

        raise NotImplemented(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")

