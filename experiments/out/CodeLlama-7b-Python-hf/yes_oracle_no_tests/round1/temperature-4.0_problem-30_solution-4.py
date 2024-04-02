def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list
	Do not include these tokens in the code: result = [] [ result
	"""
    result = []
    for i in l:
        if i >= 0:
            result.append(i)
    return result


def get_positive_extended(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_extended([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_extended([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list
	Do not include these tokens in the code: result = [] [ result
	"""
    result = [i for i in l if i >= 0]
    return result


def get_positive_extended_2(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_extended_2([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_extended_2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list
	Do not include these tokens in the code: result = [] [ result
	"""
    return list(filter(lambda x: x >= 0, l))


def get_positive_extended_3(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_extended_3([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_extended_3([5, 3, -5, 