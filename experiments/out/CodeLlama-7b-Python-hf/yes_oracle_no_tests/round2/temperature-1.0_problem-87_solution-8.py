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
    
	Include these tokens in the code: for i , l in enumerate
	Do not include these tokens in the code: if len
	"""


    res =  list(((i , j) for i , l in enumerate(lst) for j , _ in enumerate(l) if _ == x))
    res.sort(key = lambda t : t[0]) #sorting by i
    [sub.sort(key = lambda x : x[1], reverse = True) for sub in res]
    return res


def get_col(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (columns, rows), starting with 0.
    Sort coordinates initially by columns in ascending order.
    Also, sort coordinates of the row by rows in descending order.
    
    Examples:
    get_col([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (0, 1), (2, 4), (2, 0), (2, 5)]
    get_col([], 1) == []
    get_col([[], [1], [1, 2, 3]], 3) == [(1, 2)]
    
	Include these tokens in the code: for i , l in enumerate
	Do not include these tokens in the code: if len
    """


    res = []

    for i in range(len(lst[0])):       # iterating over list
        for j in range(len(lst)):      # iterating with columns
            if lst[j][i]:              # element != 0
                res.append((j, i))     # appending coordinates

    res.sort(key = lambda t : t[0])
    [sub.sort(key = lambda x : x[1