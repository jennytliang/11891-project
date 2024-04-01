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
    
	Include these tokens in the code:  N
	Do not include these tokens in the code: n
	"""

    N = len(grid)
    # create a matrix of size N x N x (N * N) to store the minimum path
    # from (i, j) to (i, j) with k steps
    min_path = [[[float("inf")] * (N * N) for _ in range(N)] for _ in range(N)]

    # base case: (i, j) to (i, j) with 0 steps
    for i in range(N):
        for j in range(N):
            min_path[i][j][(i * N) + j] = grid[i][j]

    # recursive case: (i, j) to (i, j) with k steps
    for k in range(1, N * N):
        for i in range(N):
            for j in range(N):
                # compute the minimum path from (i, j) to (i, j) with k steps
                for x in range(N):
                    for y in range(N):
                        min_path[i][j][k] = min(min_path[i][j][k], min_path[x][y][k - 1] + grid[i][j])

    # return the minimum path from (0, 0) to (N - 1, N - 1) with k steps
    return min_path[0][0][N * N - 1]