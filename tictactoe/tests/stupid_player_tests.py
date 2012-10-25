import sys
sys.path.append('.')

import unittest
from players.stupid_player import Player

class StupidPlayerTests(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.marker = 'X'

    def test_name_is_stupid_player(self):
        self.assertEqual(self.player.name, "Stupid Player")

    def test_place_piece_gives_random_answer(self):
        move = self.player.place_piece([
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '])

        self.assertIn(move, range(9))

    def test_place_piece_never_chooses_occupied_space(self):
        move = self.player.place_piece([
            'X', 'X', 'O',
            'O', 'X', ' ',
            'O', 'X', 'O'])

        self.assertEqual(move, 5)

unittest.main()
