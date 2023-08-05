from src.client.displays.display import Display
from src.common.playergamestate import PlayerGameState
from src.player.strategies.strategy import Strategy
from src.player.strategies.terminalstrategy import TerminalStrategy
from src.player.strategies.minimaxstrategy import MiniMaxStrategy


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

        hostname = input('What is the hostname of the server?\n')
        port = int(input('What is the port number to connect to?\n'))
        strategy_str = input('What is the strategy you would like to use?'+\
                             '\n1) TerminalStrategy\n2) MiniMaxStrategy\n')
        strategy = TerminalStrategy()
        if strategy_str == 'MiniMaxStrategy':
            strategy = MiniMaxStrategy()
        return (hostname, port, strategy)
    

    def end_game(self, winner: bool) -> None:
        '''
        Display the endgame scenario with information about winning or losing.
        '''

        if winner:
            print('YOU WON!')
        else:
            print('YOU LOST!')