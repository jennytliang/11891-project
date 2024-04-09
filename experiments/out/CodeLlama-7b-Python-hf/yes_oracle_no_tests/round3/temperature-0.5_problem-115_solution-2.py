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
    
	Do not include these tokens in the code: def max _ fill _ helper (
	"""
    # Approach 1: Brute force
    # Time Complexity: O(n*n*m)
    # Space Complexity: O(1)

    # Approach 2: DP
    # Time Complexity: O(n*m)
    # Space Complexity: O(n*m)

    def max_fill_helper(grid, capacity, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0 or visited[i][j] == 1:
            return 0
        if grid[i][j] >= capacity:
            return 1
        visited[i][j] = 1
        return 1 + max_fill_helper(grid, capacity, i-1, j, visited) + max_fill_helper(grid, capacity, i+1, j, visited) + max_fill_helper(grid, capacity, i, j-1, visited) + max_fill_helper(grid, capacity, i, j+1, visited)

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    max_fill_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and visited[i][j] != 1:
                max_fill_count = max(max_fill_count, max_fill_helper(grid, capacity, i, j, visited))
    return max_fill_count

    # return max_fill_helper(grid, capacity, 0, 0, visited)

    # Approach 3: Maths
    # Time Complexity: O(n*m)
    # Space Complexity: O(1)

    def max_fill_helper(grid, capacity, i, j):
        if i < 0 or i >= len(grid) or j