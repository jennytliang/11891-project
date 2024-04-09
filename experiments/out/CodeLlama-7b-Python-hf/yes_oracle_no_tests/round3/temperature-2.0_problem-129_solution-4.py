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
    
	Do not include these tokens in the code: M = len ( grid [ 0 ])
	"""


    N = len(gri)
    M = len(gri[0])
    # build a grid of (N+1) x (M+1) to keep track of the min value for each cell
    # and the path taken to get there
    min_grid = [[[float('inf'), []] for j in range(M+1)] for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            # compute the minimum value and path for each cell
            min_grid[i][j][0] = grid[i-1][j-1]
            if i-1 >= 0:
                min_grid[i][j][0] = min(min_grid[i][j][0], min_grid[i-1][j][0])
            if j-1 >= 0:
                min_grid[i][j][0] = min(min_grid[i][j][0], min_grid[i][j-1][0])
            
            # keep track of the path taken
            if i-1 >= 0:
                min_grid[i][j][1].extend(min_grid[i-1][j][1])
            if j-1 >= 0:
                min_grid[i][j][1].extend(min_grid[i][j-1][1])
            min_grid[i][j][1].append(grid[i-1][j-1])
    
    # find the path of length k
    path = min_grid[N][M][1]
    for _ in range(k-1):
        path = min_grid[path[0]][path[1]][1]
    return path


if __name__ == "__main__":
    print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3))
    print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1))