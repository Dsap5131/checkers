# testing

Directory for all testing within the project.

This may eventually be moved or changed to facilitate CI/CD tools.

# To run

In terminal from the root project directory run the command\
`pytest testing/`

To run individual tests you can expand that command and path to any specific 
testing file.

For example
`pytest testing/test_board.py`

# Directory
|   File or Folder | About |
|   ---            | ---   |
| [test_position.py](./test_position.py) | Tests for [Position](../src/common/position.py)
| [test_board.py](./test_board.py) | Tests for [Board](../src/common/board.py)
| [test_gamestate.py](./test_gamestate.py) | Tests for [GameState](../src/common/gamestate.py)
| [test_leap.py](./test_leap.py) | Tests for [Leap](../src/common/leap.py)
| [test_move.py](./test_move.py) | Tests for [Move](../src/common/move.py)
| [test_player.py](./test_player.py) | Tests for [Player](../src/common/player.py)
| [test_playergamestate.py](./test_playergamestate.py) | Tests for [PlayerGameState](../src/common/playergamestate.py)
| [test_rulesstandard.py](./test_rulesstandard.py) | Tests for [RulesStandard](../src/common/rulesstandard.py)