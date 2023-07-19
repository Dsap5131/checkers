from src.player.strategies.strategy import Strategy
from src.common.move import Move

class MiniMaxStrategy(Strategy):
    """
    MiniMaxStrategy is a strategy that uses a MinMax Algorithm to determine the
    next best move.
    """

    def make_move(playergamestate: "PlayerGameState") -> Move:
        ...

