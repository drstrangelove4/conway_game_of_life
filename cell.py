from turtle import *
import random


# ----------------------------------------------------------------------------------------------------------------------

# Constants
CELL_GAP = 25
CELL_SHAPE = "square"
CELL_COLOR_DEAD = "black"
CELL_COLOR_ALIVE = "white"
ALIVE_INIT_CHANCE = int(100 / 20)

# ----------------------------------------------------------------------------------------------------------------------


class Cell(Turtle):
    """
    A child class of Turtle. Each cell has 2 states: alive or dead. Cells can check the status of their 8 touching
    neighbours and change their status depending on the rules of the game.
    """

    # Any cell with <2 neighbours dies (turns black)
    # Any cell with 2 or 3 neighbours lives (turns green)
    # Any cell with >3 neighbours dies (turns black)
    # Any cell with 3 neighbours comes alive (turns green)

    def __init__(self):
        super().__init__(CELL_SHAPE)
        self.color(CELL_COLOR_DEAD)
        self.alive = False
        self.alive_neighbours = 0
        self.set_status()

    # ------------------------------------------------------------------------------------------------------------------

    def check_neighbours(self, cell_list):
        """
        :param cell_list: list<cell objects>
        :return:
        Takes a list of cell objects and checks the amount of alive neighbour cells .
        """
        for row in cell_list:
            for cell in row:
                # pass if we are dealing with ourselves.
                if self.xcor() == cell.xcor() and self.ycor() == cell.ycor():
                    pass
                # Use the absolute value of the distance between cells to see if an alive cell is a neighbour
                elif abs(cell.ycor() - self.ycor()) <= CELL_GAP and cell.alive:
                    if abs(cell.xcor() - self.xcor()) <= CELL_GAP:
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
        Used to set initial cell status on game start.
        :return:
        """
        choice = random.randint(0, ALIVE_INIT_CHANCE)
        # Give the cells a 1 / X chance of being 'alive'
        if choice == 0:
            self.alive = True
            self.color(CELL_COLOR_ALIVE)
