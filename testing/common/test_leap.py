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
    

def test_get_captures() -> None:
    start_position = Position(0,0)
    end_position = Position(2,2)
    capture_position = Position(1,1)
    leap = Leap(start_position, end_position, [capture_position])

    assert leap.get_capture_positions() == [Position(1,1)], \
        "Leap.get_capture() not working correctly."
    

def test_get_promote_positions() -> None:
    start_position = Position(0,0)
    end_position = Position(2,2)
    capture_position = Position(1,1)
    promotes = Position(2,2)
    leap = Leap(start_position, end_position, [capture_position], [promotes])
    
    assert leap.get_promote_positions() == [Position(2,2)], \
        "Leap.get_promote_positions() not working correctly."


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
    
    # Test eq with captures
    start_position_five = Position(0,0)
    end_position_five = Position(2,2)
    capture_positions_five = [Position(1,1)]
    leap_five = Leap(start_position_five, 
                     end_position_five, 
                     capture_positions_five)

    start_position_six = Position(0,0)
    end_position_six = Position(2,2)
    capture_positions_six = [Position(1,1)]
    leap_six = Leap(start_position_six,
                    end_position_six,
                    capture_positions_six)
    
    start_position_seven = Position(0,0)
    end_position_seven = Position(2,2)
    capture_positions_seven = [Position(1,1), Position(3,3)]
    leap_seven = Leap(start_position_seven,
                      end_position_seven,
                      capture_positions_seven)

    start_position_eight = Position(0,0)
    end_position_eight = Position(2,2)
    capture_positions_eight = [Position(3,3)]
    leap_eight = Leap(start_position_eight,
                      end_position_eight,
                      capture_positions_eight)
    
    start_position_nine = Position(0,0)
    end_position_nine = Position(2,2)
    leap_nine = Leap(start_position_nine, end_position_nine)
    
    assert leap_five == leap_six, \
        "Leap.__eq__ not working correctly."
    assert leap_five != leap_seven, \
        "Leap.__eq__ not working correctly."
    assert leap_five != leap_eight, \
        "Leap.__eq__ not working correctly."
    assert leap_five != leap_nine, \
        "Leap.__eq__ not working correctly."
    

    # Test eq with promotes

    start_position_10 = Position(0,0)
    end_position_10 = Position(1,1)
    promote_position_10 = Position(1,1)
    leap_10 = Leap(start_position_10,
                   end_position_10,
                   promote_positions=[promote_position_10])

    start_position_11 = Position(0,0)
    end_position_11 = Position(1,1)
    promote_position_11 = Position(1,1)
    leap_11 = Leap(start_position_11,
                   end_position_11,
                   promote_positions=[promote_position_11])

    start_position_12 = Position(0,0)
    end_position_12 = Position(1,1)
    promote_position_12 = Position(0,0)
    leap_12 = Leap(start_position_12,
                   end_position_12,
                   promote_positions=[promote_position_12])
    
    start_position_13 = Position(0,0)
    end_position_13 = Position(1,1)
    leap_13 = Leap(start_position_13,
                   end_position_13)

    start_position_14 = Position(0,0)
    end_position_14 = Position(1,1)
    promote_position_14_1 = Position(1,1)
    promote_position_14_2 = Position(0,0)
    leap_14 = Leap(start_position_14,
                   end_position_14,
                   promote_positions=[promote_position_14_1,
                                      promote_position_14_2])
    
    assert leap_10 == leap_11, "Leap == Leap not working correctly."
    assert leap_10 != leap_12, "Leap == Leap not working correctly."
    assert leap_10 != leap_13, "Leap == Leap not working correctly."
    assert leap_10 != leap_14, "Leap == Leap not working correctly."