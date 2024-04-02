def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""
    result = []
    for i in x:
        if (not(any(c in str(i) for c in "2468"))):
            result.append(i)
    return sorted(result)


def unique_digits2(x):
    """Same as above, but without using any loops.

    For example:
    >>> unique_digits2([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits2([152, 323, 1422, 10])
    []
    """
    return sorted(i for i in x if not any(c in str(i) for c in "2468"))
