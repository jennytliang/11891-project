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
    for i in range(len(lst)):
        for j in range(len(lst[i])-1, -1, -1):
            if lst[i][j] == x:
                res.append((i, j))
    return res

def get_row_pythonic(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in enumerate(lst)]))))

def get_row_pythonic_lambda(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in enumerate(lst)]), key=lambda t: t[0])))

def get_row_pythonic_lambda_2(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in enumerate(lst)]), key=lambda t: t[0], reverse=True)))

def get_row_pythonic_lambda_3(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in enumerate(lst)]), key=lambda t: (t[0], -t[1]))))

def get_row_pythonic_lambda_4(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in enumerate(lst)]), key=lambda t: (t[0], -t[1]), reverse=True)))

def get_row_pythonic_lambda_5(lst, x):
    return list(map(lambda t: t[::-1], sorted(filter(lambda t: t[1] == x, [tuple(reversed(i)) for i in