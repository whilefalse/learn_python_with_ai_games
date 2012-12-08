from board import Board
from time import sleep
from termcolor import colored

class Game(object):
    name = 'Tic Tac Toe'

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1.marker = 'O'
        self.player2.marker = 'X'

        self.player1.games_won = 0
        self.player2.games_won = 0

        self.next_player = player1

    def player_to_play(self):
        to_play = self.next_player

        if to_play == self.player1:
            self.next_player = self.player2
        else:
            self.next_player = self.player1

        return to_play

    def player_from_marker(self, marker):
        if self.player1.marker == marker:
            return self.player1
        else:
            return self.player2

    def game_ended(self):
        won = self.board.someone_has_one()
        if won:
            player_won = self.player_from_marker(won)
            player_won.games_won += 1
            self.print_game(player_won)
            return True

        if self.board.full():
            self.print_game('none')
            return True

        return False

    def print_game(self, last_won=None):
        print chr(27) + "[2J"

        o = self.player_from_marker('O')
        x = self.player_from_marker('X')

        o_won = colored('WINNER!!', 'red', attrs=['bold']) if last_won == o else ''
        x_won = colored('WINNER!!', 'red', attrs=['bold']) if last_won == x else ''

        if last_won == 'none':
            o_won = x_won = colored('STALEMATE!!', 'red', attrs=['bold'])

        print colored('O:', 'green', attrs=['bold']) + " %s %s %s" % (colored(o.name, 'green', attrs=['bold']), colored('(%s)' % o.games_won, 'yellow'), o_won)
        print colored('X:', 'red', attrs=['bold']) + " %s %s %s" % (colored(x.name, 'red', attrs=['bold']), colored('(%s)' % x.games_won, 'yellow'), x_won)
        print

        self.board.print_board()

    def play(self):
        for i in range(5):
            self.game_run = i
            self.board = Board()

            while (not self.game_ended()):
                self.print_game()

                sleep(0.5)

                player_to_play = self.player_to_play()

                index = player_to_play.place_piece(self.board.board)

                self.board.place_piece(index, player_to_play.marker)

                self.print_game()
            sleep(2)
            self.player1.marker, self.player2.marker = self.player2.marker, self.player1.marker
            self.next_player = self.player_from_marker('O')

        print
        if self.player1.games_won > self.player2.games_won:
            print "%s WON %s to %s." % (self.player1.name, self.player1.games_won, self.player2.games_won)
        elif self.player2.games_won > self.player1.games_won:
            print "%s WON %s to %s." % (self.player2.name, self.player2.games_won, self.player1.games_won)
        else:
            print "%s and %s tied." % (self.player1.name, self.player2.name)



