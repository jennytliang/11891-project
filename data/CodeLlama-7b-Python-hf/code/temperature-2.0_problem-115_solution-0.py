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
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    if n_rows <= 0 or n_cols <= 0:
        return 0

    # Find how many buckets are needed
    n_buckets = math.ceil(n_cols / capacity)

    # Initialize buckets
    buckets = [0] * n_buckets

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                buckets[j // capacity] += 1

    return n_buckets - sum(buckets)

print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))