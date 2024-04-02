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
    # Get the number of rows and cols in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Get the capacity of the buckets
    bucket_capacity = capacity
    # Initialize the number of buckets needed to be lowered
    num_buckets_lowered = 0
    # Initialize a counter to track the number of times a bucket is lowered
    num_times_bucket_lowered = 0
    # Loop through the grid
    for row in range(num_rows):
        for col in range(num_cols):
            # Get the current value of the well
            curr_well_value = grid[row][col]
            # If there is water to be extracted from the well
            if curr_well_value == 1:
                # Increment the number of buckets needed to be lowered
                num_buckets_lowered += 1
            else:
                # If there is no water to be extracted from the well
                # Check to see if the bucket is full
                if num_times_bucket_lowered == bucket_capacity:
                    # If the bucket is full
                    # Increment the number of buckets needed to be lowered
                    num_buckets_lowered += 1
                # Increment the number of times the bucket was lowered
                num_times_bucket_lowered += 1
    # Return the number of buckets needed to be lowered
    return num_buckets_lowered


if __name__ == "__main__":
    # Example 1:
    # Input: 
    #     grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    #     bucket_capacity : 1
    # Output: 6
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    print(f"Example 1: {max_fill(grid, bucket_capacity)}")

    # Example 2:
    # Input