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
	Do not include these tokens in the code: # 1 st solution : B
	"""
    # 1 st solution : B
    # O(n) time | O(n) space
    # where n is the number of rows in grid
    def max_fill(grid, capacity):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_buckets = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_buckets += 1
                else:
                    max_buckets = max(max_buckets - 1, 0)
            if max_buckets > capacity:
                return math.ceil(max_buckets / capacity)
        return math.ceil(max_buckets / capacity)

    # 2nd solution
    # O(n) time | O(n) space
    # where n is the number of rows in grid
    def max_fill(grid, capacity):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_buckets = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_buckets += 1
                else:
                    max_buckets = max(max_buckets - 1, 0)
            if max_buckets > capacity:
                return math.ceil(max_buckets / capacity)
        return math.ceil(max_buckets / capacity)

    # 3rd solution
    # O(n) time | O(n) space
    # where n is the number of rows in grid
    def max_fill(grid, capacity):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_buckets = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_buckets += 1
               