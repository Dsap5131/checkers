from src.common.position import Position

def test_constructor() -> None:
    position_one = Position(5, 3)
    position_two = Position(0,0)
    position_three = Position(-5, -5)


def test_get_row() -> None:
    position_one = Position(5, 3)
    assert position_one.get_row() == 5, \
        "Position.get_row() not returning the correct value."
    
    position_two = Position(-3, 0)
    assert position_two.get_row() == -3, \
        "Position.get_row() not returning the correct value."
    

def test_get_column() -> None:
    position_one = Position(5, 10)
    assert position_one.get_column() == 10, \
        "Position.get_column() not returning the correct value."
    
    position_two = Position(3, -10)
    assert position_two.get_column() == -10, \
        "Position.get_column() not returning the correct value."
    

def test_eq() -> None:
    position_one = Position(5, 5)
    position_two = Position(5, 5)
    position_three = Position(6, 6)

    assert position_one == position_two, \
        "Position.__eq__ is not working correctly."
    
    assert (position_one == position_three) == False, \
        "Position.__eq__ is not working correctly."