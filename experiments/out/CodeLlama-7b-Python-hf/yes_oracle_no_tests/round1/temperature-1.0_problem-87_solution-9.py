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
    
    for row in range(len(lst)):
        for col in range(len(lst[row]) - 1, -1, -1):
            if lst[row][col] == x:
                res.append((row, col))
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1], reverse=True)
    return res


def test_function():
    assert get_row([
        [1,2,3,4,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert get_row([], 1) == []
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [(2, 2), (1, 2), (0, 2)]

if __name__ == '__main__':
    test_function()
