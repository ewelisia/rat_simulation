import random
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

class Rat:
    """
    Represents a rat with health, position, age, and ability to move, reproduce, and die.
    """

    def __init__(self, health, x, y, age=0):
        """
        Initializes a new rat with specified health, x and y coordinates, and age.

        :param health: Health status of the rat.
        :param x: X-coordinate of the rat on the grid.
        :param y: Y-coordinate of the rat on the grid.
        :param age: Age of the rat, defaults to 0.
        """
        self.age = age
        self.health = health  # Health can be set here or initialized randomly if needed.
        self.x = x
        self.y = y

    def move(self, a, b, allowed_moves):
        """
        Moves the rat to a new position based on random choice and allowed moves.

        :param a: Width of the grid.
        :param b: Height of the grid.
        :param allowed_moves: List of allowed moves for the rat.
        """
        los = random.randint(0, 4)
        # Randomly choose a direction and move if within bounds and allowed.
        if los==0 and self.y<b:
            if (self.x, self.y+1) in allowed_moves:
                self.y = self.y+1
        if los==1 and self.y>0:
            if (self.x, self.y-1) in allowed_moves:
                self.y=self.y-1
            # to do
        if los==2 and self.x<a:
            if (self.x+1, self.y) in allowed_moves:
                self.x=self.x+1
        if los==3 and self.x>0:
            if (self.x-1, self.y) in allowed_moves:
                self.x=self.x-1 

    def reproduction(self):
        """
        Determines if the rat reproduces based on its age.

        :return: 1 if reproduction occurs, otherwise 0.
        """
        probability = min(0.3, 1 - self.age / 12)
        return 1 if random.random() < probability else 0

    def die(self):
        """
        Determines if the rat dies based on its age.

        :return: 1 if the rat dies, otherwise 0.
        """
        probability = min(1, self.age / 10)
        return 1 if random.random() < probability else 0

    def place(self):
        """
        Returns the current position of the rat.

        :return: A tuple of x and y coordinates.
        """
        return self.x, self.y

    def update_age(self):
        """ Increments the age of the rat by 1. """
        self.age += 1


class Grid:
    """
    Represents a grid environment where rats can move, reproduce, and die.
    """

    def __init__(self, a=20, b=20):
        """
        Initializes a new grid with specified dimensions.

        :param a: Width of the grid.
        :param b: Height of the grid.
        """
        self.a = a
        self.b = b
        self.rat_list = []  # Store the rats on the grid.

    def add(self, rat):
        """ Adds a rat to the grid. """
        self.rat_list.append(rat)

    def initialize(self):
        """
        Initializes the grid with a random number of rats.
        """
        num = random.randint(5, 15)
        positions=[]
        
        for _ in range(num):
            x=random.randint(0, self.a)
            y=random.randint(0, self.b)
            if (x,y) not in positions:
                new_rat = Rat("good", x, y, age=random.randint(0,10))
                self.add(new_rat)
                positions.append((x,y))

    def define_possible_moves(self, rat):
        rat_positions = [other_rat.place() for other_rat in self.rat_list]
        pos_moves = self.possible_move(rat.x, rat.y)
        pos_moves_rat = [move for move in pos_moves if move not in rat_positions]
        return pos_moves_rat

    def run_step(self):
        """
        Runs a single step in the simulation, updating each rat's status.
        """
        rat_to_die = []
        for i, rat in enumerate(self.rat_list):
            rat.update_age()
            pos_moves_rat = self.define_possible_moves(rat)
            rat.move(self.a, self.b, pos_moves_rat)

            if rat.reproduction() == 1:
                reproducted_rat_location=self.define_possible_moves(rat)
                if len(reproducted_rat_location)>0:
                    new_rat = Rat("good", pos_moves_rat[0][0], pos_moves_rat[0][1])
                    self.add(new_rat)

            if rat.die() == 1:
                rat_to_die.append(i)

        for i in sorted(rat_to_die, reverse=True):
            del self.rat_list[i]

    def position(self):
        """ Prints the positions of all rats on the grid. """
        for rat in self.rat_list:
            print(rat.place())

    def possible_move(self, x, y):
        """
        Determines the possible moves for a rat based on its position.

        :param x: X-coordinate of the rat.
        :param y: Y-coordinate of the rat.
        :return: List of possible moves.
        """
        possible_moves = []
        if x != 0:
            possible_moves.append((x - 1, y))
        if x != self.a:
            possible_moves.append((x + 1, y))
        if y != 0:
            possible_moves.append((x, y - 1))
        if y != self.b:
            possible_moves.append((x, y + 1))
        return possible_moves
    
    def display_rats(self, i):
        rat_positions=[other_rat.place() for other_rat in self.rat_list]
        print("ratpositions", rat_positions)
        print(self.a)
        print(self.b)
        grid=np.zeros((21, 21))
        # grid=np.zeros(self.a, self.b)

        for x, y in rat_positions:
            grid[x,y]+=1

        plt.imshow(grid, cmap='hot', interpolation='nearest')
        plt.title("Rat Position Heatmap")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.colorbar(label='Number of Rats')
        plt.savefig(f'heatmap_{i}')
        plt.close()


# def create_heatmap(rat_coords, grid_size):
#     """
#     Create a heatmap based on the positions of rats on a grid.

#     :param rat_coords: List of tuples representing the coordinates of rats on the grid.
#     :param grid_size: Tuple representing the size of the grid (rows, columns).
#     :return: None, displays a heatmap.
#     """
#     # Initialize an empty grid
#     grid = np.zeros(grid_size)

#     # Increment grid cells based on rat positions
#     for x, y in rat_coords:
#         grid[x, y] += 1

#     # Plot the heatmap
#     plt.imshow(grid, cmap='hot', interpolation='nearest')
#     plt.title("Rat Position Heatmap")
#     plt.xlabel("X Coordinate")
#     plt.ylabel("Y Coordinate")
#     plt.colorbar(label='Number of Rats')
#     plt.show()

# # Example usage:
# rat_positions = [(1, 2), (2, 3), (1, 2), (2, 3), (1, 1)]  # Example rat coordinates
# grid_dimensions = (5, 5)  # Example grid size

# create_heatmap(rat_positions, grid_dimensions)


# Main simulation
grid_console = Grid()
grid_console.initialize()
print(grid_console.position())
for n in range(10):
    grid_console.run_step()
    grid_console.display_rats(n)
    print(len(grid_console.rat_list))
