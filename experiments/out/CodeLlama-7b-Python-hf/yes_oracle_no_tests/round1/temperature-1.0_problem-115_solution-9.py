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
    pass

def max_fill_2(grid, capacity):
    """
    Input:
    grid = [
      [0,0,1,0],
      [0,1,0,0],
      [1,1,1,1]
    ]

    Output: 4
    """
    def solve(grid, used, capacity):
        """
        Idea:
            When used buckets meet the wall, put it on top of the next wall we see.
            Putting it on top of the next wall means that the used buckets are reset to 0.
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0  # number of steps needed
        used += [0] * (m+1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                used[i] = max(used[i], j*min(grid[i-1][j-1], capacity))
                ans += capacity - used[i]
            if i != m: used[i+1] = 0
            ans += 1
        return ans
    return solve(grid, [0] * (len(grid)+1), capacity)

if __name__ == '__main__':
    t1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    print('max steps needed to fill all wells:', max_fill_2(t1, 1))

    t2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    print('max steps needed to fill all wells:', max_fill_2(t2, 2))

    t3 = [[0,0,0], [0,0,0]]
    print('max steps needed to fill all wells:', max_fill_2(t3, 5))