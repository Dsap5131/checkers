from src.client.displays.dumbdisplay import DumbDisplay
from src.player.strategies.dumbstrategy import DumbStrategy


def test_constructor() -> None:
    dumbdisplay = DumbDisplay('127.0.0.1', 12345)


def test_start_game() -> None:
    expected_hostname = '127.0.0.1'
    expected_port = 12345
    dumbdisplay = DumbDisplay(expected_hostname, expected_port)
    hostname, port, strategy = dumbdisplay.start_game()

    assert hostname == expected_hostname, \
        'DumbDisplay.start_game() not working.'
    assert port == expected_port, \
        'DumbDisplay.start_game() not working.'
    assert isinstance(strategy, DumbStrategy), \
        'DumbDisplay.start_game() not working.'


def test_end_game() -> None:
    dumbdisplay = DumbDisplay('127.0.0.1', 12345)
    
    assert dumbdisplay.end_game(True), \
        'DumbDisplay.end_game() not working correctly.'
    assert dumbdisplay.end_game(False) == False, \
        'DumbDisplay.end_game() not working correctly.'
    