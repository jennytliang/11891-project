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
	Do not include these tokens in the code: M
	"""

    N = len(grid)

    # Create the 2-d matrix
    dp = [[0 for _ in range(N)] for _ in range(k)]

    # Initialize the first column
    for i in range(N):
        dp[0][i] = grid[i][0]

    # Fill the 2-d matrix
    for i in range(1, k):
        for j in range(N):
            min_val = float('inf')
            for k in range(N):
                if k != j:
                    min_val = min(min_val, dp[i - 1][k])
            dp[i][j] += min_val
            dp[i][j] += grid[j][i]

    # Find the minimum value in the last column
    min_val = float('inf')
    for i in range(N):
        min_val = min(min_val, dp[k - 1][i])

    # Find the path
    path = []
    i = N - 1
    while k:
        path.append(dp[k - 1][i])
        k_1 = k - 1
        if i == 0:
            break
        while k_1 and dp[k_1 - 1][i - 1] >= dp[k_1][i - 1]:
            k_1 -= 1
        i -= 1
        k = k_1

    path.append(min_val)
    path.reverse()

    return path


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(minPath(grid, 3))
