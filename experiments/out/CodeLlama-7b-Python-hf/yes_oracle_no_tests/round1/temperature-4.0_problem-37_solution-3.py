def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: l 1
	"""
    new_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(sorted(l[i:i+1]))
        else:
            new_list.append(l[i])
    return new_list


def sort_even_s(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_s([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_s([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even, sorted, slicing
	Do not include these tokens in the code: l 1
	"""
    new_list = []
    for i in range(0, len(l), 2):
        new_list.append(l[i])
    for i in range(1, len(l), 2):
        new_list.append(sorted(l[i:i+1]))
    return new_list


def sort_even_t(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_t([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_t([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even, sorted, slicing, ternary
	Do not include these tokens in the code: l 1
	"""
    return [l[i] if i % 2 else sorted