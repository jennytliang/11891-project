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
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: if not grid or not grid [ 0 ]:
	"""

    # --------------------------------------------------------------------------
    # If we are given an empty grid, we can't do anything.
    # --------------------------------------------------------------------------
    if not grid:
        return 0

    # --------------------------------------------------------------------------
    # If we are given a grid of all zeros, we can't do anything.
    # --------------------------------------------------------------------------
    if not any(grid):
        return 0

    # --------------------------------------------------------------------------
    # We'll be counting the number of times we lower the bucket.
    # --------------------------------------------------------------------------
    count = 0

    # --------------------------------------------------------------------------
    # We'll be using the capacity to make sure we don't over-fill a bucket.
    # --------------------------------------------------------------------------
    capacity = capacity

    # --------------------------------------------------------------------------
    # We'll be using the max_count to keep track of the maximum number of 
    # times we've had to lower the bucket.
    # --------------------------------------------------------------------------
    max_count = 0

    # --------------------------------------------------------------------------
    # We'll be using the row_offset to keep track of the number of rows we've
    # already processed.
    # --------------------------------------------------------------------------
    row_offset = 0

    # --------------------------------------------------------------------------
    # We'll be using the col_offset to keep track of the number of columns we've
    # already processed.
    # --------------------------------------------------------------------------
    col_offset = 0

    # --------------------------------------------------------------------------
    # We'll be using the max_col to keep track of the maximum number of columns
    # we've processed.
    # --------------------------------------------------------------------------
    max_col = len(grid[0])

    # --------------------------------------------------------------------------
    # We'll be using the max_row to keep track of the maximum number of rows
    # we've processed.
    # --------------------------------------------------------------------------
    max_row = len(grid)

    #