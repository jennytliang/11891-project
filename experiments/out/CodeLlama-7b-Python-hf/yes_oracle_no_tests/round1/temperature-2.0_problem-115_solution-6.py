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
    def lower_buckets(grid, capacity):
        """
        The function takes the grid and the capacity of the buckets and 
        returns the number of times the buckets need to be lowered.
        """
        rows = len(grid)
        cols = len(grid[0])
        total_buckets = rows
        buckets_used = 0
        lowered = 0

        # Iterate over each row
        for row in range(rows):
            # Iterate over each column
            for col in range(cols):
                # If the cell is not empty
                if grid[row][col] == 1:
                    # Increment the buckets used
                    buckets_used += 1
                    # If the buckets used is equal to the capacity
                    if buckets_used == capacity:
                        # Increment the lowered
                        lowered += 1
                        # Reset the buckets used
                        buckets_used = 0

            # If the buckets used is not equal to zero
            if buckets_used != 0:
                # Increment the lowered
                lowered += 1
                # Reset the buckets used
                buckets_used = 0

        # Return the lowered
        return lowered

    # Read the grid
    rows = int(input())
    cols = int(input())
    grid = []
    for _ in range(rows):
        # Read the list
        grid.append(list(map(int, input().rstrip().split())))

    # Read the bucket capacity
    capacity = int(input())

    # Print the number of times the buckets need to be lowered
    print(lower_buckets(grid, capacity))


def max_distance(grid, start, end):
    """
    Given a grid of integers and a start and end cell, 
    find the maximum distance between two cells 
    in the grid, moving only in the direction of the arrow.
    
    Example 1:
        Input: 
            grid : [[1,1,1,1,1],
                    [1