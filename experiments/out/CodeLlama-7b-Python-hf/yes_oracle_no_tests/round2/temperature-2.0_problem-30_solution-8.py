def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = []
    for i in l:
        if i > 0:
            r.append(i)
    return r


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [1, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 9, 1]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = []
    for i in l:
        if i % 2 != 0:
            r.append(i)
    return r


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [-4, 2]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 3, 3, 0, 123]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = []
    for i in l:
        if i % 2 == 0:
            r.append(i)
    return r


def get_positive_odd(l: list):
    """Return only odd positive numbers in the list.
    >>> get_positive_odd([-1, 2, -4, 5, 6])
    [5]
    >>> get_positive_odd([5, 3, -5, 2, -3, 3, 9, 0, 1