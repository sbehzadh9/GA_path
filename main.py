from environment.world import Environment
from ga.ga_utils import initialize_population, crossover, mutate, fitness
from visualization.plot_utils import Visualizer
import random

POP_SIZE = 40
GENS = 80

# Initialize environment
env = Environment()
visualizer = Visualizer()

# Interactive environment setup
visualizer.interactive_env(env)

if not env.is_valid():
    raise ValueError("Start and Goal must be defined!")

start, goal, obstacles = env.start, env.goal, env.obstacles

# Initialize GA population
population = initialize_population(POP_SIZE)

# Run GA
for gen in range(GENS):
    scores = [(fitness(ind, start, goal, obstacles), ind) for ind in population]
    scores.sort(reverse=True, key=lambda x: x[0])
    best_score, best_path = scores[0]
    print(f"Gen {gen}: Best fitness={best_score:.2f}")
    if best_score > -20:
        print("✅ Suitable path found!")
        break
    new_pop = []
    for _ in range(POP_SIZE):
        p1 = random.choice(scores[:10])[1]
        p2 = random.choice(scores[:10])[1]
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)
    population = new_pop

# Visualize the best path
visualizer.plot_path(start, goal, obstacles, best_path)
