def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l = sorted ( l )
	"""
    l = sorted(l)
    m = len(l) // 2
    if len(l) % 2 == 0:
        return (l[m - 1] + l[m]) / 2
    else:
        return l[m]


def median_sorted(l: list):
    """Return median of elements in the list l.
    >>> median_sorted([3, 1, 2, 4, 5])
    3
    >>> median_sorted([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: _ l = l[ ( len(l) - 1 ) // 2 ]
	"""
    l = l[len(l) // 2]
    if isinstance(l, list):
        return median(l)
    else:
        return l


def median_recursive(l: list):
    """Return median of elements in the list l.
    >>> median_recursive([3, 1, 2, 4, 5])
    3
    >>> median_recursive([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: _ l = l[ ( len(l) - 1 ) // 2 ]
    """
    l = l[len(l) // 2]
    if isinstance(l, list):
        return median_recursive(l)
    else:
        return l
