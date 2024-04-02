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
    def max_fill_helper(grid, bucket_capacity, i, j):
        if i == len(grid) or j == len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1

        cur_bucket_capacity = bucket_capacity - grid[i][j]
        if cur_bucket_capacity < 0:
            return math.inf

        min_water = min(
            max_fill_helper(grid, bucket_capacity, i + 1, j - 1),
            max_fill_helper(grid, bucket_capacity, i + 1, j),
            max_fill_helper(grid, bucket_capacity, i + 1, j + 1),
            max_fill_helper(grid, bucket_capacity, i, j - 1),
            max_fill_helper(grid, bucket_capacity, i, j + 1),
            max_fill_helper(grid, bucket_capacity, i - 1, j - 1),
            max_fill_helper(grid, bucket_capacity, i - 1, j),
            max_fill_helper(grid, bucket_capacity, i - 1, j + 1),
        )

        return min_water + 1

    return max_fill_helper(grid, bucket_capacity, 0, 0)


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    print(max_fill(grid, bucket_capacity))
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    bucket_capacity = 2
    print(max_fill(grid, bucket_capacity))
    grid =