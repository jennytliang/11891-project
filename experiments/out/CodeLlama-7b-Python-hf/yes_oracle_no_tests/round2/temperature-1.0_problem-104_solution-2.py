def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: num s = []
	"""
    s = set()
    for x_k in x:
        if not (1 in str(x_k) or 2 in str(x_k) or 3 in str(x_k) or 4 in str(x_k) or 5 in str(x_k) or 6 in str(x_k) or 7 in str(x_k) or 8 in str(x_k) or 9 in str(x_k)):
            s.add(x_k)
    return(list(s))


print(unique_digits([152, 323, 1422, 10]))
print(unique_digits([15, 33, 1422, 1]))


