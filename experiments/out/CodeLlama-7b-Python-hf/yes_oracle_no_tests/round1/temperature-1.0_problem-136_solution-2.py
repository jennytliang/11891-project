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
    # 1. Create a list of negative integers
    neg = list(filter(lambda x: x < 0, lst))
    # 2. Create a list of positive integers
    pos = list(filter(lambda x: x > 0, lst))
    # 3. If there is negative integers, return the largest
    if neg:
        a = max(neg)
    else:
        a = None
    # 4. If there is positive integers, return the smallest
    if pos:
        b = min(pos)
    else:
        b = None
    return (a, b)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
