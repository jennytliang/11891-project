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
    # calculate how many full rows can be created
    new_lines = math.floor(sum(sum(row) for row in grid)/capacity)

    # calculate how many extra lines are needed
    for i in range(len(grid)):
        # if the last value of each line is empty
        if grid[i] and grid[i][-1] == 1:
            # if adding this row is below the cap, use it
            if new_lines * 5 + i < len(grid):
                new_lines+=1
    # total lines is the total new full lines plus any partial lines
    return math.ceil(new_lines + grid[-(new_lines*new_lines%4-new_lines*3%4)/2:].count(1)/capacity)
    

if __name__=="__main__":
    grid = [ [0,0,1,1],[0,0,0,0],[1,1,1,1],[0,1,1,1] ]
    cap = 2
    # output: 5
    # ans = 5
    print(max_fill(grid, cap))
    
    grid = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
    cap = 1
    # output: 6
    # ans = 6
    print(max_fill(grid, cap))
    
    grid = [ [0,0,0], [0,0,0] ]
    cap = 5
    # output : 0
    # ans = 0
    print(max_fill(grid, cap))
