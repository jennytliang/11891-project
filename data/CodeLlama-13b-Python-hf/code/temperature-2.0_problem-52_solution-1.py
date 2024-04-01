def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i > t:
            return False
    return True


def has_sum_greater_than(l: list, t: int):
    """Return True if the sum of numbers in the list l is greater than threshold t.
    >>> has_sum_greater_than([1, 2, 4, 10], 100)
    False
    >>> has_sum_greater_than([1, 20, 4, 10], 50)
    True
    """
    s = 0
    for i in l:
        s += i
    return s > t
