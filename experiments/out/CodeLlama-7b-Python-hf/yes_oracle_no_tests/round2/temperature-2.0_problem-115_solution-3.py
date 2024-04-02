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
    # To solve this problem, we need to understand the following:
    # 1. How many times do we need to lower the bucket?
    # 2. How many times can we lower the bucket?
    # 3. What is the maximum number of water units we can extract?
    # 4. What is the maximum number of water units we can extract at a given time?
    # 5. What is the maximum number of water units we can extract at a given row?

    # We can use the following formula to find out how many times we need to lower the bucket:
    # (max_number_of_water_units - number_of_water_units_extracted) / bucket_capacity
    # 
    # We can use the following formula to find out how many times we can lower the bucket:
    # (number_of_water_units_extracted - max_number_of_water_units) / bucket_capacity
    
    # We can use the following formula to find out the maximum number of water units we can extract:
    # max_number_of_water_units = sum(grid[i][j] for j in range(len(grid[i])) for i in range(len(grid)))

    # We can use the following formula to find out the maximum number of water units we can extract at a given time:
    # max_number_of_water_units_at_given_time = sum(grid[i][j] for j in range(len(grid[i])) for i in range(len(grid)) if j <= time)

    # We can use the following formula to find out the maximum number of water units we can extract at a given row:
    # max_number_of_water_units_at_given_row = sum(grid[i][j] for j in range(len(grid[i])) if j <= row)

    # We can use the following formula to find out the number of water units we can extract at a given time:
    # number_of_water_units_extracted_at_given_time = sum(grid[i][j] for j in range(