def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    
	Include these tokens in the code: neg = list ( filter ( lambda x : x
	'''
    negs = []
    poss = []
    # split into neg and poss, or keep None
    for i in lst:
        if i >= 0:
            poss.append(i)
        else:
            negs.append(i)



    return (max(poss) if len(poss) > 0 else None , min(negs) if len(negs) > 0 else None)