import matplotlib.pyplot as plt
import random


def shift_y_axis():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.spines['left'].set_position(('data', 0.0))
    ax.yaxis.set_label_coords(0.0, 1.0)


class OneDimRandomWalk:
    """
        One spatial dimension random walk simulation

        Initialise with a time scale as an positive integer, and a number
        of walkers

        Two instance methods:

            1. walk, which returns a list of lists for as many walkers
        as initialised with, each list showing the position vector for each
        time increment

            2. show paths, which genreates the paths and outputs a visualisation
        of the path taken for each random walker, y-axis time, x-axis position
    """

    directions = [1, -1]

    def __init__(self, time, walkers):
        self.time_coordinates = [t for t in range(0, time + 1)]
        self.walkers = walkers

    def walk(self):
        self.paths = []
        for walker in range(0, self.walkers):
            path = [0]
            for increment in self.time_coordinates[1:]:
                path.append(path[-1] + random.choice(self.directions))
            self.paths.append(path)
        return self.paths

    def show_paths(self):
        tracks = self.walk()
        x_max = max([max(x) for x in tracks])
        x_min = min([min(x) for x in tracks])
        shift_y_axis()
        for track in tracks:
            plt.plot(track, self.time_coordinates)
        plt.xlabel("distance (x)")
        plt.ylabel("time")
        plt.xlim(x_min - 1, x_max + 1)
        plt.ylim(0, self.time_coordinates[-1] + 1)
        plt.show()
