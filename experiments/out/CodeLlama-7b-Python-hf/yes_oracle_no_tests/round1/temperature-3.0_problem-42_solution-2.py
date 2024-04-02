def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: +
	"""

    retu = []
    for i in l:
        retu.append(i + 1)
    return retu


def incr_list2(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list2([1, 2, 3])
    [2, 3, 4]
    >>> incr_list2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: +
	"""

    return [i + 1 for i in l]


def incr_list3(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list3([1, 2, 3])
    [2, 3, 4]
    >>> incr_list3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: +
	"""

    return list(map(lambda i: i + 1, l))
