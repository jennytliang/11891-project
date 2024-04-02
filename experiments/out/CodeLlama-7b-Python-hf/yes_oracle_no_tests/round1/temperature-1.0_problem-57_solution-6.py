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
    inc, dec = True, True
    for i in range(len(l)-1):
        if inc and l[i] > l[i+1]:
            inc = False
        if dec and l[i] < l[i+1]:
            dec = False
    return inc or dec


def monotonic_v2(l: list):
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
    inc, dec = True, True
    for i in range(len(l)-1):
        if inc and l[i] > l[i+1]:
            inc = False
        if dec and l[i] < l[i+1]:
            dec = False
    return inc or dec


if __name__ == "__main__":
    import doctest
    doctest.testmod()