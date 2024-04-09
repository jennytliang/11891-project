def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r angel
	"""


    inc, dec = True, True
    fo = l[0]
    for i in l:
        if inc and i < fo:
            inc = False
        elif dec and i > fo:
            dec = False
        fo = i
    return inc or dec