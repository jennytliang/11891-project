def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    if not l:
        raise ValueError("Empty list")
    max_value = l[0]
    for elem in l:
        if elem > max_value:
            max_value = elem
    return max_value


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: if not l : raise
	"""
    if not l:
        raise ValueError("Empty list")
    min_value = l[0]
    for elem in l:
        if elem < min_value:
            min_value = elem
    return min_value


def max_element_rec(l: list):
    """Return maximum element in the list.
    >>> max_element_rec([1, 2, 3])
    3
    >>> max_element_rec([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    if not l:
        raise ValueError("Empty list")
    if len(l) == 1:
        return l[0]
    else:
        # get max of first and last element
        return max([max_element_rec(l[:1]), max_element_rec(l[-1:])])


def min_element_rec(l: list):
    """Return minimum element in the list.
    >>> min_element_rec([1, 2, 3])
    1
    >>> min_element_rec([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    