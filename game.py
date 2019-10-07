import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import random

def get_life():

    universe = np.zeros((25, 25))

    blinker = [1, 1, 1]

    toad =     [[1, 1, 1, 0],
                [0, 1, 1, 1]]

    glider =   [[1, 0, 0],
                [0, 1, 1],
                [1, 1, 0]]

    beacon =   [[1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]]

    life_choices = [blinker, toad, glider, beacon]

    life = random.choice(life_choices)

    return life, universe


def run_life():
    image_plot = None
    while True:
        if not image_plot:
            life, universe = get_life()

            # Get the number of rows in life
            rows = np.size(life, 0)
            # Get the number of columns in life
            columns = np.size(life, 1)

            # how to randomly insert life within the game boundary?

            x = random.randint(1, np.size(universe, 0))
            y = random.randint(1, np.size(universe, 1))

            try:
                universe[x:x+rows, y:y+columns] = life
                image_plot = plt.imshow(universe, cmap="binary")
            except:
                print("life out of bounds")
        else:
            new_universe = convolve2d(universe, np.ones((3, 3), dtype=int), 'same') - universe
            universe[new_universe < 2] = 0
            universe[new_universe == 3] = 1
            universe[new_universe > 3] = 0
            image_plot = plt.imshow(universe, cmap="binary")
        plt.draw()
        plt.pause(0.5)

run_life()