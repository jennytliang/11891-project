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
    # N = len(grid)
    # l = len(grid[0])
    # import heapq as hq
    # heap = [(-minPathCost(grid, k, [r][c], l - 1), [r][c]) for c in range (l) for r in range (N)]
    # hq.heapify(heap)
    # visited = set()
    # ans = []
    # for _ in range (N * N):
    #     cost, (x, y) = hq.heappop(heap)
    #     if ans and cost <= ans[-1][2]:
    #         break
    #     elif (x, y) in visited:
    #         continue
    #     else:
    #         visited.add((x, y))
    #         ans.append((x, y, cost))
    # return [grid[i][j] for (i, j, _) in ans]
    
    import heapq as hq

    h = [(minPathCost(grid, k, (x, y), 1), (x, y), x * len(grid) + y)
         for x in range(len(grid)) for y in range(len(grid[0]))]
    hq.heapify(h)
    visited = set()
    ans = [-1] * (len(grid) * len(grid))

    for _ in range(len(grid) * len(grid)):
        cost, (x, y), index = hq.heappop(h)
        ans[index] = (x + 1) * len(grid) + (y + 1)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if len(visited) == len(grid) * len(grid):
            return ans[1:]
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid) and 