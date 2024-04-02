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
    def get_max_fill(grid, capacity):
        """
        Return the max number of times you can lower the bucket
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        bucket_count = rows
        max_fill = 0

        # fill the first row with water
        for col in range(cols):
            if grid[0][col] == 1:
                max_fill += 1

        # start from the second row
        for row in range(1, rows):
            # if the row is empty, no need to continue
            if sum(grid[row]) == 0:
                continue

            # if the row is full, no need to continue
            if sum(grid[row]) >= capacity:
                max_fill += bucket_count
                continue

            # if the row is not full, we need to check the previous row
            # to see if there is a need to lower the bucket
            prev_row = row - 1
            if prev_row >= 0:
                # get the number of 1's in the previous row
                prev_row_ones = sum(grid[prev_row])

                # get the number of 1's in the current row
                curr_row_ones = sum(grid[row])

                # if the number of 1's in the previous row is less than
                # the number of 1's in the current row, no need to continue
                if prev_row_ones < curr_row_ones:
                    continue

                # we need to lower the bucket
                # get the number of 1's in the previous row that are not 1's in the current row
                diff = prev_row_ones - curr_row_ones
                max_fill += math.ceil(diff / capacity)

            # get the number of 1's in the current row
            curr_row_ones = sum(grid[row])

            # if the number of 1's in the current row is less than
            # the capacity, we need to fill the row with