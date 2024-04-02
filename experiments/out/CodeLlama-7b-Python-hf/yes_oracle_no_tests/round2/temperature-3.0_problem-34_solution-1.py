def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: list (
	"""

    r = []

    for i in l:
        if i not in r:
            r.append(i)
    
    return sorted(r)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
