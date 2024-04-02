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
    def get_max_fill(grid, capacity):
        """
            :param grid: list[list[int]]
            :param capacity: int
            :returns: int
        """
        # TODO: Write your code here
        # raise NotImplementedError()
        n, m = len(grid), len(grid[0])
        max_fill_times = 0
        for _ in range(m):
            for i in range(n):
                if grid[i][_] == 1:
                    max_fill_times += 1
                else:
                    break
        return max_fill_times

    def get_max_fill_optimized(grid, capacity):
        """
            :param grid: list[list[int]]
            :param capacity: int
            :returns: int
        """
        # TODO: Write your code here
        # raise NotImplementedError()
        n, m = len(grid), len(grid[0])
        max_fill_times = 0
        for _ in range(m):
            for i in range(n):
                if grid[i][_] == 1:
                    max_fill_times += 1
                    if max_fill_times == capacity:
                        break
                else:
                    break
        return max_fill_times

    def get_max_fill_optimized_2(grid, capacity):
        """
            :param grid: list[list[int]]
            :param capacity: int
            :returns: int
        """
        # TODO: Write your code here
        # raise NotImplementedError()
        n, m = len(grid), len(grid[0])
        max_fill_times = 0
        for _ in range(m):
            for i in range(n):
                if grid[i][_] == 1:
                    max_fill_times += 1
                else:
                    break
        return max_fill_times

    def get_max_fill_optimized_3(grid, capacity):
        """
            :param grid: list[list[int]]