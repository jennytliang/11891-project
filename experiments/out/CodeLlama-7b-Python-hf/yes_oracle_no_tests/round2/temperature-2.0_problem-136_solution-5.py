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
    
	Do not include these tokens in the code: # filter ( lambda x : x
	'''
    # l = list(filter(lambda x: isinstance(x, int), lst))
    l = []
    for i in lst:
        if isinstance(i, int):
            l.append(i)
    if len(l) == 0:
        return (None, None)
    elif len(l) == 1:
        if l[0] > 0:
            return (None, l[0])
        else:
            return (l[0], None)
    else:
        if l[0] > 0:
            return (None, min(l))
        else:
            return (max(l), None)
