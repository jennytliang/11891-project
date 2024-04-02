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
	Do not include these tokens in the code: if ( len ( grid ) <
	"""
    def get_neighbors(i, j):
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < N and 0 <= nj < N:
                yield ni, nj

    N = len(grid)
    if N < 2:
        return []
    # dp[i][j][k] means the minimum path of length k in grid[i][j]
    dp = [[[float('inf')] * k for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = grid[0][0]

    for k in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                for ni, nj in get_neighbors(i, j):
                    dp[i][j][k] = min(dp[i][j][k], dp[ni][nj][k - 1])
                if k < N:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j][k - 1] + grid[i][j])
    return dp[N - 1][N - 1][k - 1]

def test_minPath():
    assert minPath([ [1,2,3], [4,5,6], [7,8,9]], 3) == [1, 2, 1]
    assert minPath([ [5,9,3], [4,1,6], [7,8,2]], 1) == [1]