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
    def max_fill_helper(grid, capacity, row_count, col_count, i, j):
        """
        Helper function for calculating the number of times we need to lower
        the buckets.
        """
        if i >= row_count or j >= col_count:
            return 0

        if grid[i][j] == 1:
            return 1 + max_fill_helper(grid, capacity, row_count, col_count, i, j + 1)
        else:
            return max_fill_helper(grid, capacity, row_count, col_count, i + 1, j)

    def max_fill_helper_2(grid, capacity, row_count, col_count, i, j):
        """
        Helper function for calculating the number of times we need to lower
        the buckets.
        """
        if i >= row_count or j >= col_count:
            return 0

        if grid[i][j] == 1:
            return 1 + max_fill_helper_2(grid, capacity, row_count, col_count, i, j + 1)
        elif grid[i][j] == 0:
            return max_fill_helper_2(grid, capacity, row_count, col_count, i + 1, j)

    row_count = len(grid)
    col_count = len(grid[0])
    total_water = 0
    for i in range(row_count):
        for j in range(col_count):
            total_water += grid[i][j]

    if total_water <= capacity:
        return 0

    # Use the helper function to calculate the number of times we need to lower
    # the buckets.
    return math.ceil(total_water / capacity)


if __name__ == "__main__":
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    capacity = 1
    print(max_fill_helper(