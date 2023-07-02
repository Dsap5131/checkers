from src.common.move import Move
from src.common.position import Position
from src.common.gamepiece import GamePiece


def test_constructor() -> None:
    curr_pos1 = Position(3, 3)
    new_pos1 = Position(4,4)
    mv1 = Move(curr_pos1, new_pos1)

    curr_pos2 = Position(4, 2)
    new_pos2 = Position(7, 7)
    mv2 = Move(curr_pos2, new_pos2)


def test_get_current_position() -> None:
    curr_pos1 = Position(3, 3)
    new_pos1 = Position(4, 4)
    mv1 = Move(curr_pos1, new_pos1)
    assert mv1.get_current_position() == curr_pos1, \
        "Move.get_current_position() not working."

    curr_pos2 = Position(4, 2)
    new_pos2 = Position(7, 7)
    mv2 = Move(curr_pos2, new_pos2)
    assert mv2.get_current_position() == curr_pos2, \
        "Move.get_current_position() not working."


def test_get_new_position() -> None:
    curr_pos1 = Position(3, 3)
    new_pos1 = Position(4, 4)
    mv1 = Move(curr_pos1, new_pos1)
    assert mv1.get_new_position() == new_pos1, \
        "Move.get_new_position() not working."

    curr_pos1 = Position(3, 3)
    new_pos1 = Position(4, 4)
    mv2 = Move(curr_pos1, new_pos1)
    assert mv2.get_new_position() == new_pos1, \
        "Move.get_new_position() not working."
