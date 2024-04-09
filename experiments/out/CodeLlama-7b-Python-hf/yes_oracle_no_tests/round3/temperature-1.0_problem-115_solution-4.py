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
	Do not include these tokens in the code: # The number of well s
	"""
    # This solution runs in O(n) time and O(1) space
    # where n is the number of elements in the grid
    #
    # The solution uses a simple greedy algorithm that
    # fills the buckets in order of the wells. It fills
    # the bucket with the highest well first and then
    # moves on to the next well.

    # The algorithm is based on the following observations:
    # 1. There is no need to keep track of the amount of water
    #    in the buckets. We can simply keep track of the amount
    #    of water that has been extracted.
    # 2. The buckets are filled in order of the wells. This means
    #    that if we have a well with 10 units of water, it is
    #    more efficient to extract 10 units of water from that
    #    well rather than extracting 1 unit of water from multiple
    #    wells.
    # 3. The total amount of water extracted from the grid is
    #    calculated using the following equation:
    #    total = (n - m) * min(w)
    #    where n is the number of wells, m is the number of buckets
    #    and w is the amount of water in each well.
    # 4. The number of buckets needed is calculated using the
    #    following equation:
    #    m = n - floor(total / min(w))

    # Get the number of wells
    n = len(grid)

    # Get the number of buckets
    m = n

    # Get the minimum amount of water in all the wells
    w_min = min(min(row) for row in grid)

    # Get the total amount of water extracted
    total = (n - m) * w_min

    # Get the number of buckets needed
    m = math.ceil(total / w_min)

    # Return the number of buckets needed
    return m


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0