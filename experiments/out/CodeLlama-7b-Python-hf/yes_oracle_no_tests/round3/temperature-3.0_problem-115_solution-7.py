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
    # grid: list[list[int]]
    # capacity: int
    # return: int

    def get_bucket_count(grid):
        return sum(1 for row in grid for well in row if well)

    def get_well_count(grid):
        return sum(len(row) for row in grid)

    def get_water_count(grid):
        return sum(well for row in grid for well in row)

    def get_bucket_capacity(grid):
        return math.ceil(get_water_count(grid) / get_bucket_count(grid))

    if get_bucket_count(grid) == 0:
        return 0

    bucket_capacity = get_bucket_capacity(grid)
    well_count = get_well_count(grid)

    # 0. check if we can empty the grid with the given capacity
    if bucket_capacity >= well_count:
        return 0

    # 1. find the number of buckets to use
    # 2. fill the buckets with water
    # 3. lower the buckets to extract water
    # 4. repeat until no more water
    count = 0
    while get_water_count(grid):
        count += 1
        for row in grid:
            # fill the buckets
            for i in range(len(row)):
                if row[i]:
                    row[i] = min(row[i], bucket_capacity)
            # lower the buckets
            for i in range(len(row)):
                if row[i] > 0:
                    row[i] -= 1
                    if row[i] == 0:
                        row[i] = 0
            # check if we can empty the grid with the given capacity
            if get_water_count(grid) < well_count:
                return count

    return count


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity