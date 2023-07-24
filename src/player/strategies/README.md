# strategies

Strategies represent strategies to calculate moves given playergamestates.

# Design

DumbStrategy is developed not to be a viable or good strategy for basic
testing where strategies are needed; however, not used or checked by rules.

BasicStrategy is a basic strategy that, like Dumbstrategy, is not a viable
or good strategy but does return valid moves that can be checked by rules.

MiniMaxStrategy is a strategy that can properly play a game of checkers.

# Directory 
| File or Folder | About |
| ---            | ---   |
| [strategy.py](./strategy.py) | [Strategy](./strategy.py) |
| [dumbstrategy.py](./dumbstrategy.py) | [DumbStrategy](./dumbstrategy.py) |
| [basicstrategy.py](./basicstrategy.py) | [BasicStrategy](./basicstrategy.py) |
| [minimaxstrategy.py](./minimaxstrategy.py) | [MiniMaxStrategy](./minimaxstrategy.py) |
| [terminalstrategy.py](./terminalstrategy.py) | [TerminalStrategy](./terminalstrategy.py) |