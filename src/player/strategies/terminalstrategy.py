from collections import deque

from src.player.strategies.strategy import Strategy
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.common.board import Board

class TerminalStrategy(Strategy):
    '''
    TerminalStrategy is a way of playing through the terminal.

    It outputs to the terminal and listens for human input through the terminal.

    The terminal strategy isn't responsible for verifying the move a player
    makes. The player should know whats legal and not.
    '''

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Make a move based on the given playergamestate.

        Given playergamestate should never be in a gameover state. Thus a valid
        move should exist.

        @param: playergamestate: PlayerGameState

        @returns: Move
        '''

        board = playergamestate.get_board()

        print('---------------Board State---------------')
        print(board)
        print(
            f'You are {playergamestate.get_current_player().get_piece().value}')
        leaps = []
        leaping = True
        while leaping:
            start_position = self.__get_position(
                'Enter the position of the piece you would like to move.'+\
                    '(r,c)\n')
            end_position = self.__get_position(
                'Enter the position of where to move the piece to. (r,c)\n')
            
            capture_positions = []
            capture = input('Does this capture a piece? Y/n\n')
            if capture == 'Y':
                capture_positions.append(self.__get_position(
                    'Enter the position of the captured piece. (r,c)\n'))
                
            promote_positions = []
            promote = input('Does this promote a piece? Y/n\n')
            if promote == 'Y':
                promote_positions.append(self.__get_position(
                    'Enter the position of the promoted piece. (r,c)\n'))
                
            keep_leaping = input('Does this piece continue leaping? Y/n\n')
            leaping = keep_leaping == "Y"

            leaps.append(Leap(start_position,
                              end_position,
                              capture_positions,
                              promote_positions))
        return Move(deque(leaps))
            


    def __get_position(self, message: str) -> Position:
        '''
        Print the message and get user input in the form of (r,c)
        Convert this to a Position and return

        @params: message: str

        @returns: Position
        '''

        position = input(message).strip()[1:-1].split(',')
        return Position(int(position[0]), int(position[1]))
        


