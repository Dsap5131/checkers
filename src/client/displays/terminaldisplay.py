from src.client.displays.display import Display
from src.common.playergamestate import PlayerGameState
from src.player.strategies.strategy import Strategy
from src.player.strategies.terminalstrategy import TerminalStrategy


class TerminalDisplay(Display):
    '''
    TerminalDisplay allows interactions between the client and the user 
    to happen within the terminal.
    '''

    def start_game(self) -> tuple[str, int, Strategy]:
        '''
        To start a game a player must give the client the hostname and port
        of the server to connect to. It must also give a strategy to be used.

        @returns: tuple[Hostname: str, Port: int, strategy: Strategy]
        '''

        hostname = input('What is the hostname of the server?')
        port = int(input('What is the port number to connect to?'))
        strategy = TerminalStrategy()
        return (hostname, port, strategy)
    

    def end_game(self, winner: bool) -> None:
        '''
        Display the endgame scenario with information about winning or losing.
        '''

        if winner:
            print('YOU WON!')
        else:
            print('YOU LOST!')