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
    
	Do not include these tokens in the code: # The D P table is ordered
	"""
	assert len(grid) >= 2 and len(grid) - 1 == len(grid[0]) and \
		all(all(1 <= i <= len(grid) ** 2 for i in l) for l in grid) and \
		0 < k <= len(grid) ** 2
	
	# 0-based indexing, use DP table for DP
	T = [[0] * len(grid[0])]
	
	for j in range(len(grid)):  # row i
		for i in range(len(grid[0])):
			if j == 0:
				# top row
				T.append(T[-1][:])
				T[-1][i] = grid[j][i]
			elif i == 0:
				# left col
				T[-1][i] = T[-2][i] + 1 if T[-2][i] + 1 <= k else 1
			else:
				min1 = T[-1][i - 1] + 1 if T[-1][i - 1] + 1 <= k else 1
				min2 = T[-2][i] + 1 if T[-2][i] + 1 <= k else 1
				
				if min1 >= k:
					min1 = k + 1
				
				if min2 >= k:
					min2 = k + 1
				
				T[-1][i] = min(min1, min2)
			
				if T[-1][i] < k:  # need to keep path at k if possible
					if j == len(grid[0]) - 1:
						if min(T[-1]) == k - 1:  # corner case
							return [grid[i - 1][j], grid[i][j], grid[i][