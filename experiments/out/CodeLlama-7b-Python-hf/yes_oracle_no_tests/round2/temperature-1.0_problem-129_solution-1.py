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
    def minPathHelper(grid, k, row, col, path):
        if len(path) == k:
            return path
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return []
        if grid[row][col] in path:
            return []
        path.append(grid[row][col])
        nextPath = []
        if row > 0:
            nextPath += minPathHelper(grid, k, row - 1, col, path)
        if row < len(grid) - 1:
            nextPath += minPathHelper(grid, k, row + 1, col, path)
        if col > 0:
            nextPath += minPathHelper(grid, k, row, col - 1, path)
        if col < len(grid[0]) - 1:
            nextPath += minPathHelper(grid, k, row, col + 1, path)
        if len(nextPath) == 0:
            path.pop()
        else:
            return min(nextPath, key = lambda x: x[0])
    
    return minPathHelper(grid, k, 0, 0, [])

print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 3))
print(minPath([ [5,9,3], [4,1,6], [7,8,2]], 1))
print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 2))
print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 4))
print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 5))
print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 6))
print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 7))