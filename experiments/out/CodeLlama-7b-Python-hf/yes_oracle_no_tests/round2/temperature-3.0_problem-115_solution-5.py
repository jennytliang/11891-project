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
    # Approach 1: Brute Force
    # Time Complexity: O(n^2 m)
    # Space Complexity: O(1)
    # n = number of rows
    # m = number of columns
    # n = len(grid)
    # m = len(grid[0])
    # m * n = number of wells
    # m * n * bucket_capacity = number of times we need to lower the buckets
    def max_fill_brute_force(grid, bucket_capacity):
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    bucket_capacity -= 1
                    if bucket_capacity == 0:
                        ans += 1
                        bucket_capacity = bucket_capacity
        return ans

    # Approach 2: Optimized Brute Force
    # Time Complexity: O(n^2 m)
    # Space Complexity: O(1)
    def max_fill_optimized_brute_force(grid, bucket_capacity):
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    bucket_capacity -= 1
                    if bucket_capacity == 0:
                        ans += 1
                        bucket_capacity = bucket_capacity
                elif bucket_capacity != 0:
                    bucket_capacity += 1
        return ans

    # Approach 3: DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def max_fill_dp(grid, bucket_capacity):
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for i in range(m)] for j in range(n)]
       