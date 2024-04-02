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
    # Time: O(m*n)
    # Space: O(1)

    if grid[0][0] == 0 and grid[-1][-1] == 0:
        return 0

    buckets = capacity
    m = len(grid)
    n = len(grid[0])
    moves = 0
    i = 0
    j = n - 1
    while buckets < n - 1 and grid[-1][-1] == 1:
        if math.gcd(i, n) == 1:
            moves += 1
        if grid[i][-1] == 1:
            buckets += 1
            grid[i][-1] = 0
        if grid[i][-1] == 0:
            grid[-1][-1] = 0
            i = i+1
    i = m - 1
    j = 0
    while buckets < m - 1 and grid[0][0] == 1:
        if math.gcd(i, n) == 1:
            moves += 1
        if grid[i][j] == 1:
            buckets += 1
            grid[i][j] = 0
        if grid[i][j] == 0:
            grid[0][0] = 0
            j = j+1

    return moves
