def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True

def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 5)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True

def some_above_threshold(l: list, t: int):
    """Return True if at least one number in the list l is above threshold t.
    >>> some_above_threshold([1, 2, 4, 10], 5)
    True
    >>> some_above_threshold([1, 20, 4, 10], 5)
    True
    >>> some_above_threshold([1, 2, 4, 10], 20)
    False
    """
    for i in l:
        if i > t:
            return True
    return False

def some_below_threshold(l: list, t: int):
    """Return True if at least one number in the list l is below threshold t.
    >>> some_below_threshold([1, 2, 4, 10], 5)
    True
    >>> some_below_threshold([1, 20, 4, 10], 5)
    False
    >>> some_below_threshold([1, 2, 4, 10], 20)
    True
    """
    for i in l:
        if i < t:
            return True
    return False