def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    return sorted(list(set([i for i in x if not '2' in str(i) and not '4' in str(i) and not '6' in str(i) and not '8' in str(i)])))

print(unique_digits([15, 33, 1422, 1]))