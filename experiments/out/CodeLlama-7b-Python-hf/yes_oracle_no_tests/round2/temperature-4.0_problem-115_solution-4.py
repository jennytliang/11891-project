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
    # ANSWER
    # for each row, find the max water that can be extracted from that row
    # then, find the max water that can be extracted from the grid
    # if the max water from the grid is less than the capacity,
    # then we need to lower the bucket
    # else don't need to lower the bucket

    # init variables
    n_rows = len(grid)
    max_water = 0
    bucket_capacity = capacity

    # loop through each row
    for row_num, row in enumerate(grid):
        # find the max water that can be extracted from that row
        max_water_row = 0
        left_pointer = 0
        right_pointer = len(row) - 1
        while left_pointer < right_pointer:
            # find the max water that can be extracted from that row
            # and update the max_water_row
            if row[left_pointer] > row[right_pointer]:
                max_water_row += row[right_pointer]
                right_pointer -= 1
            else:
                max_water_row += row[left_pointer]
                left_pointer += 1
        # update max_water
        max_water += max_water_row
    
    # find the max water that can be extracted from the grid
    max_water_grid = math.floor(max_water / bucket_capacity)

    # if the max water from the grid is less than the capacity,
    # then we need to lower the bucket
    if max_water_grid < n_rows:
        return n_rows - max_water_grid
    return 0

    # ANOTHER SOLUTION
    # for each row, find the max water that can be extracted from that row
    # then, find the max water that can be extracted from the grid
    # if the max water from the grid is less than the capacity,
    # then we need to lower the bucket
    # else don't need to lower the bucket

    # init variables
    n_rows = len(grid)
    max_water = 0
    bucket_cap