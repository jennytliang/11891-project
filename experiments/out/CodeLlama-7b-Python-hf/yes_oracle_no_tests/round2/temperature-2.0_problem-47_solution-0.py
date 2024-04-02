def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    l.sort()
    mid = len(l) // 2
    return (l[mid] + l[mid - 1]) / 2.0 if len(l) % 2 == 0 else l[mid]