def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: print ( inc r _ list ([ 1 ,
	"""

    return [x + 1 for x in l]


def incr_dict(d: dict):
    """Return dictionary with values incremented by 1.
    >>> incr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 2, 'b': 3, 'c': 4}
    >>> incr_dict({'a': 5, 'b': 3, 'c': 3, 'd': 2, 'e': 3, 'f': 3, 'g': 9, 'h': 0, 'i': 123})
    {'a': 6, 'b': 4, 'c': 4, 'd': 3, 'e': 4, 'f': 4, 'g': 10, 'h': 1, 'i': 124}
    
	Do not include these tokens in the code: print ( inc r _ dict ({ ' a ' : 1 ,
	"""

    return {k: v + 1 for k, v in d.items()}


def incr_tuple(t: tuple):
    """Return tuple with elements incremented by 1.
    >>> incr_tuple((1, 2, 3))
    (2, 3, 4)
    >>> incr_tuple((5, 3, 5, 2, 3, 3, 9, 0, 123))
    (6, 4, 6, 3, 4, 4, 10, 1, 124)
    
	Do not include these tokens in the code: print ( inc r _ tuple (( 1 ,
	"""

    return tuple(x + 1 for x in t)


def incr_set(s: set):
    """Return set with elements incremented by 1.
    >>> incr_set({1, 2, 3})
    {2, 3, 4}
    >>> incr_set({5, 3, 5, 2, 3, 3, 9, 0, 123})