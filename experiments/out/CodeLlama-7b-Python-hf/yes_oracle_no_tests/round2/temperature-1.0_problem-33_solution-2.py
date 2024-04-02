def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Do not include these tokens in the code: # Your code here
	"""
    return [item for items in sorted(l) if items not in list(range(3, len(l) + 1, 3)) for item in l]
l = list(range(3, len(l) + 1, 3))

