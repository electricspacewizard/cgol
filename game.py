import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


universe = np.zeros((10,10))


def get_life():

    life =  [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]]

    return life

def run_life():
    im = None
    while True:

        if not im:

            life = get_life()

            universe[1:5, 1:5] = life

            im = plt.imshow(universe, cmap="binary")

        else:
            new_universe = convolve2d(universe, np.ones((3, 3), dtype=int), 'same') - universe

            universe[new_universe == 1] = 0
            universe[new_universe <  2] = 0
            universe[new_universe == 3] = 1
            universe[new_universe == 4] = 0

            im = plt.imshow(universe, cmap="binary")

        plt.draw()
        plt.pause(1)

run_life()