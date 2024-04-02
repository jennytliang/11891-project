def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: #
	"""
    if len(l) == 0:
        return True
    elif l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True
    elif l[0] > l[1]:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
