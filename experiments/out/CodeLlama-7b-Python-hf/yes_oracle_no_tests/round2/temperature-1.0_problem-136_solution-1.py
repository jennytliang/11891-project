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
    
	Do not include these tokens in the code: if len ( lst ) ==
	'''
    num_lst = [number for number in range(len(lst)) if (number in lst and str(number)[0] is not "-" and str(number)[0] is not "+")]
    try:
        return (min(num_lst),max(num_lst)) if len(num_lst) > 0 else (None,None)
    except:
        return (None,None)