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
    # grid -> 2D array
    # capacity -> int
    # return int

    #==================================================================
    # Time Limit Exceeded
    #==================================================================

    # O(n * m * k)
    # n -> len(grid)
    # m -> len(grid[0])
    # k -> number of buckets
    def bucket_fill(grid, capacity, buckets):
        if not grid:
            return 0
        if not buckets:
            return 0

        n = len(grid)
        m = len(grid[0])
        k = len(buckets)

        # O(n * m)
        wells = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    wells.append((i, j))

        # O(n * m)
        # Fill the buckets
        for well in wells:
            fill_bucket(grid, capacity, buckets, well)

        # O(k)
        # Count the number of buckets that are not empty
        return sum(1 for bucket in buckets if bucket)

    # O(k)
    def fill_bucket(grid, capacity, buckets, well):
        if not buckets:
            return 0

        n = len(grid)
        m = len(grid[0])
        k = len(buckets)

        # O(k)
        # Fill the bucket with water
        bucket = buckets[0]
        while bucket:
            well_row, well_col = well
            well_row -= 1
            well_col -= 1

            # O(n * m)
            # Find the first available well
            for row in range(n):
                for col in range(m):
                    if grid[row][col] == 1:
                        # O(1)
                        # Fill the well
                        grid[row][col] = 0
                        bucket -= 1

                        # O(