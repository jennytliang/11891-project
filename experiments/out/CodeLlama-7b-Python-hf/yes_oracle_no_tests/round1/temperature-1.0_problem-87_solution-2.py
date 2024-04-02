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

    coordinates = []

    row = 0

    for l in lst:
        for xi in range(len(l)):
            if l[xi] == x:
                coordinates.append((row, xi))
        row += 1

    # Sort coordinates initially by rows in ascending order
    res = sorted(coordinates, key = lambda j: j[0])

    # Sort coordinates of the row by columns in descending order
    resn = [tuple((r[0], len(r[1]) - 1 - r[1].index(i)) for r in res if r[0] == i) for i in range(len(res)) if len(res) > 1 and  res.count(i) > 1]

    return sorted(j for s in resn for j in s)

def test_function():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_row([
        [1,2,3,4,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert get_row([
        [1, 1, 1]
    ], 1) == [(0, 0), (0, 1), (0, 2)]
    assert get_row([
        [ 7, 7, 7, 8, 8, 8, 8 ]
    ], 7) == [(0, 0), (0, 1), (0, 2), (0, 3)]
    assert get_row([
        [5, 5, 7, 7],
        [5, 7, 5, 7],
        [7, 5, 5, 5],
        [7, 7, 7, 5]
    ], 5) == [(1, 0), (2, 1), (3