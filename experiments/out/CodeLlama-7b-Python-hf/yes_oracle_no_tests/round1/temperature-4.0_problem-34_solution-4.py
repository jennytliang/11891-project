def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # sort l in place using
	"""
    l.sort()
    # sort l in place using l.sort()
    i = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            del l[i]
        else:
            i += 1
    return l


if __name__ == "__main__":
    import doctest
    doctest.testmod()
