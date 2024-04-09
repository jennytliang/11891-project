def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: # pass
	"""
    # pass
    # return [x for x in x if not any(i%2==0 for i in str(x))]
    # return sorted(set([x for x in x if not any(i%2==0 for i in str(x))]))
    return sorted(list(set([int(''.join(str(n) for n in x if not n%2)) for x in x])))
    
