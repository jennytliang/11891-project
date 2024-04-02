def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    
	Include these tokens in the code: res
	Do not include these tokens in the code: result
	"""

    res = []
    if len(lst) == 0:
        return res
    cur_row, i_col = (0, 0)
    xi = lst[0]
    lxi = len(xi)
    n_rows = len(lst)
    while i_col < lxi and xi[i_col] <= x:
        i_col += 1
    if i_col >= lxi:
        return  [ [i_col-1, xi[i_col-1]] ]
    while i_row < n_rows:
        xi = lst[i_row]
        if cur_row != i_row:
            i_col = 0
            cur_row = i_row
        if x < mi or mi < x:
            cur_x = xi[cur_col-1]
            j_col = cur_col - 1
            while j_col >= 0:
                cur_x = xi[j_col]
                if cur_x >= x:
                    res.append([i_row, j_col])
                if j_col == 0:
                    break
            i_row += 1
        i_col += 1
    return res
    
if __name__ == "__main__":
    print(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 100))
