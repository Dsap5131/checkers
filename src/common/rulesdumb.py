from typing import List

from src.common.move import Move
from src.common.board import Board
from src.common.player import Player
from src.common.position import Position
from src.common.rules import Rules
from src.common.playerstate import PlayerState
from src.common.gamepiece import GamePiece
from src.common.piece import Piece

class RulesDumb(Rules):
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

        RulesDumb doesn't care and will always return an empty list.
        
        @params: board: Board
        @params: player: Player

        @returns: List[Move]
        '''

        return []
    

    def is_winner(self, board: Board, playerstate: PlayerState) -> bool:
        '''
        Return if the player is a winner based on the given board
        
        @params: board: Board
        @params: playerstate: PlayerState
        
        @returns: List[Move]
        '''

        return False
                

    def starting_board(self) -> Board:
        '''
        Return the starting Board for a game using these rules.

        @returns: Board
        '''

        return Board(1,1,[[GamePiece(Piece.BLANK)]])

        



