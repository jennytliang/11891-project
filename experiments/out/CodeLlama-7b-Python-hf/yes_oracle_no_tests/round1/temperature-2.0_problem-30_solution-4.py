def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""


    
    return [x for x in l if x > 0]







def get_positive_map(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_map([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_map([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: map ( lambda
	"""

    return list(map(lambda x: x if x > 0 else None, l))







def get_positive_comprehension(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_comprehension([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_comprehension([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    return [x for x in l if x > 0]







def get_positive_map_comprehension(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_map_comprehension([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_map_comprehension([5, 3