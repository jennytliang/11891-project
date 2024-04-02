def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	"""


    return sorted(s for s in set(l))

print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))


def unique2(l: list):
    """Return sorted unique elements in a list using sets
    >>> unique2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


print(unique2([5, 3, 5, 2, 3, 3, 9, 0, 123]))