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
    
	Do not include these tokens in the code: # grid = [[ 0 , 0
	"""
    def get_num_buckets(self, grid):
        return len(grid)

    def get_capacity_of_bucket(self, grid):
        return len(grid[0])

    def get_num_water_in_well(self, grid, i, j):
        return grid[i][j]

    def get_num_water_in_bucket(self, grid, i, j):
        return sum(grid[i][j:])

    def get_bucket_capacity(self, capacity):
        return capacity

    def get_num_buckets_needed_to_empty_well(self, grid, i, j, capacity):
        return math.ceil(self.get_num_water_in_well(grid, i, j) / capacity)

    def get_num_water_in_well(self, grid, i, j):
        return grid[i][j]

    def get_num_water_in_bucket(self, grid, i, j):
        return sum(grid[i][j:])

    def get_bucket_capacity(self, capacity):
        return capacity

    def get_num_buckets_needed_to_empty_well(self, grid, i, j, capacity):
        return math.ceil(self.get_num_water_in_well(grid, i, j) / capacity)

    def get_num_buckets_needed_to_empty_well(self, grid, i, j, capacity):
        return math.ceil(self.get_num_water_in_well(grid, i, j) / capacity)

    def get_num_buckets_needed_to_empty_well(self, grid, i, j, capacity):
        return math.ceil(self.get_num_water_in_well(grid, i, j) / capacity)

    def get_num_buckets_needed_to_empty_well(self, grid, i, j, capacity):
        return math.ceil(self.get_num_water_in_well(grid, i, j