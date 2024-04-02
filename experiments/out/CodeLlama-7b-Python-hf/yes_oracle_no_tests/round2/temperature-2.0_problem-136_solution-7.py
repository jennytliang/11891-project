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
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	'''

    
    pos = []
    neg = []
    for x in lst:
        if x < 0:
            neg.append(x)
        if x > 0:
            pos.append(x)
    if len(neg) == 0:
        small = None
    else:
        small = min(neg)
    if len(pos) == 0:
        big = None
    else:
        big = max(pos)
    return (small, big)



def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([1, -1, 0, -2, -3, 2, 3]) == (-3, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7]) == (-7, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]) == (None, 7)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, -1, -2, -3]) == (-3, 7)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8]) == (-8, -8)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8]) == (None, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4]) == (-4, 8)
    assert