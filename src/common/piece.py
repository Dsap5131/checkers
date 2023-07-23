from enum import Enum

class Piece(Enum):
    '''
    Represents a game type on a checkers board.
    
    A Blank game piece presents a blank that isn't owned by either player.
    This is done because I do not know about optional typing within Python.
    If possible I would remove Piece.BLANK and instead have optional typing
    around the use of Piece
    '''
    BLANK = " "
    BLACK = "X"
    RED = "O"
    