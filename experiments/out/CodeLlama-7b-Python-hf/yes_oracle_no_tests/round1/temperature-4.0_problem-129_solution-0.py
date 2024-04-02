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

    M = len(grid)
    N = len(grid[0])
    dp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    result = []
    i = M - 1
    j = N - 1
    while k > 0:
        result.append(dp[i][j])
        if i == 0 and j == 0:
            break
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        k -= 1
    return result[::-1]


print(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))
print(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1))
