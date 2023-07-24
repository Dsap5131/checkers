class Server():
    '''
    Server is the object to boot up a server of checkers to play games.
    
    @params: port: int: Port number for server to read TCP connections.
    '''

    def __init__(self, port: int) -> None:
        self.__port = port
        self.__connections = []

    
    def run_game(self) -> None:
        '''
        Runs a full game of checkers. 

        Opens a server on the port of the computer running this.
        Waits an listens for players to connect.
        After players connection run a game of checkers.
        '''
        
        # Open a socket 
        # listen for TCP connections of a user 
            # each spot of a game will listen for 30 seconds before 
            # timing out and not connecting a user
            # if there arent enough players to run a game then try again
            # if there still arena enough then shut down the game
                    # Maybe start a game with localplayer bots?
        # create playerstates
        # create referee and start a game 
        

        ...