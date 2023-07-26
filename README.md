# CHECKERS

Its Checkers :) 

Just a simple project updated every once in awhile as I improve my software development skills.
The main goals of this project being to improve my Python software development skills.
This includes using new software, like Flask. 

Practice makes perfect.
Feel free to leave comments and help improve the professional and socially
responsible code I write.

# TODO

1. playerproxy and refereeproxy
2. Implement online player
3. Implement Server and Client
4. Update diagrams and design pngs
5. Instance checking on parameters? What is the best practice
6. Should Move return copies of the Position? Is this a vulnerability if not.
7. Add makefile, just needs pytest
8. (Optional) Research and implement optional typing for the use of GamePiece
9. Should typing be done through strings and not imports (this can help with circular imports?)


# Project Design

![Fig project_wide_mock.png](./resources/UML_diagrams/project_wide_mock.png)
This mock represents the software design for this project. 

The key features for this mock were:
1. Support Remote Connections
2. Support AI players (Strategies that do not use client input)
3. Leave room for future front end development

With these features in mind the above mock was made. The idea is to have a Referee that contains information about a GameState, Rules, and Players. With this it can ask players to make moves, validate the moves against the rules, then apply the move to the GameState, then update the players with the new GameState. 

This will allow for easy expansion and updates to the game. For special verizons or rule updates all you have to do is update the Rules object without needing to update the GameState. 

Proxies will be used to facilitate communicate between the Client and Server. The Player object will be on the server side and have a PlayerProxy object that allows it to communicate to the Client. The Client will use the RefereeProxy to communicate back. 

The Strategy object will be used to determine the next move for the player. I.e whether its user input from the client or an AI. The use of AI will come in handy for automated testing.


# Directories

|   Location     |   About   |
|   :---         |   :---     |
| [resources](./resources/README.md) | Represents information about the project.
| [src](./src/README.md) | source code for the project |
| [testing](./testing/README.md) | testing for the project |