def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third = [ l [ i ] for i in
	"""
    third = [l[i] for i in xrange(0,len(l),3)]
    third_sorted = sorted(third)
    unsorted = [l[i] for i in xrange(0,len(l),3)]
    for i in xrange(len(third)):
        unsorted[i*3] = third_sorted[i]
    
    return unsorted


    third = [l[i] for i in xrange(0,len(l),3)]
    third_sorted = sorted(third)
    unsorted = [l[i] for i in xrange(0,len(l),3)]
    for i in xrange(len(third)):
        unsorted[i*3] = third_sorted[i]
    
    return unsorted


    