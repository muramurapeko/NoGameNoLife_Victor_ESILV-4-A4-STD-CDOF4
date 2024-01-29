import os
import random
import time

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


def display_grid(grid):
    for row in grid:
        for cell in row:
            print("■" if cell else " ", end="")
            print(" ", end="")
        print()


def get_neighbour_count(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
                count += grid[row + i][col + j]
    return count

def update_grid(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count = get_neighbour_count(grid, row, col)
            if grid[row][col] == 1:
                if count < 2 or count > 3:
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 1
            else:
                if count == 3:
                    new_grid[row][col] = 1
    return new_grid

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(rows, cols, generations, delay):
    grid = create_grid(rows, cols)
    for _ in range(generations):
        clear_console()
        display_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

# Example usage
main(rows=40, cols=80, generations=100, delay=0.1)