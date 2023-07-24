from src.player.strategies.strategy import Strategy
from src.common.playergamestate import PlayerGameState
from src.common.move import Move
from src.common.playerstate import PlayerState

class MiniMaxStrategy(Strategy):
    '''
    Performs the MiniMax algorithm to determine the next best move for the
    current player.
    '''
    
    def make_move(self, playergamestate: PlayerGameState) -> Move:
        '''
        Make a move based on the given playergamestate.

        Given playergamestate should never be in a gameover state. Thus a valid
        move should exist.

        @param: playergamestate: PlayerGameState

        @returns: Move
        '''
        
        # Pseudocode
        # function minimax(node, depth, maximizingPlayer) is
        #       if depth = 0 or node is terminal node then
        #               return the heuristic value of node
        #       if maximizingPlayer than
        #           value := -infinity
        #           for each child of node do
        #               value = max(value, minimax(child, depth-1, false))
        #       else (*minimizing player*)
        #           value := infinity
        #           for each child of node do
        #               value = min(value, minimax(child, depth-1,true))
        #           return value

        rules = playergamestate.get_rules()
        current_player = playergamestate.get_current_player()
        playergamestate.set_next_player()
        board = playergamestate.get_board()
        players = playergamestate.get_players()

        moves = rules.valid_moves(board, current_player)
        best_value = float('-inf')
        best_move = moves[0]
        for move in moves:
            new_playergamestate = PlayerGameState(board,
                                                  rules,
                                                  players)
            value = self.__minimax(move,
                                   new_playergamestate,
                                   current_player)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move
    

    def __minimax(self,
                  move: Move,
                  playergamestate: PlayerGameState, 
                  our_player: PlayerState) -> int:
        
        rules = playergamestate.get_rules()
        current_player = playergamestate.get_current_player()
        playergamestate.set_next_player()
        players = playergamestate.get_players()
        num_players = playergamestate.get_num_players()

        board = playergamestate.get_board()
        board.move_piece(move)
        move.reset()


        if rules.is_game_over(board, num_players, current_player):
            return self.__value_gamestate(playergamestate, our_player)
        
        if current_player == our_player:
            moves = rules.valid_moves(board, current_player)
            value = float('-inf')
            for move in moves:
                new_playergamestate = PlayerGameState(board,
                                                      rules,
                                                      players)
                value = max(value, self.__minimax(move,
                                                  new_playergamestate,
                                                  our_player))
            return value
        
        else:
            moves = rules.valid_moves(board, current_player)
            value = float('inf')
            for move in moves:
                new_playergamestate = PlayerGameState(board,
                                                      rules,
                                                      players)
                value = min(value, self.__minimax(move,
                                                  new_playergamestate,
                                                  our_player))
            return value



        

    def __value_gamestate(self,
                          playergamestate: PlayerGameState,
                          our_player: PlayerState) -> int:
        '''
        This gets the value of the gamestate.

        1 represents a state in which our_player wins
        -1 represents a state in which our_player loses
        0 represents a state in which all players lose

        @params: playergamestate: PlayerGameState
        @params: our_player: PlayerState

        @returns: int
        '''

        rules = playergamestate.get_rules()
        board = playergamestate.get_board()
        num_players = playergamestate.get_num_players()

        if rules.is_winner(board, our_player, num_players):
            return 1
        
        players = playergamestate.get_players()
        players.remove(our_player)
        for player in players:
            if rules.is_winner(board, player, num_players):
                return -1

        return 0 

