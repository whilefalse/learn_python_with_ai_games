import random

class Player(object):
    def __init__(self):
        self.name = 'Stupid Player'

    def place_ships(self):
        return [
                [4, 0, 0, 'across'],
                [3, 0, 1, 'across'],
                [3, 1, 2, 'down'],
                [2, 0, 2, 'down'],
                [2, 3, 1, 'down'],
                [2, 4, 0, 'down'],
                [1, 2, 2, 'across'],
                [1, 2, 3, 'across'],
                [1, 0, 5, 'across'],
                [1, 0, 4, 'across'],
                ]

    def take_shot(self, board, ships):
        return [random.randint(0, 9), random.randint(0,9)]
