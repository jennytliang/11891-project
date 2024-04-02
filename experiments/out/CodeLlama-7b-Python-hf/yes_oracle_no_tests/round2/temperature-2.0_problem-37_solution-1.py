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
    # Your code here
    even = [l[i] for i in range(0, len(l), 2)]
    even.sort()
    return [even[i // 2] if i % 2 == 0 else l[i] for i in range(len(l))]


def sort_even_2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_2([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_2([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l [ i ] for i in
	"""
    # Your code here
    even = [l[i] for i in range(0, len(l), 2)]
    even.sort()
    return [even[i // 2] if i % 2 == 0 else l[i] for i in range(len(l))]
