def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    
	Include these tokens in the code: N = len ( grid ) x ,
	"""
    import heapq

    
    
    class Cell:
        def __init__(self, i_val: int, i_row: int, i_col: int):
            self.val = i_val
            self.row = i_row
            self.col = i_col
            
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    class Solution:
        
        def __init__(self):
            self.heap = None
            self.grid = None
            self.nrows = None
            self.ncols = None
            self.grid_hits = None   # count for how many times cell (i,j) is accessed
            self.nvisited = None
            self.k = None
            self.visited = None  # keep track of which positions we have visited
            self.c_values = None
            self.min_len = None
            
        def printHardestPaths(self, i, j, remaining_steps, c_values, min_len):
            print ("i = ", i, "j = ", j, "cval = ", c_values[i][j].val, "minlen = ", min_len)
            
            remaining_steps = remaining_steps - 1
            
            if remaining_steps == 0:
                return
            elif min_len <= self.k:
                return

            for x in (i-1, i+1, i, i):
                for y in (j-1, j+1, j, j):
                    if x < 0 or x >= self.nrows or y < 0 or y >= self.ncols or self.visited[x * self.ncols + y]:
                        continue
                    self.visited[x * self.ncols + y] = True
                    min_len = min_len - 1
                    c_values[x][y] = c_values[i][j]    # we should pass the same value of the cell
                    self.printHardestPaths (x, y