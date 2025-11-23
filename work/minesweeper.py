import random
import time
import os
import platform
from typing import Callable


class Board:
    def __init__(self, rows: int = 9, cols: int = 9):
        self.cols: int = rows
        self.rows: int = cols

        self.unselect_coord: str = "□"

        self.quit: bool = False
        self.true_board: list[list[int | str]] = [[0] * cols for _ in range(rows)]
        self.user_board: list[list[int | str]] = [[self.unselect_coord] * cols for _ in range(rows)]
        self.command: str = ""
        self.mines_coordinates: list[list[int]] = []
        self.flag_coordinates: list[list[int]] = []
        self.coordinates: list[int] = [0, 0]


    def create(self):
        num_mines = 10
        
        # populate board
        has_dupes = True
        mines_coordinates = [
            (random.randint(0, self.cols-1), random.randint(0, self.rows-1)) for _ in range(num_mines)
        ]
        
        self.mines_coordinates = list(map(lambda x: list(x), mines_coordinates))

        # remove dupes
        while has_dupes:
            for c in mines_coordinates:
                if mines_coordinates.count(c) > 1:
                    mines_coordinates = [
                        (random.randint(0, self.cols-1), random.randint(0, self.rows-1))
                        for _ in range(num_mines)
                    ]
                    self.mines_coordinates = list(map(lambda x: list(x), mines_coordinates))

                else:
                    has_dupes = False

        # assign mines to board
        for coord in mines_coordinates:
            self.true_board[coord[0]][coord[1]] = "*"

        # create numbers on cells around mines
        surrounding_coordinates: dict[str, int] = {}
        for c in mines_coordinates:
            y = c[0]
            x = c[1]

            for j in range(-1, 2):
                for i in range(-1, 2):
                    stringified_coordinate = f"{y + i},{x + j}"
                    if (
                        y + i,
                        x + j,
                    ) not in mines_coordinates:  # so a number is not placed on the mine
                        if (
                            list(surrounding_coordinates.keys()).count(
                                stringified_coordinate
                            )
                            != 0
                        ):
                            surrounding_coordinates[stringified_coordinate] += 1
                        else:
                            surrounding_coordinates[stringified_coordinate] = 1

        # replace nums in board
        for c in surrounding_coordinates:
            y, x = map(lambda n: int(n), c.split(","))
            if 0 <= y < self.cols and 0 <= x < self.rows:
                self.true_board[y][x] = surrounding_coordinates[c] 





    def __reveal(self):
        y, x = self.coordinates
        self.user_board[y][x] = self.true_board[y][x]

    def __sweep(self):
        swept_coord = self.coordinates

        # use cache list to check for used coords
        checked_coordinates: list[list[int]] = []
        def propogate(coordinate: list[int]):
            y, x = coordinate
            val = self.true_board[y][x]
            if val != 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        ry, rx = y + i, x + j
                        if (
                            coordinate not in checked_coordinates
                            and 0 <= ry < self.cols
                            and 0 <= rx < self.rows
                            and self.true_board[ry][rx] == 0
                        ):
                            self.coordinates = [ry, rx]
                            self.click()
                            propogate([ry, rx])
                        elif 0 <= ry < self.cols and 0 <= rx < self.rows:
                            self.coordinates = [ry, rx]
                            self.click()

        propogate(swept_coord)


    def click(self):
        y, x = self.coordinates
        val = self.true_board[y][x]

        # eval number
        match val:
            case 0:
                # set empty cell to 0
                self.true_board[y][x] = "0"
                self.__sweep()
            case "*":
                self.__reveal()
                self.user_board = self.true_board
                self.display()
                print("kaboom you lose :( play again sometime")
                self.quit = True

            case _:
                self.__reveal() # reveal num and continue
    
    def flag(self):
        y, x = self.coordinates
        val = self.user_board[y][x]
        if val == self.unselect_coord:
            self.user_board[y][x] = "\x1b[31mf\x1b[0m"
            self.flag_coordinates.append([y, x])
        elif val == "\x1b[31mf\x1b[0m":
            self.user_board[y][x] = self.unselect_coord
            self.flag_coordinates.remove([y, x])

    def clear(self):
        if platform.system() == "Windows":
            _ = os.system("cls")
        else:
            _ = os.system("clear")
        


    def display(self):
        colguides = [i+1 for i in range(self.rows)]
        print(" ", *colguides, sep="   ")
        for i, row in enumerate(self.user_board):
            u_row = [" " if x == "0" else x for x in row]
            print(f"{i+1} | ", end="")
            print(*u_row, sep=" | ", end=" |\n")
            print("")

    def choose(self):
        """
        action:
            0 = click
            1 = flag
        """

        match self.command:
            case "c":
                self.click()
            case "f":
                self.flag()
            case _:
                print("invalid response: {action}")
        pass

    def play(self):
        self.clear()
        welcome_msg = f"""
            welcome to minesweeper meow
            here are your options for choices:
              - click
              - flag

            coordinates are given as x, y
            where 1 <= x,y <= board length

            e.g. 
                "f 3 9"
                "c 1 2"
                 
            board size is {self.cols} by {self.rows}.
            have fun :3
        """.strip()
        print(welcome_msg)
        print("\n\n\n")

        self.create()
        time.sleep(1)

        # conditions
        valid_coords: Callable[[list[int]], bool] = lambda n: 1 <= n[0] <= self.rows and 1 <= n[1] <= self.cols

        while not self.quit:
            self.display()
            command = input("\nhere is your board. what would you like to do?: ").split()

            if command and command[0] == "quit":
                self.quit = True
                continue

            if len(command) < 3:
                print(f"uh oh not enough inputs in your command <{command}>")
                continue

            
            command, x, y = command

            coords = list(map(int, [x, y]))

            if not valid_coords(coords):
                print(f"your coords {coords} are invalid")
                continue

            self.command = command
            self.coordinates = list(map(lambda x: x-1, coords))
            self.coordinates.reverse() # y, x from x, y

            self.choose()

            if sorted(self.flag_coordinates) == sorted(self.mines_coordinates):
                print("YOU WIN YAYYYYYYY YAYYYYYY")
                self.quit = True

            if self.quit:
                break #STUPID SOLUTION B ICBA

            self.clear()
            print(self.mines_coordinates)


            


b = Board()
b.play()
