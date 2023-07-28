from src.player.strategies.terminalstrategy import TerminalStrategy
from src.player.strategies.minimaxstrategy import MiniMaxStrategy
from src.player.localplayer import LocalPlayer
from src.common.piece import Piece
from src.common.rulesstandard import RulesStandard
from src.referee.referee import Referee

player_2_1 = LocalPlayer(Piece.RED, TerminalStrategy())
player_2_2 = LocalPlayer(Piece.BLACK, MiniMaxStrategy())
players = [player_2_2, player_2_1]
referee_2 = Referee()
referee_2.start_game(RulesStandard(), players)

if player_2_1.get_is_winner():
    print('YOU WIN!')
else:
    print('YOU LOSE')
