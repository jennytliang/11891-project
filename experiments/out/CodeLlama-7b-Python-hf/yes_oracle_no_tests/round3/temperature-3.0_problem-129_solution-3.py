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
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: =
	"""


    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            grid[i][j] = [grid[i][j], i, j]

    for i in range(1, N):
        for j in range(M):
            grid[i][j][0] += grid[i-1][j][0]

    for j in range(1, M):
        for i in range(N):
            grid[i][j][0] += grid[i][j-1][0]

    for i in range(1, N):
        for j in range(1, M):
            grid[i][j][0] += min(grid[i-1][j][0], grid[i][j-1][0])

    def dfs(i, j, k):
        if k == 0:
            return []
        res = [grid[i][j][0]]
        if grid[i][j][1] > 0:
            res.extend(dfs(i-1, j, k-1))
        if grid[i][j][2] > 0:
            res.extend(dfs(i, j-1, k-1))
        return res

    mn = float('inf')
    ans = None
    for i in range(N):
        for j in range(M):
            cand = dfs(i, j, k)
            if cand is not None and len(cand) == k and cand[-1] < mn:
                mn = cand[-1]
                ans = cand
    return ans

print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 3))
print(minPath([ [5,9,3], [4,1,6], [7,8,2]], 1))