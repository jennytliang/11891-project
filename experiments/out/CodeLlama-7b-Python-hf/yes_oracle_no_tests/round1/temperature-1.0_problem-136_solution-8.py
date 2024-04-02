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
        neg_largest = max(neg)
    else:
        neg_largest = None
    if pos:
        pos_smallest = min(pos)
    else:
        pos_smallest = None
    return (neg_largest, pos_smallest)


def largest_smallest_integers1(lst):
    neg = [x for x in lst if x < 0]
    pos = [x for x in lst if x > 0]
    if neg:
        neg_largest = max(neg)
    else:
        neg_largest = None
    if pos:
        pos_smallest = min(pos)
    else:
        pos_smallest = None
    return (neg_largest, pos_smallest)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]))
print(largest_smallest_integers([]))
