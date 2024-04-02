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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: def max _ dist ributed _
	"""

def solution_1(grid, bucket_capacity):

    # Find height of grid and width
    height, width = len(grid), len(grid[0])
    ans = 0
    
    # Loop through rows and columns
    for i in range(0, height, 1): # row number (0 to N-1)
        for j in range(0, width, 1): # column number (0 to M-1) 

            # Check to see if grid at [i][j] at bottom row
            if i == height - 1:
                # Add 0 to bucket capacity to empty water from current well  
                bucket_capacity += 0
                # Subtract 1 from bucket capacity if filled
                if bucket_capacity <= 0:
                    return -1 # Well is invalid because bucket empty
                # Subtract 1 from well if filled
                grid[i][j] = abs(grid[i][j] - 1)
                # Reset bucket capacity
                bucket_capacity = 0
                

            # Check to see if grid at [i][j] at left column
            if j == 0:
                # Subtract row value from bucket capacity
                bucket_capacity -= grid[i][j]
                # Add 0 to bucket capacity if filled
                if bucket_capacity <= 0:
                    return -1 # Well is invalid because bucket empty
                # Subtract 1 from well if filled
                grid[i][j] = abs(grid[i][j] - 1)
                # Reset bucket capacity
                bucket_capacity = 0
                

            # Check to see if grid at [i][j] at right column
            if j == width - 1:
                # Add row value to bucket capacity
                bucket_capacity += grid[i][j]
                # Add 0 to bucket capacity if filled
                if bucket_capacity <= 0:
                    return -1 # Well is invalid because bucket empty
                # Subtract 1 from well if filled
                grid[i][j] = abs(grid[i][j] - 1)
