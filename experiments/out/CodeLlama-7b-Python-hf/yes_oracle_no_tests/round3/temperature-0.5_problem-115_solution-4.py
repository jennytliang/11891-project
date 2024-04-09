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
    # time O(n*m)
    # space O(1)

    def get_water_sum(grid, capacity):
        """
        Get the total amount of water that can be collected.
        """
        # time O(n*m)
        # space O(n)
        n = len(grid)
        m = len(grid[0])
        buckets = [0] * n
        water = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buckets[i] += 1
            water += min(buckets[i], capacity)
        return water

    def get_water_sum_optimized(grid, capacity):
        """
        Get the total amount of water that can be collected.
        """
        # time O(n*m)
        # space O(n)
        n = len(grid)
        m = len(grid[0])
        buckets = [0] * n
        water = 0
        left = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buckets[i] += 1
            left = max(left, buckets[i])
            water += min(buckets[i], capacity)
        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                if grid[i][j] == 1:
                    buckets[i] += 1
            water += min(buckets[i], capacity)
        return water

    def get_water_sum_optimized_2(grid, capacity):
        """
        Get the total amount of water that can be collected.
        """
        # time O(n*m)
        # space O(n)
        n = len(grid)
        m = len(grid[0])
        buckets = [0] * n
        left = 0
        water = 0
        for i