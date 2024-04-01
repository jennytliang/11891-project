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
    """
    def shortest(grid, r, c, visited, k):
        if k == 0:
            return 0
        if r < 0 or r >= N or c < 0 or c >= N or grid[r][c] == 0:
            return float('inf')
        if (r, c) in visited:
            return float('inf')
        visited.add((r, c))
        rmin = min(shortest(grid, r-1, c, visited, k-1), 
                   shortest(grid, r+1, c, visited, k-1), 
                   shortest(grid, r, c-1, visited, k-1), 
                   shortest(grid, r, c+1, visited, k-1))
        return 1 + rmin

    N = len(grid)
    start = min([(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1], 
                key=lambda x: grid[x[0]][x[1]])
    return min([[grid[r][c] for r, c in zip(t, t[1:])] for t in permutations(shortest_path(grid, start, k)) if t[0] == k])