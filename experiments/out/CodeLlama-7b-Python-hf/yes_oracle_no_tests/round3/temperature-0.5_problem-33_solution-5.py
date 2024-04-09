def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 1
	"""
    l1 = [i for i in l if i % 3 != 0]
    l2 = [i for i in l if i % 3 == 0]
    l2.sort()
    return l1 + l2


def third_sort(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> third_sort([1, 2, 3])
    [1, 2, 3]
    >>> third_sort([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 1
	"""
    l1 = [i for i in l if i % 3 != 0]
    l2 = [i for i in l if i % 3 == 0]
    l2.sort()
    return l1 + l2
