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
	Do not include these tokens in the code: def get _ bucket _ count
	"""
    def get_bucket_count(grid):
        bucket_count = 0
        for row in grid:
            for well in row:
                if well == 1:
                    bucket_count += 1
        return bucket_count

    def get_water_count(grid):
        water_count = 0
        for row in grid:
            for well in row:
                if well == 1:
                    water_count += 1
        return water_count

    def get_bucket_water_count(grid, bucket_count):
        bucket_water_count = 0
        for row in grid:
            for well in row:
                if well == 1 and bucket_water_count < bucket_count:
                    bucket_water_count += 1
        return bucket_water_count

    def get_max_bucket_water_count(grid, bucket_count):
        max_bucket_water_count = 0
        for row in grid:
            for well in row:
                if well == 1:
                    max_bucket_water_count += 1
                else:
                    max_bucket_water_count -= 1
        return max_bucket_water_count

    def get_bucket_water_count_for_row(grid, bucket_count, row_index):
        bucket_water_count = 0
        for well in grid[row_index]:
            if well == 1 and bucket_water_count < bucket_count:
                bucket_water_count += 1
        return bucket_water_count

    def get_bucket_water_count_for_column(grid, bucket_count, col_index):
        bucket_water_count = 0
        for row in grid:
            if row[col_index] == 1 and bucket_water_count < bucket_count:
                bucket_water_count += 1
        return bucket_water_count

    def get_bucket_water_count_for_diagonal(grid, bucket_count, row_index, col_index):
        bucket_water_count = 0
        for i in range