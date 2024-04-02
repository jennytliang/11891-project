def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = list(filter(lambda x: x > 0, l))
    return r


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 3, 3, 123]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = list(filter(lambda x: x % 2 == 0, l))
    return r


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [3, -3, -10]
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in l if i
	"""

    r = list(filter(lambda x: x % 2 == 1, l))
    return r


def get_divide(l: list):
    """Return only numbers which are divisible by 5.
    >>> get_divide([-1, 2, -4, 5, 6])
    [5]
    >>> get_divide([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 123]
    
	Include these tokens in the code: list ( filter ( lambda x : x