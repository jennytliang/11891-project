def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Do not include these tokens in the code: #
	"""
    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return (l[length // 2 - 1] + l[length // 2]) / 2
    else:
        return l[length // 2]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
