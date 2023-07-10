from enum import Enum

class GamePiece(Enum):
    '''
    Represents a game piece on a checkers board.
    
    A Blank game piece presents a blank that isn't owned by either player.
    This is done because I do not know about optional typing within Python.
    If possible I would remove GamePiece.BLANK and instead have optional typing
    around the use of GamePiece
    '''
    BLANK = 0
    BLACK = 1
    RED = 2
    BLACK_KING = 3
    RED_KING = 4
    