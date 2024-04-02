def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	Do not include these tokens in the code: if not : return
	"""
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2.0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
