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
    # Write your code here
    # Initialize the dp (dp[i][j] stores the minimum path from cell (0, 0) to 
    # cell (i, j) with length k)
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(N)]
    dp[0][0] = 0
    # Initialize the grid (grid[i][j] stores the value on the cell (i, j))
    grid_ = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            grid_[i][j] = grid[i][j]
    # Fill the table
    for k in range(1, N * N + 1):
        for i in range(N):
            for j in range(N):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + di < N and 0 <= j + dj < N:
                        dp[i][j] = min(dp[i][j], dp[i + di][j + dj] + grid_[i][j])
    # Find the minimum path
    path = []
    i = j = 0
    for _ in range(N * N):
        path.append(grid_[i][j])
        di, dj = [(0, 1), (0, -1), (1, 0), (-1, 0)][dp[i][j] - 1]
        i += di
        j += dj
    return path


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 3
    print(minPath(grid, k))
