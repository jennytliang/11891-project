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
    # grid is a list of lists
    # each list represents the wells in a row
    # each element in each list represents the amount of water in that well
    # capacity is the amount of water that each bucket can hold
    # return the number of times to lower the buckets
    
    # calculate the number of buckets needed
    num_buckets = sum([sum(row) for row in grid])
    # calculate the number of times the buckets need to be lowered
    num_times = math.ceil(num_buckets / capacity)
    return num_times

if __name__ == "__main__":
    grid_1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    grid_2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    grid_3 = [[0,0,0], [0,0,0]]
    grid_4 = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    print(max_fill(grid_1, 1))
    print(max_fill(grid_2, 2))
    print(max_fill(grid_3, 5))
    print(max_fill(grid_4, 1))
