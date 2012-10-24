from board import Board
from time import sleep

class Game(object):
    name = 'Tic Tac Toe'

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1.marker = 'O'
        self.player2.marker = 'X'

        self.next_player = player1

    def player_to_play(self):
        to_play = self.next_player

        if to_play == self.player1:
            self.next_player = self.player2
        else:
            self.next_player = self.player1

        return to_play

    def game_ended(self):
        won = self.board.someone_has_one()
        if won:
            print
            print "%s WON!" % won
            return True

        if self.board.full():
            print
            print "STALEMATE!"
            return True

        return False

    def print_game(self):
        print chr(27) + "[2J"

        print "Game %s/5" % (self.game_run + 1)
        print
        print "O: %s" % self.player1.name
        print "X: %s" % self.player2.name
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
