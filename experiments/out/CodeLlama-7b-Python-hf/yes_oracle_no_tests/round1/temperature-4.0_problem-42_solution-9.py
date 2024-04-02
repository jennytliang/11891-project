def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: return [ x +
	"""
    return [x + 1 for x in l]


def incr_list_comprehension(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_comprehension([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_comprehension([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def incr_list_comprehension_conditional(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_comprehension_conditional([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_comprehension_conditional([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l if x % 2 == 0]


def incr_list_map(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_map([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(map(lambda x: x + 1, l))


def incr_list_map_conditional(l: list):
   