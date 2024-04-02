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
    # define variables
    ROW_COUNT = len(grid)
    COLUMN_COUNT = len(grid[0])
    BUCKET_CAPACITY = capacity
    # define buckets
    buckets = [BUCKET_CAPACITY for i in range(ROW_COUNT)]
    # define total movement
    total_movement = 0
    # iterate through grid
    for row_index in range(ROW_COUNT):
        for column_index in range(COLUMN_COUNT):
            if grid[row_index][column_index] == 1:
                # move water from this well
                total_movement += move_water(row_index, column_index, buckets)
    return total_movement

def move_water(row, column, buckets):
    """
    Move water from well to bucket
    """
    # define variables
    well_water_count = grid[row][column]
    bucket_water_count = buckets[row]
    # move water
    movement_count = 0
    # move water to bucket
    while well_water_count > 0 and bucket_water_count < BUCKET_CAPACITY:
        movement_count += 1
        bucket_water_count += 1
        well_water_count -= 1
    # move water to well
    while well_water_count < 0 and bucket_water_count > 0:
        movement_count += 1
        bucket_water_count -= 1
        well_water_count += 1
    # update buckets
    buckets[row] = bucket_water_count
    # return movement count
    return movement_count

if __name__ == '__main__':
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    print(max_fill(grid, 1))
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    print(max_fill(grid