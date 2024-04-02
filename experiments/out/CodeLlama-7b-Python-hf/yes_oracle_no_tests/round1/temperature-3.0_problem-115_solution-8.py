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
    # 1st solution: BFS
    # O(mn) time | O(mn) space
    def max_fill_bfs(grid, capacity):
        rows, cols = len(grid), len(grid[0])
        max_water = 0
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
        while queue:
            curr_level = len(queue)
            max_water += curr_level * capacity
            for _ in range(curr_level):
                row, col = queue.pop(0)
                for (row_offset, col_offset) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + row_offset, col + col_offset
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = 1
        return max_water

    # 2nd solution: DP
    # O(mn) time | O(mn) space
    def max_fill_dp(grid, capacity):
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_water = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dp[i][j] = capacity
                else:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                    if j == 0:
                        dp[i][j] = 0
                    else:
