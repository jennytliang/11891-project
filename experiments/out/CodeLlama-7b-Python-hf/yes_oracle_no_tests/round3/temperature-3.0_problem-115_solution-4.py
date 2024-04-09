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
	Do not include these tokens in the code: # Appro ach 1 :
	"""
    # Approach 1 :
    n = len(grid)
    m = len(grid[0])
    # 1) Calculate the water in each row
    water_row = [0]*n
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                water_row[i] += 1
    # 2) Calculate the total water
    total_water = sum(water_row)
    # 3) Calculate the water that we can extract
    extracted_water = 0
    # 4) Find the number of times we need to lower the bucket
    count = 0
    while extracted_water < total_water:
        extracted_water = 0
        for i in range(n):
            if water_row[i] > 0:
                extracted_water += min(water_row[i], capacity)
                water_row[i] -= capacity
        count += 1
    return count

if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))