def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: def inc r _ list _ v 2 (
	"""

    return [x + 1 for x in l]


def incr_dict(d: dict):
    """Return dictionary with keys incremented by 1.
    >>> incr_dict({'a': 2, 'b': 3})
    {'a': 3, 'b': 4}
    >>> incr_dict({'a': 3, 'b': 2, 'c': 5, 'd': 0})
    {'a': 4, 'b': 3, 'c': 6, 'd': 1}
    
	Do not include these tokens in the code: def inc r _ dict _ v 2 (
	"""

    return {k: v + 1 for k, v in d.items()}
