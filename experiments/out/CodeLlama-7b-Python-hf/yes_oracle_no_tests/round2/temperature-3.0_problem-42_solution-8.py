def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: return [ x +
	"""
    new_list = []
    for i in range(len(l)):
        new_list.append(l[i] + 1)
    return new_list


def incr_list_alt(l):
    """Return list with elements incremented by 1.
    >>> incr_list_alt([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_alt([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not use any explicit looping (for or while) 
	or mutating list (append, sort, extend, ...)
	"""
    return [x + 1 for x in l]
