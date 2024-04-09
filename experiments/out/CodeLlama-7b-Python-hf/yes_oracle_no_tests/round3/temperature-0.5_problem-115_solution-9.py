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

    # initialize the variables
    height = len(grid)
    width = len(grid[0])
    capacity = bucket_capacity
    count = 0
    # traverse the grid
    for i in range(height):
        for j in range(width):
            # if the well is empty, skip it
            if grid[i][j] == 0:
                continue
            # if the well is full, lower the bucket
            elif grid[i][j] >= capacity:
                count += 1
            # if the well is not full, lower the bucket until it is full
            else:
                count += math.ceil(grid[i][j] / capacity)
    # return the number of times the bucket was lowered
    return count














