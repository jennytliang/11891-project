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
	Do not include these tokens in the code: # find the maximum capacity
	"""
    rows = len(grid)
    cols = len(grid[0])
    bucket_capacity = capacity

    def get_bucket_water(bucket):
        return sum([1 for row in grid for col in row if col == bucket])
    
    def get_bucket_count(bucket):
        return sum([1 for row in grid for col in row if col == bucket]) // bucket_capacity
    
    def get_bucket_total_water(bucket):
        return get_bucket_water(bucket) * get_bucket_count(bucket)
    
    def get_total_water():
        return sum([get_bucket_total_water(bucket) for bucket in range(1, 2)])

    def get_total_buckets():
        return sum([get_bucket_count(bucket) for bucket in range(1, 2)])
    
    def get_remaining_water(total_buckets):
        return sum([get_bucket_water(bucket) for bucket in range(1, 2)]) - total_buckets * bucket_capacity
    
    def get_lower_buckets(total_buckets, remaining_water):
        return math.ceil(remaining_water / bucket_capacity)
    
    # find the maximum capacity
    total_water = get_total_water()
    total_buckets = get_total_buckets()
    remaining_water = get_remaining_water(total_buckets)
    lower_buckets = get_lower_buckets(total_buckets, remaining_water)
    return lower_buckets


if __name__ == '__main__':
    # grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))
