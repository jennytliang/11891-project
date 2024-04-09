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
    # Approach 1: Brute Force
    # Time Limit Exceeded
    def brute_force(grid, capacity):
        # get the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        # get the number of wells
        wells = rows * cols
        # get the number of buckets
        buckets = wells // capacity
        # get the number of moves
        moves = math.inf
        for _ in range(buckets):
            # get the number of moves for each bucket
            moves = min(moves, brute_force_helper(grid, capacity))
        return moves

    def brute_force_helper(grid, capacity):
        # get the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        # get the number of wells
        wells = rows * cols
        # get the number of buckets
        buckets = wells // capacity
        # get the number of moves
        moves = math.inf
        for i in range(buckets):
            # get the number of moves for each bucket
            moves = min(moves, brute_force_helper_helper(grid, capacity, i))
        return moves

    def brute_force_helper_helper(grid, capacity, bucket):
        # get the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        # get the number of wells
        wells = rows * cols
        # get the number of buckets
        buckets = wells // capacity
        # get the number of moves
        moves = math.inf
        # get the number of units in the bucket
        units = 0
        # get the number of wells filled
        filled = 0
        # get the row index
        row = bucket // cols
        # get the column index
        col = bucket % cols
        # get the number of units in the bucket
        units = sum(grid[row][col:col + capacity])
        # get the number of units in the wells
        filled = sum(grid[row])
        #