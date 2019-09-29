import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


universe = np.zeros((25,25))


def get_life():

    life = [[0, 0, 1, 1, 0],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 1, 0],
             [0, 1, 1, 0, 0]]

    # number of rows np.size(life, 0)
    # number of columns np.size(life, 1)

    return life

def run_life():
    im = None
    while True:

        if not im:

            life = get_life()

            # how to randomly insert life within the game boundary?

            universe[1:5, 1:6] = life

            im = plt.imshow(universe, cmap="binary")

        else:
            new_universe = convolve2d(universe, np.ones((3, 3), dtype=int), 'same') - universe

            universe[new_universe < 2] = 0
            universe[new_universe == 3] = 1
            universe[new_universe > 3] = 0

            im = plt.imshow(universe, cmap="binary")

        plt.draw()
        plt.pause(0.5)

run_life()