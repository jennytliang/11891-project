def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: # Init ialize variables to check whether
	"""
    prev = 0
    for x in l:
        if prev > x:
            return False
        prev = x
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
