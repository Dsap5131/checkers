from src.player.strategies.strategy import Strategy
from src.common.playergamestate import PlayerGameState

class Display():
    '''
    Displays represent ways to communicate through the user and client.
    '''

    def start_game(self) -> tuple[str, int, Strategy]:
        '''
        To start a game a player must give the client the hostname and port
        of the server to connect to. It must also give a strategy to be used.

        @returns: tuple[Hostname: str, Port: int, strategy: Strategy]
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")
    

    def end_game(self, winner: bool) -> None:
        '''
        Display the endgame scenario with information about winning or losing.
        '''

        raise NotImplementedError(
            "THIS IS NOT IMPLEMENTED AND SHOULD NEVER BE CALLED.")