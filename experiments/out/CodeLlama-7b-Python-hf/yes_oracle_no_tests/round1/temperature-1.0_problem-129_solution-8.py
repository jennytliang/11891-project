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
    N = len ( grid )
    # Initialize the grid for visited. By default, all cells are not visited.
    visited_grid = [[False for c in range ( N )] for r in range ( N )]
    
    minpath_list = findMinPath(grid, visited_grid, 0, 0, N , N, k)
    
    print ("Input grid: \n" + str ( grid ))
    
    # print the result
    print ("Min Path with k = {} : {}".format(k, minpath_list) )
            
def findMinPath(grid, visited_grid, row, col, prevRows, prevCols, k):
    currentRow = row
    currentCol = col
    currentK = k
    
    if (currentRow >= prevRows and currentCol >= prevCols) and (currentRow < N and currentCol < N):
        minpath_list = []
        if k > 0:
            cellValue = grid[currentRow][currentCol]
            minpath_list.append(cellValue)
            
            min_cell_list = []
            # check cell
            if not visited_grid[currentRow][currentCol]:
                visited_grid[currentRow][currentCol] = True
                newK = currentK - 1
                min_cell_list = findMinPath (grid, visited_grid, currentRow, currentCol, prevRows, prevCols, newK)
                
            if len ( min_cell_list ) > 0:
                for e in min_cell_list:
                    minpath_list.append(e)
            
            # check up
            if currentRow > 0:
                if not visited_grid[currentRow - 1][currentCol]:
                    visited_grid[currentRow - 1][currentCol] = True
                    newCurrentRow = currentRow - 1
                    newK = currentK - 1
                    newPrevRows = prevRows
                    newPrevCols = prevCols
                    min_cell_list  =   findMinPath (grid, visited_grid, newCurrentRow, currentCol, newPre