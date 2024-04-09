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
    
	Do not include these tokens in the code: # Appro ach 1 : Br
	"""
    def max_fill_helper(grid, capacity, row, col, visited):
        if (row, col) in visited:
            return 0
        if row >= len(grid):
            return 0
        if col >= len(grid[0]):
            return 0
        if grid[row][col] == 0:
            return 0
        if grid[row][col] > capacity:
            return math.ceil(grid[row][col] / capacity)
        
        visited.add((row, col))
        return 1 + max_fill_helper(grid, capacity, row + 1, col, visited) + max_fill_helper(grid, capacity, row, col + 1, visited)
    
    visited = set()
    max_num = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_num = max(max_num, max_fill_helper(grid, capacity, i, j, visited))
    return max_num

if __name__ == '__main__':
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    print(max_fill([[0,0,0], [0,0,0]], 5))