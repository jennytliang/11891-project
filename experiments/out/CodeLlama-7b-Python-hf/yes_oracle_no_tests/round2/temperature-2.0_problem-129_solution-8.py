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
    
	Do not include these tokens in the code: # base case
	"""
    # base case
    if len(grid) <= 0:
        return None
    if len(grid[0]) <= 0:
        return None
    if k <= 0:
        return None

    # get the size of the grid
    rows = len(grid)
    cols = len(grid[0])

    # initialize the min path
    minPath = []

    # set the initial state
    state = (0, 0)
    visited = set()

    # perform BFS
    queue = [(state, [grid[state[0]][state[1]]])]
    while len(queue) > 0:
        # dequeue a state
        state, path = queue.pop(0)

        # check if we have reached the desired length
        if len(path) == k:
            # add the path to the min path
            minPath = path
            break

        # check if the state is valid
        if state[0] < 0 or state[0] >= rows or state[1] < 0 or state[1] >= cols:
            continue

        # check if the state has already been visited
        if state in visited:
            continue

        # add the state to the visited set
        visited.add(state)

        # get the next states
        nextStates = getNextStates(state, grid)

        # enqueue the next states
        for nextState in nextStates:
            queue.append((nextState, path + [grid[nextState[0]][nextState[1]]]))

    return minPath


def getNextStates(state, grid):
    nextStates = []
    rows = len(grid)
    cols = len(grid[0])

    # check if the state is valid
    if state[0] < 0 or state[0] >= rows or state[1] < 0 or state[1] >= cols:
        return nextStates

    # get the next states
    if state[0] > 0:
        nextStates.append((state[0] - 1, state[1]))