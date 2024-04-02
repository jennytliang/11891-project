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

    # first, set-up
    if len(grid) == 0:
        return 0

    number_of_buckets = len(grid[0])
    max_level = 1000
    bucket_capacity = max_level
    
    # now, solve the problem
    rows_water = []
    number_of_buckets = len(grid[0])
    for row in grid:
        level = 0
        for value in row:
            if value == 1:
                level += 1
        if level == 0:
            return 0

        rows_water.append(level)
        
    for i in range(1, len(rows_water)):
        bucket_capacity = min(bucket_capacity, (rows_water[i-1] + rows_water[i]) // 2)
    
    # bucket_capacity *= len(rows_water)
    # print(rows_water)
    # print(bucket_capacity)
        
    min_moves = math.inf
    
    return bucket_capacity


def my_sol_00(grid, bucket_capacity):
    """
    first, calculate how much water needs to be removed
    once that's figured out, see how many "moves" need to happen
    """
    if len(grid) == 0:
        return 0

    water_levels = [1 if value==1 else 0 for value in grid[0]]
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                water_levels[j] -= 1

    move_count = 0
    total_to_empty = 0
    for row in grid:
        for col in row:
            if col == 1:
                total_to_empty += water_levels[col]
    return round(total_to_empty / bucket_capacity)



print(max_fill([[0,0,1,1], [0,