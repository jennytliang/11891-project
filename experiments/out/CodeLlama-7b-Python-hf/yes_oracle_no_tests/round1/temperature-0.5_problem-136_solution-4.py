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
    
	Do not include these tokens in the code: atives
	'''

    nega = []
    posi = []
    for n in lst:
        if n < 0:
            nega.append(n)
        elif n > 0:
            posi.append(n)
        else:
            pass

    if len(posi) == 0:
        return (None, None)
    elif len(nega) == 0:
        return (None, min(posi))
    else:
        return (max(nega), min(posi))


if __name__ == '__main__':
    print('Example:')
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-4, 0, 6]) == (-4, 0)
    assert largest_smallest_integers([-4, -2, 6]) == (-4, -2)
    assert largest_smallest_integers([-4, -2, -6]) == (-6, -4)
    assert largest_smallest_integers([-4, 0, 6, -6]) == (-6, -4)
    assert largest_smallest_integers([-4, 0, 6, -6, -12]) == (-12, -4)
    assert largest_smallest_integers([-4, 0, 6, -6, -12, 10]) == (-6, -4)
    assert largest_smallest_integers([-4, 0, 6, -6, -12, 10, 100]) == (-6, -4)
    print('Wow, you are doing