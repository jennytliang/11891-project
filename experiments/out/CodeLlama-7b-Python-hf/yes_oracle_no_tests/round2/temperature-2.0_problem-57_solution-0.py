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
    for i in r_range(len(l) - 1):
        if l[i + 1] > l[i]:
            inc = False
        elif l[i + 1] < l[i]:
            dec = False
    return inc or dec


def r_range(n):
    """Return range(n) in descending order.

    >>> [i for i in r_range(3)]
    [2, 1, 0]
    >>> [i for i in r_range(5)]
    [4, 3, 2, 1, 0]
    >>> [i for i in r_range(7)]
    [6, 5, 4, 3, 2, 1, 0]
    """

    return range(n - 1, -1, -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
