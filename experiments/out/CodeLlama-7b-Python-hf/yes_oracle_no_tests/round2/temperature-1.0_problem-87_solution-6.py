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
    
	Do not include these tokens in the code: def get _ row ( lst , x
	"""
    # Do not change the code below
    return sorted(
        [
            (row, cols)
            for (row, inner_lst) in enumerate(lst)
            for cols in get_items(inner_lst, x, [], True)
        ]
    )


def get_items(lst, item_to_find, cols, to_reverse):
    if lst == []:
        return []
    if lst[0] == item_to_find:
        return [cols + [0]] if not to_reverse else [cols + [len(lst) - 1]]

    return (
        get_items(lst[1:], item_to_find, cols + [0], to_reverse)
        + get_items(lst[1:], item_to_find, cols + [len(lst) - 1])
    )


# Below run the tests. DO NOT CHANGE

# This is designed to fail
try:
    assert get_row([], 1) == []
    print "Fail"
except:
    print "OK"

# This is designed to fail
try:
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    print "Fail"
except:
    print "OK"

# This is designed to succeed
try:
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    assert get_row([[7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7]], 7) == [(0, 3),
                                                                        (1, 4),
                                                                        (1