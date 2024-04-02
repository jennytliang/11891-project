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
    # return (largest_negative, smallest_positive)
    # pass
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if len(neg) == 0:
        largest_negative = None
    else:
        largest_negative = max(neg)
    if len(pos) == 0:
        smallest_positive = None
    else:
        smallest_positive = min(pos)
    return (largest_negative, smallest_positive)


if __name__ == '__main__':
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
    # (None, 1)
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]))
    # (None, None)
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7, -3]))
    # (None, -3)
    print(largest_smallest_integers([-3, -4, 1, 3, 5, 7, -3]))
    # (-3, -3)
    print(largest_smallest_integers([-3, -4, 1, 3, 5, 7, -3, 0]))
    # (-3, -3)
