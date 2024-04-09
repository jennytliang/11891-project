def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ): for ch in
	"""
    #result = []
    #for ch in x:
    #    if not any(d % 2 == 0 for d in set(str(ch))):
    #        result.append(ch)
    #return sorted(result)
    return sorted(set(x))


