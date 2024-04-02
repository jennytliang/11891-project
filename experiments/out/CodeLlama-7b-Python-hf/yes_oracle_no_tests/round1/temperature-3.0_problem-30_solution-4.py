def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list ( filter ( lambda x : x >
	"""
    return list(filter(lambda x: x > 0, l))


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -3, -10]
    
	Include these tokens in the code: return list ( filter ( lambda x : x <
	"""
    return list(filter(lambda x: x < 0, l))


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [3, -3, 3, -10]
    
	Include these tokens in the code: return list ( filter ( lambda x : x %
	"""
    return list(filter(lambda x: x % 2 != 0, l))


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, -4, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, 2, -3, 3, 0, 123, -10]
    
	Include these tokens in the code: return list ( filter ( lambda x : x %
	"""
    return list(filter(lambda x: x % 2 == 0, l))


if __name__ == "__main