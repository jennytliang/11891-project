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
    
	Include these tokens in the code: x , y = 0 , 0
	"""

    N = len(g)
    M = len(g[0])

    def find_min_path(grid, k, x, y):
        if k == 0:
            return []
        if k == 1:
            return [grid[x][y]]
        if x < 0 or x >= N or y < 0 or y >= M:
            return []
        if visited[x][y]:
            return []
        visited[x][y] = True
        min_path = []
        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            min_path += find_min_path(grid, k - 1, x + i, y + j)
        if len(min_path) == 0:
            min_path.append(grid[x][y])
        else:
            min_path.sort()
        return min_path

    visited = [[False for _ in range(M)] for _ in range(N)]
    min_path = find_min_path(grid, k, 0, 0)
    return min_path


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = 3
    print(minPath(grid, k))

    grid = [
        [5, 9, 3],
        [4, 1, 6],
        [7, 8, 2]
    ]
    k = 1
    print(minPath(grid, k))
