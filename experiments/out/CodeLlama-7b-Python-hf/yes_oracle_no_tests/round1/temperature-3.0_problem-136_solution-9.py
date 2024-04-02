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
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if neg:
        return (max(neg), min(pos))
    else:
        return (None, None)


def run_test(test_number, expected_output, actual_output):
    print("==== test {} ====".format(test_number))
    print("expected: {}".format(expected_output))
    print("actual: {}".format(actual_output))
    print("")


def output_test():
    test_list = [2, 4, 1, 3, 5, 7]
    expected_output = (None, 1)
    actual_output = largest_smallest_integers(test_list)
    run_test("1. basic", expected_output, actual_output)

    test_list = [2, 4, -1, 3, 5, 7]
    expected_output = (-1, None)
    actual_output = largest_smallest_integers(test_list)
    run_test("2. negative", expected_output, actual_output)

    test_list = [2, 4, -1, 3, 5, 7, 0]
    expected_output = (-1, 0)
    actual_output = largest_smallest_integers(test_list)
    run_test("3. negative and zero", expected_output, actual_output)

    test_list = [2, 4, -1, 3, 5, 7, -2]
    expected_output = (-2, -1)
    actual_output = largest_smallest_integers(test_list)
    run_test("4. negative and zero", expected_output, actual_output)

    test_list = [2, 4, -1, 3, 5, 7, -2, 0]
    expected_output = (-2, -1)
    actual_output = largest_smallest_integers(test_list