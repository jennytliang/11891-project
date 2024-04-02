def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec =
	Do not include these tokens in the code: if l == [] :
	"""
    inc = True
    dec = True
    if len(l) <= 1:
        return True
    for i in range(1, len(l)):
        if l[i-1] < l[i]:
            inc = False
        if l[i-1] > l[i]:
            dec = False
    return inc or dec


if __name__ == "__main__":
    import doctest
    doctest.testmod()
