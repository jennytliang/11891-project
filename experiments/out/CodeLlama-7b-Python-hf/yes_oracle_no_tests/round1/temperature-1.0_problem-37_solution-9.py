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
    
    # This function takes a list l and returns a list l' such that
    # l' is identical to l in the odd indicies, while its values at the even indicies are equal
    # to the values of the even indicies of l, but sorted.
    
    # Make the new, l' as a copy of l
    
    lprimes = l.copy()

    # loop over the even indicies
    for i in list(range(0, len(lprimes), 2)):
        # set the even values
        lprimes[i] = min(l[i::2])

    return lprimes

#print(sort_even([1,2,4,3,6,5]))
#print(sort_even( [7,2,6,3,2,-1]))

l = [22,10,101,490,57,22,3,5,11,12,12]
print(sort_even(l))
