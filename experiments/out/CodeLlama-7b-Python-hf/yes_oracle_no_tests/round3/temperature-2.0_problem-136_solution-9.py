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
	Do not include these tokens in the code: ) or None )
	'''


    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    return (max(neg) if neg else None, min(pos) if pos else None)


def test_function():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, -10, 11]) == (-10, 1)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, -10, 11, -100]) == (-100, -10)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, -10, 11, -100, 10]) == (-100, -10)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7, -10, 11, -100, 10, -15]) == (-15, -10)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == (-9, -1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == (-9, -1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5,