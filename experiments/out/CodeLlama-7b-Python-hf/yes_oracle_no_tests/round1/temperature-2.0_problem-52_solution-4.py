def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    return all(x < t for x in l)


def below_threshold([1, 2, 4, 10], 100)
	return all(x < t for x in l)


def below_threshold([1, 20, 4, 10], 5)
	return all(x < t for x in l)
