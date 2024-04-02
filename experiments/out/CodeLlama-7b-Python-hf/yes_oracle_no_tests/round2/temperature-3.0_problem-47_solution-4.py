def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    s = sorted(l)
    l = len(l)
    if l % 2 == 0:
        return (s[l // 2] + s[l // 2 - 1]) / 2
    return s[l // 2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
