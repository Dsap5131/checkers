from src.client.displays.display import Display
from src.player.strategies.strategy import Strategy
from src.player.strategies.dumbstrategy import DumbStrategy

class DumbDisplay(Display):
    '''
    DumbDisplay uses dumb strategy and is meant to be used for testing where
    displays arent used.
    
    @param: port to be used
    '''

    def __init__(self, hostname: str, port: int) -> None:
        self.__hostname = hostname
        self.__port = port
        

    def start_game(self) -> tuple[str, int, Strategy]:
        '''
        To start a game a player must give the client the hostname and port
        of the server to connect to. It must also give a strategy to be used.

        @returns: tuple[Hostname: str, Port: int, strategy: Strategy]
        '''

        return (self.__hostname, self.__port, DumbStrategy())
    

    def end_game(self, winner: bool) -> None:
        '''
        Display the endgame scenario with information about winning or losing.
        '''

        return winner