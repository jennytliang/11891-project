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
        height, width = len(grid), len(grid[0])
        # we use a 2d array to represent the buckets
        # we use a 1d array to represent the water
        buckets = [[0 for _ in range(width)] for _ in range(height)]
        water = [0] * width

        # fill the buckets
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    buckets[i][j] += 1
                    water[j] += 1

        # lower the buckets
        times = 0
        for i in range(height):
            for j in range(width):
                if water[j] > 0:
                    times += 1
                    water[j] -= capacity
                    if water[j] < 0:
                        buckets[i][j] += water[j]
                        water[j] = 0

        # lower the buckets
        for i in range(height):
            for j in range(width):
                if buckets[i][j] > capacity:
                    times += buckets[i][j] // capacity
                    buckets[i][j] %= capacity
                elif buckets[i][j] > 0:
                    times += 1
                    buckets[i][j] = 0

        return times

    # O(n^2) solution
    def max_fill_helper_2(grid, capacity):
        """
        Helper function for max_fill
        """
        height, width = len(grid), len(grid[0])
        # we use a 2d array to represent the buckets
        # we use a 1d array to represent the water
        buckets = [[0 for _ in range(width)] for _ in range(height)]
        water = [0] * width

        # fill the buckets
        for i in range(height):
           