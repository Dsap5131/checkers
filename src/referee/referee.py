from collections import deque

from src.common.rules import Rules
from src.common.player import Player
from src.common.gamestate import GameState

class Referee():
    '''
    A referee is the component that runs a game.
    '''


    def start_game(self, rules: Rules, players: list[Player]) -> None:
        '''
        Start a new game of checkers as specified by the rules. With given
        players.

        @params: rules: Rules
        @params: players: list[Player]
        '''
        
        self.continue_game(
            GameState(rules.starting_board(), rules, deque(players), 0))


    def continue_game(self, gamestate: GameState) -> None:
        '''
        Continue a game of checkers using the given gamestate.

        @params: gamestate: GameState
        '''

        while gamestate.is_game_over() == False:
            gamestate.take_turn()
        gamestate.end_game()
