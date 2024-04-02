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
    
	Do not include these tokens in the code: # Initial ization
	"""
    # find the minimum path
    n = len(grid)
    m = len(grid[0])
    # initialisation
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][1] = grid[i][j]
    # calculate the dp table
    for step in range(2, k + 1):
        for i in range(n):
            for j in range(m):
                for x in range(n):
                    for y in range(m):
                        if i != x and j != y:
                            dp[i][j][step] = min(dp[i][j][step], dp[x][y][step - 1])
                        if i == x and j != y:
                            dp[i][j][step] = min(dp[i][j][step], dp[i][y][step - 1])
                        if i != x and j == y:
                            dp[i][j][step] = min(dp[i][j][step], dp[x][j][step - 1])
    # find the minimum path
    ans = []
    i, j = 0, 0
    for step in range(1, k + 1):
        ans.append(dp[i][j][step])
        i, j = next_position(dp, i, j, step)
    return ans


def next_position(dp, i, j, step):
    # find the next position
    n = len(dp)
    m = len(dp[0])
    min_value = float('inf')
    ans_i, ans_j = i, j
    for x in range(n):
        for y in range(m):
            if dp[x][y][step] < min_value:
                min_value = dp[x][y][step]
                ans_i, ans_j = x, y
   