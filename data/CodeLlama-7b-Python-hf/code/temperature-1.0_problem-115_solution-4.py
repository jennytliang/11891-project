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
    """
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    n_rows = len(grid)
    n_cols = len(grid[0])
    n_buckets = n_rows
    bucket_capacity = capacity

    buckets = [0] * n_buckets
    total_water = 0

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                total_water += 1
            else:
                buckets[i] += 1

    if total_water <= bucket_capacity:
        return 0

    times = math.ceil(total_water / bucket_capacity)

    for i in range(n_rows - 1, -1, -1):
        for j in range(n_cols - 1, -1, -1):
            if grid[i][j] == 1:
                buckets[i] -= 1
                if buckets[i] == 0:
                    break
        if buckets[i] == 0:
            break

    return times


if __name__ == "__main__":
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
