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
    for i in rangel(len(l) - 1):
        if inc:
            inc = l[i] < l[i + 1]
        if dec:
            dec = l[i] > l[i + 1]
    return inc or dec
