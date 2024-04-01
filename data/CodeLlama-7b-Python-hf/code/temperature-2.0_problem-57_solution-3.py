def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return l == sorted(l) or l == sorted(l, reverse=True)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
