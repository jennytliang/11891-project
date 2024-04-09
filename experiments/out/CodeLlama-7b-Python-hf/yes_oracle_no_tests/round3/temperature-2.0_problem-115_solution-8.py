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
	Do not include these tokens in the code: def get _ total _ water (
	"""
    # The approach to this problem is to first find out the total water
    # that is available in the grid. Then, we will use the capacity of the
    # buckets to determine how many times the buckets need to be lowered.
    # We then return the number of times the buckets need to be lowered.
    #
    # To find out the total water available in the grid, we will use the
    # following formula:
    #
    # Total Water = (Total Water in Rows) - (Total Water in Columns)
    #
    # The total water in each row can be found by adding the number of
    # units of water in each row.
    #
    # The total water in each column can be found by multiplying the
    # number of units of water in each column by the number of rows.
    #
    # The total water in the grid is then equal to the total water in
    # the rows minus the total water in the columns.
    #
    # To determine the number of times the buckets need to be lowered,
    # we will find the difference between the total water in the grid
    # and the total water that can be extracted from the grid. We will
    # then divide this difference by the capacity of the buckets.
    #
    # To find the total water that can be extracted from the grid, we
    # will multiply the number of units of water in each column by the
    # number of rows.
    #
    # To find the number of units of water in each column, we will find
    # the maximum value in each column.
    #
    # To find the number of units of water in each row, we will find the
    # maximum value in each row.
    #
    # To find the number of rows, we will use the length of the grid.
    #
    # To find the number of columns, we will use the length of the first
    # row.
    #
    # To find the maximum value in a column, we will iterate through each
    # column. We will find the maximum value in the current column by
    # iterating through each row and comparing it to the maximum value of
    # the current