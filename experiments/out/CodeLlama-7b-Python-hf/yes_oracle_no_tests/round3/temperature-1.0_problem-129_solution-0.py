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
    
	Include these tokens in the code: N =
	Do not include these tokens in the code: def min Path Helper ( grid ,
	"""
    N = len(grid)
    M = len(grid[0])
    # Do not include these tokens in the code: def min Path Helper ( grid , k ,
    # startRow , startCol )
    # return: list of numbers on the path
    # Precondition: 0 <= startRow < N, 0 <= startCol < M, 0 < k <= N + M
    # grid is a 2D list of integers, where each integer is in the range [1, N *
    # M], and each integer occurs exactly once in the grid
    
    # 1. If k = 1, just return the list of the grid[startRow][startCol]
    # 2. If k > N + M, return an empty list
    # 3. Helper function
    # 4. Main function
    # 5. In each step, we can go to any of the four neighbor cells
    # 6. The helper function helper(grid, k, startRow, startCol) should return a list
    # of numbers on the path
    # 7. The main function should return a list of numbers on the path
    # 8. The main function should call the helper function helper(grid, k,
    # startRow, startCol)
    # 9. The main function should return a list of numbers on the path
    
    # 1. If k = 1, just return the list of the grid[startRow][startCol]
    if k == 1:
        return [grid[startRow][startCol]]
    
    # 2. If k > N + M, return an empty list
    if k > N + M:
        return []
    
    # 3. Helper function
    def helper(grid, k, startRow, startCol):
        # 4. Main function
        # 5. In each step, we can go to any of the four neighbor cells
        # 6. The helper function helper(grid, k, startRow, startCol) should return a list
        # of numbers on the path
        # 7. The main function should return a list of numbers on the path
        # 8. The