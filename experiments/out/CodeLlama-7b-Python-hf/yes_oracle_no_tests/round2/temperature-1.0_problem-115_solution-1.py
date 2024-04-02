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
    
	Do not include these tokens in the code: # grid = [[ 0 , 0
	"""
    # Approach:
    # 1. Calculate the total number of water units.
    # 2. Calculate the number of buckets needed.
    # 3. Calculate the number of lowering operations required.
    # 4. Return the number of lowering operations.
    
    def max_fill(grid, capacity):
        # 1. Calculate the total number of water units.
        total_water = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    total_water += 1
        # 2. Calculate the number of buckets needed.
        n_buckets = math.ceil(total_water / capacity)
        # 3. Calculate the number of lowering operations required.
        n_lowerings = math.ceil(n_buckets / len(grid[0]))
        # 4. Return the number of lowering operations.
        return n_lowerings

    # Test cases:
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    return max_fill(grid, capacity)

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    return max_fill(grid, capacity)

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    return max_fill(grid, capacity)

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    return max_fill(grid, capacity)

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    return max_fill(