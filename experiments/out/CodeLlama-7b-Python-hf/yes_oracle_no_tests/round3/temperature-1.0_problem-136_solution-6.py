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
	Do not include these tokens in the code: )
	'''


    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))

    if neg and pos:
        return (min(neg), max(pos))
    elif neg:
        return (min(neg), None)
    elif pos:
        return (None, min(pos))
    else:
        return (None, None)


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6]) == (-6, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6]) == (-6, 1)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]) == (-6, 1)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 0]) == (-6, 0)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 0, 7, 8, 9]) == (-6, 1)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 0, 