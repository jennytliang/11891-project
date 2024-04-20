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

    # grid[i][j] -> (0, 1)
    # 0 -> empty
    # 1 -> water

    # 1. Find the number of wells
    # 2. Find the number of buckets
    # 3. Find the capacity of the buckets
    # 4. Find the wells that are empty
    # 5. Find the wells that are full
    # 6. Count the number of times we need to lower the buckets

    # 1. Find the number of wells
    num_wells = len(grid)

    # 2. Find the number of buckets
    num_buckets = num_wells

    # 3. Find the capacity of the buckets
    bucket_capacity = capacity

    # 4. Find the wells that are empty
    empty_wells = []
    for i in range(num_wells):
        for j in range(num_wells):
            if grid[i][j] == 0:
                empty_wells.append([i, j])

    # 5. Find the wells that are full
    full_wells = []
    for i in range(num_wells):
        for j in range(num_wells):
            if grid[i][j] == 1:
                full_wells.append([i, j])

    # 6. Count the number of times we need to lower the buckets
    num_buckets_needed = math.ceil(len(full_wells) / num_buckets)

    return num_buckets_needed