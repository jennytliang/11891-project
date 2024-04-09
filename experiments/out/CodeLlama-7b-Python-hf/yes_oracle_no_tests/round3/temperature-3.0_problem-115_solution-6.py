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
    def max_fill_helper(grid, capacity, row_index, column_index):
        if row_index == len(grid):
            return 0
        if column_index == len(grid[0]):
            return 0
        if grid[row_index][column_index] == 0:
            return 0

        bucket_count = 0
        if column_index + capacity <= len(grid[0]) - 1:
            bucket_count += max_fill_helper(grid, capacity, row_index, column_index + 1)
        if row_index + capacity <= len(grid) - 1:
            bucket_count += max_fill_helper(grid, capacity, row_index + 1, column_index)
        if column_index - capacity >= 0:
            bucket_count += max_fill_helper(grid, capacity, row_index, column_index - 1)
        if row_index - capacity >= 0:
            bucket_count += max_fill_helper(grid, capacity, row_index - 1, column_index)

        return bucket_count + 1

    ans = 0
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            ans = max(ans, max_fill_helper(grid, column_index + 1, row_index, column_index))
    return ans


def max_fill_2(grid, capacity):
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
            bucket_capacity : 