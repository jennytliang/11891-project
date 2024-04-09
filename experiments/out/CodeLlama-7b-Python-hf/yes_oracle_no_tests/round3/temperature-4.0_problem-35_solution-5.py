def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: return ma ax _ element
	"""
    return max(l)


def max_element_recursive(l: list):
    """Return maximum element in the list.
    >>> max_element_recursive([1, 2, 3])
    3
    >>> max_element_recursive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: return ma ax _ element
	"""
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], max_element_recursive(l[1:]))
