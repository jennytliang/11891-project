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
    
	Do not include these tokens in the code: # grid : [[ 0 , 0
	"""
    def get_total_water(grid, capacity):
        total_water = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total_water += 1
        return total_water

    def get_max_water(grid, capacity):
        max_water = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_water += 1
                elif grid[i][j] == 0:
                    max_water -= 1
        return max_water

    def get_bucket_count(grid, capacity):
        bucket_count = 0
        for i in range(len(grid)):
            if grid[i][0] == 1:
                bucket_count += 1
        return bucket_count

    def get_grid_length(grid):
        return len(grid)

    def get_wells_length(grid):
        return len(grid[0])

    def get_wells_count(grid):
        return get_grid_length(grid) * get_wells_length(grid)

    def get_wells_count_with_water(grid):
        wells_count = get_wells_count(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    wells_count -= 1
        return wells_count

    def get_water_per_bucket(grid, capacity):
        max_water = get_max_water(grid, capacity)
        return math.ceil(max_water / get_bucket_count(grid, capacity))

    def get_buckets_needed(grid, capacity):
        return get_water_per_bucket(grid, capacity) * get_bucket_count(grid, capacity)

    def get_buckets_needed_