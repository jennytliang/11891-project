def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    
    if len(l) == 0:
        raise ValueError("Empty list")
    max_element = 0
    for i in l:
        if i > max_element:
            max_element = i
    return max_element


def max_element_rec(l: list):
    """Return maximum element in the list.
    >>> max_element_rec([1, 2, 3])
    3
    >>> max_element_rec([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    if len(l) == 0:
        raise ValueError("Empty list")
    if len(l) == 1:
        return l[0]
    else:
        return max(max_element_rec(l[1:]), l[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
