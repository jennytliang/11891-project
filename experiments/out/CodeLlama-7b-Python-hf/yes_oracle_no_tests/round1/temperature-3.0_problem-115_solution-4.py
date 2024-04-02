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

    def max_fill_helper(grid, capacity, row, col, bucket_capacity):
        """
        Recursively fill the grid
        """
        # base case
        if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        # if we have filled all the wells, return the number of buckets used
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1

        # fill the current well
        grid[row][col] = 0
        # fill the current well with the bucket
        filled = max(bucket_capacity, grid[row][col])
        # recursively fill the grid
        return filled + max_fill_helper(grid, filled, row+1, col, bucket_capacity) + max_fill_helper(grid, filled, row, col+1, bucket_capacity)


    # find the number of rows and cols in the grid
    rows = len(grid)
    cols = len(grid[0])

    # find the number of buckets needed to fill the grid
    num_buckets = max_fill_helper(grid, capacity, 0, 0, capacity)

    # find the number of times we need to lower the buckets
    return math.ceil(num_buckets / capacity)


if __name__ == "__main__":
    # grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # capacity = 2
    # print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))