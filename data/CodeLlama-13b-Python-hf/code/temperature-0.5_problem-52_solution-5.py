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

def count_above_threshold(l: list, t: int):
    """Return the number of elements in l that are above the threshold t.
    >>> count_above_threshold([1, 2, 4, 10], 5)
    2
    >>> count_above_threshold([1, 2, 4, 10], 7)
    0
    """
    count = 0
    for i in l:
        if i > t:
            count += 1
    return count

def count_below_threshold(l: list, t: int):
    """Return the number of elements in l that are below the threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 5)
    2
    >>> count_below_threshold([1, 2, 4, 10], 7)
    4
    """
    count = 0
    for i in l:
        if i < t:
            count += 1
    return count

def count_equal_to_threshold(l: list, t: int):
    """Return the number of elements in l that are equal to the threshold t.
    >>> count_equal_to_threshold([1, 2, 4, 10], 5)
    0
    >>> count_equal_to_threshold([1, 2, 4, 10], 7)
    0
    """
    count = 0
    for i in l:
        if i == t:
            count += 1
    return count
