from src.server.server import Server


def test_constructor() -> None:
    server = Server(10_000)


def test_run_game() -> None:
    server = Server(10_000)

    # Test 1: 2 players connection through TCP and play a full game
    # check that the correct players won

    # Test 2: 2 players connection through TCP and 1 cheats
    # check that the correct player won

    # Test 3: Not enough players connection.

    ...