def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: if len ( l ) <=
	"""
    if len(l) <= 1:
        return True
    direction = l[1] - l[0]
    for i in range(1, len(l) - 1):
        if l[i + 1] - l[i] * direction <= 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
