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
    """
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    return sorted(result, key=lambda x: (x[0], -x[1]))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)], "1st example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 2) == [(0, 1), (1, 3), (1, 1), (2, 4), (2, 1)], "2nd example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 3) == [(0, 2), (1, 2), (2, 2)], "3rd example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 4) == [(0, 3), (1, 3), (2, 3)], "4th example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 5) == [(0, 4), (1, 5), (2, 4)], "5th example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 6) == [(0, 5), (1, 6), (2, 5)], "6th example"
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 7) == [], "7th example"
