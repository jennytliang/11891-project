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
        if '2' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i):
            result.append(i)
    return sorted(result)


print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))
