from _pytest.monkeypatch import MonkeyPatch
from collections import deque

from src.player.strategies.terminalstrategy import TerminalStrategy
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.piece import Piece
from src.common.gamepiece import GamePiece
from src.common.rulesdumb import RulesDumb
from src.common.playerstate import PlayerState
from src.common.position import Position
from src.common.leap import Leap
from src.common.move import Move

def test_constructor() -> None:
    strategy = TerminalStrategy()
    

def test_make_move(monkeypatch: MonkeyPatch) -> None:
    # Test single leap
    board_list_1 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED)]]
    board_1 = Board(row_size=3, column_size=3, board=board_list_1)
    players_1 = [PlayerState(Piece.RED)]
    playergamestate_1 = PlayerGameState(board_1, RulesDumb(), players_1, 0)
    monkeypatch.setattr('builtins.input', single_leap)
    move_1 = TerminalStrategy().make_move(playergamestate_1)
    assert move_1 == Move(deque([Leap(Position(2,2),Position(1,1),[],[])])),\
        "TerminalStrategy.make_move(PlayerGameState) not working."
    
    # Test leap with capture and promote
    board_list_2 = [[GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLACK), 
                   GamePiece(Piece.BLANK)],
                  [GamePiece(Piece.BLANK), GamePiece(Piece.BLANK), 
                   GamePiece(Piece.RED)]]
    board_2 = Board(row_size=3, column_size=3, board=board_list_2)
    players_2 = [PlayerState(Piece.RED)]
    playergamestate_2 = PlayerGameState(board_2, RulesDumb(), players_2, 0)
    monkeypatch.setattr('builtins.input', capture_promote_leap)
    move_2 = TerminalStrategy().make_move(playergamestate_2)
    expected_move_2 = Move(deque([Leap(Position(2,2),
                                       Position(0,0),
                                       [Position(1,1)],
                                       [Position(0,0)])]))
    assert move_2 == expected_move_2, \
        "TerminalStraetgy.make_move(PlayerGameState) not working."


def single_leap(msg: str) -> str:
    '''
    Simulates a player performing a single leap.
    
    @param: msg
    
    @returns: str
    '''

    if msg == "Enter the position of the piece you would like to move.(r,c)\n":
        return "(2,2)"
    elif msg == 'Enter the position of where to move the piece to. (r,c)\n':
        return "(1,1)"
    elif msg == 'Does this capture a piece? Y/n\n':
        return "n"
    elif msg == 'Does this promote a piece? Y/n\n':
        return "n"
    elif msg == 'Does this piece continue leaping? Y/n\n':
        return "n"
    else:
        return ""
    

def capture_promote_leap(msg: str) -> str:
    '''
    Simulates a player performing a single leap with a capture and promote.
    
    @param: msg
    
    @returns: str
    '''

    if msg == "Enter the position of the piece you would like to move.(r,c)\n":
        return "(2,2)"
    elif msg == 'Enter the position of where to move the piece to. (r,c)\n':
        return "(0,0)"
    elif msg == 'Does this capture a piece? Y/n\n':
        return "Y"
    elif msg == 'Enter the position of the captured piece. (r,c)\n':
        return "(1,1)"
    elif msg == 'Does this promote a piece? Y/n\n':
        return "Y"
    elif msg == 'Enter the position of the promoted piece. (r,c)\n':
        return "(0,0)"
    elif msg == 'Does this piece continue leaping? Y/n\n':
        return "n"
    else:
        return ""
                                    
    
