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
    # Approach 1: Brute Force
    # Time Complexity: Exponential
    # Space Complexity: Linear
    # def max_fill(grid, capacity):
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 1:
    #                 # Lower bucket to the well
    #                 bucket_water = 0
    #                 while(bucket_water < capacity):
    #                     if i+1 < len(grid):
    #                         if grid[i+1][j] == 1:
    #                             bucket_water += 1
    #                             i += 1
    #                         else:
    #                             break
    #                     else:
    #                         break
    #                 while(bucket_water > 0):
    #                     if i-1 >= 0:
    #                         if grid[i-1][j] == 1:
    #                             bucket_water -= 1
    #                             i -= 1
    #                         else:
    #                             break
    #                     else:
    #                         break
    #                 while(bucket_water > 0):
    #                     if j+1 < len(grid[0]):
    #                         if grid[i][j+1] == 1:
    #                             bucket_water -= 1
    #                             j += 1
    #                         else:
    #                             break
    #                     else:
    #                         break
    #                 while(bucket_water > 0):
    #                     if j-1 >= 0:
    #                         if grid[i][j-1] == 1:
    #                             bucket_water -= 1
    #                             j -= 1
    #                         else:
    #                             break
    #                     else:
    #                         break
    #     # return the number of times you need to lower the buckets
    #     return 

    # Approach 2: