from typing import List

from src.common.move import Move
from src.common.board import Board
from src.common.player import Player
from src.common.position import Position
from src.common.playerstate import PlayerState

class Rules():
    '''
    Rules is an abstract class / interface that represents the template all
    Rules MUST follow. This class is not to directly used.
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

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def check_position(self, position: Position, board: Board) -> bool:
        '''
        Check to see if the given Position is valid.

        @param: position: Position
        @param: board: Board

        @returns: bool: True if it is valid.
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def is_game_over(self, 
                     board: Board, 
                     num_players: int,
                     current_player: PlayerState,
                     turns: int) -> bool:
        '''
        Check to see if the game is over.

        @param: board: Board
        @param: num_players: int: Number of players in the game
        @param: current_player: PlayerState: the current player in the game
        @param: turns: int: current turn of the game.

        @returns: bool: True if the game is over.
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def kickable(self) -> bool:
        '''
        Check to see if players are kicked from the game for invalid
        inputs.

        @returns: bool: True if they are kicked.
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def valid_moves(self, board: Board, player: Player) -> List[Move]:
        '''
        Return all valid moves the given player can make on the given
        board.

        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")


    def is_winner(self, board: Board, playerstate: PlayerState) -> bool:
        '''
        Return if the player is a winner based on the given board
        
        @params: board: Board
        @params: playerstate: PlayerState
        
        @returns: List[Move]
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def starting_board(self) -> Board:
        '''
        Return the starting Board for a game using these rules.

        @returns: Board
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def __eq__(self, obj) -> bool:
        '''
        Return whether two Rules are equals

        @param: obj

        @return: bool
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.") 
