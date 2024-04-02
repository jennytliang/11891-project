def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return [x for x in l if x > 0]
get_positive([-1, 2, -4, 5, 6])
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])



# The new code should pass all its tests.
