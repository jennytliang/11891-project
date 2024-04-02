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
        """
        Time: O(R*C)
        Space: O(R*C)
        """
        R, C = len(grid), len(grid[0])
        # dp[i][j] is the minumum number of buckets needed to empty the wells
        # starting from grid[i][j]
        dp = [[math.inf for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                    
        # find the minimum number of buckets needed to empty all wells
        min_buckets = math.inf
        for j in range(C):
            if dp[-1][j] != math.inf:
                min_buckets = min(min_buckets, dp[-1][j])
        if min_buckets <= capacity:
            return min_buckets
        else:
            return -1

    def max_fill_2(grid, capacity):
        """
        Time: O(R*C)
        Space: O(1)
        """
        R, C = len(grid), len(grid[0])
        # dp[i][j] is the minumum number of buckets needed to empty the wells
        # starting from grid[i][j]
        dp = [[math.inf for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    dp[i][j] = 0
               