# encoding: utf-8
from validation_error import ValidationError
from ship import Ship
from termcolor import colored

class Sea(object):
    sea_char = colored(u'*', 'blue')
    ship_char = colored(u"▓", 'yellow')
    sunk_char = colored(u'╳', 'green')
    miss_char = colored(u'*', 'red')

    def __init__(self, ship_placements):
        self.grid = [[self.__class__.sea_char for x in range(10)] for y in range(10)]
        self.ships = []
        self.parse_ship_placements(ship_placements)
        self.ships = sorted(self.ships, key=lambda x: -len(x.squares))

    def ship_lengths_remaining(self):
        lengths = []
        for ship in self.ships:
            if self.remaining_squares(ship):
                lengths.append(len(ship.squares))
        return lengths

    def present_to_player(self):
        convert = {
                self.__class__.sea_char: '?',
                self.__class__.ship_char: '?',
                self.__class__.sunk_char: 'x',
                self.__class__.miss_char: 'o'
                }
        grid = [[] for x in range(10)]
        for y, row in enumerate(self.grid):
            for x, square in enumerate(row):
                grid[x].append(convert[square])
        return grid

    def all_sunk(self):
        for row in self.grid:
            for square in row:
                if square == self.__class__.ship_char:
                    return False
        return True

    def take_shot(self, shot):
        if shot[0] < 0 or shot[0] > 9 or shot[1] < 0 or shot[1] > 9:
            raise ValidationError("Shot is outside the board: %s" % shot)

        if self.grid[shot[1]][shot[0]] == self.__class__.ship_char:
            self.grid[shot[1]][shot[0]] = self.__class__.sunk_char
        elif self.grid[shot[1]][shot[0]] == self.__class__.sea_char:
            self.grid[shot[1]][shot[0]] = self.__class__.miss_char


    def print_sea(self):
        for i, row in enumerate(self.grid):
            for square in row:
                print ' ' + square,

            ship = self.ships[i]
            remaining = self.remaining_squares(ship)
            print "\t" + "%s " % self.__class__.ship_char*remaining,

            print ' '

    def remaining_squares(self, ship):
        remaining = 0
        for square in ship.squares:
            if self.grid[square[1]][square[0]] == self.__class__.ship_char:
                remaining += 1
        return remaining

    def squares_for_ship_placement(self, length, x, y, orientation):
        if orientation == 'down':
            dx = 0
            dy = 1
        else:
            dx = 1
            dy = 0

        squares = []
        for i in range(length):
            squares.append([x+i*dx, y+i*dy])

        return squares

    def parse_ship_placements(self, placements):
        battleships = 0
        cruisers = 0
        destroyers = 0
        submarines = 0

        if len(placements) != 10:
            raise ValidationError("Expected 10 ships, but you gave %s" % len(placements))

        for placement in placements:
            if len(placement) != 4:
                raise ValidationError("Expected ship placement to be of form [length, x, y, orientation] but was %s" % placement)

            length, x, y, orientation = placement

            if length == 4 and battleships > 0:
                raise ValidationError("You can only have 1 battleship (length 5)")
            elif length == 3 and cruisers > 1:
                raise ValidationError("You can only have 2 cruisers (length 3)")
            elif length == 2 and destroyers > 2:
                raise ValidationError("You can only have 3 destroyers (length 2)")
            elif length == 1 and submarines > 3:
                raise ValidationError("You can only have 4 submarines (length 1)")

            if length not in [1,2,3,4]:
                raise ValidationError("Invalid ship length given: %s" % length)
            if x > 9 or x < 0:
                raise ValidationError("Invalid x position given: %s" % x)
            if y > 9 or x < 0:
                raise ValidationError("Invalid y position given: %s" % y)
            if orientation not in ['down', 'across']:
                raise ValidationError("Invalid orientation %s" % orientation)

            squares = self.squares_for_ship_placement(length, x, y, orientation)
            for x, y in squares:
                if x < 0 or x > 9 or y < 0 or y > 9:
                    raise ValidationError("Ship goes off of the board: %s" % placement)
                if self.grid[y][x] != self.__class__.sea_char:
                    raise ValidationError("Ship overlaps with existing ship: %s" % placement)

                self.grid[y][x] = self.__class__.ship_char

            self.ships.append(Ship(squares))
