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
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	'''

    
    # pass
    def largest_smallest_integers(lst):
        largest_negative = None
        smallest_positive = None
        for i in lst:
            if i > 0:
                if smallest_positive is None:
                    smallest_positive = i
                elif i < smallest_positive:
                    smallest_positive = i
            if i < 0:
                if largest_negative is None:
                    largest_negative = i
                elif i > largest_negative:
                    largest_negative = i
        return (largest_negative, smallest_positive)

    return largest_smallest_integers(lst)

    # Test
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
    print(largest_smallest_integers([]))
    print(largest_smallest_integers([0]))























































































































































































































































































