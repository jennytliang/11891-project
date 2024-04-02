def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l = sorted ( l )
	"""

    s = sorted(l)
    n = len(s)
    if n % 2 == 0:
        return (s[n//2] + s[n//2 - 1]) / 2
    else:
        return s[n//2]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
