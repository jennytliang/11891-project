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
	Do not include these tokens in the code: def max _ fill ( grid ,
	"""
    # ANSWER
    # Initialize variables
    ans = 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    bucket_capacity = capacity
    n_buckets = n_rows

    # Loop through the grid, filling up the buckets
    for i in range(n_rows):
        # Initialize the bucket
        bucket = 0
        # Loop through the columns and add the water to the bucket
        for j in range(n_cols):
            bucket += grid[i][j]
            # If the bucket is full, dump it, and start a new bucket
            if bucket == bucket_capacity:
                bucket = 0
                ans += 1

    return ans

if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))
