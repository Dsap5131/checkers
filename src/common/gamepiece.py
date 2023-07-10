from src.common.piece import Piece

class GamePiece():
    """
    Represents a piece on a board. This is represented as a type of piece
    and if it is a king.
    
    @param: piece: Piece
    @parma: is_king: bool
    """

    def __init__(self, piece: Piece, is_king: bool) -> None:
        self.__piece = piece
        self.__is_king = is_king


    def get_piece(self) -> Piece:
        '''
        Get the piece of this gamepiece

        @returns: Piece
        '''

        return self.__piece
    

    def is_king(self) -> bool:
        '''
        Get whether this piece is a king or not.

        @returns: bool
        '''

        return self.__is_king
    

    def make_king(self) -> None:
        """
        Make this piece a king
        """

        self.__is_king = True

    
    
    def __eq__(self, obj) -> bool:
        '''
        GamePiece are equal if they have equal Pieces and 
        is_kings.

        @returns: bool
        '''

        return (isinstance(obj, GamePiece) and
                obj.get_piece() == self.get_piece() and
                obj.is_king() == self.is_king())

