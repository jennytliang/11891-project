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
    
    # if there is one item grid with k = 1 then 
    # the answer is this item
	if N == 1: 
		A = np.unique (grid[0]) # unique values at this step
		return A
    elif k == 1
        A = np.unique([grid[0,0], grid[0,N], grid[N,0], grid[N,N]])
    else:
        # first step, all the possible paths
        AllPaths = [[i] for i in unique(grid[0])]
        # all possible next paths
        PrevPaths = AllPaths
        PrevDist = list()
        # keep last iteration's pathes until new iteration
        NextPaths = list()
        PrevDist = [distance(v,i) for i in PrevPaths] # distance of each path
        NextDist = list()
        # for the first k-1, make next iteration's paths by using previous step's dists and paths
        for i in range(k-1):
            for i in range(len(NextPaths)):
                #  update distance of the iterative nextpaths
                NextDist = [np.amin(distance(v,i) + distance(v,j)) for i in PrevPaths for j in grid[j]]

            NextPaths = NextDist # iterative pathes
        # last iteration, compare all distances 


    #print (PrevDist, PrevPaths)
    #print(NextDist, NextPaths, PrevPaths)
    print (A)



def distance(v, u):
    from math import pow, sqrt
    return pow(u-v,  2)


minPath([[1,2,3],[4,5,6],[7,8,9]],3)