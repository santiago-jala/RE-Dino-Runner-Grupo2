from distutils.errors import DistutilsModuleError
from dino_runner.components.game import Game
from dino_runner.components.dinosaur import Dinosaur

if __name__ == "__main__":
    game = Game()
    a = Dinosaur()
    game.run()
    print("hello there...")
