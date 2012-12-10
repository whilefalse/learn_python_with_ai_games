class Player(object):
    def __init__(self):
        self.name = 'Bad Placement Player'

    def place_ships(self):
        self.queue = []
        self.seen = set([])
        self.last_shot = None

        return [
                [4, 0, 0, 'across'],
                [3, 0, 0, 'down'],
                [3, 2, 3, 'down'],
                [2, 0, 9, 'across'],
                [2, 6, 4, 'across'],
                [2, 4, 6, 'down'],
                [1, 9, 6, 'across'],
                [1, 6, 7, 'across'],
                [1, 7, 8, 'across'],
                [1, 9, 9, 'across'],
                ]

    def take_shot(self, board, ships):
        return (0,0)
