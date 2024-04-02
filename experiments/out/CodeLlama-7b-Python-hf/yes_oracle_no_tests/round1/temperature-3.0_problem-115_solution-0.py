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
    def max_fill_rec(grid, capacity, row, col, buckets, visited):
        if buckets == 0 or row == len(grid) or col == len(grid[0]):
            return buckets
        if (row, col, buckets) in visited:
            return visited[(row, col, buckets)]
        
        visited[(row, col, buckets)] = -1
        if grid[row][col] == 1:
            visited[(row, col, buckets)] = max_fill_rec(grid, capacity, row, col + 1, buckets + 1, visited)
        else:
            visited[(row, col, buckets)] = max_fill_rec(grid, capacity, row, col + 1, buckets, visited)
        if visited[(row, col, buckets)] < 0:
            visited[(row, col, buckets)] = max_fill_rec(grid, capacity, row + 1, col, buckets, visited)
        else:
            visited[(row, col, buckets)] += max_fill_rec(grid, capacity, row + 1, col, buckets, visited)
        return visited[(row, col, buckets)]

    def max_fill_dp(grid, capacity, row, col, buckets, visited):
        if buckets == 0 or row == len(grid) or col == len(grid[0]):
            return buckets
        if (row, col, buckets) in visited:
            return visited[(row, col, buckets)]
        
        visited[(row, col, buckets)] = -1
        if grid[row][col] == 1:
            visited[(row, col, buckets)] = max_fill_dp(grid, capacity, row, col + 1, buckets + 1, visited)
        else:
            visited[(row, col, buckets)] = max_fill_dp(grid, capacity, row, col + 1, buckets, visited)
        if visited[(row, col, buckets)] < 0:
            visited[(row, col, buckets)] = max_fill_dp(grid,