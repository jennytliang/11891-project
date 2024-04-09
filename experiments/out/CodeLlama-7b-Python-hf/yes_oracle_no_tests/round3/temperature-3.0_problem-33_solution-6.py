def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l _ copy
	"""
    l_copy = l[:]
    l_copy = sorted(l_copy)
    for i in range(0, len(l_copy), 3):
        l[i] = l_copy[i]
    return l


print(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]))
