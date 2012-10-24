import random

class Player(object):
    def __init__(self):
        self.name = 'Stupid Player'

    def place_piece(self, board):
        existing = 'X'
        rand = 0
        while existing != ' ':
            rand = random.randint(0,8)
            existing = board[rand]
        return rand
