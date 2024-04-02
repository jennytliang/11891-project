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
    
	Do not include these tokens in the code: , d q
	"""

    # initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # initialize the kth table
    kth = [[0 for _ in range(cols)] for _ in range(rows)]

    # initialize the path table
    path = [[0 for _ in range(cols)] for _ in range(rows)]

    # fill the kth table
    for i in range(rows):
        for j in range(cols):
            kth[i][j] = grid[i][j]
            path[i][j] = grid[i][j]

    # fill the kth table
    for i in range(1, k):
        for j in range(cols):
            kth[0][j] = kth[0][j] + grid[0][j]
            kth[rows - 1][j] = kth[rows - 1][j] + grid[rows - 1][j]
            kth[i][0] = kth[i][0] + grid[i][0]
            kth[i][cols - 1] = kth[i][cols - 1] + grid[i][cols - 1]

    # fill the kth table
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            kth[i][j] = kth[i][j] + min(kth[i - 1][j], kth[i][j - 1], kth[i + 1][j], kth[i][j + 1])

    # fill the path table
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if kth[i][j] == kth[i - 1][j] + grid[i][j]:
                path[i][j] = min(path[i][j], path[i - 1][j] + grid[i][j])
            if kth[i][j] == kth[i][j - 1] + grid[