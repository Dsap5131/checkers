class Position():
    '''
    Represents a position on a board.

    This is represented by a row and column value.
    '''

    def __init__(self, row: int, column: int) -> None: 
        self.__row = row
        self.__column = column


    def get_row(self) -> int: 
        '''
        Return row value of Position.

        @returns int
        '''
        return self.__row
    
    
    def get_column(self) -> int:
        '''
        Return col value of Position.

        @returns int
        '''
        return self.__column