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

    def max_distributed_water(grid, capacity):
        """
        Find the number of times to lower buckets for the maximum distributed water
        """
        if (not grid) or (not grid[0]):
            return 0

        # Use dynamic programming
        grid_size = len(grid) 
        no_of_well_full = grid_size # initialise to the maximum no of columns
        total_distributed_water = 0
        for j in range(min(no_of_well_full, len(grid[0]))): # iterate over number of columns that can be fully filled
            prev_row = -1 # initialise
            # get the row for current column
            for i in range(grid_size-1, -1, -1):
                if grid[i][j] == 1: # if current unit is full update row
                    prev_row = i
                elif prev_row > i: # if the row is higher than previous row
                    # update the no of rows currently full by 1
                    no_of_well_full-= 1
                else: # if row is higher than previous then row is same
                    # add current row to previous row
                    prev_row+= 1

            # get min row from current column
            min_distance_to_well = min(prev_row, grid_size-prev_row-1)
            # get max distance of water that can be distributed
            max_distributed_water = float('-inf')
            for distance in range(min_distance_to_well+1):
                # use the distance to calculate the capacities from the current column
                # get distributed water
                max_distributed_water = max(max_distributed_water, capacity*distance)

            # add distributed water to total distributed water
            total_distributed_water+= max_distributed_water

        return total_distributed_water
   
    no_of_buckets = 0
    total_distributed_water = 0
    
    # iterate over rows and get buckets
    for i in range(len(grid)):
        if i%