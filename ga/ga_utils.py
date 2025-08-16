import random
import numpy as np

WAYPOINTS = 6
MUT_RATE = 0.2

# Population
def random_path(xlim=(0,20), ylim=(0,20)):
    return [(random.uniform(*xlim), random.uniform(*ylim)) for _ in range(WAYPOINTS)]

def initialize_population(pop_size, xlim=(0,20), ylim=(0,20)):
    return [random_path(xlim, ylim) for _ in range(pop_size)]

# Crossover
def crossover(p1, p2):
    point = random.randint(1, WAYPOINTS-1)
    return p1[:point] + p2[point:]

# Mutation
def mutate(path):
    if random.random() < MUT_RATE:
        i = random.randint(0, WAYPOINTS-1)
        path[i] = (random.uniform(0,20), random.uniform(0,20))
    return path

# Fitness
def path_points(path, start, goal):
    return [start] + path + [goal]

def check_collision(p1, p2, obstacles):
    for ox, oy, r in obstacles:
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x2-x1, y2-y1
        if dx == 0 and dy == 0:
            dist = np.hypot(x1-ox, y1-oy)
        else:
            t = max(0, min(1, ((ox-x1)*dx + (oy-y1)*dy)/(dx*dx+dy*dy)))
            proj_x, proj_y = x1+t*dx, y1+t*dy
            dist = np.hypot(proj_x-ox, proj_y-oy)
        if dist < r:
            return True
    return False

def fitness(path, start, goal, obstacles):
    pts = path_points(path, start, goal)
    length = 0
    penalty = 0
    for i in range(len(pts)-1):
        p1, p2 = pts[i], pts[i+1]
        length += np.hypot(p2[0]-p1[0], p2[1]-p1[1])
        if check_collision(p1, p2, obstacles):
            penalty += 50
    dist_to_goal = np.hypot(pts[-1][0]-goal[0], pts[-1][1]-goal[1])
    return - (length + penalty + dist_to_goal)
