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
    
	Do not include these tokens in the code: # return tuple ( map ( lambda
	'''
    positive = []
    negative = []
    for x in lst:
        if x < 0:
            negative.append(x)
        elif x > 0:
            positive.append(x)
    if negative:
        small = min(negative)
    else:
        small = None
    if positive:
        big = max(positive)
    else:
        big = None
    return small, big


def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)