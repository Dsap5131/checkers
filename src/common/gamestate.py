from typing import List

from src.common.board import Board
from src.common.rules import Rules
from src.common.player import Player

class GameState():
    '''
    Represents the current state of a checkers game.

    @param: board: Board: current board state
    @param: rules: Rules: Rules for dictating this game.
    @param: players: List[Player]: list of players in the game
    '''

    def __init__(self, board: Board, rules: Rules, players: List[Player]) \
            -> None:
        self.__board = board
        self.__rules = rules
        self.__players = players


    def is_game_over(self) -> bool:
        '''
        Check if the current gamestate is in a gameover state.

        @returns: bool: True if the game is in a gameover state.
        '''

        return self.__rules.is_game_over(self.__board, len(self.__players))
    

    def take_turn(self) -> None:
        '''
        Go through one turn of the game.
        '''
        ...
