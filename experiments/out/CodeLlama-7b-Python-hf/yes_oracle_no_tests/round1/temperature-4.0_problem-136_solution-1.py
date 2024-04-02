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
    # return tuple(map(lambda x: x or None, (max(filter(lambda x: x < 0, lst)), min(filter(lambda x: x > 0, lst)))))
    neg = list(filter(lambda x: x < 0, lst))
    if neg:
        neg = max(neg)
    else:
        neg = None
    pos = list(filter(lambda x: x > 0, lst))
    if pos:
        pos = min(pos)
    else:
        pos = None
    return (neg, pos)


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([3, 2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5, -7]) == (-7, None)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5, -7, 0]) == (-7, 0)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5, -7, 1]) == (-7, 1)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5, -7, 1, 2]) == (-7, 1)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5, -7, 1, 2, 3]) == (-7, 1)
    assert largest_smallest_integers([-3, -2, -4, -1, -3, -5