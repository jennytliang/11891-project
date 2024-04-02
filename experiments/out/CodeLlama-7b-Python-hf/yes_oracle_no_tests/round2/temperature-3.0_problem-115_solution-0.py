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
    # we will use a bucket to extract water from the wells
    # we will use a function to check the height of the wells
    # we will use a function to check the number of buckets needed
    # we will use a function to check the number of buckets needed with a bucket
    # we will use a function to check the number of buckets needed with two buckets
    # we will use a function to check the number of buckets needed with three buckets

    # check the height of the wells
    # we can use the sum function to check the height of the wells
    # we can use the len function to check the height of the wells
    # we can use the max function to check the height of the wells
    # we can use the math.ceil function to check the height of the wells
    # we can use the math.floor function to check the height of the wells
    # we can use the math.sqrt function to check the height of the wells
    height = sum(grid)

    # check the number of buckets needed
    # we can use the math.ceil function to check the number of buckets needed
    # we can use the math.floor function to check the number of buckets needed
    # we can use the math.sqrt function to check the number of buckets needed
    number_buckets = math.ceil(height/capacity)

    # check the number of buckets needed with a bucket
    # we can use the math.ceil function to check the number of buckets needed with a bucket
    # we can use the math.floor function to check the number of buckets needed with a bucket
    # we can use the math.sqrt function to check the number of buckets needed with a bucket
    number_buckets_with_bucket = math.ceil(height/capacity)

    # check the number of buckets needed with two buckets
    # we can use the math.ceil function to check the number of buckets needed with two buckets
    # we can use the math.floor function to check the number of buckets needed with two buckets
    # we can use the math.sqrt function to check the number of buckets needed with two buckets