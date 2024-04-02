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
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    return (max(neg) if neg else None, min(pos) if pos else None)


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, 2, 4, 1, 3, 5, 7]) == (-1, 1)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, -1]) == (-1, 1)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]) == (None, 0)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, 0, -1]) == (-1, 0)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, 0, -1, 3]) == (-1, 0)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, 0, -1, 3, -3]) == (-3, 0)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, 0, -1, 3, -3, -5]) == (-5, -3)
