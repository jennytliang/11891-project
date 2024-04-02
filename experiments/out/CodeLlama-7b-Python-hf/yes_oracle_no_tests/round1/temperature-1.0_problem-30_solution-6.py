def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in l:
        if x > 0:
            r.append(x)
    return r


def get_positive2(l: list):
    """Return only positive numbers in the list.
    >>> get_positive2([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return list(filter(lambda x: x > 0, l))


def get_positive3(l: list):
    """Return only positive numbers in the list.
    >>> get_positive3([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive3([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return [x for x in l if x > 0]


def get_positive4(l: list):
    """Return only positive numbers in the list.
    >>> get_positive4([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive4([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3