import sys
sys.path.append('.')

import unittest
from players.stupid_player import Player

class StupidPlayerTests(unittest.TestCase):
    def test_name_is_stupid_player(self):
        player = Player()

        self.assertEqual(player.name, "Stupid Player")

    def test_place_piece_gives_random_answer(self):
        player = Player()

        move = player.place_piece([
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '])

        self.assertIn(move, range(9))

unittest.main()
