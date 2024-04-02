def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: return sorted ( set
	Do not include these tokens in the code: l . sort () #
	"""
    return sorted(set(l))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
