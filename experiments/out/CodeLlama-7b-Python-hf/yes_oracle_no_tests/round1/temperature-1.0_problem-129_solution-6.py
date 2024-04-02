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

    R, C = len(grid), len(grid[0])
    dist = [[float('inf')] * C for i in range(R)]

    
    dist[0][0] = 0
    queue = [(0,0,0)]
    res = []
    while queue and k > 0:
            r, c, d = queue.pop(0)
            m, n = R-1, C-1
            if d + 2 > k or r not in range(R) or c not in range(C):
                continue
            dist[r][c] = d
            if len(res) < k - 1:
                if r < m:
                       queue.append((r + 1, c, d + (grid[r + 1][c] > grid[r][c])))
                if r > 0:
                       queue.append((r - 1, c, d + (grid[r][c] > grid[r - 1][c])))
                if c < n:
                       queue.append((r, c + 1, d + (grid[r][c + 1] > grid[r][c])))
                if c > 0:
                       queue.append((r, c - 1, d + (grid[r][c] > grid[r][c - 1])))
            else:
                k -= 1
    return res


grid = [ [1,2,5,3], [4,3,0,2], [5,1,1,5], [2,1,1,8] ]
k = 3
print minPath(grid, k)
