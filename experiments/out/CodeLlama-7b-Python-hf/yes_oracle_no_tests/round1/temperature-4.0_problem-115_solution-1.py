import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    
	Include these tokens in the code: ans =
	"""
    def print_grid(grid):
        for row in grid:
            print(row)
        print()

    def max_fill_helper(grid, capacity):
        """
        Helper for max_fill.
        """
        if len(grid) == 0:
            return 0
        elif len(grid) == 1:
            return sum(grid[0])
        else:
            rows = len(grid)
            cols = len(grid[0])
            # print_grid(grid)
            # print(f"capacity = {capacity}")
            # print(f"rows = {rows}")
            # print(f"cols = {cols}")

            # Fill the first row
            if grid[0][0] == 1:
                grid[0][0] = capacity
            # print_grid(grid)
            # print()

            # Fill the first column
            if grid[0][0] == 1:
                for i in range(1, rows):
                    grid[i][0] = min(grid[i][0], grid[i-1][0])
            # print_grid(grid)
            # print()

            # Fill the rest of the grid
            for i in range(1, rows):
                for j in range(1, cols):
                    if grid[i][j] == 1:
                        grid[i][j] = min(grid[i-1][j], grid[i][j-1])
            # print_grid(grid)
            # print()

            # Count the number of times the buckets need to be lowered
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        count += 1
            # print(f"count = {count}")
            # print()

            return count

    def max_fill_helper_2(grid, capacity):
        """
        Helper for max_fill.
        """
        if len(grid) == 0:
            return 0
       