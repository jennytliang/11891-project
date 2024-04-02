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
    # 1st approach: brute force
    # time complexity: O(NM) where N is the number of rows in grid and M is the number of columns in grid
    # space complexity: O(1)
    def max_fill_brute(grid, capacity):
        buckets = capacity
        ans = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    buckets += 1
                elif row[i] == 0:
                    buckets -= 1
                if buckets < 0:
                    buckets = 0
                    ans += 1
        return ans

    # 2nd approach: dp
    # time complexity: O(NM) where N is the number of rows in grid and M is the number of columns in grid
    # space complexity: O(NM)
    def max_fill_dp(grid, capacity):
        buckets = capacity
        ans = 0
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    buckets += 1
                elif grid[i][j] == 0:
                    buckets -= 1
                if buckets < 0:
                    buckets = 0
                    ans += 1
                dp[i][j] = buckets
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] == 1:
                    buckets += 1
                elif grid[i][j] == 0:
                    buckets -= 1
                if buckets < 0:
                    buckets = 0
                    ans += 1
                dp[i][j] = buckets
        for i in range(len(grid) -