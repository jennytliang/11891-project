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
    # 1st solution
    def max_fill_helper(grid, capacity, row, column, bucket_capacity, count):
        if column == len(grid[0]):
            return count
        if grid[row][column] == 0:
            return max_fill_helper(grid, capacity, row, column + 1, bucket_capacity, count)
        else:
            bucket_capacity -= 1
            if bucket_capacity >= 0:
                return max_fill_helper(grid, capacity, row, column + 1, bucket_capacity, count + 1)
            else:
                return max_fill_helper(grid, capacity, row, column + 1, capacity, count)

    def max_fill(grid, capacity):
        count = 0
        for row in range(len(grid)):
            count = max(count, max_fill_helper(grid, capacity, row, 0, capacity, 0))
        return count

    # 2nd solution
    def max_fill_helper(grid, capacity, row, column, bucket_capacity, count):
        if column == len(grid[0]):
            return count
        if grid[row][column] == 0:
            return max_fill_helper(grid, capacity, row, column + 1, bucket_capacity, count)
        else:
            bucket_capacity -= 1
            if bucket_capacity < 0:
                return max_fill_helper(grid, capacity, row, column + 1, capacity, count)
            else:
                return max(max_fill_helper(grid, capacity, row, column + 1, bucket_capacity, count + 1),
                           max_fill_helper(grid, capacity, row, column + 1, capacity, count))

    def max_fill(grid, capacity):
        count = 0
        for row in range(len(grid)):
            count = max(count, max_fill_helper(grid, capacity, row, 0, capacity, 0))
        return count

    # 3rd solution
    def max_fill