class Player(object):
    def __init__(self):
        self.name = 'Methodical Player'

    def place_ships(self):
        self.queue = []
        self.seen = set([])
        self.last_shot = None

        return [
                [4, 0, 3, 'across'],
                [3, 4, 3, 'across'],
                [3, 7, 3, 'across'],
                [2, 0, 6, 'across'],
                [2, 2, 6, 'across'],
                [2, 4, 6, 'across'],
                [1, 6, 6, 'across'],
                [1, 7, 6, 'across'],
                [1, 8, 6, 'across'],
                [1, 9, 6, 'across'],
                ]

    def take_shot(self, board, ships):
        i = 0
        x = y = 0
        board_at_i = 'x'

        while board_at_i != '?':
            y, x = divmod(i, 10)
            board_at_i = board[x][y]
            i += 1

        return (x, y)
