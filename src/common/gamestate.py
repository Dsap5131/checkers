from typing import List

from src.common.player import Player
from src.common.board import Board
from src.common.position import Position
from src.common.gamepiece import GamePiece
from src.common.move import Move

class GameState():
    ''' 
    Represents the state of a checkers game.

    The idea is that with this GameState any Referee should be able to continue
    running a game given this GameState, assuming the Referees all use the same
    rulebook.

    @param: players: List[Player]
    @param: board: Board
    '''

    def __init__(self, board: Board, players: List[Player], ) -> None:
        self.__players = players
        self.__board = board

    
    def get_piece(self, position: Position) -> GamePiece:
        '''
        Get the gamepiece at a given Position
        
        @param: position: Position

        @returns: GamePiece
        '''

        return self.__board.get_piece(position)

    
    def make_move(self, move: Move) -> None:
        '''
        Make a move

        @param: move: Move
        '''

        self.__board.move_piece(move)