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
    
	Include these tokens in the code: N
	Do not include these tokens in the code: # TO DO : Im plement
	"""

    # Initialize the grid
    N = len(grid)

    # Initialize the graph
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = grid[i][j]
    
    # Initialize the cost to reach a node
    cost = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cost[i][j] = float('inf')

    # Initialize the parents
    parent = [[-1 for _ in range(N)] for _ in range(N)]

    # Initialize the cost to reach the source
    cost[0][0] = 0

    # Initialize the priority queue
    pq = [(0, 0, 0)]

    # Initialize the visited array
    visited = [[False for _ in range(N)] for _ in range(N)]

    # Initialize the results
    results = []

    # Perform the Dijkstra's algorithm
    while len(pq) > 0:
        # Pop the next node
        val, i, j = heapq.heappop(pq)

        # If the node has already been visited, skip it
        if visited[i][j]:
            continue

        # Mark the node as visited
        visited[i][j] = True

        # Add the node to the results
        results.append(graph[i][j])

        # If the node is the destination, break
        if len(results) == k:
            break

        # Loop over the neighbors
        for row, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            # If the neighbor is valid, update its cost
            if 0 <= row < N and 0 <= col < N:
                if cost[i][j] + graph[row][col] < cost[row][col]:
                    cost[row