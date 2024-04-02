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
    
	Do not include these tokens in the code: , d q
	"""

    class Node:
        def __init__(self, grid, k, i, j):
            self.grid = grid
            self.k = k
            self.i = i
            self.j = j
            self.min = float('inf')
            self.lst = []

    def minPathHelper(node):
        if node.k == 0:
            node.min = 0
            return
        if node.i == 0 and node.j == 0:
            node.min = min(minPathHelper(Node(node.grid, node.k - 1, node.i, node.j + 1)),
                           minPathHelper(Node(node.grid, node.k - 1, node.i + 1, node.j)))
        elif node.i == 0:
            node.min = minPathHelper(Node(node.grid, node.k - 1, node.i, node.j - 1))
        elif node.j == 0:
            node.min = minPathHelper(Node(node.grid, node.k - 1, node.i - 1, node.j))
        else:
            node.min = min(minPathHelper(Node(node.grid, node.k - 1, node.i, node.j - 1)),
                           minPathHelper(Node(node.grid, node.k - 1, node.i - 1, node.j)),
                           minPathHelper(Node(node.grid, node.k - 1, node.i, node.j + 1)),
                           minPathHelper(Node(node.grid, node.k - 1, node.i + 1, node.j)))
        node.lst = node.lst + [node.grid[node.i][node.j]]
        return node.min + node.grid[node.i][node.j]

    node = Node(grid, k, 0, 0)
    return minPathHelper(node).lst

print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3