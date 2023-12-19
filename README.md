# Rat Grid Simulation

## Overview
This Python application simulates the behavior of rats within a grid environment. It models the movement, reproduction, and mortality of rats, and visualizes their distribution across the grid over time.

## Features

- **Rat Simulation**: Each rat is represented with attributes like health, position, age, and is capable of moving, reproducing, and dying.
- **Dynamic Grid Environment**: The simulation takes place in a grid where rat positions and movements are tracked.
- **Heatmap Visualization**: The distribution of rats is visualized as a heatmap, providing a clear representation of rat concentrations over time.

## Classes and Methods

### `Rat`
The `Rat` class models an individual rat in the environment.

#### Attributes
- `health`: Health status of the rat.
- `x`, `y`: Coordinates of the rat in the grid.
- `age`: Age of the rat.

#### Methods
- `move(a, b, allowed_moves)`: Moves the rat within the grid.
- `reproduction()`: Determines if the rat reproduces.
- `die()`: Determines if the rat dies based on its age.
- `place()`: Returns the current position.
- `update_age()`: Increments the rat's age.

### `Grid`
The `Grid` class represents the simulation space.

#### Attributes
- `a`, `b`: Dimensions of the grid.
- `rat_list`: List of rats on the grid.

#### Methods
- `add(rat)`: Adds a new rat to the grid.
- `initialize()`: Initializes the grid with a random set of rats.
- `define_possible_moves(rat)`: Defines possible moves for a given rat.
- `run_step()`: Updates the status of each rat in the grid.
- `position()`: Displays the positions of all rats.
- `possible_move(x, y)`: Determines potential moves for a rat.
- `display_rats(i)`: Generates a heatmap of rat positions.

## Running the Simulation

1. **Initialization**: The grid is initialized with a random number of rats.
2. **Simulation Loop**: The simulation runs for a specified number of steps. In each step:
   - Each rat may move, reproduce, or die.
   - The current state of the grid is visualized as a heatmap.
3. **Visualization**: Heatmaps are saved for each step, showing rat positions.

## Requirements

- Python 3.x
- matplotlib
- numpy

## Installation

No specific installation required. Ensure Python and the necessary libraries are installed.

## Usage

Run the script to start the simulation. The grid and rat parameters can be adjusted within the script.

## Visualizations

Heatmaps are saved in the running directory, labeled by the simulation step number.

## Contributing

Contributions to the simulation are welcome. Feel free to fork the project and submit pull requests.

## License

This project is open-sourced under the MIT License.

