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
    # Approach 1: naive
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # n = len(grid)
    # ans = 0
    # while True:
    #     # find the first row with 1
    #     row_with_1 = -1
    #     for i in range(n):
    #         if grid[i][0] == 1:
    #             row_with_1 = i
    #             break
    #     # check if there is no 1 in the grid
    #     if row_with_1 == -1:
    #         break
    #     # find the first 1 in the first row
    #     col_with_1 = -1
    #     for j in range(n):
    #         if grid[0][j] == 1:
    #             col_with_1 = j
    #             break
    #     # check if there is no 1 in the grid
    #     if col_with_1 == -1:
    #         break
    #     # count the number of 1 in the first row
    #     num_of_1 = 0
    #     for j in range(col_with_1, n):
    #         if grid[0][j] == 1:
    #             num_of_1 += 1
    #     # count the number of 1 in the first column
    #     num_of_1_col = 0
    #     for i in range(row_with_1, n):
    #         if grid[i][0] == 1:
    #             num_of_1_col += 1
    #     # check if the number of 1 in the first row is greater than the bucket capacity
    #     if num_of_1 > capacity:
    #         ans += math.ceil(num_of_1/capacity)
    #     # check if the number of 1 in the first column is greater than the bucket capacity
    #     if num_of_1_col > capacity:
    #         ans +=