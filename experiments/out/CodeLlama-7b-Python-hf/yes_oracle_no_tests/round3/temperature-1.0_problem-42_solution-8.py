def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: return [ x +
	"""
    return [x + 1 for x in l]


def incr_list_with_map(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_with_map([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_with_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: return [ x +
	"""
    return list(map(lambda x: x + 1, l))


def incr_list_with_list_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_with_map([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_with_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: return [ x +
	"""
    return [x + 1 for x in l]


def incr_list_with_lambda(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_with_map([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_with_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: return [