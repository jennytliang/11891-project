def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l [ i ] for i in
	"""
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    even.sort()
    lprime = []
    for i in range(len(l)):
        if i % 2 == 0:
            lprime.append(even.pop(0))
        else:
            lprime.append(l[i])
    return lprime


def sort_even2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even2([1, 2, 3])
    [1, 2, 3]
    >>> sort_even2([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l [ i ] for i in
	"""
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    even.sort()
    lprime = []
    for i in range(len(l)):
        if i % 2 == 0:
            lprime.append(even.pop(0))
        else:
            lprime.append(l[i])
    return lprime


def sort_even3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even3([1, 2, 3])
    [1, 2, 3]
    >>> sort_even3([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l [ i ] for i in
	"""
    even