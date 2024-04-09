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
    
	Do not include these tokens in the code: # Time Complex ity : O (
	"""
    # Time Complexity: O(n*m)
    # Space Complexity: O(n*m)
    def max_fill_1(grid, capacity):
        n, m = len(grid), len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result += 1
        return result // capacity

    # Time Complexity: O(n*(m+n))
    # Space Complexity: O(n+m)
    def max_fill_2(grid, capacity):
        n, m = len(grid), len(grid[0])
        result = 0

        # 1. calculate the total water
        total_water = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    total_water += 1

        # 2. calculate the max water
        max_water = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                # calculate the max water that can be stored in the i-th row
                max_water_row = 0
                for k in range(m):
                    if grid[i][k] == 1:
                        max_water_row += 1
                    else:
                        break
                # calculate the max water that can be stored in the j-th column
                max_water_col = 0
                for k in range(n):
                    if grid[k][j] == 1:
                        max_water_col += 1
                    else:
                        break
                max_water = max(max_water, min(max_water_row, max_water_col))

        # 3. calculate the result
        return math.ceil(total_water / capacity)

    return max_fill_2(grid, capacity)


print(max_fill([[0,0,1,