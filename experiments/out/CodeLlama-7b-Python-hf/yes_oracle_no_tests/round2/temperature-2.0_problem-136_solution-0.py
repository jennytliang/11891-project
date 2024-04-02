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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	'''
    
    # Your code here
    if len(lst) == 0:
        return (None, None)
    else:
        max_num = -9999999999999999999999999999999999999999999999999999999999999999999
        min_num = 9999999999999999999999999999999999999999999999999999999999999999999
        for num in lst:
            if num >= 0:
                if num > max_num:
                    max_num = num
            else:
                if num < min_num:
                    min_num = num
        if max_num == -999999999999999999999999999999999999999999999999999999999999999999:
            max_num = None
        if min_num == 9999999999999999999999999999999999999999999999999999999999999999999:
            min_num = None
        return (max_num, min_num)
    
    return (None, None)

















































































