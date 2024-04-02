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
    # 1. check if there is a solution
    # 2. find the maximum number of buckets
    # 3. solve the problem
    # 4. return the solution
    # 5. write the code

    # 1. check if there is a solution
    if not grid or not grid[0]:
        return 0

    # 2. find the maximum number of buckets
    rows, cols = len(grid), len(grid[0])
    max_buckets = math.ceil(sum(sum(row) for row in grid) / capacity)

    # 3. solve the problem
    # 3.1. initialize the solution
    buckets = max_buckets
    ans = 0
    # 3.2. fill the grid
    for _ in range(buckets):
        # 3.2.1. find the largest empty wells
        largest_empty_wells = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    largest_empty_wells.append((row, col, -1 * (row + col)))
        # 3.2.2. sort the empty wells by their size
        largest_empty_wells.sort(key=lambda x: x[2])
        # 3.2.3. fill the largest empty wells with capacity
        for well in largest_empty_wells:
            row, col, _ = well
            for i in range(capacity):
                if row + i < rows and grid[row + i][col] == 0:
                    grid[row + i][col] = 1
                    break
            else:
                # 3.2.4. if the well is not filled, then we need to return 0
                return 0
        # 3.2.5. lower the buckets
        ans += 1
    # 3.3. return the solution
    return ans

if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0