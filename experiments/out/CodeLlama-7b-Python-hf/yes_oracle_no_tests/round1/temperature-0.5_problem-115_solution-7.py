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
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: if not grid or not grid [ 0 ]:
	"""

    def get_bucket_count(row):
        """
        Returns the number of 1s in the row
        """
        count = 0
        for cell in row:
            if cell:
                count += 1
        return count

    def get_bucket_fill_count(row):
        """
        Returns the number of times a bucket can be filled with water
        """
        count = 0
        for cell in row:
            if cell:
                count += 1

        # subtract 1 from the count because we can only fill a bucket with 
        # 1 unit of water
        return count - 1

    def get_water_in_well(row):
        """
        Returns the total water in the well
        """
        return sum(row)

    def get_water_in_bucket(row):
        """
        Returns the total water in the bucket
        """
        return bucket_capacity * get_bucket_count(row)

    def get_water_in_well_with_bucket(row):
        """
        Returns the total water in the well with the bucket
        """
        return get_water_in_well(row) - get_water_in_bucket(row)

    def get_water_in_bucket_with_well(row):
        """
        Returns the total water in the bucket with the well
        """
        return get_water_in_well(row) + get_water_in_bucket(row)

    def get_bucket_fill_count_with_well(row):
        """
        Returns the number of times a bucket can be filled with water with the well
        """
        return get_bucket_fill_count(row) + get_bucket_count(row)

    def get_row_count(grid):
        """
        Returns the number of rows in the grid
        """
        return len(grid)

    def get_bucket_count(grid):
        """
        Returns the number of rows in the grid
        """
        return len(grid[0])

    def get_bucket_fill_count(grid):
       