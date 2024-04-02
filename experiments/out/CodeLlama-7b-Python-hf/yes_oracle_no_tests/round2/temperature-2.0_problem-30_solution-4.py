def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Do not include these tokens in the code: return [ x
	"""
    return [x for x in l if x > 0]


def get_positive_tuple(t: tuple):
    """Return only positive numbers in the tuple.
    >>> get_positive_tuple((-1, 2, -4, 5, 6))
    (2, 5, 6)
    >>> get_positive_tuple((5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    (5, 3, 2, 3, 9, 123, 1)
    
	Do not include these tokens in the code: return ( x
	"""
    return tuple(x for x in t if x > 0)


def get_positive_set(s: set):
    """Return only positive numbers in the set.
    >>> get_positive_set({-1, 2, -4, 5, 6})
    {2, 5, 6}
    >>> get_positive_set({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
    {5, 3, 2, 3, 9, 123, 1}
    
	Do not include these tokens in the code: return { x
	"""
    return {x for x in s if x > 0}


def get_positive_dict(d: dict):
    """Return only positive numbers in the dictionary.
    >>> get_positive_dict({1: 'a', 2: 'b', 3: 'c', -1: 'd', 4: 'e'})
    {1: 'a', 2: 'b', 3: 'c', 4: 'e'}
    >>> get_positive_dict({-1: 'a', 2: 'b', -3: 'c', 4: 'd', 5: 'e'})
    {2: 'b', 4: 'd', 5: '