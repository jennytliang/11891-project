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
    # Approach:
    # 1. Find the wells that have water in them.
    # 2. Find the wells that have no water in them.
    # 3. For each well with no water in it:
    #    3.1. Find the nearest well with water.
    #    3.2. Calculate the number of buckets needed to empty the water.
    #    3.3. Add the number of buckets needed to the total.
    # 4. Return the total.

    # 1. Find the wells that have water in them.
    wells_with_water = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                wells_with_water.append((i,j))

    # 2. Find the wells that have no water in them.
    wells_without_water = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                wells_without_water.append((i,j))

    # 3. For each well with no water in it:
    total = 0
    for well in wells_without_water:
        # 3.1. Find the nearest well with water.
        min_distance = math.inf
        nearest_well = None
        for well_with_water in wells_with_water:
            distance = abs(well[0] - well_with_water[0]) + abs(well[1] - well_with_water[1])
            if distance < min_distance:
                min_distance = distance
                nearest_well = well_with_water
        
        # 3.2. Calculate the number of buckets needed to empty the water.
        number_of_buckets = min_distance // capacity

        # 3.3. Add the number of buckets needed to the total.
        total += number_of_buckets
    
    return total


if __