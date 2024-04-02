def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True
	"""
    inc = True
    dec = True
    for i in range(0, len(l)-1):
        if l[i+1] < l[i]:
            inc = False
        if l[i+1] > l[i]:
            dec = False
    return inc or dec


if __name__ == "__main__":
    import doctest
    doctest.testmod()
