def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 1 ,
	"""

    inc, dec = True, True
    for i in r
        if i < l[i - 1] and inc == True:
            inc = False
        elif i > l[i - 1] and dec == True:
            dec = False
    return inc or dec
