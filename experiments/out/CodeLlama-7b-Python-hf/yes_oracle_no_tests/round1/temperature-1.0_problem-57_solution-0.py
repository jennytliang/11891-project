def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) <
	"""
    inc = True
    dec = True
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            inc = False
        if l[i] > l[i - 1]:
            dec = False
    return inc or dec


def monotonic2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] >= l[i - 1] for i in range(1, len(l))) or all(
        l[i] <= l[i - 1] for i in range(1, len(l))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
