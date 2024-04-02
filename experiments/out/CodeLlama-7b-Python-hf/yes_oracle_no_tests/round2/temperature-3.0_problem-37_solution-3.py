def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: [ l [ i ]
	Do not include these tokens in the code: []
	"""

    e = [l[i] for i in range(1, len(l), 2)]
    e.sort()
    return [l[0], *e, *l[1::2]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
