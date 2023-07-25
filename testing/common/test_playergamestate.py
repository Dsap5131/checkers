from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.rulesstandard import RulesStandard
from src.common.gamepiece import GamePiece
from src.common.piece import Piece
from src.player.localplayer import LocalPlayer
from src.player.strategies.dumbstrategy import DumbStrategy
from src.common.playerstate import PlayerState
from src.common.rulesdumb import RulesDumb

def test_constructor() -> None:
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size=2, column_size=2, board=board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players, 0)


def test_get_board() -> None:
    blank_piece = GamePiece(Piece.BLANK, False)
    red_piece = GamePiece(Piece.RED, False)
    black_piece = GamePiece(Piece.BLACK, False)
    board_list_1 = [[blank_piece, blank_piece],
                    [blank_piece, blank_piece]]
    board_1 = Board(row_size=2, column_size=2, board=board_list_1)

    board_list_2 = [[red_piece, black_piece],
                    [blank_piece, blank_piece]]
    board_2 = Board(row_size=2, column_size=2, board=board_list_2)

    rules = RulesStandard()
    playerstate_1 = PlayerState(Piece.BLACK)
    players = [playerstate_1]

    playergamestate_1 = PlayerGameState(board_1, rules, players, 0)
    playergamestate_2 = PlayerGameState(board_2, rules, players, 0)

    assert playergamestate_1.get_board() == board_1, \
        "PlayerGameState.get_board() not working."
    assert playergamestate_2.get_board() == board_2, \
        "PlayerGameState.get_board() not working."


def test_get_rules() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players, 0)

    assert playergamestate.get_rules() == rules, \
        "PlayerGameState.get_rules() not working."
    

def test_get_current_player() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate = PlayerState(Piece.BLACK)
    players = [playerstate]
    playergamestate = PlayerGameState(board, rules, players, 0)

    assert playergamestate.get_current_player() == playerstate, \
        "PlayerGameState.get_piece() not working."
    

def test_set_next_player() -> None:
    row_size=2
    column_size=2
    blank_piece = GamePiece(Piece.BLANK, False)
    board_list = [[blank_piece, blank_piece],
                  [blank_piece, blank_piece]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate_1  = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.BLACK)
    players = [playerstate_1, playerstate_2]
    playergamestate = PlayerGameState(board, rules, players, 0)

    assert playergamestate.get_current_player() == playerstate_1, \
        "PlayerGameState.next_player() setup failed."
    assert playergamestate.get_turn() == 0, \
        "PlayerGameState.next_player() setup failed."
    playergamestate.set_next_player()
    assert playergamestate.get_current_player() == playerstate_2, \
        "PlayerGameState.next_player() not working."
    assert playergamestate.get_turn() == 1, \
        "PlayerGameState.next_player() not working."

def test_get_num_players() -> None:
    row_size=2
    column_size=2
    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board = Board(row_size, column_size, board_list)
    rules = RulesStandard()
    playerstate_1 = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.RED)
    players = [playerstate_1, playerstate_2]
    playergamestate = PlayerGameState(board, rules, players, 0)

    assert playergamestate.get_num_players() == 2, \
        "PlayerGameState.get_num_players() not working."
    

def test_get_players() -> None:
    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK)]]
    board = Board(row_size=2, column_size=2, board=board_list)
    rules = RulesStandard()
    playerstate_1 = PlayerState(Piece.BLACK)
    playerstate_2 = PlayerState(Piece.RED)
    players = [playerstate_1, playerstate_2]
    playergamestate = PlayerGameState(board, rules, players, 0)

    expected_players = [PlayerState(Piece.BLACK), 
                        PlayerState(Piece.RED)]
    actual_players = playergamestate.get_players()
    assert actual_players == expected_players, \
        "PlayerGameState.get_players() not working correctly."
    
    #Test actual players is a copy
    playergamestate.set_next_player()

    assert actual_players == expected_players, \
        "PlayerGameState.get_players() not working correctly."
    assert actual_players != playergamestate.get_players(), \
        "PlayerGamestate.get_players() not working correctly."
    

def test__eq() -> None:
    board_1 = Board(1,1,[[GamePiece(Piece.BLANK)]])
    board_2 = Board(1,1,[[GamePiece(Piece.BLANK)]])
    board_3 = Board(1,1,[[GamePiece(Piece.RED)]])

    players_1 = [PlayerState(Piece.BLACK)]
    players_2 = [PlayerState(Piece.BLACK)]
    players_3 = [PlayerState(Piece.BLACK), PlayerState(Piece.RED)]

    playergamestate_1 = PlayerGameState(board_1,
                                        RulesStandard(),
                                        players_1,
                                        1)
    playergamestate_2 = PlayerGameState(board_2,
                                        RulesStandard(),
                                        players_2,
                                        1)
    playergamestate_3 = PlayerGameState(board_3,
                                        RulesStandard(),
                                        players_2,
                                        1)
    playergamestate_4 = PlayerGameState(board_2,
                                        RulesDumb(),
                                        players_2,
                                        1)
    playergamestate_5 = PlayerGameState(board_2,
                                        RulesStandard(),
                                        players_3,
                                        1)
    playergamestate_6 = PlayerGameState(board_2,
                                        RulesStandard(),
                                        players_2,
                                        2)
    
    assert playergamestate_1 == playergamestate_2, \
        "PlayerGameState == PlayerGameState not working."
    assert playergamestate_1 != playergamestate_3, \
        "PlayerGameState == PlayerGameState not working."
    assert playergamestate_1 != playergamestate_4, \
        "PlayerGameState == PlayerGamestate not working."
    assert playergamestate_1 != playergamestate_5, \
        "PlayerGameState == PlayerGameState not working."
    assert playergamestate_1 != playergamestate_6, \
        "PlayerGameState == PlayerGameState not working."
    assert playergamestate_1 != 5, \
        "PlayerGameState == PlayerGameState not working."
    