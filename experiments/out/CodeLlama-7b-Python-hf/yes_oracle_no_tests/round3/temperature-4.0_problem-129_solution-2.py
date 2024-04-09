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
    
	Include these tokens in the code: N = len ( grid )
	"""
    N = len ( grid )
    for row in grid:
        row.append (-1)
    for i in range ( N ):
        grid[i].append (-1)

    # Initialize the memoization table
    memo = [ [ [0 for k in range ( N + 1 ) ] for j in range ( N + 1 ) ] for i in range ( N + 1 ) ]
    for i in range ( N ):
        for j in range ( N ):
            memo[i][j][N] = 0

    def min_path ( i, j, k ):
        if k == 0:
            return 0

        if memo[i][j][k] != 0:
            return memo[i][j][k]

        if k == 1:
            memo[i][j][k] = min ( grid[i][j-1], grid[i-1][j], grid[i][j] )
            return memo[i][j][k]

        ret = min_path ( i - 1, j, k - 1 ) + grid[i][j]
        if j > 1:
            ret = min ( ret, min_path ( i, j - 1, k - 1 ) + grid[i][j] )
        if i > 1:
            ret = min ( ret, min_path ( i - 1, j, k - 1 ) + grid[i][j] )
        memo[i][j][k] = ret
        return ret

    ret = min_path ( N - 1, N - 1, k )
    return [ grid[i][j] for i, j in path ( N - 1, N - 1, k ) ]


def path ( i, j, k ):
    """
    Return the path from (i, j) to (0, 0) with length k.
    """
    if k == 0:
        return []

    if i == 0 and j == 0:
        return [ (i, j) ]

    if