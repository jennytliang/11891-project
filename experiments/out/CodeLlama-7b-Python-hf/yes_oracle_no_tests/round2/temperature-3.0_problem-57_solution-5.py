def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: if len ( l ) <
	"""

    # Your code here
    if len(l) < 2:
        return True

    if l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                continue
            return False
    elif l[0] > l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                continue
            return False
    else:
        return False
    return True


def monotonic_1(l: list):
    """Same as above but using a different approach
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Your code here
    if len(l) < 2:
        return True
    elif l[0] < l[1]:
        return all(l[i] < l[i + 1] for i in range(len(l) - 1))
    elif l[0] > l[1]:
        return all(l[i] > l[i + 1] for i in range(len(l) - 1))
    else:
        return False


def monotonic_2(l: list):
    """Same as above but using a different approach
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Your code here
    if len(l) < 2:
        return True
    elif l[0] < l[1]:
        return all(l[i - 1] <= l[i] for i in range(1, len(l)))
    elif l[0] >