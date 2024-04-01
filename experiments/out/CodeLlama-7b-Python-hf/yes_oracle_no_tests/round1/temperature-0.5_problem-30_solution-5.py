def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return  list(filter(lambda x: x > 0, l))


def get_unique(l: list):
    """Return only unique numbers in the list.
    >>> get_unique([1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> get_unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5])
    [1, 2, 3, 4, 5]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return  list(filter(lambda x: l.count(x) == 1, l))


def get_smallest(l: list):
    """Return only smallest numbers in the list.
    >>> get_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1]
    >>> get_smallest([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5])
    [1, 2, 3, 4, 5]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return  list(filter(lambda x: l.count(x) == l.count(min(l)), l))


def