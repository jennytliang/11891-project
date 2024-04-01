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
	Do not include these tokens in the code: # initialize variables rows
	"""
    # initialize variables rows
    rows = len(grid)
    cols = len(grid[0])

    # initialize variables ans, capacity
    ans = 0
    capacity = capacity

    # initialize variables bucket_capacity, buckets, count
    bucket_capacity = capacity
    buckets = [0 for _ in range(rows)]
    count = 0

    # initialize variables i, j
    i = 0
    j = 0

    # initialize variables max_capacity
    max_capacity = 0

    # loop through rows
    while i < rows:
        # loop through cols
        while j < cols:
            # if grid[i][j] == 1
            if grid[i][j] == 1:
                # add 1 to count
                count += 1
            # increment j
            j += 1

        # if count is greater than or equal to bucket_capacity
        if count >= bucket_capacity:
            # increment ans by 1
            ans += 1
            # set count to 0
            count = 0

        # increment i
        i += 1

        # set j to 0
        j = 0

    # return ans
    return ans

def max_fill_2(grid, capacity):
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
            grid : [[0,0,1,1], [0,0,0,0],