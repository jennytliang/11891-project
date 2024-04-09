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
    
	Include these tokens in the code: x
	Do not include these tokens in the code: def get _ ne igh b ors (
	"""


    N = len(gri)
    # create a graph
    graph = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i > 0:
                graph[i][j] = grid[i-1][j]
            if j > 0:
                graph[i][j] = min(graph[i][j], grid[i][j-1])
            if i < N-1:
                graph[i][j] = min(graph[i][j], grid[i+1][j])
            if j < N-1:
                graph[i][j] = min(graph[i][j], grid[i][j+1])
    
    # find the kth smallest element in graph
    def kth_smallest(arr, l, r, k):
        if k > 0 and k <= r-l+1:
            pos = parition(arr, l, r)
            if pos-l == k-1:
                return arr[pos]
            if pos-l > k-1:
                return kth_smallest(arr, l, pos-1, k)
            return kth_smallest(arr, pos+1, r, k-pos+l-1)
        return None
    
    def parition(arr, l, r):
        pivot = arr[r]
        i = l-1
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1

    # find the kth smallest element on the graph
    kth = kth_smallest(graph, 0, N*N-1, k)
    # find the kth smallest element on the grid
    kth_on_grid = kth_smallest(grid, 0, N*N-1, k)
    # find the path on the graph
    path = []
