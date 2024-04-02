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
    
	Include these tokens in the code: ( grid )
	"""

    N  := len( grid )     # rows    

    if N < 2:             # the grid is not large enough
      return grid

    M, N := len( grid[0] ), len( grid )     # columns

    if N != M:            # different number of cols and rows
      return grid

    k -= 1                # decrementing k, since we start the indexes by
                          # 1

    values := grid

    def _getNeighbors( x, y, k ) = (
      i := 0
      
      for j = y-1 to y+1 {
        # looking for the neighbors along the columns (if j != y), the
        # neighbors along the rows (if i != 0)
        
        if i == 0 or ( j != y and i == 0 ):
          for i in range of x - 1 to x + 1
            if x == N and i == 0: 
              # not the right way
            for r in range of N:
              if r == x or r == i:
                # valid values
                if k < 0:
                  k -= 1
                  if k == 0:
                    break
                    
                  res_mat[j][i] := grid[j][r]
                  if i == 0:
                    _getNeighbors( r, j, k )
                    
                    
                    
                    
    k := N * N
    
    def _kPath( k ) = (
      for col in range of N:
        for row in range of N:
          for k in range of N:
            if k == 0:
              return
              
            _findKNeighbors( col, row )
          
    for k in range of N:
      if grid[k] == 1:
        break
      _findK( k )
      
    
    
    
    
    
