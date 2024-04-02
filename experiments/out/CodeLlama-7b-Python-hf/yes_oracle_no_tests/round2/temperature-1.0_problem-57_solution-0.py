def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec =
	Do not include these tokens in the code: if len ( l ) ==
	"""
    
    flag = None
    comp = int.__lt__ if l[0] < l[-1] else int.__gt__
    for x, y in zip(l, l[1:]):
        if flag == None:
            flag = comp(x, y);
        if flag != comp(x, y):
            return False
    return True




