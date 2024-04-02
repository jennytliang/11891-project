def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Do not include these tokens in the code: if len ( l ) ==
	"""
    l = sorted(l)
    mid = len(l) // 2
    if len(l) % 2 == 1:
        return l[mid]
    else:
        return (l[mid - 1] + l[mid]) / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
