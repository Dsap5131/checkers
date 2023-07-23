from src.player.strategies.strategy import Strategy
from src.common.move import Move
from src.common.playergamestate import PlayerGameState
from src.common.rules import Rules
from src.common.player import Player
from src.common.board import Board
from src.common.playerstate import PlayerState

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
        player = playergamestate.get_current_player()
        board = playergamestate.get_board()

        moves = rules.valid_moves(board, player)
        suicide_move = moves[0]
        for move in moves:
            score = self.__score_move(move, playergamestate)
            if score == 1:
                return move
            elif score == 0:
                suicide_move = move
        return suicide_move
    
    
    def __score_move(self, move: Move, playergamestate: PlayerGameState) -> int:
        '''
        Return the score of a move by running MiniMax algorithms on the move.

        A score of 1 represents a move that leads to the player winning.
        A score of -1 represents a move that leads to the opponent winning.
        A score of 0 represents a move that leads to noone winning.
        
        @params: move: Move
        @params: playergamestate: PlayerGameState

        @returns: int
        '''

        our_player = playergamestate.get_current_player()
        return self.__max(move, playergamestate, our_player)
    

    def __max(self, 
              move: Move, 
              playergamestate: PlayerGameState,
              our_player: PlayerState) -> int:
        '''
        Return the score of a move by running MiniMax algorithms on the move.

        A score of 1 represents a move that leads to the player winning.
        A score of -1 represents a move that leads to the opponent winning.
        A score of 0 represents a move that leads to noone winning.
        
        @params: move: Move
        @params: playergamestate: PlayerGameState
        @params: our_player: PlayerState
        
        @returns: int
        '''


        rules = playergamestate.get_rules()
        board = playergamestate.get_board()
        num_players = playergamestate.get_num_players()

        new_board = Board.from_board(board)
        new_board.move_piece(move)
        move.reset()

        if rules.is_game_over(new_board, num_players, our_player):
            active_players = playergamestate.get_players()
            active_players.remove(our_player)
            return self.__score_gamestate(rules,
                                          new_board,
                                          our_player,
                                          active_players)
        
        playergamestate.set_next_player()
        next_player = playergamestate.get_current_player()
        if next_player == our_player:
            valid_moves = rules.valid_moves(new_board, next_player)
            best_score = -1
            for move in valid_moves:
                active_players = playergamestate.get_players()
                new_playergamestate = PlayerGameState(new_board,
                                                      rules,
                                                      active_players)
                score = self.__max(move,
                                   new_playergamestate,
                                   our_player)
                if score > best_score: 
                    best_score = score
                if best_score == 1:
                    return best_score
            return best_score
        else:
            valid_moves = rules.valid_moves(new_board, next_player)
            best_score = -1
            for move in valid_moves:
                active_players = playergamestate.get_players()
                new_playergamestate = PlayerGameState(new_board,
                                                      rules,
                                                      active_players)
                score = self.__min(move,
                                   new_playergamestate,
                                   our_player)
                if score > best_score:
                    best_score = score
                if best_score == 1:
                    return best_score
                
    
    def __min(self,
              move: Move,
              playergamestate: PlayerGameState,
              our_player: PlayerState):
        '''
        Return the score of a move by running MiniMax algorithms on the move.

        A score of -1 represents a move that leads to the player winning.
        A score of 1 represents a move that leads to the opponent winning.
        A score of 0 represents a move that leads to noone winning.
        
        @params: move: Move
        @params: playergamestate: PlayerGameState
        @params: our_player: PlayerState
        
        @returns: int
        '''

        rules = playergamestate.get_rules()
        board = playergamestate.get_board()
        num_players = playergamestate.get_num_players()
        current_player = playergamestate.get_current_player()

        new_board = Board.from_board(board)
        new_board.move_piece(move)
        move.reset()

        if rules.is_game_over(new_board, num_players, current_player):
            active_players = playergamestate.get_players()
            active_players.remove(our_player)
            return self.__score_gamestate(rules,
                                          new_board,
                                          our_player,
                                          active_players)
        
        playergamestate.set_next_player()
        next_player = playergamestate.get_current_player()
        if next_player == our_player:
            valid_moves = rules.valid_moves(new_board, next_player)
            best_score = 1
            for move in valid_moves:
                active_players = playergamestate.get_players()
                new_playergamestate = PlayerGameState(new_board,
                                                      rules,
                                                      active_players)
                score = self.__max(move,
                                   new_playergamestate,
                                   our_player)
                if score < best_score: 
                    best_score = score
                if best_score == -1:
                    return best_score
            return best_score
        else:
            valid_moves = rules.valid_moves(new_board, next_player)
            best_score = 1
            for move in valid_moves:
                active_players = playergamestate.get_players()
                new_playergamestate = PlayerGameState(new_board,
                                                      rules,
                                                      active_players)
                score = self.__min(move,
                                   new_playergamestate,
                                   our_player)
                if score < best_score:
                    best_score = score
                if best_score == -1:
                    return best_score
            


    def __score_gamestate(rules: Rules,
                          new_board: Board,
                          our_player: PlayerState,
                          active_players: list[PlayerState]) -> int:
        '''
        This takes a board that is in a gameover state and checks scores the
        game.

        1 represents that our_player won the game.
        -1 represents that an active_player other than our_player won the game.
        0 represents that noone is a winner.

        @params: rules: Rules
        @params: new_board: Board
        @params: our_player: PlayerState
        @params: active_players: list[PlayerState]

        @returns: int
        '''

        if rules.is_winner(new_board, our_player):
            return 1
        
        for player in active_players:
            if rules.is_winner(new_board, player):
                return -1
        
        return 0



        