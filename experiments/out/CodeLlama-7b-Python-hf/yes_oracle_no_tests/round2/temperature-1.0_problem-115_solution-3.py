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

    # generate buckets
    rows = len(grid)
    cols = len(grid[0])
    water = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                water += 1

    print(f"initial amount of water: {water}")

    bucket_capacity = capacity
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                continue

            col_water =  min(bucket_capacity, water)
            bucket_capacity -= col_water
            water -= col_water
            grid[row][col] = 0
            # print(f"{col_water} units dropped into {row},{col}")

        # print(f"bucket capacity: {bucket_capacity}\n")

    return math.ceil(water / bucket_capacity)
                

def max_fill(grid, capacity):

    # generate buckets
    rows = len(grid)
    cols = len(grid[0])
    water = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                water += 1
            elif water:
                grid[row][col] = 1
                water -= 1
    return math.ceil(water/(rows * capacity))

def main():
    # grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    # grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    # grid = [[0,0,0], [0,0,0]]
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
   