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
    
	Include these tokens in the code: filter ( lambda
	'''

    neg = 0
 
    if len(lst) == 0:
        return None
    else:
        for x in lst:
            if x < 0:
                neg = x
                
            if x == 0 :
                pass
                
            else:
                if neg == 0:
                    pos = x
                    return max(neg, 0), min(pos, 0)
                    
                else:
                    pass
                    
            # This part of the block is necessary
            # as the first value of the list might be 0.
            if x/pos == 1:
                pos = 0

                return max(neg, 0), min(pos, 0)
#largest_smallest_integers([2, 2])

print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
#print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
#print(largest_smallest_integers([0, -1]))
print(largest_smallest_integers([0]))
