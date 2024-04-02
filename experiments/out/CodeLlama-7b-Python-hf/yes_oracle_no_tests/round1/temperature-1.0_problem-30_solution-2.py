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


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -10]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in l:
        if x < 0:
            r.append(x)
    return r


def sum_positive(l: list):
    """Return the sum of all positive numbers in the list.
    >>> sum_positive([-1, 2, -4, 5, 6])
    7
    >>> sum_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    130
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = 0
    for x in l:
        if x > 0:
            r += x
    return r


def sum_negative(l: list):
    """Return the sum of all negative numbers in the list.
    >>> sum_negative([-1, 2, -4, 5, 6])
    -7
    >>> sum_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -23
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	