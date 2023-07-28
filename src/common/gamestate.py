from collections import deque

from multiprocessing import Process, Pipe
from src.common.board import Board
from src.common.rules import Rules
from src.common.player import Player
from src.common.playergamestate import PlayerGameState
from src.common.playerstate import PlayerState
from src.common.position import Position

class GameState():
    '''
    Represents the current state of a checkers game.

    @param: board: Board: current board state
    @param: rules: Rules: Rules for dictating this game.
    @param: players: deque[Player]: queue of players in the game
    @param: turn: current turn of the game
    '''

    def __init__(self, 
                 board: Board, 
                 rules: Rules, 
                 players: deque[Player], 
                 turn: int) -> None:
        self.__board = board
        self.__rules = rules
        self.__players = players
        self.__turn = turn
        self.__timeout = 30


    def is_game_over(self) -> bool:
        '''
        Check if the current gamestate is in a gameover state.

        @returns: bool: True if the game is in a gameover state.
        '''

        return self.__rules.is_game_over(self.__board, 
                                         len(self.__players), 
                                         self.__players[0],
                                         self.__turn)
    

    def take_turn(self) -> None:
        '''
        Go through one turn of the game.
        '''

        playerstates = self.__make_playergamestate()
        current_player = self.__players.popleft()
        intime, move = self.__player_interaction(current_player.get_move,
                                                 [playerstates])
        print(intime)
        if intime and self.__rules.check_move(move,self.__board,current_player):
            self.__board.move_piece(move)
            self.__players.append(current_player)
        elif not self.__rules.kickable():
            self.__players.append(current_player)
        self.__turn += 1


    def __player_interaction(self, func, args: list) -> tuple[bool, any]:
        '''
        All moments of interactions were the player is communicating to the game
        go through this function. This is to moderate timeouts and errors from 
        player interactions

        @params: func: function
        @params: args: list

        @return: tuple[bool, any]: The bool is True if there was a returned 
                                   value. If bool is false then the returned
                                   value is None.
        '''

        conn1, conn2 = Pipe()
        process = Process(target=self.__player_interaction_process,
                          args=[func, args, conn2])
        process.start()
        process.join(timeout=self.__timeout)
        process.terminate()

        if process.exitcode is None:
            return False, None
        else:
            return True, conn1.recv()


    def __player_interaction_process(self, 
                                     func,
                                     args: list,
                                     conn) -> None:
        '''
        Thread to interact to run func with args and send 
        the output through conn

        @param: func: function
        @param: args: list
        @param: conn: Pipe.connection
        '''

        conn.send(func(*args))



    def __make_playerstates(self) -> list[PlayerState]:
        '''
        Convert players into a list of playerstates

        @returns: List[PlayerState]
        '''

        playerstates = []
        for i in range(len(self.__players)):
            playerstate = self.__player_interaction(
                self.__players[i].get_playerstate, [])
            playerstates.append(playerstate)
        return playerstates


    def __make_playergamestate(self) -> None:
        '''
        Create PlayerGameState from current gamestate.
        '''
        return PlayerGameState(Board.from_board(self.__board), 
                               self.__rules,
                               self.__make_playerstates(),
                               self.__turn)
    

    def end_game(self) -> None:
        '''
        Alert players if they have won or lost.
        '''

        for player in self.__players:
            player.won(self.__rules.is_winner(self.__board, 
                                              player.get_playerstate(),
                                              len(self.__players)))



    
