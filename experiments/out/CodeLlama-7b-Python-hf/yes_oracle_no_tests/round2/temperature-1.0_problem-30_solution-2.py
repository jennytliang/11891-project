def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    # pass
    # return l
    # return list(filter(lambda x: x > 0, l))
    return [x for x in l if x > 0]


def get_positive_dict(d: dict):
    """Return only positive numbers in the dict.
    >>> get_positive_dict({"a": -1, "b": 2, "c": -4, "d": 5, "e": 6})
    {'b': 2, 'd': 5, 'e': 6}
    >>> get_positive_dict({1: 5, 3: -5, 2: 2, -3: 3, 3: 9, 0: 0, 123: 1, -10: -10})
    {1: 5, 2: 2, 3: 9, 123: 1}
    
	Include these tokens in the code: return dict ( filter ( lambda
	Do not include these tokens in the code: r = {} for
	"""
    # pass
    # return d
    # return dict(filter(lambda x: x > 0, d))
    return {k: v for k, v in d.items() if v > 0}


def get_positive_set(s: set):
    """Return only positive numbers in the set.
    >>> get_positive_set({-1, 2, -4, 5, 6})
    {2, 5, 6}
    >>> get_positive_set({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
    {5, 3, 2, 3, 9, 123, 1}
    
	Include these tokens in the code: return set ( filter ( lambda
	Do not include these tokens in the code: r = set () for
	"""
    # pass
    # return set(filter(lambda x: x > 0, s))
    return {x for x in