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
    # naive solution: 
	# 1. loop through all grid and count how many 1s
	# 2. loop through all grid and count how many 0s
	# 3. divide the 1s by the capacity
	# 4. divide the 0s by the capacity
	# 5. floor(1s / capacity) - floor(0s / capacity)
    # time: O(n)
    # space: O(1)

    # optimal solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3. floor(1s / capacity)
    # time: O(n)
    # space: O(1)

    # optimized solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3. ceil(1s / capacity)
    # time: O(n)
    # space: O(1)

    # optimized solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3. ceil(1s / capacity)
    # time: O(n)
    # space: O(1)

    # optimized solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3. ceil(1s / capacity)
    # time: O(n)
    # space: O(1)

    # optimized solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3. ceil(1s / capacity)
    # time: O(n)
    # space: O(1)

    # optimized solution:
	# 1. loop through all grid and count how many 1s
	# 2. divide the 1s by the capacity
	# 3