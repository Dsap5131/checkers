import sys

from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

from src.player.strategies.strategy import Strategy
from src.client.displays.terminaldisplay import TerminalDisplay


def test_constructor() -> None:
    terminal_display = TerminalDisplay()


def test_start_game(monkeypatch: MonkeyPatch) -> None:
    terminal_display = TerminalDisplay()

    monkeypatch.setattr('builtins.input', mock_start_game_input)

    hostname, port, strategy = terminal_display.start_game()

    assert hostname == '127.0.0.1', \
        'TerminalDisplay.start_game() not working correctly'
    assert port == 12345, \
        'TerminalDisplay.start_game() not working correctly'
    assert isinstance(strategy, Strategy), \
        'TerminalDisplay.start_game() not working correctly'


def test_end_game(capsys: CaptureFixture) -> None:
    terminal_display = TerminalDisplay()

    terminal_display.end_game(True)
    captured = capsys.readouterr()
    assert captured.out.strip() == "YOU WON!", \
        'TerminalDisplay.start_game() not working correctly.'
    
    terminal_display.end_game(False)
    captured = capsys.readouterr()
    assert captured.out.strip() == "YOU LOST!", \
        'TerminalDisplay.start_game() not working correctly.'




def mock_output(msg: str) -> str:
    return msg


def mock_start_game_input(msg: str) -> str:
    if msg == 'What is the hostname of the server?\n':
        return '127.0.0.1'
    elif msg == 'What is the port number to connect to?\n':
        return '12_345'