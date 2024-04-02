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
    n = len(grid)
    # Base Case: If a node has two children and we need to take out one of them to make it a child of another node
    # then the parent node will end up as the leaf node of the tree
    if n == 2 and k == 1: 
        return min([grid[i][j] for i in range(n) for j in range(n)])

    min_path = [(0, 0)]  
    # Create a graph. Each node is represented by an index.
    graph = [[] for _ in range(n*n)]
    dist = {}
    # Make the adjacency list.
    for i in range(n):
        for j in range(n):
            node = i*n+j
            if i > 0:
                u = i*n+j-n
                graph[node].append(u)
            if i < n-1:
                v = i*n+j+n
                graph[node].append(v)
            
    def helper(node, k, dist, visited, min_path):
        # Base Case
        if k == 0:
            return

        # Mark the current node as visited.
        visited[node] = True
        
        # Loop through the adjacency list.
        for adj in graph[node]:
            # Mark the adjacent node as visited.
            if visited[adj] == False:
                dist[adj] = grid[node // n][node % n]
                # Recurse for each adjacency node.
                helper(adj, k - 1, dist, visited, min_path)

                # After we are done with a particular node, mark it as False. The current node is not the
                # final destination.
                visited[adj] = False

        # Check if this current node was the final destination.
        elif visited[node]:
            # Update the minimum path.
            min_path.append((node,dist[node]))
    
    visited = [False for _ in range(n*n)]
    helper(0, k, dist, visited, min_path)

   