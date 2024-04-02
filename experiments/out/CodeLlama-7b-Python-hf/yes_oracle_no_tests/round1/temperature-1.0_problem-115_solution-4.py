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
    # Get the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Find the number of wells with water
    wells_with_water = 0
    for row in grid:
        wells_with_water += row.count(1)

    # Get the number of buckets
    num_buckets = num_rows

    # Find the number of times to lower the buckets
    num_lowerings = math.ceil(wells_with_water / num_buckets)

    # Return the number of lowerings
    return num_lowerings

if __name__ == "__main__":
    # Read the input
    grid = []
    for _ in range(int(input())):
        grid.append(list(map(int, input().rstrip().split())))
    bucket_capacity = int(input())

    # Print the answer
    print(max_fill(grid, bucket_capacity))
