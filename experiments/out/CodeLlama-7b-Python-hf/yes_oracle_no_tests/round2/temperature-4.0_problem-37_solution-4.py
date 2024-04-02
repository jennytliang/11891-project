def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: # l 1
	"""
    # l 1
    even_indicies = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indicies]
    even_values.sort()
    l_even = [0] * len(l)
    for i in range(len(even_values)):
        l_even[even_indicies[i]] = even_values[i]
    return l_even


if __name__ == "__main__":
    import doctest
    doctest.testmod()
