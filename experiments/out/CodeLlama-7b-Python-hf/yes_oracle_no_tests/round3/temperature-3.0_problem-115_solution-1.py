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
    # 1st solution: dp
    # O(n*m) time | O(n*m) space
    # n, m -> row, col of grid
    def max_fill(self, grid, capacity):
        n, m = len(grid), len(grid[0])
        dp = [[math.inf for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = min(dp[i][j-1] + 1 if j > 0 else 1, dp[i-1][j] + 1 if i > 0 else 1)
                else:
                    dp[i][j] = 0
        return dp[n-1][m-1]

    # 2nd solution: dp
    # O(n*m) time | O(min(n, m)) space
    # n, m -> row, col of grid
    def max_fill(self, grid, capacity):
        n, m = len(grid), len(grid[0])
        dp = [1] * min(n, m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[j] += 1
        return sum(dp) - min(dp) if len(dp) == n else sum(dp) - min(dp[:len(dp)//2])

    # 3rd solution: dp
    # O(n*m) time | O(1) space
    # n, m -> row, col of grid
    def max_fill(self, grid, capacity):
        n, m = len(grid), len(grid[0])
        i, j = 0, 0
        count = 0
        while i < n and j < m:
            if grid[i][j] == 1:
                count += 1
