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
    neg = list( filter ( lambda x : x < 0 , lst ) )
    neg_max = max(neg) if neg else None
    pos = list( filter ( lambda x : x > 0 , lst ) )
    pos_min = min(pos) if pos else None
    return (neg_max, pos_min)
    
#Tests
def test(result, expected):
    if result == expected:
        print("These are two equal lists")
    else:
        print("These are differents lists")
        
test(largest_smallest_integers([2, -4, 1, 3, 5, 7]), (-4, 1))
test(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]), (None, 1))
test(largest_smallest_integers([0, -1, 2, -2, 3, -3]), (-3, None))
test(largest_smallest_integers([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]), (-9, -1))