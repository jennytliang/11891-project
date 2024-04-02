def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 2
	"""
    l1 = []
    l2 = []
    l3 = []
    for i in l:
        if i % 3 == 0:
            l1.append(i)
        elif i % 3 == 1:
            l2.append(i)
        else:
            l3.append(i)
    l1.sort()
    l2.sort()
    l3.sort()
    l1 = l1 + l2 + l3
    return l1


def sort_third_inplace(l: list):
    """This function takes a list l and returns the same list l, but sorted.
    >>> sort_third_inplace([1, 2, 3])
    [1, 2, 3]
    >>> sort_third_inplace([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 2
	"""
    l.sort()
    return l
