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
    if neg == []:
        return None, None
    elif pos == []:
        return None, None
    else:
        return max(neg), min(pos)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Should be (None, 1)
print(largest_smallest_integers([-5, -10, -7, -3, -14]))  # Should be (-14, -7)
print(largest_smallest_integers([2, 4, 6, 1, 5]))  # Should be (None, 1)
print(largest_smallest_integers([2, 4, 6, 1, 5, 12, 14]))  # Should be (None, 1)
print(largest_smallest_integers([0]))  # Should be (None, None)
print(largest_smallest_integers([]))  # Should be (None, None)
