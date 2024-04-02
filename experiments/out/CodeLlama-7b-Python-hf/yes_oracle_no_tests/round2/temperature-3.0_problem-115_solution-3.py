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
	Do not include these tokens in the code: # define variables R OW
	"""
    
    def solve(grid, capacity):
        # ans = 0
        # max_col = len(grid[0])
        # max_row = len(grid)
        # # for each row
        # for row in range(max_row):
        #     # for each column
        #     for col in range(max_col):
        #         if grid[row][col] == 1:
        #             curr_row = row
        #             curr_col = col
        #             # while curr_row >= 0 and curr_col >= 0:
        #             while curr_row >= 0 and curr_col < max_col:
        #                 if grid[curr_row][curr_col] == 0:
        #                     return -1
        #                 else:
        #                     if curr_col < max_col - 1 and grid[curr_row][curr_col + 1] == 1:
        #                         curr_col += 1
        #                     else:
        #                         if curr_row > 0 and grid[curr_row - 1][curr_col] == 1:
        #                             curr_row -= 1
        #                         else:
        #                             if curr_col > 0 and grid[curr_row][curr_col - 1] == 1:
        #                                 curr_col -= 1
        #                             else:
        #                                 ans += 1
        #                                 break
        # return ans
        ans = 0
        max_col = len(grid[0])
        max_row = len(grid)
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == 1:
                    curr_row = row
                    curr_col = col
                    while curr_row >= 0 and curr_col >= 0:
                        if grid[curr_row][curr_col] == 0:
                            return -1
                        else:
                            if curr_col < max_col - 1 and grid[curr_