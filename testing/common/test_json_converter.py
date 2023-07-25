from collections import deque

from src.common.json_converter import JsonConverter
from src.common.piece import Piece
from src.common.position import Position
from src.common.leap import Leap
from src.common.move import Move
from src.common.playergamestate import PlayerGameState
from src.common.rulesstandard import RulesStandard
from src.common.board import Board
from src.common.playerstate import PlayerState
from src.common.gamepiece import GamePiece


def test_constructor() -> None:
    json_converter = JsonConverter()


def test_piece_to_json() -> None:
    json_converter = JsonConverter()

    assert json_converter.piece_to_json(Piece.RED) == "O", \
        "JsonConverter.piece_to_json(Piece) not working correctly."
    assert json_converter.piece_to_json(Piece.BLACK) == "X", \
        "JsonConverter.piece_to_json(Piece) not working correctly."
    assert json_converter.piece_to_json(Piece.BLANK) == " ", \
        "JsonConverter.piece_to_json(Piece) not working correctly."
    

def test_json_to_piece() -> None:
    json_converter = JsonConverter()
    
    assert json_converter.json_to_piece("O") == Piece.RED, \
        "JsonConverter.json_to_piece(str) not working correctly."
    assert json_converter.json_to_piece("X") == Piece.BLACK, \
        "JsonConverter.json_to_piece(str) not working correctly."
    assert json_converter.json_to_piece(" ") == Piece.BLANK, \
        "JsonConverter.json_to_piece(str) not working correctly."
    

def test_move_to_json() -> None:
    json_converter = JsonConverter()

    move = Move(deque([Leap(Position(4,4),
                            Position(2,2),
                            [Position(3,3)],
                            []),
                       Leap(Position(2,2),
                            Position(0,0),
                            [Position(1,1)],
                            [Position(0,0)])]))

    leap_1 = {'start_position': {'row':4,'column':4},
              'end_position': {'row':2,'column':2},
              'capture_positions':[{'row':3,'column':3}],
              'promote_positions':[]}
    leap_2 = {'start_position': {'row':2,'column':2},
              'end_position':{'row':0,'column':0},
              'capture_positions':[{'row':1,'column':1}],
              'promote_positions':[{'row':0,'column':0}]}
    expected = [leap_1, leap_2]

    assert json_converter.move_to_json(move) == expected, \
        "JsonConverter.move_to_json(move) not working correctly."
    

def test_json_to_move() -> None:
    json_converter = JsonConverter()

    leap_1 = {'start_position': {'row':4,'column':4},
              'end_position': {'row':2,'column':2},
              'capture_positions':[{'row':3,'column':3}],
              'promote_positions':[]}
    leap_2 = {'start_position': {'row':2,'column':2},
              'end_position':{'row':0,'column':0},
              'capture_positions':[{'row':1,'column':1}],
              'promote_positions':[{'row':0,'column':0}]}
    move = [leap_1, leap_2]

    expected_move = Move(deque([Leap(Position(4,4),
                                     Position(2,2),
                                     [Position(3,3)],
                                     []),
                                Leap(Position(2,2),
                                     Position(0,0),
                                     [Position(1,1)],
                                     [Position(0,0)])]))
    
    assert json_converter.json_to_move(move) == expected_move, \
        "JsonConverter.move_to_json(list) not working correctly."
    

def test_playergamestate_to_json() -> None:
    json_converter = JsonConverter()

    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                  [GamePiece(Piece.BLACK, True), GamePiece(Piece.BLANK)]]
    board = Board(row_size=2, column_size=2, board=board_list)
    playergamestate = PlayerGameState(board, 
                                      RulesStandard(),
                                      [PlayerState(Piece.RED), 
                                       PlayerState(Piece.BLACK)],
                                      1)
    
    expected = {'board': {'row_size': 2,
                          'column_size': 2,
                          'board': [[' _', 'O_'],['XK', ' _']]},
                'rules': 'RulesStandard',
                'players': [{'piece': 'O'}, {'piece': 'X'}],
                'turn': 1}

    assert json_converter.playergamestate_to_json(playergamestate) == expected,\
        "JsonConverter.playergamestate_to_json(PlayerGameState) not working."
    

def test_json_to_playergamestate() -> None:
    json_converter = JsonConverter()

    board_list = [[GamePiece(Piece.BLANK), GamePiece(Piece.RED)],
                  [GamePiece(Piece.BLACK, True), GamePiece(Piece.BLANK)]]
    board = Board(row_size=2, column_size=2, board=board_list)
    expected = PlayerGameState(board, 
                               RulesStandard(),
                               [PlayerState(Piece.RED), 
                                PlayerState(Piece.BLACK)],
                               1)
    
    json_pgs = {'board': {'row_size': 2,
                          'column_size': 2,
                          'board': [[' _', 'O_'],['XK', ' _']]},
                'rules': 'RulesStandard',
                'players': [{'piece': 'O'}, {'piece': 'X'}],
                'turn': 1}
    
    assert json_converter.json_to_playergamestate(json_pgs) == expected, \
        "JsonConverter.json_to_playergamestate(dict) not working correctly."
    
    