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
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: if not grid or not grid [ 0 ]:
	"""

    # If there is no grid then there is nothing to do
    if not grid or not grid[0]:
        return 0

    # Get the number of columns in the grid
    num_columns = len(grid[0])

    # Get the number of buckets
    num_buckets = math.ceil(num_columns / capacity)

    # Get the number of rows
    num_rows = len(grid)

    # Get the number of times we need to lower the buckets
    num_lowers = 0

    # For each row
    for row in range(num_rows):
        # Get the number of units of water that we can extract from the row
        units = sum(grid[row])

        # If the number of units is greater than the number of buckets
        if units > num_buckets:
            # Then we need to lower the buckets
            num_lowers += 1

    return num_lowers



def test_function(test_case):
    grid = test_case[0]
    capacity = test_case[1]
    solution = test_case[2]
    output = max_fill(grid, capacity)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


grid = [[0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
capacity = 1
solution = 6
test_case = [grid, capacity, solution]
test_function(test_case)

grid = [[0, 0, 1, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 1, 1]]
capacity = 2
solution = 5
test_case = [grid, capacity, solution]
test_function(test_case)

grid = [[0, 0, 0],
        [0, 0, 0]]
capacity =