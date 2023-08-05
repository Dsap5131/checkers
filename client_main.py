from src.client.client import Client
from src.client.displays.terminaldisplay import TerminalDisplay


client = Client(TerminalDisplay())
client.play_game()