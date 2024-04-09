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
    
	Do not include these tokens in the code: f = lambda lst , x : ( lst .
	"""


    res =  []
    for row_idx, row in enumerate(lst):
        for col_idx, col in enumerate(row):
            if col == x:
                res.append((row_idx, col_idx))
    
    return sorted(res, key=lambda x: (x[0], -x[1]))

def get_row(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j, e in enumerate(row) if e == x], key=lambda x: (x[0], -x[1]))


def get_row(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j, e in enumerate(row) if e == x], key=lambda x: (x[0], -x[1]))


def get_row(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j, e in enumerate(row) if e == x], key=lambda x: (x[0], -x[1]))


def get_row(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j, e in enumerate(row) if e == x], key=lambda x: (x[0], -x[1]))




























































































































































































