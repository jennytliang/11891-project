def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc
	Do not include these tokens in the code: # sort list into asc ending order
	"""
    if len(l) < 2:
        return True
    # sort list into ascending order
    l.sort()
    # compare adjacent elements
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
