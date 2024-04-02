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
	Do not include these tokens in the code: def num _ of _ bu ckets
	"""


    rows = len(grid)
    columns = len(grid[0])

    # initialize values
    number_of_buckets = 2**rows
    water_required = 0
    for row in grid:
        # we add 1 because there is water from previous row as well. The array
        # is in row major order. 
        water_required += 1 + sum(row)
    
    # initialize bucket
    buckets = [0]* number_of_buckets

    def extract(row_i, cap):
        # extract water from buckets
        extracted_water = 0
        n_extracted_buckets = 0
        # go from i-th bucket to the last bucket that contains 0
        while buckets[row_i] < cap and row_i < number_of_buckets - 1:
            extracted_water += buckets[row_i]
            bucket[row_i] = 0
            
            if row_i == n_extracted_buckets + 1:
                if n_extracted_buckets + 1 == len(grid):
                    break 
                n_extracted_buckets += 1

            row = grid[n_extracted_buckets]
            buckets[row_i+1] += row[n_extracted_buckets+1]
            
            row_i += 1
        return extracted_water

    def fill(row_i, cap):
        # fill all the buckets with water up to capacity. 
        for i in range(row_i, number_of_bucket):
            buckets[i] = cap
            cap+-1
        return cap

    def move_water(row_i, cap):
        # move water in the row and fill up the available buckets
        # first check if we can move water, else raise exception
        extracted_water = extract(row, cap)
        
        # no more water to move
        if extracted_water == 0:
            return
        moved_water = moved_water + cap

        # this could have added to all the available bu