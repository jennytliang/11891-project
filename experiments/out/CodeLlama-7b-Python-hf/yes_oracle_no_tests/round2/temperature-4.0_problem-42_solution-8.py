def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: def inc r _ list 2 ( l :
	"""

    return [x + 1 for x in l]



def incr_tuple(t: tuple):
    """Return tuple with elements incremented by 1.
    >>> incr_tuple((1, 2, 3))
    (2, 3, 4)
    >>> incr_tuple((5, 3, 5, 2, 3, 3, 9, 0, 123))
    (6, 4, 6, 3, 4, 4, 10, 1, 124)
    
	Do not include these tokens in the code: def inc r _ tuple 2 ( t :
	"""

    return tuple(x + 1 for x in t)



def incr_set(s: set):
    """Return set with elements incremented by 1.
    >>> incr_set({1, 2, 3})
    {2, 3, 4}
    >>> incr_set({5, 3, 5, 2, 3, 3, 9, 0, 123})
    {6, 4, 6, 3, 4, 4, 10, 1, 124}
    
	Do not include these tokens in the code: def inc r _ set 2 ( s :
	"""

    return {x + 1 for x in s}



def incr_dict(d: dict):
    """Return dict with elements incremented by 1.
    >>> incr_dict({1: 2, 3: 4})
    {2: 3, 4: 5}
    >>> incr_dict({5: 3, 5: 5, 2: 3, 3: 3, 3: 9, 0: 123})
    {6: 4, 6: 5, 3: 4, 4: 4, 4: 10, 1: 124}
    
	Do not include these tokens in the code: def inc r _ dict 2 ( d :
	