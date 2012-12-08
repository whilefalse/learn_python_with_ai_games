from termcolor import colored

class Board(object):
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.winning_combination=[]

    def print_board(self):
        pipe = colored('|', 'blue', attrs=['bold'])
        print "%s %s %s %s %s" % (self.colorize(0), pipe, self.colorize(1), pipe, self.colorize(2))
        print colored("---------", 'blue', attrs=['bold'])
        print "%s %s %s %s %s" % (self.colorize(3), pipe, self.colorize(4), pipe, self.colorize(5))
        print colored("---------", 'blue', attrs=['bold'])
        print "%s %s %s %s %s" % (self.colorize(6), pipe, self.colorize(7), pipe, self.colorize(8))

    def colorize(self, index):
        uncolored = self.board[index]
        if index in self.winning_combination:
            return colored(uncolored, 'red', 'on_magenta', attrs=['bold']) if uncolored == 'X' else colored(uncolored, 'green', 'on_magenta', attrs=['bold'])
        else:
            return colored(uncolored, 'red') if uncolored == 'X' else colored(uncolored, 'green')


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
                won = self.board[x]
                self.winning_combination = (x,y,z)
                return won

        return False
