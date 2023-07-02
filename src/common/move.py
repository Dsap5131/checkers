from src.common.position import Position

class Move(): 
    '''
    Represents a move in checkers. A move in checkers is characterized by 
    2 Positions. The first representing the current position of a GamePiece and 
    the second representing the new position to move the GamePiece.
    '''

    def __init__(self, current_position: Position, new_position: Position) -> None:
        self.__current_position = current_position
        self.__new_position = new_position

    
    def get_current_position(self) -> Position:
        '''
        Get the current position of the GamePiece to be moved.

        @returns: Position
        '''

        return self.__current_position
    

    def get_new_position(self) -> Position:
        '''
        Get the new position of the GamePiece to be moved.

        @returns: Position
        '''

        return self.__new_position
    
    
    