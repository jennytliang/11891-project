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
    # Initialization
    rows = len(grid)
    cols = len(grid[0])
    buckets = capacity
    ans = 0

    # Traverse the grid
    for row in range(rows):
        # Find the last 1 in the row
        last_1 = cols - 1
        while last_1 >= 0:
            if grid[row][last_1] > 0:
                break
            last_1 -= 1

        # Find the first 1 in the row
        first_1 = 0
        while first_1 < cols:
            if grid[row][first_1] > 0:
                break
            first_1 += 1

        # If the row is full, we don't need to check the other rows
        if last_1 == cols-1 and first_1 == 0:
            break

        # If the row is empty, we don't need to check the other rows
        if last_1 == -1 and first_1 == cols:
            continue

        # If the row is mixed, we need to check the other rows
        else:
            # If the row is not full, we need to check the other rows
            if first_1 > 0 and last_1 < cols-1:
                # If the row is not empty, we need to check the other rows
                if first_1 != last_1:
                    # If the row is not mixed, we need to check the other rows
                    if first_1 == 0 or last_1 == cols-1:
                        # If the row is not full, we need to check the other rows
                        if first_1 < last_1:
                            # If the row is not empty, we need to check the other rows
                            if first_1 > 0 or last_1 < cols-1:
                                # If the row is not mixed, we need to check the other rows
                                if first_1 == 0 or last_1 == cols-1:
                                    # If the row is not full, we need to check the other rows
                                    if first_1 < last_1: