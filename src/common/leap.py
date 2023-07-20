

from src.common.position import Position

class Leap():
    '''
    A Leap represents a singular move a GamePiece makes.
    This includes the data about the movement of a piece and which pieces
    it captures.

    @params: start_position: Position
    @params: end_position: Position
    @params: capture_positions: List[Positions]: (Default) None
    '''


    def __init__(self, 
                 start_position: Position, 
                 end_position: Position,
                 capture_positions: list[Position]=None) -> None:
        
        self.__start_position = start_position
        self.__end_position = end_position
        self.__capture_positions = capture_positions

    
    def get_start_position(self) -> Position:
        '''
        Get the start position of the leap.

        @returns: Position
        '''

        return self.__start_position
    

    def get_end_position(self) -> Position:
        '''
        Get the end position of the leap.

        @returns: Position
        '''

        return self.__end_position
    

    def get_capture_positions(self) -> list[Position]:
        '''
        Get the positions captured by this leap.

        @returns: List[Positions]
        '''

        return self.__capture_positions
    

    def __eq__(self, obj) -> bool:
        '''
        Leaps are equal if they have equal starting_positions and 
        ending_positions.

        @returns: bool
        '''

        return (isinstance(obj, Leap) and
                obj.get_start_position() == self.get_start_position() and
                obj.get_end_position() == self.get_end_position() and
                obj.get_capture_positions() == self.get_capture_positions())
