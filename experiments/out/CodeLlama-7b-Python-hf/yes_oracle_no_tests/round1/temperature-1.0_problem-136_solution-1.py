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
    if len(lst) == 1:
        if lst[0] > 0:
            return None, lst[0]
        else:
            return lst[0], None
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if len(neg) == 0:
        return None, min(pos)
    elif len(pos) == 0:
        return max(neg), None
    else:
        return max(neg), min(pos)

#test 
#print(largest_smallest_integers([2, 4, 1, 3, 5, -7]))
#print(largest_smallest_integers([2, -4, 1, 3, 5, -7]))
#print(largest_smallest_integers([2, -8, 0]))
#print(largest_smallest_integers([0, 0, 0]))
    
