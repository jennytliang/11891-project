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
	Do not include these tokens in the code: res = [] for i
	"""
    res = []
    for i in x:
        if i < 10:
            res.append(i)
        else:
            a = i
            while a > 0:
                if a % 10 == 0:
                    a = a // 10
                elif a % 2 == 0:
                    res.append(i)
                    break
                else:
                    a = a // 10
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
