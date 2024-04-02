def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: pos _ = []
	"""
    pos_list = []
    for i in l:
        if i > 0:
            pos_list.append(i)
    return pos_list


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -10]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: neg _ = []
	"""
    neg_list = []
    for i in l:
        if i < 0:
            neg_list.append(i)
    return neg_list


def get_zero(l: list):
    """Return only zero in the list.
    >>> get_zero([-1, 2, -4, 5, 6])
    []
    >>> get_zero([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [0]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: zero _ = []
	"""
    zero_list = []
    for i in l:
        if i == 0:
            zero_list.append(i)
    return zero_list


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-1, 3, 3, 9, -10