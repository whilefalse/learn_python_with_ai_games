from time import sleep
from sea import Sea
from validation_error import ValidationError
from termcolor import colored
import sys

class Game(object):
    name = 'Battleships'

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1.games_won = 0
        self.player2.games_won = 0

        self.player_turn = self.player1


    def start_game(self):
        try:
            self.player1.sea = Sea(self.player1.place_ships())
            self.player2.sea = Sea(self.player2.place_ships())
        except ValidationError as e:
            print e.message
            sys.exit()

    def print_game(self, last_won=None):
        print chr(27) + "[2J"

        star = colored(' WINNER!!', 'red') if last_won == self.player1 else ''

        print colored(self.player1.name, 'blue', attrs=['bold']) +\
        colored(" (%s/5)" % (self.player1.games_won), 'yellow') + star

        self.player1.sea.print_sea()
        star = colored(' WINNER!!', 'red') if last_won == self.player2 else ''
        print
        print colored(self.player2.name, 'green', attrs=['bold']) +\
        colored(" (%s/5)" % (self.player2.games_won), 'yellow') + star
        self.player2.sea.print_sea()

    def next_player(self):
        player = self.player_turn
        if player == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1
        return player

    def play(self):
        for i in range(5):
            self.start_game()
            self.print_game()

            while not self.player1.sea.all_sunk() and not self.player2.sea.all_sunk():
                player = self.next_player()
                other_player = self.player_turn
                shot = player.take_shot(other_player.sea.present_to_player(), other_player.sea.ship_lengths_remaining())

                other_player.sea.take_shot(shot)

                self.print_game()
                sleep(0.1)

            if self.player1.sea.all_sunk():
                self.player2.games_won += 1
                self.print_game(self.player2)
            if self.player2.sea.all_sunk():
                self.player1.games_won += 1
                self.print_game(self.player1)

            if i < 4:
                sleep(2)
            self.player1, self.player2 = self.player2, self.player1

        if self.player1.games_won > self.player2.games_won:
            print "%s WON %s to %s" % (colored(self.player1.name, 'blue', attrs=['bold']), colored(self.player1.games_won, 'blue'), colored(self.player2.games_won, 'green'))
        else:
            print "%s WON %s to %s" % (colored(self.player2.name, 'green', attrs=['bold']), colored(self.player2.games_won, 'green'), colored(self.player1.games_won, 'blue'))
