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
    
	Do not include these tokens in the code: # Initial ization rows =
	"""
    def max_fill_helper(grid, capacity, i, j):
        """
        Helper function to compute the max number of times the buckets can be lowered to empty all wells.
        """
        # base cases
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        
        # check if we have reached a well
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        
        # check if we have reached a bucket
        if i == len(grid) - 1:
            return max_fill_helper(grid, capacity, i, j + 1)
        if j == len(grid[0]) - 1:
            return max_fill_helper(grid, capacity, i + 1, j)
        
        # check if we have reached a water unit
        if grid[i][j] == 1:
            return max(max_fill_helper(grid, capacity, i, j + 1), max_fill_helper(grid, capacity, i + 1, j))
        
        # if we have reached here, we have a bucket and a water unit
        # if we can empty the well with 1 bucket, we return 1
        if grid[i][j] <= capacity:
            return 1
        # if we can empty the well with 2 buckets, we return 2
        elif grid[i][j] <= 2 * capacity:
            return 2
        # otherwise, we lower both buckets and check again
        else:
            return 1 + max_fill_helper(grid, capacity, i + 1, j) + max_fill_helper(grid, capacity, i, j + 1)
    
    # calculate the max number of times we can lower the buckets to empty all wells
    return max_fill_helper(grid, capacity, 0, 0)


























