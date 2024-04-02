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
    m, n, c = sum(grid), len(grid), capacity

    if n == 1: # can be completed in zero steps
        return 0

    if m <= c * n: # all wells can be filled, can be completed in zero steps
        return 0

    if math.gcd(n, c) == 1: # impossible to be completed in less than n steps
        return -1

    # ans = m // (n // gcd) + 1
    gcd = 1
    while n // gcd > 1 and c // gcd > 1:
        gcd = math.gcd(gcd, n // gcd)

    num_steps = m // (n // gcd) + 1
    return num_steps