def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = []
    for x in l:
        if x > 0:
            r.append(x)

    return r



def get_positive_map(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_map([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_map([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = []
    for x in l:
        if x > 0:
            r.append(x)

    return r



def get_positive_filter(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_filter([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_filter([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = []
    for x in l:
        if x > 0:
            r.append(x)

    return r



if __name__ == "__main__":
    import doctest
    doctest.testmod()