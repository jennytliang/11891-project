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
    
	Do not include these tokens in the code: l ol = []
	"""

    res = [idx for idx, lst in enumerate(lst) if x in lst]
    result = []
    if res:
        for idx, row in enumerate(lst):
            if idx in res:
                result += [(idx, len(lst) - col - 1) for col, x in enumerate(row) if x == x]
    return sorted(result, key=lambda x: x[0])




list2d_1 = [
  [1, 2, 3, 4, 5, 6],
  [1, 2, 3, 4, 1, 6],
  [1, 2, 3, 4, 5, 1]
]
print(get_row(list2d_1, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])


list2d_2 = [-1, -1, 5]
print(get_row(list2d_2, 5) == [(2, 2)])

list2d_3 = [[], [1], [1, 2, 3]]
print(get_row(list2d_3, 3) == [(2, 2)])

list2d_4 = [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3]
]
print(get_row(list2d_4, 3) == [(2, 2), (3, 2), (4, 2), (5, 2),
                               (6, 2), (7, 2), (8, 2), (9, 2),
                               (10, 2)])