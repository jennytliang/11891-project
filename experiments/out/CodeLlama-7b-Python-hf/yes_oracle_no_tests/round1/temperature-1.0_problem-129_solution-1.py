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
    global_min = min(grid[0][0], grid[0][1])
    l_global_min = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    l_global_min_coords = [[0,0]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            l_local_min = []
            for k in range(3):
                for l in range(3):
                    if (i-k>=0) and (j-l>=0) and (i-k<len(grid)) and (j-l<len(grid[0])) and (k+l!=0) and (k+l!=3):
                        if l_global_min[i][j]:
                            if grid[i-k][j-l] < l_global_min[i][j]:
                                l_global_min[i][j] = grid[i-k][j-l]
                                l_global_min_coords.clear()
                                l_global_min_coords.append([k, l])
                                l_local_min.clear()
                                l_local_min.append([[k+l, i-k, j-l] , l_global_min[i][j]])
                        else:
                            l_global_min[i][j] = grid[i-k][j-l]
                            l_global_min_coords.clear()
                            l_global_min_coords.append([k, l])
                            l_local_min.clear()
                            l_local_min.append([[k+l, i-k, j-l] , l_global_min[i][j]])
            if not l_global_min[i][j]:
                l_global_min[i][j] = grid[i][j]
                l_global_min_coords.append([0, 0])
    # print(l_local_min)
    # print(l_global_min)
    # print