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
    
	Include these tokens in the code: neg
	Do not include these tokens in the code: max _
	'''
    neg = None
    pos = None
    
    for i in lst:
        if i < 0:
            if neg == None:
                neg = i
            else:
                if i > neg:
                    neg = i

        if i > 0:
            if pos == None:
                pos = i
            else:
                if i < pos:
                    pos = i

    return (neg, pos)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
