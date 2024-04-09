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
	Do not include these tokens in the code: # Define the maximum number of bu
	"""
    # Brute force solution
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    # n = len(grid)
    # ans = math.inf
    # for i in range(n):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             # Empty the well
    #             for k in range(n):
    #                 if grid[i][k] == 1:
    #                     grid[i][k] = 0
    #                     grid[k][j] = 0
    #                     if sum(grid[i]) == 0 and sum(grid[k]) == 0:
    #                         ans = min(ans, 1)
    #                     else:
    #                         ans = min(ans, 2)
    # return ans

    # DP solution
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    n = len(grid)
    dp = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # Empty the well
                dp[i][j] = 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # Empty the well
                for k in range(n):
                    if grid[i][k] == 1:
                        dp[i][j] = min(dp[i][j], dp[k][j] + 1)
    return min(dp[i][j] for i in range(n) for j in range(n) if grid[i][j] == 1)




if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
