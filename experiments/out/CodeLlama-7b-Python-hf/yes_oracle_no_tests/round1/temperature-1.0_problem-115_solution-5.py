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
    # O(n*m) time | O(1) space
    def max_fill(grid, capacity):
        # find the row with the most water
        max_water = 0
        for i in range(len(grid)):
            max_water = max(max_water, get_max_water(grid, i, capacity))
        return max_water

    def get_max_water(grid, row_index, bucket_capacity):
        # find the column with the most water
        max_water = 0
        left = 0
        right = len(grid[row_index]) - 1
        while left < right:
            # extract the water
            water = min(grid[row_index][left], grid[row_index][right]) * (right - left)
            # move the bucket
            if grid[row_index][left] < grid[row_index][right]:
                left += 1
            else:
                right -= 1
            # update the max water
            max_water = max(max_water, water)
        return max_water

    # 2nd solution
    # O(n*m) time | O(1) space
    def max_fill(grid, capacity):
        # find the row with the most water
        max_water = 0
        for i in range(len(grid)):
            max_water = max(max_water, get_max_water(grid, i, capacity))
        return max_water

    def get_max_water(grid, row_index, bucket_capacity):
        # find the column with the most water
        max_water = 0
        left = 0
        right = len(grid[row_index]) - 1
        while left < right:
            # extract the water
            water = min(grid[row_index][left], grid[row_index][right]) * (right - left)
            # move the bucket
            if grid[row_index][left] < grid[row_index][right]:
                left += 1
            else:
                right -= 1
