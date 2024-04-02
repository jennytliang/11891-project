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
	Do not include these tokens in the code: M
	"""

    N = len(grid)
    M = len(grid[0])

    def get_neighbors(x, y):
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        if x < N - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < M - 1:
            neighbors.append((x, y + 1))
        return neighbors

    def get_path(x, y, k):
        if k == 0:
            return []
        min_path = [grid[x][y]]
        min_path.extend(get_path(x, y, k - 1))
        return min_path

    def get_min_path(x, y, k):
        if k == 0:
            return []
        min_path = [grid[x][y]]
        neighbors = get_neighbors(x, y)
        for x_new, y_new in neighbors:
            path = get_min_path(x_new, y_new, k - 1)
            if len(path) < len(min_path):
                min_path = path
        return min_path

    def get_min_path_recursive(x, y, k):
        if k == 0:
            return []
        min_path = [grid[x][y]]
        neighbors = get_neighbors(x, y)
        min_path_neighbors = []
        for x_new, y_new in neighbors:
            path = get_min_path(x_new, y_new, k - 1)
            if len(path) < len(min_path):
                min_path = path
                min_path_neighbors = [(x_new, y_new)]
            elif len(path) == len(min_path):
                min_path_neighbors.append((x_new, y_new



import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3], [[[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1], [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4], [[[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7], [[[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5], [[[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9], [[[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8], [[[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8], [[[1, 2], [3, 4]], 10], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9], [[[9, 8, 7], [6, 5, 4], [3, 2, 1]], 3], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 5], [[[5, 4, 7], [2, 1, 8], [3, 6, 9]], 4], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5], [[[1, 5, 3], [4, 2, 6], [7, 8, 9]], 4], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 6], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15], [[[1, 5, 3], [4, 2, 6], [7, 8, 9]], 2], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 13], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 4], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 5], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 7], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 18], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 9], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10], [[[1, 5, 3], [4, 2, 6], [7, 8, 9]], 3], [[[5, 4, 7], [2, 1, 8], [3, 6, 9]], 12], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 1], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 20], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 19], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 17], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 17], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 3], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 6], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 13], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 14], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 2], [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 21], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 12], [[[5, 4, 7], [2, 1, 8], [3, 6, 9]], 1], [[[2, 3, 4], [5, 6, 7], [8, 9, 1]], 15], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 16], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 16], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 1], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 5], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 10], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 20], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 10], [[[1, 2], [3, 4]], 2], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 1], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 9], [[[1, 2], [3, 4]], 3], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 8], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 11], [[[1, 2], [3, 4]], 24], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 11], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 6], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 4], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 10], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 9], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 15], [[[1, 2], [3, 4]], 18], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 14], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 5], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 23], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 6], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 8], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 9], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 15], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 18], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 9], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 4], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 17], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 25], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 16], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 7], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 19], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 3], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 21], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 5], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 9], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 14], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 7], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 11], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 2], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 22], [[[1, 2], [3, 4]], 25], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 7], [[[1, 2], [3, 4]], 17], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 12], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 20], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 17], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 2], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 13], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 16], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 24], [[[1, 2], [3, 4]], 19], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 13], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 13], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 24], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 9], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 22], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 12], [[[1, 2], [3, 4]], 16], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 19], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 10], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 3], [[[1, 2], [3, 4]], 22], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 22], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 24], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 23], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 23], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 22], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 19], [[[1, 2], [3, 4]], 5], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 10], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 1], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 8], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 18], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 23], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 11], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 2], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 12], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 7], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 11], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 18], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 8], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 18], [[[1, 2], [3, 4]], 21], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 21], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 24], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 2], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 2], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 12], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 8], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 21], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 16], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 19], [[[1, 2], [3, 4]], 1], [[[1, 2], [3, 4]], 4], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 16], [[[1, 2], [3, 4]], 7], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 4], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 19], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 17], [[[1, 2], [3, 4]], 6], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 18], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 6], [[[1, 2], [3, 4]], 23], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 14], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 18], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 9], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 7], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 23], [[[1, 2], [3, 4]], 8], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 17], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 22], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 20], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 15], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 14], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 14], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 8], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 1], [[[1, 2], [3, 4]], 11], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 3], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 1], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 2], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 6], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 15], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 22], [[[1, 2], [3, 4]], 12], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 14], [[[1, 2], [3, 4]], 9], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 21], [[[1, 2], [3, 4]], 20], [[[10, 7, 14, 1], [15, 9, 8, 5], [12, 6, 2, 16], [13, 11, 3, 4]], 20], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 11], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 4], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 11], [[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 13], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 23], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 4], [[[1, 6, 13, 14], [9, 8, 7, 16], [12, 10, 2, 11], [5, 4, 3, 15]], 25], [[[1, 3, 5, 7], [9, 11, 13, 15], [2, 4, 6, 8], [10, 12, 14, 16]], 20], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 20], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 1], [[[2, 7, 4], [3, 1, 5], [6, 8, 9]], 14], [[[10, 5, 20, 14, 16], [7, 11, 12, 17, 9], [13, 19, 1, 15, 8], [3, 18, 4, 6, 2], [22, 21, 23, 24, 25]], 3], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 17]]
    results = [[1, 2, 1], [1], [1, 2, 1, 2], [1, 10, 1, 10, 1, 10, 1], [1, 7, 1, 7, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 3, 1, 3, 1, 3, 1, 3], [1, 5, 1, 5, 1, 5, 1, 5], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1], [1, 7, 1, 7, 1], [1, 2, 1, 2], [1, 2, 1, 2, 1], [1, 4, 1, 4], [1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 4], [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1], [1, 2, 1, 2, 1, 2], [1, 7, 1, 7], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 4, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 7, 1], [1, 7, 1, 7, 1, 7], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 7], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7], [1], [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1], [1, 3, 1, 3, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 2], [1], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 3, 1, 3, 1, 3], [1, 5, 1, 5], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 5, 1, 5, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 4, 1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1, 2], [1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 3, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 4, 1, 4, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 4, 1, 4, 1, 4, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 5], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2], [1, 5, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1], [1, 4, 1, 4, 1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 6], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 6, 1, 6, 1, 6, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 2], [1, 4], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 6, 1, 6, 1, 6, 1, 6], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1], [1], [1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 5, 1, 5, 1, 5], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 5, 1, 5, 1, 5, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 2, 1, 2, 1, 2, 1, 2], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 5, 1, 5, 1, 5, 1, 5], [1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1], [1], [1, 3], [1, 6, 1, 6, 1, 6], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1], [1, 3, 1, 3], [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4], [1], [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3], [1, 4, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(minPath)