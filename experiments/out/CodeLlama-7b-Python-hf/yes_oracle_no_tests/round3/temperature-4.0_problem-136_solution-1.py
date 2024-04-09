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
    
	Include these tokens in the code: neg
	Do not include these tokens in the code: positive
	'''
    neg = None
    pos = None
    for i in lst:
        if i < 0:
            if neg == None:
                neg = i
            elif i > neg:
                neg = i
        elif i > 0:
            if pos == None:
                pos = i
            elif i < pos:
                pos = i
    if neg == None and pos == None:
        return (None, None)
    return (neg, pos)