def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: max
	Do not include these tokens in the code: ma ax
	"""



    max_el = l[0]
    for el in l:
        if el > max_el:
            max_el = el
    return max_el


def max_element_v2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: max
	Do not include these tokens in the code: ma ax
	"""
    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: min
	Do not include these tokens in the code: mi n
	"""



    min_el = l[0]
    for el in l:
        if el < min_el:
            min_el = el
    return min_el


def min_element_v2(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: min
	Do not include these tokens in the code: mi n
	"""
    return min(l)


def reverse_list(l: list):
    """Return a list with elements in reverse order.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>>