from src.player.strategies.strategy import Strategy
from src.common.move import Move
from src.common.playergamestate import PlayerGameState
from src.common.rules import Rules
from src.common.player import Player
from src.common.board import Board

class MiniMaxStrategy(Strategy):
    """
    MiniMaxStrategy is a strategy that uses a MinMax Algorithm to determine the
    next best move.
    """

    def make_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Make a move based on the given playergamestate.

        Given playergamestate should never be in a gameover state. Thus a valid
        move should exist.

        @param: playergamestate: PlayerGameState

        @returns: Move
        '''
        
        rules = playergamestate.get_rules()
        board = playergamestate.get_board()
        player = playergamestate.get_player()

        # Get Valid Moves
        #valid_moves = self.__get_valid_moves(rules, board, player)
        # if a valid move leads to a winning gamestate, store that move.
        # Tiebreaker between winning moves. 
            # Prioritize moving the piece to the top left most position
        
        

