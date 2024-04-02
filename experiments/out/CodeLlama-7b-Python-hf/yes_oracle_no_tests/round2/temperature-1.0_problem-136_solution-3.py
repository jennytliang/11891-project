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

    num_list = [int(n) for n in lst if n.isdigit()]
    
    if not num_list: return (None, None)
    
    neg = [x for x in num_list if x < 0]
    pos = [x for x in num_list if x > 0]
    
    if neg:
        n = neg[::-1] # reverse neg as max will return the first occurence.
        n = n[0]
    else: n = None
    
    if pos:
        p = pos[0]
    else: p = None
    return (n, p)
