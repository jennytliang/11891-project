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
    # get the length of the wells
    well_length = len(grid[0])
    # get the number of wells
    number_of_wells = len(grid)

    # get the number of buckets
    number_of_buckets = int(math.ceil(well_length / capacity))

    # get the number of times the buckets need to be lowered
    times_lowered = number_of_wells * number_of_buckets

    return times_lowered


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(f"Number of times the buckets need to be lowered: {max_fill(grid, capacity)}")

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(f"Number of times the buckets need to be lowered: {max_fill(grid, capacity)}")

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(f"Number of times the buckets need to be lowered: {max_fill(grid, capacity)}")