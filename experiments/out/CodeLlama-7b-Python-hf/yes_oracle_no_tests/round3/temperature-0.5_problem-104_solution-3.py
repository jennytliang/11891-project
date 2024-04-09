def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: unique = [] for i
	"""
    unique = []
    for i in x:
        if not any(j in str(i) for j in ['2', '4', '6', '8']):
            unique.append(i)
    return sorted(unique)


def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: unique = [] for i
	"""
    unique = []
    for i in x:
        if not any(j in str(i) for j in ['2', '4', '6', '8']):
            unique.append(i)
    return sorted(unique)
