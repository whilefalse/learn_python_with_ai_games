class Board(object):
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def print_board(self):
        print "%s | %s | %s" % tuple(self.board[:3])
        print "---------"
        print "%s | %s | %s" % tuple(self.board[3:6])
        print "---------"
        print "%s | %s | %s" % tuple(self.board[6:])

    def place_piece(self, index, letter):
        if self.board[index] == ' ':
            self.board[index] = letter

    def full(self):
        return filter(lambda x: x == ' ', self.board) == []

    def someone_has_one(self):
        winning_combinations = [
                (0,1,2),
                (3,4,5),
                (6,7,8),
                (0,3,6),
                (1,4,7),
                (2,5,8),
                (0,4,8),
                (2,4,6)]

        for x,y,z in winning_combinations:
            if self.board[x] == self.board[y] == self.board[z] and self.board[x] != ' ':
                return self.board[x]

        return False
