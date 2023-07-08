from src.common.player import Player
from src.common.gamepiece import GamePiece

def test_constructor() -> None:
    player_one = Player(GamePiece.RED)


def test_get_gamepiece() -> None:
    player_one = Player(GamePiece.RED)
    assert player_one.get_gamepiece() == GamePiece.RED, \
        "Player.get_gamepiece() not working."

    player_two = Player(GamePiece.BLACK)
    assert player_two.get_gamepiece() == GamePiece.BLACK, \
        "Player.get_gamepiece() not working."


def test_get_move() -> None:
    '''
    Since Player is an abstract class this method is not implemented 
    thus we will not test it
    '''
    ...