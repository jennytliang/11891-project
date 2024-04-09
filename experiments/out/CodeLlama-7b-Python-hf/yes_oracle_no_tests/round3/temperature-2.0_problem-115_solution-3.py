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
    # Find the longest row, and set the number of buckets to that number
    # Start at the bottom left, and move right until you find a 1, and then move down and repeat
    # Keep track of the number of buckets needed to empty the wells
    # Answer is the number of times you need to lower the buckets
    # For each row, you need to find the number of buckets needed to empty it
    # For each column, you need to find the number of buckets needed to empty it

    # Find the longest row, and set the number of buckets to that number
    rows = len(grid)
    cols = len(grid[0])
    buckets = 0
    for row in grid:
        if len(row) > buckets:
            buckets = len(row)
    
    # Start at the bottom left, and move right until you find a 1, and then move down and repeat
    # Keep track of the number of buckets needed to empty the wells
    # Answer is the number of times you need to lower the buckets
    # For each row, you need to find the number of buckets needed to empty it
    # For each column, you need to find the number of buckets needed to empty it
    current_bucket_count = 0
    buckets_needed = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                current_bucket_count += 1
            else:
                if current_bucket_count > buckets_needed:
                    buckets_needed = current_bucket_count
                current_bucket_count = 0
        if current_bucket_count > buckets_needed:
            buckets_needed = current_bucket_count
        current_bucket_count = 0
    
    return math.ceil(buckets_needed / capacity)




grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 2
print(max_fill