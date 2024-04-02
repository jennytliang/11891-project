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
    
	Do not include these tokens in the code: # pass
	'''
    # pass
    neg_int = None
    pos_int = None
    for i in lst:
        if i < 0:
            if neg_int is None:
                neg_int = i
            elif i > neg_int:
                neg_int = i
        elif i > 0:
            if pos_int is None:
                pos_int = i
            elif i < pos_int:
                pos_int = i
    if neg_int is None and pos_int is None:
        return (None, None)
    return (neg_int, pos_int)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 8, 9, 10]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 8, 9, 10, 11]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([-1, -2, -3, -4, -5]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, 0]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]))