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
    
    
def test_eq() -> None:
    start_position_one = Position(3, 3)
    start_position_two = Position(3, 3)
    start_position_three = Position(4, 4)
    end_position_one = Position(4,4)
    end_position_two = Position(4,4)
    
    leap_one = Leap(start_position_one, end_position_one)
    leap_two = Leap(start_position_two, end_position_two)
    leap_three = Leap(start_position_three, end_position_two)

    move_one = Move(deque([leap_one, leap_two]))
    move_two = Move(deque([leap_two, leap_one]))
    move_three = Move(deque([leap_one, leap_three]))
    move_four = Move(deque([leap_three]))

    assert move_one == move_two, \
        "Move == Move not working correctly."
    assert (move_one == move_three) == False, \
        "Move == Move not working correctly."
    assert (move_one == move_four) == False, \
        "Move == Move not working correctly."
    assert (move_one == 3) == False, \
        "Move == Move not working correctly."