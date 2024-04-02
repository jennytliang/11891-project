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
    # grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # capacity = 1
    # print(max_fill(grid, capacity))
    
    def lower_buckets(grid, capacity):
        # get the row length
        row_length = len(grid[0])
        # count the number of 1s in the grid
        ones_count = sum([sum(row) for row in grid])
        # get the number of buckets required to empty the grid
        buckets_count = math.ceil(ones_count / capacity)
        # count the number of times we need to lower the buckets
        lower_count = 0
        for row in grid:
            # get the number of ones in the row
            ones = sum(row)
            # count the number of times we need to lower the buckets
            lower_count += ones // capacity
            # get the number of ones that are not filled
            empty = ones % capacity
            # get the number of empty spaces in the row
            empty_spaces = row_length - ones
            # if the number of empty spaces is less than the number of empty ones, 
            # then we need to lower the buckets
            if empty_spaces < empty:
                lower_count += 1
        return lower_count
    
    # get the number of buckets required to empty the grid
    buckets_count = sum([sum(row) for row in grid])
    # count the number of times we need to lower the buckets
    lower_count = 0
    # count the number of times we need to lower the buckets
    lower_count = lower_buckets(grid, capacity)
    return lower_count


grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
print(max_fill(grid, capacity))

grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 