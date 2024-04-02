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
    # get the number of wells
    num_wells = len(grid)
    # get the number of columns in each well
    num_cols = len(grid[0])
    # get the bucket capacity
    bucket_capacity = capacity

    # get the total number of wells filled
    total_wells_filled = sum(grid[i][j] for i in range(num_wells) for j in range(num_cols))

    # get the number of buckets needed
    num_buckets = math.ceil(total_wells_filled / bucket_capacity)

    # get the number of times the buckets need to be lowered
    num_buckets_lowered = num_buckets - 1

    return num_buckets_lowered


def main():
    # grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    # bucket_capacity = 1
    # print(max_fill(grid, bucket_capacity))

    # grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    # bucket_capacity = 2
    # print(max_fill(grid, bucket_capacity))

    grid = [[0, 0, 0], [0, 0, 0]]
    bucket_capacity = 5
    print(max_fill(grid, bucket_capacity))

if __name__ == "__main__":
    main()