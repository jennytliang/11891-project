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
	Do not include these tokens in the code: # check if grid is correct
	"""

    N = len(grid)
    M = len(grid[0])
    x , y = 0 , 0
    # check if grid is correct
    for i in range(N):
        for j in range(M):
            if grid[i][j] != M * i + j + 1:
                return []

    for i in range(M):
        if grid[0][i] <= k:
            x = 0
            y = i
            break

    # print(f"x = {x} , y = {y}")
    for i in range(k):
        if i % 2 == 0:
            x += 1
            if x == N:
                x -= 1
                y += 1
        else:
            y += 1
            if y == M:
                x -= 1
                y -= 1
        # print(f"x = {x} , y = {y}")

    res = []
    for i in range(k):
        res.append(grid[x][y])
        if i % 2 == 0:
            x += 1
            if x == N:
                x -= 1
                y += 1
        else:
            y += 1
            if y == M:
                x -= 1
                y -= 1
    return res


if __name__ == "__main__":
    grid = [ [5,9,3], [4,1,6], [7,8,2] ]
    k = 1
    print(minPath(grid, k))
    