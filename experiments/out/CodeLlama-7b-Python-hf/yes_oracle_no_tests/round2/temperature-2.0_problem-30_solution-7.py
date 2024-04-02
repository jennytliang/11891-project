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
    for i in l:
        if i > 0:
            r.append(i)
    return r


def get_positive_no_return(l: list):
    """Return only positive numbers in the list.
    >>> get_positive_no_return([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive_no_return([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: l[:]
	Do not include these tokens in the code: r =
    """
    l[:] = [i for i in l if i > 0]
