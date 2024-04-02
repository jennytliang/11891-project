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
    
	Do not include these tokens in the code: if len (
	'''
    
    # my code
    smallest = None
    largest = None
    for x in lst:
        x = int(x)
        if x < 0 and x > smallest:
            smallest = x
        if x > 0 and x < largest:
            largest = x
    return smallest, largest


def test_case(argv):
    if len(argv) == 2:
        arg1 = argv[0]
        arg2 = argv[1]
    else:
        print("Input arguments are wrong!")
        return

    print(largest_smallest_integers(arg1.split(',')))
    print(largest_smallest_integers(arg2.split(',')))


if __name__ == '__main__':
    from sys import argv
    test_case(argv)
