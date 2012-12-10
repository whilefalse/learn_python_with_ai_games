class Player(object):
    def __init__(self):
        self.name = 'Methodical Player'

    def place_piece(self, board):
        for i in range(9):
            if board[i] == ' ':
                return i
