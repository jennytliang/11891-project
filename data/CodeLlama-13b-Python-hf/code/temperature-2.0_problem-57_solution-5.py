def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return monotonic_increasing(l) or monotonic_decreasing(l)


def monotonic_increasing(l: list):
    """Return True is list elements are monotonically increasing.
    >>> monotonic_increasing([1, 2, 4, 20])
    True
    >>> monotonic_increasing([1, 20, 4, 10])
    False
    >>> monotonic_increasing([4, 1, 0, -10])
    False
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


def monotonic_decreasing(l: list):
    """Return True is list elements are monotonically decreasing.
    >>> monotonic_decreasing([1, 2, 4, 20])
    False
    >>> monotonic_decreasing([1, 20, 4, 10])
    False
    >>> monotonic_decreasing([4, 1, 0, -10])
    True
    """
    return all(l[i] >= l[i+1] for i in range(len(l)-1))