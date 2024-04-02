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
    n_rows = len(grid)
    n_cols = len(grid[0])

    # Create a new array to hold the number of water units in each well.
    # We will use this to track the amount of water in each well.
    # Initialize each well to zero.
    n_water = []
    for i in range(n_rows):
        n_water.append([0 for j in range(n_cols)])

    # Fill the n_water array with the number of water units in each well.
    # Each row corresponds to a well, and each column corresponds to a bucket.
    # The value in the n_water array at [i][j] represents the number of water
    # units that can be taken from well i and put into bucket j.
    # The value at [i][j] is equal to the number of units in well i, 
    # minus the number of units in the left well, plus the number of units in 
    # the right well.
    for i in range(n_rows):
        for j in range(n_cols):
            if j == 0:
                n_water[i][j] = grid[i][j]
            else:
                n_water[i][j] = n_water[i][j - 1] + grid[i][j]

    # Create a new array to hold the number of times we need to lower a bucket.
    # We will use this to track how many times we need to lower a bucket to
    # empty the grid.
    # Initialize each well to zero.
    n_lowers = []
    for i in range(n_rows):
        n_lowers.append([None for j in range(n_cols)])

    # Fill the n_lowers array with the number of times to lower a bucket.
    # Each row corresponds to a well, and each column corresponds to a bucket.
    # The value in the n_lowers array at [i][j] represents the number of times
    # we need to lower bucket j in order to empty well i.
    # The value at [i][j] is equal to the