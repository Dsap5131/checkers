from collections import deque

from src.common.board import Board
from src.common.rules import Rules
from src.common.player import Player
from src.common.playergamestate import PlayerGameState

class GameState():
    '''
    Represents the current state of a checkers game.

    @param: board: Board: current board state
    @param: rules: Rules: Rules for dictating this game.
    @param: players: deque[Player]: queue of players in the game
    '''

    def __init__(self, board: Board, rules: Rules, players: deque[Player]) \
            -> None:
        self.__board = board
        self.__rules = rules
        self.__players = players


    def is_game_over(self) -> bool:
        '''
        Check if the current gamestate is in a gameover state.

        @returns: bool: True if the game is in a gameover state.
        '''

        return self.__rules.is_game_over(self.__board, 
                                         len(self.__players), 
                                         self.__players[0])
    

    def take_turn(self) -> None:
        '''
        Go through one turn of the game.
        '''
        current_player = self.__players.popleft()
        move = current_player.get_move(self.__make_playergamestate())
        if self.__rules.check_move(move, self.__board, current_player):
            self.__board.move_piece(move)
            self.__players.append(current_player)
        elif not self.__rules.kickable():
            self.__players.append(current_player)


    def __make_playergamestate(self) -> None:
        '''
        Create PlayerGameState from current gamestate.
        '''
        return PlayerGameState(Board.from_board(self.__board), self.__rules)



    
