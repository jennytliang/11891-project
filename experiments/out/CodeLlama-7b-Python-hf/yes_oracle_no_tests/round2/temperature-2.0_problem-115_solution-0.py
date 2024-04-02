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
    def max_fill_helper(grid, capacity, buckets):
        if buckets == 0:
            return 0

        if len(grid) == 0:
            return 0

        if grid[0] > capacity:
            return 1 + max_fill_helper(grid[1:], capacity, buckets)
        
        if grid[0] == 0:
            return max_fill_helper(grid[1:], capacity, buckets)
        
        if grid[0] <= capacity:
            return 1 + max_fill_helper(grid[1:], capacity - grid[0], buckets - 1)

    def max_fill(grid, capacity):
        buckets = math.ceil(len(grid) / capacity)
        return max_fill_helper(grid, capacity, buckets)
    
    return max_fill(grid, capacity)


if __name__ == '__main__':
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))
