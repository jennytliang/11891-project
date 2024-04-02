def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l :
	"""

    if len(l) == 0:
        return None
    else:
        max_el = l[0]
        for elem in l:
            if elem > max_el:
                max_el = elem
        return max_el


def max_element_v2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l :
	"""

    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: if not l :
	"""

    if len(l) == 0:
        return None
    else:
        min_el = l[0]
        for elem in l:
            if elem < min_el:
                min_el = elem
        return min_el


def min_element_v2(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: if not l :
	"""

    return min(l)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
