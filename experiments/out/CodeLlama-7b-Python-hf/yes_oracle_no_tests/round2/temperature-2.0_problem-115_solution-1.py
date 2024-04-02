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
	Do not include these tokens in the code: def count _ bu ckets ( grid
	"""
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    def count_buckets(grid, capacity):
        """
        Count the number of buckets required to empty the grid
        """
        # initialize variables
        buckets = 0
        rows = len(grid)
        cols = len(grid[0])

        # iterate over each row
        for i in range(rows):
            # iterate over each column
            for j in range(cols):
                # if the current cell is a 1, add a bucket
                if grid[i][j] == 1:
                    buckets += 1
                # if the current cell is a 0, subtract a bucket
                elif grid[i][j] == 0:
                    buckets -= 1
                # if the current cell is a 0, and the number of buckets is less than 0
                # then add a bucket
                if buckets < 0:
                    buckets += 1
        return buckets

    def max_fill(grid, capacity):
        """
        Find the maximum number of buckets required to empty the grid
        """
        # initialize variables
        buckets = 0
        rows = len(grid)
        cols = len(grid[0])
        max_buckets = 0

        # iterate over each row
        for i in range(rows):
            # iterate over each column
            for j in range(cols):
                # if the current cell is a 1, add a bucket
                if grid[i][j] == 1:
                    buckets += 1
                # if the current cell is a 0, subtract a bucket
                elif grid[i][j] == 0:
                    buckets -= 1
                # if the number of buckets is greater than the max buckets,
                # update the max buckets
                if buckets > max_buckets:
                    max_buckets = buckets
        return max_buckets

    # initialize variables
    buckets = 0
    rows = len(grid)
    cols = len(grid[