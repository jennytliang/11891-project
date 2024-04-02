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
    height = len(grid)
    width = len(grid[0])
    capacity = bucket_capacity

    # Get the number of wells with water
    wells = sum([sum(row) for row in grid])

    # If there are no wells, we don't need to do anything
    if wells == 0:
        return 0

    # We don't need to extract all the water, so we can just return 0
    if wells <= capacity:
        return 0

    # The number of buckets needed is just the number of wells
    buckets = wells

    # The number of times we need to lower the buckets is the floor of the log of the number of wells
    times_needed = math.floor(math.log(wells, 2))

    # Return the number of buckets needed
    return buckets



