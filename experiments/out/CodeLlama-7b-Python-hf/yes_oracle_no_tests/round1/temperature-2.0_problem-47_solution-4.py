def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l = sorted ( l )
	Do not include these tokens in the code: . sort ()
	"""
    sorted_l = sorted(l)
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2.0
    return sorted_l[mid]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
