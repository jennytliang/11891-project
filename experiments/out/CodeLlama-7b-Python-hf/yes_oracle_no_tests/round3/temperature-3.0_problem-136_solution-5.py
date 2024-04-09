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
    
	Include these tokens in the code: ))
	Do not include these tokens in the code: ) )
	'''


    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))

    if neg == []:
        a = None
    else:
        a = max(neg)

    if pos == []:
        b = None
    else:
        b = min(pos)

    return (a, b)


# TESTS
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8]) == (-8, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8]) == (None, 1)
assert largest_smallest_integers([-1, 2, 3, 4, 5, 6, 7, 8]) == (-1, 1)
assert largest_smallest_integers([-1, 2, -3, 4, 5, 6, 7, 8]) == (-3, -1)
assert largest_smallest_integers([-1, -2, 3, 4, 5, 6, 7, 8]) == (-2, -1)
