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
    # YOUR CODE HERE
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if not neg:
        neg = None
    if not pos:
        pos = None
    return (neg, pos)


if __name__ == '__main__':
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
    # (None, 1)

    print(largest_smallest_integers([]))
    # (None, None)

    print(largest_smallest_integers([0]))
    # (None, None)

    print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7]))
    # (-7, None)

    print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]))
    # (None, 1)

    print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 0]))
    # (None, 0)

    print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, -1]))
    # (-1, None)

    print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, -1, -2]))
    # (-2, -1)

    print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, -1, -2, -3]))
    # (-3, -1)

    print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, 1]))
    # (-3, -7)
