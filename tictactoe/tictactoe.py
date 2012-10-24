import sys
sys.path.append('..')

from common.runner import Runner
from game import Game

Runner(Game).play_game()
