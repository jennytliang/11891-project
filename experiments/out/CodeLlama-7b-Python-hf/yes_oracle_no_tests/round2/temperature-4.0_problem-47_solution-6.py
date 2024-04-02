def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    return sorted(l)[len(l)//2]

def median2(l: list):
    """Return median of elements in the list l.
    >>> median2([3, 1, 2, 4, 5])
    3
    >>> median2([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2 - 1] + l[len(l)//2])/2

def median3(l: list):
    """Return median of elements in the list l.
    >>> median3([3, 1, 2, 4, 5])
    3
    >>> median3([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2 - 1] + l[len(l)//2])/2

def median4(l: list):
    """Return median of elements in the list l.
    >>> median4([3, 1, 2, 4, 5])
    3
    >>> median4([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2 - 1] + l[len(l)//2])