import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import random


universe = np.zeros((25,25))


def get_life():
    blinker = [1, 1, 1]

    toad = [[1, 1, 1, 0],
            [0, 1, 1, 1]]

    glider = [[1, 0, 0],
              [0, 1, 1],
              [1, 1, 0]]

    life_choices = [blinker, toad, glider]

    life = random.choice(life_choices)

    """life = [[0, 0, 1, 1, 0],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 1, 0],
             [0, 1, 1, 0, 0]]"""

    return life


def run_life():
    im = None
    while True:
        if not im:
            life = get_life()

            # Get the number of rows in life
            rows = np.size(life, 0)
            # Get the number of columns in life
            columns = np.size(life, 1)

            # how to randomly insert life within the game boundary?

            x = random.randint(1, np.size(universe, 0))
            y = random.randint(1, np.size(universe, 1))

            try:
                universe[x:x+rows, y:y+columns] = life
                im = plt.imshow(universe, cmap="binary")
            except:
                print("life out of bounds")
        else:
            new_universe = convolve2d(universe, np.ones((3, 3), dtype=int), 'same') - universe
            universe[new_universe < 2] = 0
            universe[new_universe == 3] = 1
            universe[new_universe > 3] = 0
            im = plt.imshow(universe, cmap="binary")
        plt.draw()
        plt.pause(0.5)

run_life()