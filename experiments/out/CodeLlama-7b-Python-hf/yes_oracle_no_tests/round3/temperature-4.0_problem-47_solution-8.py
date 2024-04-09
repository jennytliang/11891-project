def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    return l[len(l)//2]


def median_sorted(l: list):
    """Return median of elements in the list l.
    >>> median_sorted([3, 1, 2, 4, 5])
    3
    >>> median_sorted([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted l
	"""
    l.sort()
    return l[len(l)//2]