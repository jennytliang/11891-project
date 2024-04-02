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
    # grid -> 2d array
    # capacity -> int
    # ans -> int
    # bucket_capacity -> int
    # buckets -> int
    
    # 1. find the number of buckets needed
    buckets = 0
    for row in grid:
        for cell in row:
            if cell == 1:
                buckets += 1
    buckets = math.ceil(buckets/capacity)

    # 2. find the number of times the buckets need to be lowered
    ans = 0
    for row in grid:
        # find number of water units in the row
        water_units = sum(row)
        # if there are no water units in the row, then we can move on to the next row
        if water_units == 0:
            continue
        # otherwise, we need to lower buckets at least once
        ans += 1
        # if the number of water units is less than the number of buckets, then we need to lower buckets more than once
        if water_units < buckets:
            # we need to lower buckets buckets - water_units times
            ans += buckets - water_units
    return ans


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))
