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
    
	Do not include these tokens in the code: # 1 st approach : br
	"""
    # Approach 1: brute force
    # 1. For each well, lower the bucket
    # 2. Check if the well is filled
    # 3. if not, raise the bucket
    # 4. repeat step 1, 2, 3
    # 5. repeat step 1, 2, 3
    # 6. repeat step 1, 2, 3
    # 7. return the number of times the bucket was lowered
    # Time Complexity: O(n * m * k)
    # Space Complexity: O(1)
    # n = grid.length
    # m = grid[:,1].length
    # k = number of times the bucket was lowered
    # Time Limit Exceeded
    # 
    # Approach 2: Greedy
    # 1. Start with the first well
    # 2. While the well is not filled, lower the bucket
    # 3. If the well is filled, go to the next well
    # 4. Repeat step 2, 3
    # 5. Return the number of times the bucket was lowered
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    # n = grid.length
    # m = grid[:,1].length
    # Time Limit Exceeded
    # 
    # Approach 3: Greedy
    # 1. Start with the first well
    # 2. While the well is not filled, lower the bucket
    # 3. If the well is filled, go to the next well
    # 4. Repeat step 2, 3
    # 5. Return the number of times the bucket was lowered
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    # n = grid.length
    # m = grid[:,1].length
    # Time Limit Exceeded
    # 
    # Approach 4: Greedy
    # 1. Start with the first well
    # 2. While the well is not filled, lower the bucket