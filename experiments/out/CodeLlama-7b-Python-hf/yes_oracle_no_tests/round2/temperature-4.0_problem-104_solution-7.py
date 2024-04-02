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
    a = []
    for i in x:
        b = str(i)
        for j in b:
            if int(j) % 2 == 0:
                break
        else:
            a.append(i)
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
