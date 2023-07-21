from src.common.piece import Piece


class PlayerState():
    """
    PlayerState represents the public knowledge of a Player.

    PlayerState is used to send players information about other players.
    
    @params: piece: Piece
    """

    def __init__(self, piece: Piece) -> None:
        self.__piece = piece

    
    def get_piece(self) -> Piece:
        '''
        Get the piece of the player.

        @returns: Piece
        '''
        
        return self.__piece
    

    def __eq__(self, obj) -> bool:
        '''
        Two PlayerStates are equal if their fields are equal

        @returns: bool
        '''

        if not isinstance(obj, PlayerState):
            return False
        
        return obj.get_piece() == self.get_piece()