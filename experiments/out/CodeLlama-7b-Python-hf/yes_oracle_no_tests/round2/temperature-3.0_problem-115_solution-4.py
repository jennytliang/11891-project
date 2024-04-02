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
	Do not include these tokens in the code: def max _ fill _ helper
	"""
    # Approach 1:
    # 1) find the total capacity of the grid
    # 2) find the maximum capacity of a row
    # 3) use the max capacity of a row to determine how many times the buckets can be lowered
    # 4) return the number of lowerings
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    # where n is the number of rows in the grid
    # and m is the number of columns in the grid

    def max_fill_helper(grid, capacity):
        # find the total capacity of the grid
        total_capacity = 0
        for row in grid:
            for well in row:
                total_capacity += well
        
        # find the maximum capacity of a row
        max_capacity = 0
        for row in grid:
            for well in row:
                if well and max_capacity < well:
                    max_capacity = well
        
        # use the max capacity of a row to determine how many times the buckets can be lowered
        return math.ceil(total_capacity / max_capacity)
    
    # find the number of times the buckets can be lowered
    return max_fill_helper(grid, capacity)

    # Approach 2:
    # 1) find the total capacity of the grid
    # 2) find the maximum capacity of a row
    # 3) use the max capacity of a row to determine how many times the buckets can be lowered
    # 4) return the number of lowerings
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    # where n is the number of rows in the grid
    # and m is the number of columns in the grid

    def max_fill_helper(grid, capacity):
        # find the total capacity of the grid
        total_capacity = 0
        for row in grid:
            for well in row:
                total_capacity += well
        
        # find the maximum capacity of a row
        max_capacity = 0