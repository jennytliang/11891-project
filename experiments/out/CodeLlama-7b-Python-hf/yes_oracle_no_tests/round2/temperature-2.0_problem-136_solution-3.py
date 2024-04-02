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
    
	Include these tokens in the code: :
	'''

    neg = list(filter(lamda x: x < 0, lst))
    pos = list(filter(lamda x: x > 0, lst))
    if len(neg) == 0:
        return (None, None)
    elif len(pos) == 0:
        return (None, None)
    else:
        return (max(neg), min(pos))


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([1, -1, 0, -2, 2]))
