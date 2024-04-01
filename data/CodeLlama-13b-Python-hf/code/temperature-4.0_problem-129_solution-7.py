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
    """
    rows = len(grid)
    index = [0, 0]
    values = [grid[0][0]]
    while k > 0:
        index, values = next(index, rows, values, 0, grid, k, values[-1], k-1, rows, index, values, False), values# 1st direction is horizontal
        index, values = nextBestIndex(index, rows, values, values[-1], 1, grid, index, k, values, index, values, indexesToBeExcluded, is_vertical_traversal=False)#, 0
        index, values = nextBestIndex(values=values, is_back_direction=True, next_direction_index=[],
            is_last_cell=(k <= 0), current_cell_value=values[-1], grid=grid, grid_indexes=[],
            k_left_to_move=(k+1), rows_num=rows, cells=values, starting_cell_index=index)
        if isLastCell(index[0], rows):
            return values[-1:]
    return values
def isValidNext(index, rows, val, value):
    if (index[0] < 0 or index[0] >= rows or
       index[1] < 0 or index[1] >= rows or
       index in next_cells and not index[1]:
       or alreadyVisited(index, values))

def findBestNextValueAndPosition(n, r, rows, first_value, second_value):
    values = [] if not previous_best else [previous_best[0]] if not previous_best[1] else previous_best
    for index in indexesToBeExcluded: nextBestValueAndPosition[index[1]['cell_number']] = values[index[1][:2]]# we do not want to take the path which is shorter than the least value we already visited
    for current_index in range([0, first_val], [rows, second_value]]
                                  nextBestIndexToVisit, first_row_value, index, row_positions, k_left_to_move=3):