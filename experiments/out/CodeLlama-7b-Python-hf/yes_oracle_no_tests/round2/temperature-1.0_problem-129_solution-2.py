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
    N = len(grid)
    for r in range(N):
        for c in range(N):
            grid[r][c] = (grid[r][c], r, c)

    # Create a list of all the possible paths
    paths = []
    for r in range(N):
        for c in range(N):
            paths.append(paths_helper(r, c, N))

    # Sort the list of paths
    paths.sort()

    # Find the path with the minimum sum
    min_path = paths[0]
    for path in paths:
        if sum(path) < sum(min_path):
            min_path = path

    # Print the minimum path
    print(min_path)


def paths_helper(r, c, N):
    """
    Helper function to create a list of all the possible paths
    """
    if r == N - 1 and c == N - 1:
        return [grid[r][c]]

    if r == N - 1:
        return paths_helper(r, c + 1, N) + [grid[r][c]]

    if c == N - 1:
        return paths_helper(r + 1, c, N) + [grid[r][c]]

    return paths_helper(r + 1, c, N) + paths_helper(r, c + 1, N) + [grid[r][c]]


grid = [ [1,2,3], [4,5,6], [7,8,9] ]
minPath(grid, 3)

grid = [ [5,9,3], [4,1,6], [7,8,2] ]
minPath(grid, 1)