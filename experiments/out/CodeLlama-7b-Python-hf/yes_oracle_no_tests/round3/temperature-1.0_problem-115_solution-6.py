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
    def max_fill_helper(grid, capacity):
        """
        Helper function for max_fill
        """
        if not grid:
            return 0

        # Number of wells
        wells = len(grid)

        # Number of columns in each well
        cols = len(grid[0])

        # Number of buckets
        buckets = (wells * cols) // capacity

        # Number of rows in each bucket
        rows = capacity // cols

        if buckets == 1:
            return wells

        # Number of times buckets have to be lowered
        ans = wells

        for i in range(buckets):
            # Number of wells filled
            filled = 0

            for j in range(rows):
                # Number of filled columns in the current row
                count = 0

                for k in range(cols):
                    if i * rows + j < wells and i * rows + j >= 0:
                        count += grid[i * rows + j][k]

                filled += count

            filled = min(filled, capacity)

            ans = min(ans, math.ceil(filled / capacity))

        return ans

    def max_fill_helper2(grid, capacity):
        """
        Helper function for max_fill
        """
        if not grid:
            return 0

        # Number of wells
        wells = len(grid)

        # Number of columns in each well
        cols = len(grid[0])

        # Number of buckets
        buckets = (wells * cols) // capacity

        # Number of rows in each bucket
        rows = capacity // cols

        if buckets == 1:
            return wells

        # Number of times buckets have to be lowered
        ans = wells

        for i in range(buckets):
            # Number of wells filled
            filled = 0

            for j in range(rows):
                # Number of filled columns in the current row
                count = 0

                for k in range(cols):
