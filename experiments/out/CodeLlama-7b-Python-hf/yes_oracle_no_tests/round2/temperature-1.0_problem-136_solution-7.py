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
    
	Include these tokens in the code: None if neg == [] else max
	Do not include these tokens in the code: (
	'''

    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    r = None if neg == [] else max(neg), None if pos == [] else min(pos)
    return r


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([2, 4, 1, -3, 5, 7]) == (-3, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, -7]) == (None, -7)
    assert largest_smallest_integers([-2, 4, 1, 3, 5, 7]) == (-2, None)
    assert largest_smallest_integers([2, -4, 1, 3, 5, 7]) == (None, -4)
    assert largest_smallest_integers([2, 4, -1, 3, 5, 7]) == (-1, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 0]) == (None, 0)
    assert largest_smallest_integers([2, 4, 1, 3, 5, -0]) == (-0, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 0.0]) == (None, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7.0]) == (None, None)
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7.0, -7.0]) == (-7.0, None)


if __name__ == '__main__':
    test_largest_smallest_integers()
