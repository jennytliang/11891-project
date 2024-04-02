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
    height, width = len(grid), len(grid[0])
    n_moves = 0
    i, j = 0, 0
    b_height = 1 # start with a bucket
    while j < width or b_height < height:
        if grid[b_height - 1][j] == 1:
            n_moves += 1
            grid[b_height - 1][j] -= 1
        else:
            j = j + 1 
        b_height = min(b_height + 1, height)
    return n_moves
    
if __name__ == "__main__":
    grid1 = [
        [0,0,1,0],
        [0,1,0,0],
        [1,1,1,1]
    ]
    print(max_fill(grid1, 1))
    grid2 = [
        [0,0,1,1],
        [0,0,0,0],
        [1,1,1,1],
        [0,1,1,1]
    ]
    print(max_fill(grid2, 2))
    grid3 = [
        [0,0,0],
        [0,0,0]
    ]
    print(max_fill(grid3, 5))