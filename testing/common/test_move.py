from collections import deque

from src.common.move import Move
from src.common.position import Position
from src.common.leap import Leap


def test_constructor() -> None:
    start_position = Position(3, 3)
    end_position = Position(4,4)
    leap = Leap(start_position, end_position)
    mv1 = Move(deque([leap]))

    start_position_2 = Position(4, 2)
    end_position_2 = Position(7, 7)
    leap2 = Leap(start_position_2, end_position_2)
    mv2 = Move(deque([leap2]))


def test_get_next_leap() -> None:
    start_position = Position(3, 3)
    end_position = Position(4,4)
    leap = Leap(start_position, end_position)

    start_position_2 = Position(4, 2)
    end_position_2 = Position(7, 7)
    leap2 = Leap(start_position_2, end_position_2)
    move = Move(deque([leap, leap2]))

    assert move.get_next_leap() == leap, \
        "Move.get_next_leap() not working properly."
    
    assert move.get_next_leap() == leap2, \
        "Move.get_next_leap() not working properly."
    

def test_reset() -> None:
    start_position = Position(3, 3)
    end_position = Position(4,4)
    leap = Leap(start_position, end_position)

    start_position_2 = Position(4, 2)
    end_position_2 = Position(7, 7)
    leap2 = Leap(start_position_2, end_position_2)
    move = Move(deque([leap, leap2]))

    assert move.get_next_leap() == leap, \
        "Move.get_next_leap() not working properly."
    
    move.reset()

    assert move.get_next_leap() == leap, \
        "Move.get_next_leap() not working properly."
    

def test_leaps_remaining() -> None:
    start_position = Position(3, 3)
    end_position = Position(4,4)
    leap = Leap(start_position, end_position)

    start_position_2 = Position(4, 2)
    end_position_2 = Position(7, 7)
    leap2 = Leap(start_position_2, end_position_2)
    move = Move(deque([leap, leap2]))

    assert move.leaps_remaining() == 2, \
        "Move.leaps_remaining() not working properly."

    assert move.get_next_leap() == leap, \
        "Move.get_next_leap() not working properly."
    
    assert move.leaps_remaining() == 1, \
        "Move.leaps_remaining() not working properly."

    move.reset()

    assert move.leaps_remaining() == 2, \
        "Move.leaps_remaining() not working properly."
    
    
