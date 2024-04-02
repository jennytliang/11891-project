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
    # find the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # initialize the bucket capacity
    bucket_capacity = capacity

    # initialize the number of times we need to lower the buckets
    num_times_lowered = 0

    # loop over the rows
    for row in range(rows):
        # loop over the columns
        for col in range(cols):
            # if the current value is 1, increment the number of times we need to lower the buckets
            if grid[row][col] == 1:
                num_times_lowered += 1

    # initialize the number of units of water that we have to extract from the wells
    num_units_extracted = 0

    # loop over the rows
    for row in range(rows):
        # loop over the columns
        for col in range(cols):
            # if the current value is 1, increment the number of units of water that we have to extract from the wells
            if grid[row][col] == 1:
                num_units_extracted += 1

    # calculate the number of buckets needed
    num_buckets_needed = math.ceil(num_units_extracted / bucket_capacity)

    # return the number of times we need to lower the buckets minus the number of buckets needed
    return num_times_lowered - num_buckets_needed

def main():
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    print(max_fill([[0,0,0], [0,0,0]], 5))

main()
