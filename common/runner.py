import sys
from os.path import basename

class Runner(object):
    def __init__(self, game_class):
        self.game_class = game_class

    def play_game(self):
        if len(sys.argv) != 3:
            print "Please provide first and second player modules..."
            sys.exit()

        player1 = self.generate_player(sys.argv[1])
        player2 = self.generate_player(sys.argv[2])

        print "Booting Game '%s': '%s' VS '%s'...\n\n" % (
                self.game_class.name,
                player1.name,
                player2.name)
        game = self.game_class(player1, player2)

        game.play()

    def generate_player(self, path):
        module_path = path.replace('.py', '').replace('/', '.')

        module = __import__(module_path, globals(), locals(), ['Player'])

        return module.Player()
