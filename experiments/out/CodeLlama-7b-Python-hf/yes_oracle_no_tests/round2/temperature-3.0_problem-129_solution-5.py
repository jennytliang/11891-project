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

    # Create a list of all moves that can be made
    moves = []
    for i in range(N):
        for j in range(N):
            if i > 0:
                moves.append((i-1,j))
            if i < N-1:
                moves.append((i+1,j))
            if j > 0:
                moves.append((i,j-1))
            if j < N-1:
                moves.append((i,j+1))

    # Initialize a list of all possible paths of length k
    paths = []
    for i in range(N):
        for j in range(N):
            paths.append((i,j,k))

    # Find the minimum path
    min_path = []
    for path in paths:
        path_length = path[2]
        path_values = []
        i = path[0]
        j = path[1]
        path_values.append(grid[i][j])
        if path_length > 1:
            for k in range(path_length-1):
                new_moves = []
                for move in moves:
                    if move[0] == i or move[1] == j:
                        new_moves.append(move)
                i = new_moves[0][0]
                j = new_moves[0][1]
                path_values.append(grid[i][j])
        if len(min_path) == 0 or min(min_path) > min(path_values):
            min_path = path_values

    return min_path


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 3
    print("The minimum path in the grid with length {} is {}".format(k, minPath(grid, k)))

    grid = [[5,9,3],[4,1,6],[7,8,2]]
    k = 1
    print("The minimum path in the grid with length {} is {}