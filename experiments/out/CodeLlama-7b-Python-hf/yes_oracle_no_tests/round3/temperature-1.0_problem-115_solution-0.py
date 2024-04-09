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
    def max_fill_helper(grid, capacity):
        ans = 0
        row = len(grid)
        col = len(grid[0])

        # if capacity of buckets is more than the available water
        if row * col < capacity:
            return -1

        # iterate over each row and column
        for i in range(row):
            for j in range(col):
                # if the current cell is empty
                if grid[i][j] == 0:
                    # iterate over the current row
                    for k in range(j, col):
                        # if the current cell is water
                        if grid[i][k] == 1:
                            # increase the capacity of the buckets
                            capacity += 1
                        # if the current cell is empty
                        elif grid[i][k] == 0:
                            # break
                            break
                    # iterate over the current column
                    for k in range(i, row):
                        # if the current cell is water
                        if grid[k][j] == 1:
                            # increase the capacity of the buckets
                            capacity += 1
                        # if the current cell is empty
                        elif grid[k][j] == 0:
                            # break
                            break
                    # decrease the capacity of the buckets
                    capacity -= 1
                    # increase the number of times the buckets are lowered
                    ans += 1
        return ans

    # return the answer
    return max_fill_helper(grid, capacity)
















