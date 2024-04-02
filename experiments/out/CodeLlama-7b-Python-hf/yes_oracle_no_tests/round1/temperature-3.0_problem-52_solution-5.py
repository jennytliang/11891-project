def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x < t:
            continue
        else:
            return False
    return True


def summation(l: list, t: int):
    """Return the sum of all numbers in the list l that are below threshold t.
    >>> summation([1, 2, 4, 10], 100)
    16
    >>> summation([1, 20, 4, 10], 5)
    6
    
	Include these tokens in the code: return sum(x for x in l if x < t)
    """

    return sum(x for x in l if x < t)


def count_below_threshold(l: list, t: int):
    """Return the number of elements in l that are below threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 100)
    4
    >>> count_below_threshold([1, 20, 4, 10], 5)
    2
    
	Include these tokens in the code: return len([x for x in l if x < t])
    """

    return len([x for x in l if x < t])


def filter_by_threshold(l: list, t: int):
    """Return a list of all elements in l that are below threshold t.
    >>> filter_by_threshold([1, 2, 4, 10], 100)
    [1, 2, 4]
    >>> filter_by_threshold([1, 20, 4, 10], 5)
    [1, 4]
    
	Include these tokens in the code: return [x for x in l if x < t]
    """

    return [x for x in l if x < t]


def filter_by_threshold_with_func(l: list, t: int, f):
    """Return a list of all elements in l that are below threshold t.
    >>> filter_by_threshold_with_func([