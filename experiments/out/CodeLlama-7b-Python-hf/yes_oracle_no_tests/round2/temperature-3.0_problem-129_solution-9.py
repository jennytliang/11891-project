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
    
	Do not include these tokens in the code: #
	"""
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            grid[i][j] -= 1
    dp = [[[float("inf")] * (k + 1) for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            dp[i][j][1] = grid[i][j]
    for i in range(1, k):
        for x in range(n):
            for y in range(m):
                if x > 0:
                    dp[x][y][i + 1] = min(dp[x][y][i + 1], dp[x - 1][y][i])
                if y > 0:
                    dp[x][y][i + 1] = min(dp[x][y][i + 1], dp[x][y - 1][i])
                if x < n - 1:
                    dp[x][y][i + 1] = min(dp[x][y][i + 1], dp[x + 1][y][i])
                if y < m - 1:
                    dp[x][y][i + 1] = min(dp[x][y][i + 1], dp[x][y + 1][i])
    res = []
    x, y, i = 0, 0, k
    while i > 0:
        res.append(dp[x][y][i] + 1)
        if x > 0 and dp[x][y][i] == dp[x - 1][y][i]:
            x -= 1
        elif y > 0 and dp[x][y][i] == dp[x][y - 1][i]:
            y -= 1
        elif x < n - 1 and dp[x][y][i] == dp[x + 1][y][i]:
            x += 1
