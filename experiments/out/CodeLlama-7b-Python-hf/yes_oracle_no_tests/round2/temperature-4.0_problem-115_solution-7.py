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
	Do not include these tokens in the code: # Appro ach 1 : Br
	"""
    def get_min_buckets(self, grid, capacity):
        """
        This function returns the minimum number of buckets
        required to empty the wells.
        """
        # initialize the number of buckets
        num_buckets = 0
        # initialize the number of times buckets are lowered
        num_times_lowered = 0
        # initialize the number of wells
        total_wells = 0
        # initialize the number of units of water
        total_units = 0

        # iterate over the rows in the grid
        for row in grid:
            # iterate over the wells in the row
            for well in row:
                # increment the number of wells
                total_wells += 1
                # increment the number of units of water
                total_units += well

        # if there are no wells
        if total_wells == 0:
            # return 0
            return 0

        # if there are no units of water
        if total_units == 0:
            # return 0
            return 0

        # calculate the number of buckets needed
        num_buckets = math.ceil(total_units / capacity)

        # calculate the number of times buckets are lowered
        num_times_lowered = total_wells - num_buckets

        # return the number of times buckets are lowered
        return num_times_lowered

    def max_fill(self, grid, capacity):
        """
        This function returns the maximum number of units of water
        that can be emptied.
        """
        # initialize the number of buckets
        num_buckets = 0
        # initialize the number of wells
        total_wells = 0
        # initialize the number of units of water
        total_units = 0

        # iterate over the rows in the grid
        for row in grid:
            # iterate over the wells in the row
            for well in row:
                # increment the number of wells
                total_wells += 1
                # increment the number of units of