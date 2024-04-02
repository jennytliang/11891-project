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
    r, c, b, ans = len(grid), len(grid[0]), capacity, 0
    for i in range(r):
        jr, jc = r - len(list(y for y in reversed(grid) if y[i])) - 1, i
        while jc<c and grid[jc][jr]=='0':
            jc+=1
        w = c-jc
        ans += math.ceil(w/float(b))

    return ans
    

if __name__ == '__main__':
    # Case 1 - Example 1 
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) 
    # Case 1 - Example 2
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    # Case 3 - Example 3
    print(max_fill([[0,0,0], [0,0,0]], 5))
    # Case 2 - 20
    print(max_fill([[ 0, 0, 1,1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 1, 1, 0, 0, 0 ], [ 1, 1, 1, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 1, 0, 0, 0 ], [ 0, 0, 1, 0, 0, 0, 0, 1, 1 ], [ 0, 0, 0, 0, 1, 1, 0, 0, 0 ], [ 1, 1, 1, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0,