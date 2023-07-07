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
