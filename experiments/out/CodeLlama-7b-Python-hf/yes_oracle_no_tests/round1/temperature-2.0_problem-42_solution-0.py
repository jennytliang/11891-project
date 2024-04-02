def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    ret = []
    for i in l:
        ret.append(i + 1)
    return ret


def sum_list(l: list):
    """Return sum of all elements in list.
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    141
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    ret = 0
    for i in l:
        ret += i
    return ret


def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [123, 0, 9, 3, 3, 2, 5, 3, 5, 1]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	"""

    ret = []
    for i in range(len(l) - 1, -1, -1):
        ret.append(l[i])
    return ret


def remove_duplicates(l: list):
    """Remove duplicates from list.
    >>> remove_duplicates([1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6])
    [1, 2, 3, 4, 5, 6]
    >>> remove_duplicates([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 2, 9, 0, 123]
    
	Include these tokens in the code: x
	Do not include these