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
    
	Include these tokens in the code: neg = list (
	Do not include these tokens in the code: return max ([ *
	'''
    # pass
    for item in lst:
        if type(item) != int:
            lst.remove(item)
    neg = []
    for item in lst:
        if item < 0:
            neg.append(item)
    neg_max = None
    for item in neg:
        neg_max = item if neg_max is None else max(item, neg_max)
    pos = []
    for item in lst:
        if item > 0:
            pos.append(item)
    pos_min = None
    for item in pos:
        pos_min = item if pos_min is None else min(item, pos_min)
    return neg_max, pos_min
