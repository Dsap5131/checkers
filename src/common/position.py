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
    

    def __eq__(self, obj) -> bool:
        '''
        Positions are equal if their rows and columns are equals to each other.
        
        @returns: bool
        '''

        return (isinstance(obj, Position) and
                obj.get_row() == self.get_row() and
                obj.get_column() == self.get_column())