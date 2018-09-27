from random import choice

class RandomWalk():
    """ generate a random walk data """
    def __init__(self, num_points=5000):
        """ initialize attribute """
        self.num_points = num_points

        # all data begin at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ compute all poins of random walk """
        # random walk until areach to special length 
        while len(self.x_values) < self.num_points:
            # decide direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # defuse orieng
            if x_step == 0 and y_step == 0:
                continue

            # compute next point
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


