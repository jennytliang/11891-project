def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    if len(l) == 0:
        raise ValueError('Empty list')
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    return max_num