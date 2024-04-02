def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: return [ x +
	Do not include these tokens in the code: for i , elem in enumerate (
	"""
    return [elem + 1 for elem in l]

def incr_list_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_comp([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_comp([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: return [ x +
	Do not include these tokens in the code: for i , elem in enumerate (
	"""
    return [x + 1 for x in l]


def incr_gen(l: list):
    """Return list with elements incremented by 1.
    >>> incr_gen([1, 2, 3])
    [2, 3, 4]
    >>> incr_gen([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: yield x + 1
	Do not include these tokens in the code: for i , elem in enumerate (
	"""
    for x in l:
        yield x + 1


def incr_gen_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_gen_comp([1, 2, 3])
    [2, 3, 4]
    >>> incr_gen_comp([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: yield