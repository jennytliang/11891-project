def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def only_ints(l: list):
    """Return a list of the elements in l that are of type int.
    >>> only_ints([5, 2.5, 3, 1 / 3])
    [5, 3]
    >>> only_ints([7, 'ate', 42])
    [7]
    """
    return [x for x in l if type(x) == int]
