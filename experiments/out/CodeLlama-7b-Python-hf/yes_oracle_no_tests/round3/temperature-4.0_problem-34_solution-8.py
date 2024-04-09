def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return sorted(set(l))


# print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))


