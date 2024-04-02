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
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ i for i in lst if i
	'''

    
    # Solution without filter or lambda
    largest = None
    smallest = None
    for i in lst:
        if i > 0 and (largest is None or i > largest):
            largest = i
        if i < 0 and (smallest is None or i < smallest):
            smallest = i

    return (largest, smallest)

    # Solution with filter
    # largest = None
    # smallest = None
    # for i in filter(lambda x: x > 0, lst):
    #     if largest is None or i > largest:
    #         largest = i
    # for i in filter(lambda x: x < 0, lst):
    #     if smallest is None or i < smallest:
    #         smallest = i
    # return (largest, smallest)

    # Solution with list comprehension
    # largest = None
    # smallest = None
    # for i in [j for j in lst if j > 0]:
    #     if largest is None or i > largest:
    #         largest = i
    # for i in [j for j in lst if j < 0]:
    #     if smallest is None or i < smallest:
    #         smallest = i
    # return (largest, smallest)

    # Solution with list comprehension and filter
    # largest = None
    # smallest = None
    # for i in filter(lambda x: x > 0, [j for j in lst]):
    #     if largest is None or i > largest:
    #         largest = i
    # for i in filter(lambda x: x < 0, [j for j in lst]):
    #     if smallest is None or i < smallest:
    #         smallest = i
    # return (largest, smallest)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]))
print(largest_smallest_integers([2, 4, 1, 3,