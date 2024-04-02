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
	Do not include these tokens in the code: # The number of rows and
	"""

    # Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
    # Output: [1, 2, 1]
    # grid = [[1,2,3],[4,5,6],[7,8,9]]
    # k = 3
    # N = 3
    #
    # Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
    # Output: [1]
    # grid = [[5,9,3],[4,1,6],[7,8,2]]
    # k = 1
    # N = 3

    # A[i][j] = min distance from A[i][j] to A[0][0]
    # A[i][j] = min(A[i-1][j], A[i][j-1]) + grid[i][j]
    # A[0][0] = 0
    #
    # B[i][j] = min distance from B[i][j] to B[N-1][N-1]
    # B[i][j] = min(B[i-1][j], B[i][j-1]) + grid[i][j]
    # B[N-1][N-1] = 0
    #
    # C[i][j] = min distance from A[0][0] to B[N-1][N-1]
    # C[i][j] = min(A[i][j], B[i][j])
    #
    # D[i][j] = min distance from A[i][j] to B[N-1][N-1]
    # D[i][j] = min(D[i-1][j], D[i][j-1]) + grid[i][j]
    # D[N-1][N-1] = 0
    #
    # E[i][j] = min distance from A[i][j] to C[i][j]
    # E[