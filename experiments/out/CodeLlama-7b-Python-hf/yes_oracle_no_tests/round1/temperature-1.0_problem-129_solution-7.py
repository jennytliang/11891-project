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
    if N==1:
        return
    import heapq
    pq = []
    s = 0
    for i in range ( N ):
        for j in range ( N ):
            if grid [i] [j] == 1:
                t = ( i * N + j ) * ( 1 << k )
            else:
                t = ( i * N + j ) * ( 1 << k ) + ( grid [i] [j] * ( 1 << ( k - 1 ) ) )
            s += t
            heapq.heappush ( pq, t )
    
    for level in range ( k ):
        m = s
        s = s // 2
        r, c, v = -1, -1, -1
        pqtemp = []
        for i in range ( len ( pq ) ):
            t = heapq.heappop ( pq )
            k, r, c, v = level * 2, int ( ( t % s ) // 2 // N ), int ( ( t % s ) // 2 % N )
            if t < m:
                m, k, r, c = t, 0, -1, -1
            elif t == m:
                k = k if level % 2 == level // 2 else 1 - k
                r, c = r if k%2==0 else ( c if level % 4 <= 1 else r ), c if k %2 == 1 else ( r if level % 4 <=1 else c ) 
                v = v * 2 if level % 2 == level // 2 else v * 2 + ( grid [r] [c] if k % 4 <=1 else grid [c] [r] )
            heapq.heappush ( pqtemp, t // 2 )
        s = m
        pq = pqtemp
    
        if s >= 1:
            heapq.heappush ( pq, s )
    
    if s != 0:
        print ( s )
    return v

print ( "Expected: " + str ( [1,2