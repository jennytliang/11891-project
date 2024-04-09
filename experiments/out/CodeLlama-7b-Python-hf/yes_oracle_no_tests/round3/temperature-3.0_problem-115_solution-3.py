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
    
	Do not include these tokens in the code: def solve ( grid ,
	"""

    # Calculate the number of buckets needed and the number of wells to fill
    n_buckets = math.ceil(sum(map(sum, grid)) / capacity)
    n_wells = len(grid) * len(grid[0])

    # If the number of buckets is less than or equal to the number of wells,
    # then we can just return the number of wells
    if n_buckets <= n_wells:
        return n_wells

    # Otherwise, we need to lower the number of buckets
    else:
        return n_wells + n_buckets - n_wells

if __name__ == '__main__':
    # Test 1
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity)) # 6

    # Test 2
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity)) # 5

    # Test 3
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity)) # 0
