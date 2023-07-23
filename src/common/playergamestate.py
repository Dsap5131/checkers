from collections import deque

from src.common.board import Board
from src.common.rules import Rules
from src.common.playerstate import PlayerState

class PlayerGameState():
    '''
    Represents the knowledge a player has about the game.

    @param: board: Board
    @param: rules: Rules
    @param: players: deque[PlayerState]
    '''

    def __init__(self, 
                 board: Board, 
                 rules: Rules, 
                 players: list[PlayerState]) -> None:
        self.__board = board
        self.__rules = rules
        self.__players = deque(players)

    
    def get_board(self) -> Board:
        '''
        Get the board of the gamestate
        '''

        return self.__board
    

    def get_rules(self) -> Rules:
        '''
        Get the rules of the game
        '''

        return self.__rules
    

    def get_current_player(self) -> PlayerState:
        '''
        Get the current player
        '''

        return self.__players[0]
    

    def set_next_player(self) -> None:
        '''
        Update the current player
        '''

        current_player = self.__players.popleft()
        self.__players.append(current_player)


    def get_num_players(self) -> int:
        '''
        Get the number of players in the game
        '''

        return len(self.__players)
    

    def get_players(self) -> list[PlayerState]:
        '''
        Returns the list of active players.
        '''

        return list(self.__players)