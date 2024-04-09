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
    def get_bucket_count(grid, bucket_capacity):
        bucket_count = 0
        for row in grid:
            for col in row:
                if col == 1:
                    bucket_count += 1
        return bucket_count

    def get_bucket_wastage(grid, bucket_capacity):
        bucket_wastage = 0
        for row in grid:
            bucket_wastage += sum(row)
        return bucket_wastage

    def get_bucket_wastage_per_bucket(grid, bucket_capacity):
        bucket_wastage_per_bucket = 0
        for row in grid:
            bucket_wastage_per_bucket += sum(row) / bucket_capacity
        return bucket_wastage_per_bucket

    def get_bucket_wastage_per_bucket_rounded(grid, bucket_capacity):
        bucket_wastage_per_bucket = get_bucket_wastage_per_bucket(grid, bucket_capacity)
        return math.ceil(bucket_wastage_per_bucket)

    def get_bucket_count_for_rounded_bucket_wastage(grid, bucket_capacity, rounded_bucket_wastage):
        bucket_count = 0
        bucket_wastage = 0
        for row in grid:
            for col in row:
                if col == 1:
                    bucket_count += 1
                else:
                    bucket_wastage += 1
                if bucket_wastage >= rounded_bucket_wastage:
                    return bucket_count
        return bucket_count

    def get_minimum_bucket_count(grid, bucket_capacity):
        bucket_wastage = get_bucket_wastage(grid, bucket_capacity)
        bucket_wastage_per_bucket = get_bucket_wastage_per_bucket(grid, bucket_capacity)
        rounded_bucket_wastage = get_bucket_wastage_per_bucket_rounded(grid, bucket_