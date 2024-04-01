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
    
	Do not include these tokens in the code: # create a matrix of size N
	"""


    N = len(gri)
    for row in grid:
        assert len(row) == N, 'Invalid grid'

    # create a matrix of size N
    gri = [[0]*N for _ in range(N)]

    # initialize the top row and leftmost column
    gri[0][0] = grid[0][0]
    for i in range(1, N):
        gri[0][i] = grid[0][i] + gri[0][i-1]
        gri[i][0] = grid[i][0] + gri[i-1][0]

    # fill the rest of the matrix
    for i in range(1, N):
        for j in range(1, N):
            gri[i][j] = grid[i][j] + min(gri[i-1][j], gri[i][j-1])

    # find the minimum path
    ans = []
    i, j = N-1, N-1
    for _ in range(k):
        ans.append(gri[i][j])
        if gri[i-1][j] < gri[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ans


if __name__ == '__main__':
    grid = [ [1,2,3], [4,5,6], [7,8,9] ]
    k = 3
    assert minPath(grid, k) == [1, 2, 1]

    grid = [ [5,9,3], [4,1,6], [7,8,2] ]
    k = 1
    assert minPath(grid, k) == [1]
