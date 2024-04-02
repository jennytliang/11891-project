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
    # grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # bucket_capacity : 1

    # ans = 6

    # grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # bucket_capacity : 2

    # ans = 5

    # grid : [[0,0,0], [0,0,0]]
    # bucket_capacity : 5

    # ans = 0

    def get_min_buckets(grid, bucket_capacity):
        """
        Finds the minimum number of buckets needed to empty the grid
        """
        wells = len(grid)
        rows = len(grid[0])
        buckets = 0
        for i in range(wells):
            for j in range(rows):
                if grid[i][j] == 1:
                    buckets += math.ceil((rows - j) / bucket_capacity)
        return buckets

    def get_min_buckets_with_bucket_capacity(grid, bucket_capacity):
        """
        Finds the minimum number of buckets needed to empty the grid
        """
        wells = len(grid)
        rows = len(grid[0])
        buckets = 0
        for i in range(wells):
            for j in range(rows):
                if grid[i][j] == 1:
                    buckets += math.ceil((rows - j) / bucket_capacity)
                    bucket_capacity -= 1
                    if bucket_capacity == 0:
                        return buckets + 1
        return buckets

    def get_min_buckets_with_bucket_capacity_2(grid, bucket_capacity):
        """
        Finds the minimum number of buckets needed to empty the grid
        """
        wells = len(grid)
        rows = len(grid[0])
        buckets