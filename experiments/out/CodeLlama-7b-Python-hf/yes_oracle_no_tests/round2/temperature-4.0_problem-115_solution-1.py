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
    def get_row_sum(row):
        return sum(row)

    def get_col_sum(grid, col):
        return sum([row[col] for row in grid])

    def get_row_buckets(row, bucket_capacity):
        bucket_count = 0
        buckets = 0
        for cell in row:
            if cell == 1:
                buckets += 1
            else:
                bucket_count += buckets
                buckets = 0
        bucket_count += buckets
        return bucket_count

    def get_col_buckets(grid, col, bucket_capacity):
        bucket_count = 0
        buckets = 0
        for row in grid:
            cell = row[col]
            if cell == 1:
                buckets += 1
            else:
                bucket_count += buckets
                buckets = 0
        bucket_count += buckets
        return bucket_count

    def get_bucket_count(grid, bucket_capacity):
        row_bucket_count = 0
        col_bucket_count = 0
        for row in grid:
            row_bucket_count += get_row_buckets(row, bucket_capacity)
        for col in range(len(grid[0])):
            col_bucket_count += get_col_buckets(grid, col, bucket_capacity)
        return max(row_bucket_count, col_bucket_count)

    def get_max_buckets(grid, bucket_capacity):
        row_sums = [get_row_sum(row) for row in grid]
        col_sums = [get_col_sum(grid, col) for col in range(len(grid[0]))]
        max_buckets = 0
        for row_sum in row_sums:
            max_buckets = max(max_buckets, math.ceil(row_sum / bucket_capacity))
        for col_sum in col_sums:
            max_buckets = max(max_buckets, math.ceil(col