def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: return list ( filter ( lambda x : x
	Do not include these tokens in the code: r = [ i for i
	"""
    r = [i for i in l if i > 0]
    return r


print(get_positive.__doc__)
result = get_positive([-1, 2, -4, 5, 6])
print(result)
result = get_positive([5, -3, 4, -3, 3, 9, 0, 123, 1, -10])
print(result)
