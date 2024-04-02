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
    
	Include these tokens in the code: l
	Do not include these tokens in the code: row
	"""

    res = []
    f_lst = []
    for i in lst:
        f_lst.append(i)
    for i in range(len(f_lst)):
        for j in range(len(f_lst[i])):
            if f_lst[i][j] == x:
                res.append((i,j))
    return sorted(res, key = lambda x: (x[0], -x[1]))


def get_row_2(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x])


def get_row_3(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j in range(len(row)) if row[j] == x])


def get_row_4(lst, x):
    return sorted([(i, j) for i, row in enumerate(lst) for j in range(len(row)) if row[j] == x])


get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)

get_row_2([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)

get_row_3([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)

get_row_4([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)

























