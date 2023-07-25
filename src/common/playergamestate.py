from collections import deque
from copy import deepcopy

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
                 players: list[PlayerState],
                 turn: int) -> None:
        self.__board = board
        self.__rules = rules
        self.__players = deque(players)
        self.__turn = turn

    
    def get_board(self) -> Board:
        '''
        Get the board of the gamestate

        @return: Board
        '''

        return self.__board
    

    def get_rules(self) -> Rules:
        '''
        Get the rules of the game

        @return: Rules
        '''

        return self.__rules
    

    def get_current_player(self) -> PlayerState:
        '''
        Get the current player

        @return: PlayerState
        '''

        return self.__players[0]
    

    def set_next_player(self) -> None:
        '''
        Update the current player
        '''

        current_player = self.__players.popleft()
        self.__players.append(current_player)
        self.__turn += 1


    def get_num_players(self) -> int:
        '''
        Get the number of players in the game

        @returns: int
        '''

        return len(self.__players)
    

    def get_players(self) -> list[PlayerState]:
        '''
        Returns a copy of the list of active players.

        @returns: list[PlayerState]
        '''

        return list(deepcopy(self.__players))
    

    def get_turn(self) -> int:
        '''
        Return the current turn number.
        
        @returns: int
        '''

        return self.__turn
    

    def __eq__(self, obj) -> bool:
        '''
        Override __eq__ of PlayerGameState.

        PlayerGameStates are equal if all the fields are equal.
        '''

        if not isinstance(obj, PlayerGameState):
            return False
        
        return (obj.get_board() == self.get_board() and
                obj.get_rules() == self.get_rules() and
                obj.get_players() == self.get_players() and
                obj.get_turn() == self.get_turn())

