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
    
    
    if len(lst) < 1:
        return [None, None]
    
    neg = list(filter(lambda x : x < 0, lst))
    pos = list(filter(lambda x : x > 1, lst))
    
    if neg[0] >= -1 & pos[0] >= 2:
        return [neg[0], pos[0]]
    
    return [None, None]
    
    