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
    # 1. get the wells and buckets
    wells = []
    for row in grid:
        wells.append([i for i, val in enumerate(row) if val == 1])

    # 2. get the number of buckets
    num_buckets = len(wells)

    # 3. sort the wells
    wells.sort(key=lambda x: len(x), reverse=True)
    for i, well in enumerate(wells):
        wells[i] = sorted(well)

    # 4. get the number of times to lower the buckets
    num_times = 0
    total_capacity = capacity * num_buckets
    for i in range(num_buckets):
        if wells[i][0] > total_capacity:
            num_times += math.ceil(wells[i][0] / total_capacity)
        else:
            num_times += 1
        total_capacity -= len(wells[i])

    return num_times

if __name__ == "__main__":
    grid_1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    assert max_fill(grid_1, 1) == 6

    grid_2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    assert max_fill(grid_2, 2) == 5

    grid_3 = [[0,0,0], [0,0,0]]
    assert max_fill(grid_3, 5) == 0
