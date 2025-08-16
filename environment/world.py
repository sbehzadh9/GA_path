import numpy as np

class Environment:
    def __init__(self, xlim=(0, 20), ylim=(0, 20)):
        self.start = None
        self.goal = None
        self.obstacles = []
        self.xlim = xlim
        self.ylim = ylim

    def set_start(self, x, y):
        self.start = (x, y)

    def set_goal(self, x, y):
        self.goal = (x, y)

    def add_obstacle(self, x, y, radius):
        self.obstacles.append((x, y, radius))

    def is_valid(self):
        return self.start is not None and self.goal is not None