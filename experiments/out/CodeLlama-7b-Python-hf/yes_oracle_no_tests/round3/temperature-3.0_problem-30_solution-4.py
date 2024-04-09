def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Do not include these tokens in the code: def get _ negative ( l : list ):
	"""


    return list(filter(lambda x: x > 0, l))


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4, -10]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -3, -10]
    
	Do not include these tokens in the code: def get _ negative ( l : list ):
	"""


    return list(filter(lambda x: x < 0, l))


def get_all_even(l: list):
    """Return all even numbers in the list.
    >>> get_all_even([-1, 2, -4, 5, 6])
    [2, 6]
    >>> get_all_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 3, 3, 0, 123]
    
	Do not include these tokens in the code: def get _ all _ even ( l : list ):
	"""


    return list(filter(lambda x: x % 2 == 0, l))


def get_all_odd(l: list):
    """Return all odd numbers in the list.
    >>> get_all_odd([-1, 2, -4, 5, 6])
    [-1, -4, 5]
    >>> get_all_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-1, -3, 3, 9, 1]
    
	Do not include these tokens in the code: def get _ all _ odd ( l : list ):
	"""


    return list(filter(lambda x: x % 2 ==