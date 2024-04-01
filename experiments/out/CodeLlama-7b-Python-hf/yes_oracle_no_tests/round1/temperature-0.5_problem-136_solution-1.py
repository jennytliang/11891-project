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
    for i in lst:
        if i < 0:
            nega.append(i)
        elif i > 0:
            posi.append(i)
    
    if len(nega) == 0:
        nega = None
    if len(posi) == 0:
        posi = None

    return (max(nega), min(posi))


def test_case(test_number, result, expected):
    print("Test case #" + str(test_number))

    if result == expected:
        print("Passed")
    else:
        print("Failed, expected " + str(expected) + ", got " + str(result))


test_case(1, largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
test_case(2, largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, None))
test_case(3, largest_smallest_integers([0, 0, 0, 0, 0, 0]), (None, None))
test_case(4, largest_smallest_integers([-2, 4, -1, 3, 5, -7]), (-1, 3))
test_case(5, largest_smallest_integers([-2, 4, -1, 3, 5, 7]), (-1, 3))
test_case(6, largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, -5))
test_case(7, largest_smallest_integers([-2, -4, -1, -3, -5, 7]), (-1, None))
test_case(8, largest_smallest_integers([-2, -4, -1, -3, 5, 7]), (-1, None))
test_case(9, largest_smallest_integers([-2,