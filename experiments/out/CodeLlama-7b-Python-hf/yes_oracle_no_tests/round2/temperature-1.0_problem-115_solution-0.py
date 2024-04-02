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
    def max_fill_helper(grid, capacity):
        """
        Helper function to find the number of times we need to lower the buckets
        """
        # Number of rows and columns in the grid
        n_rows = len(grid)
        n_cols = len(grid[0])

        # Number of buckets
        n_buckets = n_rows

        # Number of water units in each well
        wells = [0] * n_rows
        for i in range(n_rows):
            for j in range(n_cols):
                wells[i] += grid[i][j]

        # Capacity of each bucket
        buckets = [capacity] * n_buckets

        # Number of times we need to lower the buckets
        lower_buckets = 0

        # Iterate over each well
        for i in range(n_rows):
            # Water units in this well
            water = wells[i]

            # Iterate over each bucket
            for j in range(n_buckets):
                # If the water units in this well is greater than the capacity of the bucket,
                # then lower the bucket and add the water units to the current bucket
                if water > buckets[j]:
                    water -= buckets[j]
                    lower_buckets += 1

                    # Set the water units in this well to the remaining water units
                    wells[i] = water

                    # Set the water units in this bucket to the capacity of the bucket
                    buckets[j] = capacity

                    # If the remaining water units are less than the capacity of the bucket,
                    # then we can lower the bucket again
                    if water < capacity:
                        lower_buckets += 1
                        buckets[j] = water
                        wells[i] = 0
                # Else, add the water units to the bucket
                else:
                    buckets[j] += water
                    wells[i] = 0

        return lower_buckets

    # Number of buckets
    n_buckets = len