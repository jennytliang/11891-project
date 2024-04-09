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
    def max_fill(grid, capacity):
        # find the number of rows and columns in the grid
        n_rows, n_cols = len(grid), len(grid[0])
        # find the number of wells
        n_wells = n_rows * n_cols
        # find the number of buckets
        n_buckets = n_rows + n_cols - 1
        # find the number of cells in the grid
        n_cells = n_rows * n_cols

        # find the number of 1s in the grid
        n_ones = sum([sum(row) for row in grid])

        # find the number of water units in the grid
        n_water = n_ones * capacity

        # find the number of times to lower the buckets
        return math.ceil(n_water / n_cells)

    return max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)