# Genetic Algorithm Robot Path Planning

This project implements a **robot path planning system** using a **Genetic Algorithm (GA)** in Python. The user can interactively define the environment (start, goal, and obstacles) using a graphical interface, and the GA will find an optimal path avoiding collisions.

---

## Features

- Interactive environment setup using mouse clicks:
  - First click: Start position
  - Second click: Goal position
  - Drag mouse: Create circular obstacles
- Genetic Algorithm:
  - Random path generation
  - Fitness evaluation (path length + collision penalty)
  - Crossover and mutation operations
- Visualization of the environment and optimal path using `matplotlib`

---

## Project Structure

```
robot-path-planning-GA/
│
├── main.py                 # Entry point for running the program
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
│
├── ga/                     # Genetic Algorithm module
│   └── ga_utils.py          # GA operations and fitness function
│
├── environment/            # Environment module
│   └── world.py             # Environment and obstacles
│
└── visualization/          # Visualization module
    └── plot_utils.py       # Interactive drawing & path plotting
```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/robot-path-planning-GA.git
   cd robot-path-planning-GA
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main program:

```bash
python main.py
```

Steps:

1. Click once to set the **Start** point.
2. Click a second time to set the **Goal** point.
3. Drag with the mouse to create **circular obstacles**.
4. Press the **Start GA** button to run the genetic algorithm.
5. The optimal path will be plotted after computation.

---

## Customization

- You can adjust the GA parameters in `main.py`:
  ```python
  POP_SIZE = 40      # Population size
  GENS = 80          # Number of generations
  ```
- Change the number of waypoints or mutation rate in `ga/ga_utils.py`.

---

## License

This project is licensed under the MIT License.

