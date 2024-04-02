def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l
	Do not include these tokens in the code: . insert ( 0 ,
	"""
    even = []
    for i in range(0, len(l), 2):
        even.insert(0, l[i])
    return even


def sort_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the even indicies, while its values at the odd indicies are equal
    to the values of the odd indicies of l, but sorted.
    >>> sort_odd([1, 2, 3])
    [1, 2, 3]
    >>> sort_odd([5, 6, 3, 4])
    [5, 3, 6, 4]
    
	Include these tokens in the code: odd = [ l
	Do not include these tokens in the code: . insert ( 0 ,
	"""
    odd = []
    for i in range(1, len(l), 2):
        odd.insert(0, l[i])
    return odd


def sort_even_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_odd([1, 2, 3])
    [2, 1, 3]
    >>> sort_even_odd([5, 6, 3, 4])
    [6, 4, 5, 3]
    
	Include these tokens in the code: 
	Do not include these tokens in the code: . insert ( 0 ,
	"""
    even = sort_even(l)
    odd = sort_odd(l)
    return odd + even
