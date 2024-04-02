def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: def inc r _ list _ 2 ( l
	"""

    return [x + 1 for x in l]


def incr_dict(d: dict):
    """Return dict with keys incremented by 1.
    >>> incr_dict({1: 2, 3: 4, 5: 6})
    {2: 2, 4: 4, 6: 6}
    >>> incr_dict({'a': 1, 'c': 3, 'b': 2, 'd': 4})
    {'b': 1, 'd': 3, 'a': 2, 'c': 4}
    """

    return {k + 1: v for k, v in d.items()}


def incr_tuple(t: tuple):
    """Return tuple with elements incremented by 1.
    >>> incr_tuple((1, 2, 3))
    (2, 3, 4)
    >>> incr_tuple((5, 3, 5, 2, 3, 3, 9, 0, 123))
    (6, 4, 6, 3, 4, 4, 10, 1, 124)
    """

    return tuple(x + 1 for x in t)


def incr_set(s: set):
    """Return set with elements incremented by 1.
    >>> incr_set({1, 2, 3})
    {2, 3, 4}
    >>> incr_set({5, 3, 5, 2, 3, 3, 9, 0, 123})
    {6, 4, 6, 3, 4, 4, 10, 1, 124}
    """

    return {x + 1 for x in s}
