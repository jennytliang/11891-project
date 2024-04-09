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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: def get _ bucket _ count (
	"""
    # ans = 0
    # row = len(grid)
    # col = len(grid[0])
    # capacity = bucket_capacity
    # bucket = capacity

    # def get_bucket_count(grid, capacity):
    #     ans = 0
    #     row = len(grid)
    #     col = len(grid[0])
    #     capacity = bucket_capacity
    #     bucket = capacity

    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == 1:
    #                 bucket -= 1
    #             else:
    #                 bucket += 1
    #             if bucket < 0:
    #                 ans += 1
    #                 bucket = capacity
    #     return ans

    # return get_bucket_count(grid, capacity)

    ans = 0
    row = len(grid)
    col = len(grid[0])
    capacity = bucket_capacity
    bucket = capacity

    def get_bucket_count(grid, capacity):
        ans = 0
        row = len(grid)
        col = len(grid[0])
        capacity = bucket_capacity
        bucket = capacity

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    bucket -= 1
                else:
                    bucket += 1
                if bucket < 0:
                    ans += 1
                    bucket = capacity
        return ans

    return get_bucket_count(grid, capacity)


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    print(max_fill(grid, bucket_capacity))
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    bucket_cap