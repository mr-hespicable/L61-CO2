from pprint import pprint
from typing import Optional
import random

class Board():
    def __init__(self, rows: int = 9, cols: int = 9):
        self.rows: int = rows
        self.cols: int = cols 
        self.board: list[list[int | str]] = [[0] * cols for _ in range(rows)]
        self.hovering: list[int] = [0, 0]
        self.command: str = ""

    def create(self):
        num_mines = 10
        # populate board
        has_dupes = True
        mines_coordinates = [(random.randint(0, 8), random.randint(0, 8)) for _ in range(num_mines)]

        # remove dupes
        while has_dupes:
            for c in mines_coordinates:
                if mines_coordinates.count(c) > 1:
                    mines_coordinates = [(random.randint(0, 8), random.randint(0, 8)) for _ in range(num_mines)]
                else:
                    has_dupes = False
            

        # assign mines to board
        for coord in mines_coordinates:
            self.board[coord[0]][coord[1]] = "-"


        print(mines_coordinates)
        self.display()

        # create numbers on cells around mines
        surrounding_coordinates: dict[str, int] = {}
        for c in mines_coordinates:
            y = c[0]
            x = c[1]

            for j in range(-1, 2):
                for i in range(-1, 2):
                    stringified_coordinate = f"{y+j},{x+i}"
                    if (y+i, x+j) not in mines_coordinates: # so a number is not placed on the mine
                        if list(surrounding_coordinates.keys()).count(stringified_coordinate) != 0:
                            surrounding_coordinates[stringified_coordinate] = surrounding_coordinates[stringified_coordinate] + 1
                        else:
                            surrounding_coordinates[stringified_coordinate] = 1

        pprint(surrounding_coordinates)


        # replace nums in board
        for c in surrounding_coordinates:
            y, x = map(lambda n: int(n), c.split(","))
            if 0 <= y < self.rows and 0 <= x < self.cols:
                self.board[y][x] = surrounding_coordinates[c]

    def click(self, coordinates: list[int]):
        pass

    def display(self) -> None:
        for row in self.board:
            print(*row)

    def choose(self, action: int, coordinates: list[int]):
        """
        action:
            0 = click
            1 = flag
        """

        match action:
            case 1:
                self.click(coordinates)
            case 2:
                pass
            case _:
                print("invalid response: {action}")
        pass
    
    def play(self, quit: bool = False):
        print("welcome to minesweeper meow")
        while not quit:
            self.create()
            self.display()

            c = input("\nhere is your board. what would you like to do?: ")



b = Board()
b.create()
b.display()

