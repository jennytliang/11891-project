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
    
	Do not include these tokens in the code: pass def max _ fill
	"""
    ## TO DO: write your code below this line and above the return statement
    
    ## TO DO: write your code above this line
    well_rows= len(grid)
    well_columns = len(grid[0])
    empty_wells = 0

    # Count how many empty wells
    for row in range(well_rows):
        for column in range(well_columns):
            if grid[row][column] == 0:
                empty_wells +=1

    
    # Find out how many times we must lower the bucket
    lowers = math.ceil(empty_wells / capacity)

    return int(lowers)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
