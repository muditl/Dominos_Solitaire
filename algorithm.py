"""
You are given a grid with 2 rows and columns.
Each box has an integer.
2x1 tiles have to be placed in the grid, filling it completely.
For each tile, the score is differences of the two integers in the tile.
The aim is to maximise the score.
"""
import random
from colorama import Fore
import numpy as np


# Generates a random grid with params.
def generate_random_grid(columns, min_n, max_n):
    if columns < 1:
        raise Exception("Need at least 1 column")
    if min_n >= max_n:
        raise Exception("Minimum is not smaller than Maximum")
    grid = np.zeros((2, columns), dtype=int)
    for i in range(columns):
        n1 = int(random.randrange(min_n, max_n + 1))
        n2 = int(random.randrange(min_n, max_n + 1))
        grid[0][i] = n1
        grid[1][i] = n2
    return grid


def dynamic_programming_algorithm(grid_):
    n = len(grid_[0])
    if n < 1:
        return 0
    if n == 1:
        return [np.abs(grid_[0][0] - grid_[1][0])], [False]
    # best solution up till element
    b = np.zeros(n, dtype=int)
    # store if vertical or horizontal
    sol = np.zeros(n, dtype=bool)
    # first vertical tile
    b[0] = np.abs(grid_[0][0] - grid_[1][0])
    # for second column
    # max of first 2 vertical tiles of first 2 horizontal tiles
    vertical_1_2 = np.abs(grid_[0][0] - grid_[1][0]) + np.abs(grid_[0][1] - grid_[1][1])
    horizontal_1 = np.abs(grid_[0][0] - grid_[0][1]) + np.abs(grid_[1][0] - grid_[1][1])
    b[1] = max(vertical_1_2, horizontal_1)

    if horizontal_1 > b[0] + vertical_1_2:
        sol[0] = 1
        sol[1] = 1
    for i in range(2, n):
        # vertical current
        vertical_i = np.abs(grid_[0][i] - grid_[1][i])
        # horizontal current and previous
        horizontal_i_1 = np.abs(grid_[0][i - 1] - grid_[0][i]) + np.abs(grid_[1][i - 1] - grid_[1][i])
        # calculate best score and append
        b[i] = max(b[i - 1] + vertical_i, b[i - 2] + horizontal_i_1)
        # mark the horizontal in solution
        if b[i - 2] + horizontal_i_1 > b[i - 1] + vertical_i:
            sol[i] = 1
            sol[i - 1] = 1

    # if odd horizontal blocks, remove the first one.
    sol = remove_odd_true(sol)
    return b, sol


# checks array for odd number of continuous true's, if found, puts false in place of the first one.
def remove_odd_true(sol):
    res = np.copy(sol)
    odd = False
    for i in np.arange(len(res) - 1, -1, -1):
        if res[i]:
            odd = not odd
        if not res[i]:
            if odd:
                res[i + 1] = 0
            odd = False
        if i == 0 and odd:
            res[0] = False
    return res


# returns grid in human-readable form.
def get_grid_string(grid_):
    box_len = get_box_len(grid_)
    grid_string = "|"
    for i in range(len(grid_[0])):
        str_i = get_str_box(grid_[0][i], box_len)
        grid_string += str_i + "|"
    grid_string += "\n|"
    for i in range(len(grid_[1])):
        str_i = get_str_box(grid_[1][i], box_len)
        grid_string += str_i + "|"
    return grid_string


# returns the max box size for the grid
def get_box_len(grid_):
    maxi = max(max(grid_[0]), max(grid_[1]))
    mini = min(min(grid_[0]), min(grid_[1]))
    max_len = max(len(str(maxi)), len(str(mini)))
    box_len = max_len + 2
    return box_len


# returns the box element for an element, given box length
def get_str_box(i, box_len):
    len_i = len(str(i))
    len_dif = box_len - len_i
    prepend = " " * int(np.ceil(len_dif / 2))
    append = " " * int(np.floor(len_dif / 2))
    str_i = prepend + str(i) + append
    return str_i


# prints the solution in human-readable form onto the terminal.
def print_grid_sol(grid_, sol):
    box_len = get_box_len(grid_)
    if sol[0]:
        print(Fore.GREEN + '|', end="")
    if not sol[0]:
        print(Fore.BLUE + '|', end="")
    for i in range(len(sol)):
        box_i = get_str_box(grid_[0][i], box_len)
        if sol[i]:
            print(Fore.GREEN + box_i + "|", end="")
        if not sol[i]:
            print(Fore.BLUE + box_i + "|", end="")

    if sol[0]:
        print(Fore.GREEN + '\n|', end="")
    if not sol[0]:
        print(Fore.BLUE + '\n|', end="")
    for i in range(len(sol)):
        box_i = get_str_box(grid_[1][i], box_len)
        if sol[i]:
            print(Fore.GREEN + box_i + "|", end="")
        if not sol[i]:
            print(Fore.BLUE + box_i + "|", end="")
