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
    def num_of_buckets(grid, capacity):
        row = len(grid)
        col = len(grid[0])

        # calculate well height and width
        wells = [0] * col
        start_row = 0
        while start_row < row:
            if grid[start_row][0] == 1:
                wells[0] += 1
                for c in range(col):
                    if grid[start_row][c] == 0:
                        break
                    elif c == col - 1:
                        wells[c] += 1
                if grid[start_row][c] == 1:
                    wells[c] += 1
                start_row += 1
            elif grid[start_row][0] == 0:
                start_row += 1

        # calculate wells height and index
        well_index = [i for i in wells if i != 0]
        well_heights = (math.ceil(i / capacity) for i in well_index)
        well_heights = [i if i > 1 else 1 for i in well_heights]

        # calculate number of drops
        total_buckets = col * val
        total_drops = (i * 2 - 1 for i in well_heights)
        total = 0
        for a, b in zip(total_buckets, total_drops):
            total += (a * b) / 2
        total = round(total)

        return total

    return num_of_buckets(grid, capacity)
