from board import Board
from time import sleep

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
            print
            print "%s WON!" % player_won.name
            return True

        if self.board.full():
            print
            print "STALEMATE!"
            return True

        return False

    def print_game(self):
        print chr(27) + "[2J"

        o = self.player_from_marker('O')
        x = self.player_from_marker('X')

        print "Game %s/5" % (self.game_run + 1)
        print
        print "O: %s (%s)" % (o.name, o.games_won)
        print "X: %s (%s)" % (x.name, x.games_won)
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

        if self.player1.games_won > self.player2.games_won:
            print "%s WON %s to %s." % (self.player1.name, self.player1.games_won, self.player2.games_won)
        elif self.player2.games_won > self.player1.games_won:
            print "%s WON %s to %s." % (self.player2.name, self.player2.games_won, self.player1.games_won)
        else:
            print "%s and %s tied." % (self.player1.name, self.player2.name)



