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
    
	Include these tokens in the code: return None
	'''

    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst) )

    if len(neg) > 0:
        a = max(neg)
    else:
        a = None

    if len(pos) > 0:
        b = min(pos)
    else:
        b = None

    return (a, b)


if __name__ == '__main__':
    print("Example:")
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-7, -1)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, None)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-2, 2, 0]) == (-2, 0)
    assert largest_smallest_integers([-1, 0, 1]) == (-1, 1)
    print("Coding complete? Click 'Check' to earn cool rewards!")