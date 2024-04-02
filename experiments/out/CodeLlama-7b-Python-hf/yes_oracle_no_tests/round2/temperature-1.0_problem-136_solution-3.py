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
    
	Do not include these tokens in the code: # return ( larg est _ negative
	'''
    largest = None
    smallest = None

    for i in lst:
        if i > 0 and largest is None:
            largest = i
        elif i > 0 and i > largest:
            largest = i
        elif i < 0 and smallest is None:
            smallest = i
        elif i < 0 and i < smallest:
            smallest = i

    return (largest, smallest)



def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6]) == (-6, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6]) == (-6, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 7]) == (-6, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 7, 8]) == (-6, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == (-6, 1)
    assert largest_smallest_integers([-1