from src.common.position import Position
from src.common.leap import Leap


def test_constructor() -> None:
    start_position = Position(0,0)
    end_position = Position(1,1)
    leap = Leap(start_position, end_position)


def test_get_start_position() -> None:
    start_position = Position(0,0)
    end_position = Position(1,1)
    leap = Leap(start_position, end_position)

    assert leap.get_start_position() == start_position, \
        "Leap.get_start_position() not working."
    

def test_get_end_position() -> None:
    start_position = Position(0,0)
    end_position = Position(1,1)
    leap = Leap(start_position, end_position)

    assert leap.get_end_position() == end_position, \
        "Leap.get_end_position() not working."


def test_eq() -> None:
    start_position_one = Position(0,0)
    start_position_two = Position(0,0)
    start_position_three = Position(1,1)

    end_position_one = Position(2,2)
    end_position_two = Position(2,2)
    end_position_three = Position(3,3)

    leap_one = Leap(start_position_one, end_position_one)
    leap_two = Leap(start_position_two, end_position_two)
    leap_three = Leap(start_position_two, end_position_three)
    leap_four = Leap(start_position_three, end_position_two)

    assert leap_one == leap_two, \
        "Leap == Leap not working correctly."
    assert (leap_one == leap_three) == False, \
        "Leap == Leap not working correctly."
    assert (leap_one == leap_four) == False, \
        "Leap == Leap not working correctly."
    assert (leap_one == 3) == False, \
        "Leap == Leap not working correctly."