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
    
	Include these tokens in the code: x , y
	Do not include these tokens in the code: d p
	"""

    N = len(grid)
    M = len(grid[0])
    x, y = 0, 0
    d = {}
    for i in range(0, N):
        for j in range(0, M):
            d[(i, j)] = grid[i][j]

    for i in range(0, k):
        x, y = min_path(x, y, d)

    return [d[(x, y)]]


def min_path(x, y, d):
    """
    Returns the coordinates of the min path
    """
    if x + 1 < len(d) and y + 1 < len(d[x + 1]):
        a = d[(x, y)]
        b = d[(x + 1, y)]
        c = d[(x, y + 1)]
        d1 = a + min(b, c)
    elif x + 1 < len(d):
        a = d[(x, y)]
        b = d[(x + 1, y)]
        d1 = a + b
    elif y + 1 < len(d[x]):
        a = d[(x, y)]
        c = d[(x, y + 1)]
        d1 = a + c
    else:
        d1 = d[(x, y)]

    if x + 1 < len(d) and y + 2 < len(d[x + 1]):
        a = d[(x + 1, y + 1)]
        b = d[(x + 1, y + 2)]
        d2 = a + min(b, d1)
    elif y + 2 < len(d[x]):
        a = d[(x + 1, y + 1)]
        d2 = a + d1
    else:
        d2 = d1

    if d1 <= d2:
        return x + 1, y + 1
    else:
        return x + 1, y + 2


if __name__ == "__main__":
    grid = [[1, 2