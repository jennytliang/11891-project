def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    result = []
    for x in x:
        string = str(x)
        for i in string:
            if int(i) % 2 == 0:
                break
        else:
            result.append(x)
    return sorted(result)


def unique_digits(x):
    return sorted([i for i in x if not set(str(i)) & set('2468')])


def unique_digits(x):
    return sorted(set(str(i) for i in x if not '2468' in str(i)))
