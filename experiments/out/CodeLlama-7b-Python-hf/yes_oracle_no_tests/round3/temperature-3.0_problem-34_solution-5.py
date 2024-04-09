def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: print ( unique ([ 5 , 3
	"""



    return sorted(seethrough(l))


def seethrough(l: list):
    """Return the elements in a list that are not in another list
    >>> seethrough([5, 3, 5, 2, 3, 3, 9, 0, 123], [3, 5])
    [0, 2, 9, 123]
    """



    return [x for x in l if x not in [3, 5]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()