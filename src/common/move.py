from collections import deque

from src.common.leap import Leap

class Move(): 
    '''
    Represents a move in checkers. A move in checkers is characterized by 
    as a list of leaps.
    '''

    def __init__(self, leaps: deque[Leap]) -> None:
        self.__next_leaps = leaps
        self.__previous_leaps = deque()

    
    def leaps_remaining(self) -> int:
        '''
        Gets the number of leaps remaining.

        @return: int
        '''
        return len(self.__next_leaps)


    def get_next_leap(self) -> Leap:
        '''
        Get the next leap to be performed during this move. 
        It is expected to only call this method while a positive number 
        of leaps remain. Otherwise this will error.

        @returns: Leap
        '''

        next_leap = self.__next_leaps.popleft()
        self.__previous_leaps.append(next_leap)
        return next_leap
    

    def reset(self) -> None:
        '''
        Resets the Move so that get_next_leap will return the first leap.
        '''
        self.__next_leaps = self.__previous_leaps + self.__next_leaps
        self.__previous_leaps = deque()
    

    
    