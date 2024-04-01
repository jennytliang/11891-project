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
    def max_fill_helper(grid, capacity, row, col, buckets):
        def check_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        if buckets >= capacity:
            return 0
        
        if grid[row][col] == 0:
            return 0
        
        if check_bounds(row, col) and grid[row][col] > 0:
            grid[row][col] -= 1
            buckets += 1
            return 1 + max_fill_helper(grid, capacity, row, col+1, buckets) + \
                    max_fill_helper(grid, capacity, row+1, col, buckets) + \
                    max_fill_helper(grid, capacity, row, col-1, buckets) + \
                    max_fill_helper(grid, capacity, row-1, col, buckets)
        return 0
    
    buckets = 0
    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            buckets = 0
            ans += max_fill_helper(grid, capacity, row, col, buckets)
    
    return ans

# test cases
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity1 = 1
print(max_fill(grid1, capacity1))

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity2 = 2
print(max_fill(grid2, capacity2))

grid3 = [[0,0,0], [0,0,0]]
capacity3 = 5
print(max_fill(grid3, capacity3))

grid4 = [[0,0,0], [0,0,0], [0,0,0]]
capacity4 = 5
print(max