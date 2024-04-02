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
    def max_fill_helper(grid, capacity, i, j, buckets):
        if i >= len(grid) or j >= len(grid[0]):
            return buckets

        if grid[i][j] == 0:
            return max_fill_helper(grid, capacity, i + 1, j, buckets)

        # We have a well, need to fill it.
        # If we have enough capacity, just fill it, otherwise return -1
        if buckets >= capacity:
            buckets -= capacity
            return max_fill_helper(grid, capacity, i + 1, j, buckets)

        # We have to fill the well
        # Fill it as much as we can, then move on
        buckets += grid[i][j]
        return max_fill_helper(grid, capacity, i + 1, j, buckets)

    def max_fill(grid, capacity):
        # ans = -1
        buckets = 0
        for i in range(len(grid)):
            buckets = max_fill_helper(grid, capacity, 0, i, buckets)

        return buckets

    return max_fill(grid, capacity)


if __name__ == "__main__":
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    print(max_fill([[0,0,0], [0,0,0]], 5))