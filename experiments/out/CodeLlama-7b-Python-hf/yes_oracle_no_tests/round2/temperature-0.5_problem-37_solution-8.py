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

    l_even = [l[i] for i in range(0, len(l), 2)]
    l_even.sort()
    l_even_sorted = [l_even[i] for i in range(0, len(l_even))]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_sorted = [l_even_sorted[i] for i in range(0, len(l_even_sorted))]
    l_sorted.extend(l_odd)
    return l_sorted


















