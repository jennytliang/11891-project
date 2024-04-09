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
    def max_fill(self, grid, bucket_capacity):
        if not grid or not grid[0]:
            return 0

        # number of columns
        n = len(grid[0])

        # number of rows
        m = len(grid)

        # water level in each column
        level = [0] * n

        # number of times the buckets are lowered
        count = 0

        # iterate over the columns
        for i in range(n):
            # iterate over the rows
            for j in range(m):
                # if the cell is not empty
                if grid[j][i] == 1:
                    # update the level in the column
                    level[i] += 1

        # iterate over the columns
        for i in range(n):
            # iterate over the buckets
            for j in range(bucket_capacity):
                # if the level in the column is greater than the bucket
                if level[i] > j:
                    # update the number of times the buckets are lowered
                    count += 1
                    # update the level in the column
                    level[i] -= j

        return count

    def max_fill_2(self, grid, bucket_capacity):
        if not grid or not grid[0]:
            return 0

        # number of columns
        n = len(grid[0])

        # number of rows
        m = len(grid)

        # water level in each column
        level = [0] * n

        # number of times the buckets are lowered
        count = 0

        # iterate over the columns
        for i in range(n):
            # iterate over the rows
            for j in range(m):
                # if the cell is not empty
                if grid[j][i] == 1:
                    # update the level in the column
                    level[i] += 1

        # iterate over the columns
        for i in range(n):
            # iterate over the buckets
            for j in range(bucket_capacity):
               