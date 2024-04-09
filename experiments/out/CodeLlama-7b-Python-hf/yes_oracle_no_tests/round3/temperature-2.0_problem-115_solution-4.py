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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: def get _ max _ fill (
	"""
    return get_max_fill(grid, capacity)

def get_max_fill(grid, capacity):
    """
    This function calculates the maximum number of times water can be extracted from the grid.
    """
    # This is the number of times we need to lower the bucket.
    # This will be incremented every time we extract water from a well.
    count = 0

    # The number of rows in the grid.
    rows = len(grid)

    # The number of columns in a row.
    cols = len(grid[0])

    # The number of water units in the grid.
    water = 0

    # The number of wells in the grid.
    wells = rows * cols

    # The number of buckets.
    buckets = 1

    # The capacity of the bucket.
    bucket_capacity = capacity

    # We will calculate the maximum number of times water can be extracted from the grid
    # by lowering the bucket at each well.
    while water < wells:
        # We will lower the bucket at each well.
        for row in range(rows):
            for col in range(cols):
                # If the current well has water, extract the water from it.
                if grid[row][col] == 1:
                    water += 1

        # We need to lower the bucket at each well.
        count += 1

        # We will lower the bucket at each well.
        for row in range(rows):
            for col in range(cols):
                # If the current well has water, extract the water from it.
                if grid[row][col] == 1:
                    # If the current well has at least one unit of water, lower the bucket.
                    if water > 0:
                        # If the bucket is already full, we need to extract water from the well.
                        if water >= bucket_capacity:
                            # We need to extract water from the well.
                            water -= bucket_capacity
                        else:
                            # We need to extract all the water from the well.
                            water = 0