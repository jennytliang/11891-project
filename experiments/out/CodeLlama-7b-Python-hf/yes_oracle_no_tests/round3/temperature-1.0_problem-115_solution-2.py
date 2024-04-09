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
    # approach: dynamic programming
    # memory: O(n)
    # runtime: O(n)
    # n = rows * columns
    def max_fill(grid, capacity):
        # initialize variables
        rows, columns = len(grid), len(grid[0])
        buckets = math.ceil(rows / capacity)
        # create buckets
        buckets = [0] * buckets
        # initialize buckets
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    buckets[i % buckets] += 1
        # fill wells
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    buckets[(i + 1) % buckets] -= 1
                    buckets[i % buckets] += 1
        # output answer
        return buckets.count(0)

    return max_fill(grid, capacity)
