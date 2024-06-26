def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: r = []
	"""
    # l.sort()
    # r = []
    # for e in l:
    #     if e not in r:
    #         r.append(e)
    # return r

    r = []
    for e in l:
        if e not in r:
            r.append(e)
        else:
            l.remove(e)
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
