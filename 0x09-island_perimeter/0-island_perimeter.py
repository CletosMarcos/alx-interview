#!/usr/bin/python3
"""
Calculate the Perimeter of an Island
"""


def calculate_island_perimeter(grid):
    """
    Determines the perimeter of the island represented in the grid.
    Args:
        grid: A 2D list of integers where 0 represents water and 1 represents land.
    Returns:
        The total perimeter of the island.
    """
    
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # Check the top cell
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check the bottom cell
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check the left cell
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check the right cell
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
