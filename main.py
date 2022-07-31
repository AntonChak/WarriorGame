import os
import sys
sys.path.insert(0, os.path.abspath(__file__))
sys.path.append(os.path.abspath(__file__))

from game import Game
from menu import Menu


END_GAME = False


def run():
    menu = Menu()

    game = Game(menu=menu)
    game.start_new_game()
    print(f"Your character is: \n{game.character}")


if __name__ == "__main__":
    run()
