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
    lol = []
    for l in lst:
        if len(l):
            lol.append(list(enumerate(l)))
            
    for i in lol:
        for j in range(1, len(i) + 1):
            if x in i[-j][1]: # O(n^2)
                res.append(i[-j]) # O(n^2)
    
    return sorted(res, key=lambda t: (t[0], -t[1]), reverse=True)
 
if __name__ == "__main__":
    # execute only if run as a script
    # Test 1
    val1 = get_row([
      [1,2,3,4,5,6], # O(n^2)
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1)             # O(n^2)

    res1 = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert val1 == res1, "Function get_row does not produce expected results."

    # Test 2
    val2 = get_row([], 1)   # O(n)

    res2 = []
    assert val2 == res2, "Function get_row does not produce expected results."
    
    # Test 3
    val3 = get_row([[], [1], [1, 2, 3]], 3)   # O(n)
    
    res3 = [(2, 2)]
    assert val3 == res3, "Function get_row does not produce expected results."   
    print("Congratulations! All tests passed!")