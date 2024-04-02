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
	Do not include these tokens in the code: n
	"""
    def dfs(i, j, n):
        visited[i][j] = 0
        moves.append((i,j))
        if n == 1: return
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < N and 0 <= new_j < N:
                if visited[new_i][new_j] == 0 \
                        and grid[new_i][new_j] != 0:
                    dfs(new_i, new_j, n-1)

    N = len(grid) # no of rows
    visited = [[0] * N for _ in range(N)]

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    result = set()

    for i in range(N):
        for j in range(N):
            movable_grid = [grid[i][j]]

            visited = [[0] * N for _ in range(N)]
            moves = []
            dfs(i, j, k)
            last_pos = moves[-1]

            movable_grid += [grid[row][col] for row, col in moves[:-1]]
            result.add(tuple(movable_grid))

    min_movable = list(min(result))

    # return final path to target
    return min_movable