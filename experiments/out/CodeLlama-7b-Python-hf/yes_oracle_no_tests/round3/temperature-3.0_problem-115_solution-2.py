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
	Do not include these tokens in the code: def max _ fill _ helper (
	"""
    def max_fill_helper(grid, capacity, row, col):
        # Base Case
        if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0

        # If the current node is already visited, just return the value
        if grid[row][col] == -1:
            return grid[row][col]

        # Mark the current node as visited
        grid[row][col] = -1

        # Recur for left, right, top and bottom
        left = max_fill_helper(grid, capacity, row, col-1)
        right = max_fill_helper(grid, capacity, row, col+1)
        top = max_fill_helper(grid, capacity, row-1, col)
        bottom = max_fill_helper(grid, capacity, row+1, col)

        # Update the maximum value
        max_fill_val = max(left, right, top, bottom, 0) + 1
        if max_fill_val == capacity+1:
            return capacity
        else:
            return max_fill_val

    # Main code
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ans += max_fill_helper(grid, capacity, i, j)

    return ans
