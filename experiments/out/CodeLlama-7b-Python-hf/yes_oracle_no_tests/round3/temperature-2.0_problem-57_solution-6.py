def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) ==
	"""
    inc = True
    dec = True
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            inc = False
        if l[i] < l[i+1]:
            dec = False
    return inc or dec


def monotonic2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic2([1, 2, 4, 20])
    True
    >>> monotonic2([1, 20, 4, 10])
    False
    >>> monotonic2([4, 1, 0, -10])
    True
    """
    return l == sorted(l) or l == sorted(l, reverse=True)


if __name__ == "__main__":
    import doctest
    doctest.testmod()