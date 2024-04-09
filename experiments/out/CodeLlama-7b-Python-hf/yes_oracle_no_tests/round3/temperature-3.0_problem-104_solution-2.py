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
    result = []
    for x in x:
        if not any(i in str(x) for i in '2468'):
            result.append(x)
    return sorted(result)


def unique_digits(x):
    return sorted(i for i in x if not any(j in str(i) for j in '2468'))
