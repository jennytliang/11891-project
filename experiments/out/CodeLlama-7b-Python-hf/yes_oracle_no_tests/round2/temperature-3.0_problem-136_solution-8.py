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
    
	Do not include these tokens in the code: if not lst : return
	'''

    max_neg = None
    min_pos = None

    for i in lst:
        if i < 0:
            if max_neg == None:
                max_neg = i
            elif i > max_neg:
                max_neg = i
        elif i > 0:
            if min_pos == None:
                min_pos = i
            elif i < min_pos:
                min_pos = i

    return (max_neg, min_pos)


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-10, 2, 4, 1, 3, 5, 7]) == (-10, 1)
    assert largest_smallest_integers([-9, -10, 2, 4, 1, 3, 5, 7]) == (-10, -9)
    assert largest_smallest_integers([-9, -10, -11, 2, 4, 1, 3, 5, 7]) == (-11, -10)
    assert largest_smallest_integers([-9, -10, -11, 2, 4, 1, 3, 5, 7, 12]) == (-11, -9)
    assert largest_smallest_integers([-9, -10, -11, 2, 4, 1, 3, 5, 7, -12]) == (-12, -11)
    assert largest_smallest_integers([-9, -10, -11, -12, 2, 4, 1, 3, 5, 7]) == (-12, -10)
    assert largest_small