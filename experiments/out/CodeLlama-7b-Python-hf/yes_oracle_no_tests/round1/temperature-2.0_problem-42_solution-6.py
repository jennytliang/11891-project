def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    ret = []
    for i in l:
        ret.append(i + 1)
    return ret


def incr_list_inplace(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_inplace([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_inplace([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    for i in range(len(l)):
        l[i] += 1
    return l


def incr_list_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_comp([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_comp([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    return [x + 1 for x in l]


def incr_list_func(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_func([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_func([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 1