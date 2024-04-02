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
    
	Include these tokens in the code: N
	Do not include these tokens in the code: # O ( n ^ 3
	"""
    N = len(grid)
    n = N ** 2
    for i in range(N):
        for j in range(N):
            grid[i][j] += (i + j) * N
    def dfs(grid, k, i, j, visited):
        if k == 0:
            return []
        if k == 1:
            return [grid[i][j] % N]
        ans = []
        for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= i + x < N and 0 <= j + y < N and (i + x, j + y) not in visited:
                visited.add((i + x, j + y))
                ans.append(grid[i + x][j + y] % N)
                ans += dfs(grid, k - 1, i + x, j + y, visited)
                visited.remove((i + x, j + y))
        return ans
    def dfs2(grid, k, i, j, visited, lst):
        if k == 0:
            return
        if k == 1:
            lst.append(grid[i][j] % N)
            return
        for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= i + x < N and 0 <= j + y < N and (i + x, j + y) not in visited:
                visited.add((i + x, j + y))
                dfs2(grid, k - 1, i + x, j + y, visited, lst)
                visited.remove((i + x, j + y))
    visited = set()
    visited.add((0, 0))
    lst = dfs(grid, k, 0, 0, visited)
    visited = set()
    visited.add((0, 0))
    lst2 = []
    dfs2(grid, k, 0, 0, visited, lst2)
