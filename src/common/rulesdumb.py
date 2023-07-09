from src.common.move import Move
from src.common.board import Board
from src.common.player import Player
from src.common.position import Position

class RulesDumb():
    '''
    RulesDumb is a dumb set of rules. Everything is valid and the game never
    ends.
    '''

    def check_move(self, move: Move, board: Board, player: Player) -> bool:
        '''
        Check move checks a move based on a given move, board, and player 
        making the move.

        @param: move: Move: move being made.
        @param: board: Board: board the move is made on.
        @param: player: Player: player making the move.

        @returns: bool: True if it is valid and False if not.
        '''

        return True
    

    def check_position(self, position: Position, board: Board) -> bool:
        '''
        Check to see if the given Position is valid.

        @param: position: Position
        @param: board: Board

        @returns: bool: True if it is valid.
        '''

        return True
    

    def is_game_over(self, board: Board, num_players: int) -> bool:
        '''
        Check to see if the game is over.

        @param: board: Board
        @param: num_players: int: Number of players in the game

        @returns: bool: True if the game is over.
        '''

        return False
    

    def kickable(self) -> bool:
        '''
        Check to see if players are kicked from the game for invalid
        inputs.

        @returns: bool: True if they are kicked.
        '''

        return True

