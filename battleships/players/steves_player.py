import random

class Player(object):
    def __init__(self):
        self.name = 'Steve\'s Player'

    def place_ships(self):
        self.queue = []
        self.seen = set([])
        self.last_shot = None

        return [
                [4, 6, 0, 'across'],
                [3, 0, 1, 'down'],
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
        if self.last_shot and board[self.last_shot[0]][self.last_shot[1]] == 'x':
            if self.last_shot[0] >= 1 and self.last_shot[0] <= 9:
                self.queue.append((self.last_shot[0] - 1, self.last_shot[1]))
            if self.last_shot[0] >= 0 and self.last_shot[0] <= 8:
                self.queue.append((self.last_shot[0] + 1, self.last_shot[1]))
            if self.last_shot[1] >= 1 and self.last_shot[1] <= 9:
                self.queue.append((self.last_shot[0], self.last_shot[1] - 1))
            if self.last_shot[1] >= 1 and self.last_shot[1] <= 8:
                self.queue.append((self.last_shot[0], self.last_shot[1] + 1))

        move = None
        while move is None and self.queue:
            move = self.queue.pop()
            if move in self.seen:
                move = None

        if not move:
            move = (random.randint(0, 8), random.randint(0,8))

        self.last_shot = move
        self.seen.add(move)
        return move
