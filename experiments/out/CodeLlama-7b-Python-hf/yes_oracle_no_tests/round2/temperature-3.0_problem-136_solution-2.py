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
    if neg == []:
        neg = None
    else:
        neg = max(neg)
    if pos == []:
        pos = None
    else:
        pos = min(pos)
    return (neg, pos)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # == (None, 1)
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7])) # == (-7, -1)
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0])) # == (-7, None)
print(largest_smallest_integers([0, 0, 1, 2, 3, 4, 5, 6, 7])) # == (None, 1)
print(largest_smallest_integers([0, 0, 0, 0, 0, 0, 0, 0, 0])) # == (None, None)