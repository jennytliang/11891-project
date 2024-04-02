def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: l 2
	"""
    ## BEGIN SOLUTION
    
    assert len(l) % 2 == 0 # There must always be an even number of indicies
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            value = l[i]
            index = i
            break
    l2 = l[index::]
    l2.sort()
    l2 = l2[::-1] # reverse the list
    i = 0
    while i < len(l):
        if i % 2 == 0:
            x = l[i]
            l[i] = l2[i//2]
            l2[i//2] = x
        i += 1
    return l
    ## END SOLUTION
