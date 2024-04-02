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
    # TODO: Write your code here
    def find_max_fill(grid, capacity):
        if len(grid) == 0:
            return 0
        buckets = capacity
        for row in grid:
            buckets -= sum(row)
            if buckets < 0:
                return -1
        return sum(grid[0])

    def lower_buckets(grid, capacity):
        if len(grid) == 0:
            return 0
        buckets = capacity
        count = 0
        for row in grid:
            buckets -= sum(row)
            if buckets < 0:
                count += 1
                buckets = capacity
        return count

    def max_fill_helper(grid, capacity, row, col):
        if row >= len(grid):
            return 0
        if col >= len(grid[0]):
            return 0
        if grid[row][col] == 0:
            return 0
        if grid[row][col] == 1:
            grid[row][col] = 0
            return 1 + max_fill_helper(grid, capacity, row, col + 1) + max_fill_helper(grid, capacity, row + 1, col)

    def lower_buckets_helper(grid, capacity, row, col, buckets, count):
        if row >= len(grid):
            return count
        if col >= len(grid[0]):
            return count
        if grid[row][col] == 0:
            return count
        if grid[row][col] == 1:
            if buckets - 1 >= 0:
                grid[row][col] = 0
                count += 1
                return lower_buckets_helper(grid, capacity, row, col + 1, buckets - 1, count) + lower_buckets_helper(grid, capacity, row + 1, col, buckets, count)
            else:
                return count

    ans = lower_buckets(grid, capacity)
    max_fill = find_max_fill(grid, capacity)
