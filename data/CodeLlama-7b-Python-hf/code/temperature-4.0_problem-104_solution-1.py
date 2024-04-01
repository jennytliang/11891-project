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

    # The idea is to keep removing even digits
    x_string = [str(x)[i] for i in list(range(min([len(x), 15]))) if x % (5 * 2 ** i) < x * 1 // 5]
    return sorted(int("".join(x_string)))