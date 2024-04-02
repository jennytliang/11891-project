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
	Do not include these tokens in the code: # The idea is to keep a
	"""
    # pass
    def judge(x):
        return int(str(x).replace('0','').replace('2','').replace('4','').replace('6','').replace('8',''))
    return sorted(list(set([x for x in x if judge(x) == x])))


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
	Do not include these tokens in the code: # The idea is to keep a
	"""
    # pass
    def judge(x):
        return int(str(x).replace('0','').replace('2','').replace('4','').replace('6','').replace('8',''))
    return sorted(list(set([x for x in x if judge(x) == x])))


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
	Do not include these tokens in the code: # The idea is to keep a
	"""
    # pass
    def judge(x):
        return int(str(x).replace('0','').replace('2','').replace('4','').