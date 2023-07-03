from src.common.player import Player
from src.common.gamepiece import GamePiece

def test_constructor() -> None:
    gp1 = GamePiece.RED
    player1 = Player(gp1)

    gp2 = GamePiece.BLACK
    player2 = Player(gp2)


def test_get_gamepiece() -> None:
    gamepiece1 = GamePiece.RED
    player1 = Player(gamepiece1)
    assert player1.get_gamepiece() == GamePiece.RED, \
        "Player.get_gamepiece() not working."
    
    gamepiece2 = GamePiece.BLACK
    player2 = Player(gamepiece2)
    assert player2.get_gamepiece() == GamePiece.BLACK, \
        "Player.get_gamepiece() not working."