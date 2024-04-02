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
    def fill(grid, capacity):
        """
        Returns the number of times you need to lower the buckets.
        """
        ans = 0
        for row in grid:
            ans += math.ceil(sum(row) / capacity)
        return ans

    def empty(grid, capacity):
        """
        Returns the number of times you need to raise the buckets.
        """
        ans = 0
        for row in grid:
            ans += math.ceil(sum(row) / capacity)
        return ans

    def balance(grid, capacity):
        """
        Returns the number of times you need to raise or lower the buckets.
        """
        return fill(grid, capacity) - empty(grid, capacity)

    # return balance(grid, capacity)
    # return fill(grid, capacity)
    return empty(grid, capacity)


if __name__ == '__main__':
    # grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    # capacity = 1
    # print(max_fill(grid, capacity))
    # grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    # capacity = 2
    # print(max_fill(grid, capacity))
    grid = [[0, 0, 0], [0, 0, 0]]
    capacity = 5
    print(max_fill(grid, capacity))
