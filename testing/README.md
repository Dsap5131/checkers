# testing

Directory for all testing within the project.

This may eventually be moved or changed to facilitate CI/CD tools.

# To run

In terminal from the root project directory run the command\
`python3 -m pytest testing/`

To run individual tests you can expand that command and path to any specific 
testing file.

For example
`python3 -m pytest testing/test_board.py`

The tests in [remote](./remote/README.md) require use of port 12345
Some tests in [player](./player/README.md) require use of port 12345

# Directory
| File or Folder | About |
| ---            | ---   |
| [common](./common/README.md) | Tests for [src/common](../src/common/README.md) |
| [player](./player/README.md) | Tests for [src/player](../src/player/README.md) |
| [referee](./referee/README.md) | Tests for [src/referee](../src/referee/README.md) |
| [server](./server/README.md) | Tests for [src/server](../src/server/README.md) |
| [remote](./remote/README.md) | Tests for [src/remote](../src/remote/README.md) |