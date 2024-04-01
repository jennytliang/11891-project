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

    def get_row_sum(grid, row):
        """
        Returns the sum of the values in the given row.
        """
        return sum(grid[row])

    def get_col_sum(grid, col):
        """
        Returns the sum of the values in the given column.
        """
        return sum([row[col] for row in grid])

    def is_empty(grid, row, col):
        """
        Returns True if the given cell is empty.
        """
        if grid[row][col] == 0:
            return True
        return False

    def is_full(grid, row, col):
        """
        Returns True if the given cell is full.
        """
        if grid[row][col] == 1:
            return True
        return False

    def is_valid_row(grid, row):
        """
        Returns True if the given row is valid.
        """
        if row < 0 or row >= len(grid):
            return False
        return True

    def is_valid_col(grid, col):
        """
        Returns True if the given column is valid.
        """
        if col < 0 or col >= len(grid[0]):
            return False
        return True

    def is_valid_cell(grid, row, col):
        """
        Returns True if the given cell is valid.
        """
        if is_valid_row(grid, row) and is_valid_col(grid, col):
            return True
        return False

    def get_num_buckets(grid):
        """
        Returns the number of buckets
        """
        return math.ceil(sum(grid[0]) / capacity)

    def get_num_rows(grid):
        """
        Returns the number of rows
        """
        return len(grid)

    def get_num_cols(grid):
        """
        Returns the number of columns
        """
        return len(grid[0])

    def get_num_buckets_from_row(grid, row, bucket_count):
        """