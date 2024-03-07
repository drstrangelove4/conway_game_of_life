from turtle import *
import random

# ----------------------------------------------------------------------------------------------------------------------

# Constants
CELL_SHAPE = "square"
CELL_COLOR_DEAD = "black"
CELL_COLOR_ALIVE = "white"
ALIVE_INIT_CHANCE = int(100 / 20)


# ----------------------------------------------------------------------------------------------------------------------


class Cell(Turtle):
    """
    A child class of Turtle. Each cell has 2 states: 'alive' or 'dead' (white or black). Cells can check the status of
    their (up to) 8 touching neighbours and change their status depending on the rules of the game.
    """

    # Any cell with <2 neighbours dies (turns black)
    # Any cell with 2 or 3 neighbours lives (stays white if currently white)
    # Any cell with >3 neighbours dies (turns black)
    # Any cell with 3 neighbours comes alive (turns white)

    def __init__(self, x, y):
        super().__init__(CELL_SHAPE)
        self.color(CELL_COLOR_DEAD)
        self.alive = False

        # Stores a list of adjacent cells. From this we can derive the amount of alive neighbours and thus the action
        # of what this cell should take.
        self.neighbours_list = []
        self.alive_neighbours = 0

        # The position of the cell in the cell list used by the main function. Useful for calculating neighbours and
        # reducing the amount of operations needed per loop.
        self.x = x
        self.y = y

        # Sets its status to a random choice of alive/dead on creation.
        self.set_status()

    # ------------------------------------------------------------------------------------------------------------------

    def check_neighbours(self):
        """
        Looks at the cells in the self.neighbours_list and counts how many are alive.
        :return:
        """

        for cell in self.neighbours_list:
            if cell.alive:
                self.alive_neighbours += 1

    # ------------------------------------------------------------------------------------------------------------------

    def change_status(self):
        """
        Checks if the cell should be "alive" or "dead" based upon neighbour status and then changes the cell status.
        :return:
        """
        # If there are less than 2 or more than 3 neighbours the cell should be set to "dead".
        if self.alive_neighbours < 2 or self.alive_neighbours > 3:
            self.alive = False
            self.color(CELL_COLOR_DEAD)

        # If there are 2 neighbours and the cell is currently alive then it should stay alive.
        elif self.alive_neighbours == 2 and self.alive:
            pass

        # If there are 3 neighbours alive then the cell should come alive.
        elif self.alive_neighbours == 3:
            self.alive = True
            self.color(CELL_COLOR_ALIVE)

        # Set the counter of alive neighbours to 0 before the next round of calculations.
        self.alive_neighbours = 0

    # ------------------------------------------------------------------------------------------------------------------

    def set_status(self):
        """
        Gives a cell X chance of being made "alive" when called.
        :return:
        """
        choice = random.randint(0, ALIVE_INIT_CHANCE)
        # Give the cells a 1 / X chance of being 'alive'
        if choice == 0:
            self.alive = True
            self.color(CELL_COLOR_ALIVE)

    # ------------------------------------------------------------------------------------------------------------------

    def find_neighbours(self, cell_list, gap):
        """
        Iterates over all the created cells and finds possible neighbours using distance between cell objects to
        discriminate for valid neighbours.
        :param gap: an int indicating the distance between cell centers.
        :param cell_list: a list of cell objects containing all cells created by the game.
        :return:
        """

        for row in cell_list:
            for cell in row:

                # pass if we are dealing with ourselves.
                if self.xcor() == cell.xcor() and self.ycor() == cell.ycor():
                    pass

                # Use the absolute value of the distance between cells to see if an alive cell is a neighbour
                elif abs(cell.ycor() - self.ycor()) <= gap:
                    if abs(cell.xcor() - self.xcor()) <= gap:
                        self.neighbours_list.append(cell)

